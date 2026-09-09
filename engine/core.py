from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class CandidateResponse:
    action: str
    score: float
    reasons: List[str] = field(default_factory=list)

class DigitalSelfEngine:
    """Minimal generic research skeleton. No person-specific priors belong here."""
    def __init__(self, persona: Dict[str, Any]):
        self.persona = persona

    def evaluate(self, event: Dict[str, Any]) -> List[CandidateResponse]:
        candidates=[]
        for tendency in self.persona.get("conditional_tendencies", []):
            candidates.append(CandidateResponse(
                action=tendency.get("then", "unknown"),
                score=float(tendency.get("weight", 0.5)),
                reasons=[f"persona_tendency:{tendency.get('if','unspecified')}"]
            ))
        if not candidates:
            candidates.append(CandidateResponse("unknown",0.0,["insufficient_person_specific_evidence"]))
        return sorted(candidates,key=lambda x:x.score,reverse=True)

    def update(self, evidence: Dict[str, Any]) -> None:
        self.persona.setdefault("evidence_bank", []).append(evidence)
