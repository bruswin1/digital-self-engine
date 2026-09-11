#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

VALID_SCORES = {
    "strong_match",
    "partial_match",
    "deviation",
    "unknown",
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def canonical_json(data) -> bytes:
    text = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return text.encode("utf-8")


def prediction_payload(data):
    """
    Return only the fields that must be frozen before blind answers.

    Participant answers and final scores are intentionally excluded.
    """
    frozen_cases = []

    for case in data.get("cases", []):
        frozen_cases.append(
            {
                "case_id": case.get("case_id"),
                "scenario": case.get("scenario"),
                "prediction": case.get("prediction"),
                "prediction_confidence": case.get("prediction_confidence"),
                "expected_mechanism": case.get("expected_mechanism", []),
                "acceptable_region": case.get("acceptable_region", []),
                "scoring_rule": case.get("scoring_rule"),
            }
        )

    return {
        "test_id": data.get("test_id"),
        "engine_version": data.get("engine_version"),
        "persona_version": data.get("persona_version"),
        "cases": frozen_cases,
    }


def compute_freeze_hash(data) -> str:
    payload = prediction_payload(data)
    return hashlib.sha256(canonical_json(payload)).hexdigest()


def create_test(args):
    path = Path(args.file)

    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path}")

    template = {
        "schema_version": "0.2",
        "test_id": args.test_id,
        "engine_version": args.engine_version,
        "persona_version": args.persona_version,
        "status": "draft",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "frozen_at": None,
        "freeze_hash_sha256": None,
        "cases": [
            {
                "case_id": "B01",
                "scenario": "Write a blind scenario here.",
                "prediction": "Write the prediction before the participant answers.",
                "prediction_confidence": 0.0,
                "expected_mechanism": [],
                "acceptable_region": [],
                "scoring_rule": "Define what would count as match / partial / deviation.",
                "actual": None,
                "score": None,
                "error_layer": None,
                "notes": None,
            }
        ],
    }

    save_json(path, template)

    print(f"Created blind-test file: {path}")
    print("Edit the scenarios and predictions, then run:")
    print(f"  python tools/blind_test_cli.py freeze {path}")


def freeze_test(args):
    path = Path(args.file)
    data = load_json(path)

    if data.get("status") == "frozen":
        print("This test is already frozen.")
        print(f"Freeze hash: {data.get('freeze_hash_sha256')}")
        return

    for case in data.get("cases", []):
        required = [
            "case_id",
            "scenario",
            "prediction",
            "prediction_confidence",
            "scoring_rule",
        ]

        missing = [key for key in required if case.get(key) in (None, "")]

        if missing:
            raise SystemExit(
                f"Case {case.get('case_id', '<unknown>')} is missing: "
                + ", ".join(missing)
            )

    freeze_hash = compute_freeze_hash(data)

    data["status"] = "frozen"
    data["frozen_at"] = datetime.now(timezone.utc).isoformat()
    data["freeze_hash_sha256"] = freeze_hash

    save_json(path, data)

    print("Predictions frozen.")
    print(f"File: {path}")
    print(f"SHA-256: {freeze_hash}")
    print("")
    print("Do not change prediction fields after this point.")
    print("You may now collect participant answers.")


def verify_test(args):
    path = Path(args.file)
    data = load_json(path)

    expected = data.get("freeze_hash_sha256")

    if not expected:
        raise SystemExit("This file has no freeze hash. Freeze it first.")

    actual = compute_freeze_hash(data)

    if actual == expected:
        print("PASS: frozen prediction fields are unchanged.")
        print(f"SHA-256: {actual}")
        return

    print("FAIL: frozen prediction fields were modified.")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    sys.exit(1)


def record_answer(args):
    path = Path(args.file)
    data = load_json(path)

    if data.get("status") != "frozen":
        raise SystemExit("Freeze the test before recording blind answers.")

    target = None

    for case in data.get("cases", []):
        if case.get("case_id") == args.case_id:
            target = case
            break

    if target is None:
        raise SystemExit(f"Case not found: {args.case_id}")

    target["actual"] = args.actual

    if data.get("status") == "frozen":
        data["status"] = "answering"

    save_json(path, data)

    print(f"Recorded answer for {args.case_id}.")
    print("Frozen prediction fields were not changed.")


def score_case(args):
    if args.score not in VALID_SCORES:
        raise SystemExit(
            "Score must be one of: "
            + ", ".join(sorted(VALID_SCORES))
        )

    path = Path(args.file)
    data = load_json(path)

    target = None

    for case in data.get("cases", []):
        if case.get("case_id") == args.case_id:
            target = case
            break

    if target is None:
        raise SystemExit(f"Case not found: {args.case_id}")

    if target.get("actual") in (None, ""):
        raise SystemExit(
            f"Case {args.case_id} has no participant answer yet."
        )

    target["score"] = args.score
    target["error_layer"] = args.error_layer
    target["notes"] = args.notes

    save_json(path, data)

    print(f"Scored {args.case_id}: {args.score}")


