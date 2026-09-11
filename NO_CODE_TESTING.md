# No-Code Testing Guide

This guide is for participants who want to test the Digital Self Engine without installing Python, Git, or any programming tools.

You only need:

- a web browser
- a text editor or notes app
- your own answers
- enough time to complete a small blind test

---

## What you are testing

The goal is not to create a perfect personality profile.

The goal is to test whether the same Generic Engine can learn different people and predict how they respond in new situations.

A good test asks:

> Does the model predict this person specifically, or does it fall back to generic “average person” behavior?

---

## Part 1 — Create a local Persona Package

Do not upload private personal information to GitHub.

Create a local document on your own computer.

You may use a simple table like this:

| Field | Example |
|---|---|
| Participant ID | anon_001 |
| Stable tendencies | cautious in high-responsibility decisions |
| Conditional tendencies | if unsure and expert evidence is strong, increase expert weight |
| Values | family, responsibility, autonomy |
| Current state | normal |
| Known unknowns | reactions under public conflict are unclear |

Keep this file private.

---

## Part 2 — Calibration

Before blind testing, collect some examples of how the participant really thinks and acts.

Use questions from different areas:

- family
- work
- money
- risk
- relationships
- unfamiliar opportunities
- responsibility
- conflict
- confidence
- cooperation
- fatigue
- uncertainty

For each answer, record:

1. the situation
2. the participant's actual answer
3. what mechanism may explain it
4. whether this is:
   - a temporary state
   - a conditional rule
   - a domain-specific strategy
   - a possible stable tendency
   - still unknown

Do not turn one answer into a permanent personality trait.

---

## Part 3 — Prepare blind scenarios

Now create new situations that were not used during calibration.

A blind scenario should:

- be genuinely new
- test a mechanism rather than repeat the same wording
- allow mixed or uncertain answers
- avoid leading the participant toward the prediction

Example:

> You are invited to join a project you find interesting.  
> The possible reward is high, the risk is moderate, and the decision must be made quickly.  
> A trusted person disagrees with you.  
> What would you most likely do?

Before asking the participant, write your prediction.

---

## Part 4 — Freeze the prediction manually

Before the participant answers, record:

| Field | Example |
|---|---|
| Case ID | B01 |
| Scenario | New project decision |
| Prediction | Ask for reasons, compare evidence, then decide |
| Confidence | 0.70 |
| Expected mechanism | decision arbitration |
| Acceptable response region | may follow expert if evidence is stronger |
| Scoring rule | strong match if participant compares evidence before deciding |

Then freeze it.

For a no-code test, "freeze" means:

- save the document
- do not edit the prediction after seeing the answer
- optionally export it as PDF or take a screenshot with a timestamp

The purpose is simple:

> prediction first, answer second

---

## Part 5 — Ask the participant

Now show only the scenario.

Do not show:

- your prediction
- expected mechanism
- scoring rule
- acceptable response region

Let the participant answer naturally.

Allowed answers include:

- mixed reactions
- “depends”
- “I don't know”
- a completely different answer
- a response that changes after reflection

Do not force the participant into A/B/C if their real response is more complicated.

---

## Part 6 — Compare after the chain ends

Do not score immediately after every answer if that could influence later predictions.

After the planned blind-test chain is complete, compare prediction and actual answer.

Use four labels:

### strong_match

The predicted direction and mechanism are both close to the actual response.

### partial_match

The prediction captured part of the response, but missed an important condition, weight, or competing reaction.

### deviation

The prediction was meaningfully wrong.

### unknown

The participant's answer is too unclear, unstable, or context-dependent to judge fairly.

---

## Part 7 — Identify the error layer

If the prediction failed, do not immediately change personality traits.

First ask which layer was wrong.

Possible error layers:

- temporary state
- relationship context
- competence
- confidence
- responsibility
- motivation
- risk sensitivity
- process memory
- decision arbitration
- self narrative
- identity continuity
- missing information
- unknown region

Prefer the smallest explanation that fits the error.

---

## Part 8 — Submit only anonymous results

Do not upload raw private conversations.

A useful public submission looks like this:

```text
Participant ID: anon_037

Calibration cases: 32
Blind cases: 12

Strong match: 7
Partial match: 3
Deviation: 2
Unknown: 0

Repeated error:
The model over-weighted expert authority when the participant had strong first-hand experience.

Likely error layer:
decision arbitration

Possible engine-level issue:
The engine may need a stronger self-evidence / expert-evidence comparison rule.
