# Digital Self Engine

An open research prototype for building and testing a **generic digital-self engine**.

The central question is:

> Can the same Generic Engine learn very different people without hard-coding any one person's personality?

This project separates the **shared engine** from the **person-specific Persona Package**, then tests whether the same engine can model different people, predict unseen situations, and continue learning without collapsing everyone toward an “average person.”

---

## Start here

If you want to test the project:

1. Read [TESTING.md](TESTING.md)
2. Copy `templates/empty_persona.json`
3. Build your Persona Package locally
4. Use calibration cases to collect person-specific evidence
5. Prepare new blind scenarios that were not used during calibration
6. Freeze predictions before the participant answers
7. Collect the participant's real answers
8. Score only after the blind-test chain ends
9. Submit anonymized error summaries, not raw private data

The most useful contribution is not:

> “My model scored 90%.”

The most useful contribution is:

> “Here is a situation where the engine predicted the wrong mechanism, and here is the smallest structural change that may explain the failure.”

---

## Privacy first

Do **not** upload raw personal data by default.

Please avoid publishing:

- real names
- email addresses
- phone numbers
- home or work addresses
- private chat logs
- health or medical information
- financial identifiers
- intimate relationship details
- identifiable third-party information

Keep personal Persona Packages on your own device unless you have deliberately anonymized them.

See [PRIVACY.md](PRIVACY.md).

---

## Core design principle

The project is built around a strict separation:

### Generic Engine

The Generic Engine contains mechanisms that should be reusable across people, such as:

- state vs trait separation
- memory retrieval
- meaning memory
- relationship modulation
- intuition before deeper analysis
- decision arbitration
- competence vs subjective confidence
- process memory
- conditional policies
- self narrative
- motivation and commitment
- outcome attribution
- prediction-error attribution
- identity continuity
- long-term growth
- unknown-region handling
- provenance tracking

The Generic Engine should **not** contain one participant's personal experiences, memories, preferences, or relationship history.

### Persona Package

The Persona Package contains person-specific evidence and parameters, such as:

- stable tendencies
- conditional tendencies
- values
- current state
- memories
- relationship context
- competence beliefs
- confidence patterns
- self narrative
- unresolved thoughts
- unknown regions
- evidence provenance

Changing people should mean:

> Change the Persona Package, not the Generic Engine.

---

## Why this matters

A model can appear accurate simply because it has been manually tuned to one person.

That is not enough.

The harder question is whether:

- Person A can become A
- Person B can become B
- Person C can become C

while the engine itself stays substantially unchanged.

This repository is designed to make that claim testable.

---

## Validation philosophy

Calibration and validation must be separated.

### Calibration

Answers collected before prediction are **training/calibration evidence**.

They can be used to build or refine the Persona Package.

### Blind validation

Before asking the participant a new question, save:

- exact scenario
- model prediction
- prediction confidence
- expected mechanism
- acceptable response region
- scoring rule

Then freeze that prediction.

Only after the prediction is frozen should the participant answer.

### Reveal and score

After the blind-test chain is complete, classify each result as:

- `strong_match`
- `partial_match`
- `deviation`
- `unknown`

Then identify the smallest likely error layer.

Examples:

- state mistaken for trait
- confidence mistaken for competence
- relationship context missed
- motivation overestimated
- responsibility underestimated
- process memory ignored
- identity continuity drift
- insufficient evidence

The model should be updated **after** evaluation, not during the blind run.

---

## Evidence-first rule

Do not jump directly from one answer to a personality trait.

Store the evidence first.

Example:

Bad:

> “The participant hesitated once, therefore they are indecisive.”

Better:

> “In this high-responsibility context, the participant hesitated.”

Then test whether the pattern repeats across:

- different stakes
- different relationships
- different domains
- different emotional states
- different levels of reversibility

Stable traits should be updated more slowly than temporary state or process rules.

---

## Unknown is a valid result

The engine should not invent a personality rule simply because data are missing.

If evidence is weak, contradictory, or absent, use an unknown region.

Examples:

```json
{
  "region": "career_decisions_under_social_pressure",
  "reason": "insufficient evidence"
}
