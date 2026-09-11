# How to Test the Digital Self Engine

This repository is an early research prototype. The current public version is best used to test the architecture and validation protocol. It is not yet a fully autonomous system that can infer a complete person from raw chat logs.

## Goal

The key question is not whether one person can be fit well. It is whether the same Generic Engine can represent many different people without rewriting engine logic for each person.

## Recommended participant workflow

### 1. Calibrate locally

Copy `templates/empty_persona.json` and keep the working copy on your own computer.

Use calibration situations to collect person-specific evidence. Calibration answers are training evidence, not validation evidence.

### 2. Compile only supported person-specific rules

Add rules to the Persona Package only when they are supported by evidence.

If evidence is weak, contradictory, or missing, use `unknown_regions` instead of guessing.

### 3. Prepare blind scenarios

Create new situations that were not used during calibration.

Before the participant answers, record:

- exact scenario
- predicted response
- prediction confidence
- expected mechanism
- acceptable response region
- scoring rule

### 4. Freeze predictions

Make a read-only copy before collecting answers.

Do not edit predictions after seeing participant answers.

### 5. Collect ground truth

The participant may answer freely, including:

- mixed reactions
- depends
- unknown
- a response outside the offered choices

Do not force a clean binary label when the person does not naturally have one.

### 6. Score only after the chain ends

Classify each case as:

- `strong_match`
- `partial_match`
- `deviation`
- `unknown`

Then identify the smallest likely error layer, for example:

- state vs trait
- decision arbitration
- competence vs confidence
- relationship context
- motivation / commitment
- process memory
- identity continuity
- unknown / insufficient evidence

### 7. Submit only anonymized findings

Useful public contributions are model failures and cross-person patterns, not raw private histories.

Do not upload names, contact details, private chats, health information, intimate relationship details, addresses, or identifiable third-party data.

## What counts as strong evidence for the Generic Engine?

A mechanism becomes more interesting when the same engine-level failure repeats across multiple independent participants.

A rule that fits only one participant should normally stay inside that participant's Persona Package.

## Important limitation of v0.1

The current engine skeleton does not claim validated predictive accuracy.

It mainly provides:

- separation between Generic Engine and Persona Package
- evidence-first representation
- blinded evaluation structure
- error-layer reporting
- a path toward cross-person falsification

Future versions should automate more of the persona compilation and prediction process while preserving blind-test integrity.
