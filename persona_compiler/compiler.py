from typing import Any, Dict

def add_evidence(persona: Dict[str, Any], evidence: Dict[str, Any]) -> Dict[str, Any]:
    persona=dict(persona)
    bank=list(persona.get("evidence_bank", []))
    bank.append(evidence)
    persona["evidence_bank"]=bank
    return persona

def mark_unknown(persona: Dict[str, Any], region: str, reason: str) -> Dict[str, Any]:
    persona=dict(persona)
    unknowns=list(persona.get("unknown_regions", []))
    unknowns.append({"region":region,"reason":reason})
    persona["unknown_regions"]=unknowns
    return persona