def summarize_test(args):
    path = Path(args.file)
    data = load_json(path)

    counts = {key: 0 for key in VALID_SCORES}
    unscored = 0
    answered = 0

    for case in data.get("cases", []):
        if case.get("actual") not in (None, ""):
            answered += 1

        score = case.get("score")

        if score in VALID_SCORES:
            counts[score] += 1
        else:
            unscored += 1

    total = len(data.get("cases", []))

    print(f"Test ID: {data.get('test_id')}")
    print(f"Status: {data.get('status')}")
    print(f"Cases: {total}")
    print(f"Answered: {answered}")
    print("")
    print("Scores:")

    for key in [
        "strong_match",
        "partial_match",
        "deviation",
        "unknown",
    ]:
        print(f"  {key}: {counts[key]}")

    print(f"  unscored: {unscored}")

    if total:
        usable = (
            counts["strong_match"]
            + counts["partial_match"]
            + counts["deviation"]
        )

        print("")
        print(
            "Note: this tool intentionally does not convert these labels "
            "into a scientific 'accuracy percentage'."
        )

        if usable:
            print(
                "Use the pattern of errors and error layers to improve "
                "the model after the blind run."
            )


def finalize_test(args):
    path = Path(args.file)
    data = load_json(path)

    verify_hash = compute_freeze_hash(data)
    expected_hash = data.get("freeze_hash_sha256")

    if not expected_hash:
        raise SystemExit("Test was never frozen.")

    if verify_hash != expected_hash:
        raise SystemExit(
            "Cannot finalize: frozen prediction fields were modified."
        )

    for case in data.get("cases", []):
        if case.get("actual") in (None, ""):
            raise SystemExit(
                f"Cannot finalize: {case.get('case_id')} has no answer."
            )

        if case.get("score") not in VALID_SCORES:
            raise SystemExit(
                f"Cannot finalize: {case.get('case_id')} is not scored."
            )

    data["status"] = "completed"
    data["completed_at"] = datetime.now(timezone.utc).isoformat()

    save_json(path, data)

    print("Blind test finalized.")
    print(f"File: {path}")
    print("")
    summarize_test(
        argparse.Namespace(file=str(path))
    )


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Minimal CLI for creating, freezing, verifying, "
            "answering, and scoring blind tests."
        )
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser(
        "create",
        help="Create a new blind-test JSON file.",
    )
    p_create.add_argument("file")
    p_create.add_argument(
        "--test-id",
        default="blind_test_001",
    )
    p_create.add_argument(
        "--engine-version",
        default="0.1",
    )
    p_create.add_argument(
        "--persona-version",
        default="local",
    )
    p_create.set_defaults(func=create_test)

    p_freeze = sub.add_parser(
        "freeze",
        help="Freeze prediction fields and write a SHA-256 hash.",
    )
    p_freeze.add_argument("file")
    p_freeze.set_defaults(func=freeze_test)

    p_verify = sub.add_parser(
        "verify",
        help="Verify frozen prediction fields have not changed.",
    )
    p_verify.add_argument("file")
    p_verify.set_defaults(func=verify_test)

    p_answer = sub.add_parser(
        "answer",
        help="Record a participant's blind answer.",
    )
    p_answer.add_argument("file")
    p_answer.add_argument("case_id")
    p_answer.add_argument("actual")
    p_answer.set_defaults(func=record_answer)

    p_score = sub.add_parser(
        "score",
        help="Score one completed blind case.",
    )
    p_score.add_argument("file")
    p_score.add_argument("case_id")
    p_score.add_argument(
        "score",
        choices=sorted(VALID_SCORES),
    )
    p_score.add_argument(
        "--error-layer",
        default=None,
    )
    p_score.add_argument(
        "--notes",
        default=None,
    )
    p_score.set_defaults(func=score_case)

    p_summary = sub.add_parser(
        "summary",
        help="Show the current blind-test summary.",
    )
    p_summary.add_argument("file")
    p_summary.set_defaults(func=summarize_test)

    p_finalize = sub.add_parser(
        "finalize",
        help="Verify and finalize a fully answered/scored test.",
    )
    p_finalize.add_argument("file")
    p_finalize.set_defaults(func=finalize_test)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except FileNotFoundError as exc:
        raise SystemExit(f"File not found: {exc.filename}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {exc}")


if __name__ == "__main__":
    main()
