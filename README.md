# Digital Self Engine

A research project for building a digital agent that behaves as much as possible like a specific real person.

The core question is:

> If we know enough about a person, can we build an agent that thinks, reacts, decides, remembers, hesitates, and changes in a way that still feels like that person?

The goal is not to create a personality type.

The goal is to model **an individual person**.

---

## What we want

When a new situation appears, the system should not answer like an average person.

It should try to answer:

> “What would this person most likely think, feel, say, or do?”

A realistic digital self may:

- hesitate
- change its mind
- make mistakes
- trust different people differently
- feel less confident under responsibility
- keep emotional residue
- hold conflicting thoughts at the same time

The goal is not the best decision.

The goal is the decision that is most consistent with that person.

---

## How it works

We separate the system into two parts.

### Generic Engine

Shared mechanisms such as:

- memory
- current state
- intuition
- reasoning
- relationships
- competence
- confidence
- responsibility
- motivation
- habits
- learning
- identity continuity

### Persona Package

Person-specific information such as:

- memories
- values
- relationships
- decision tendencies
- confidence patterns
- personal rules
- unknown areas

So:

> Same Engine + different Persona Package = different person

If every new person requires rewriting the engine, the engine is not truly general.

---

## How we test it

We use blind prediction.

1. Learn from earlier evidence
2. Create a new unseen situation
3. Predict the person's response
4. Freeze the prediction
5. Ask the real person
6. Compare prediction with reality
7. Update the model only afterward

The rule is:

> prediction first, answer second

Wrong predictions are useful because they reveal what the model misunderstood.

---

## The harder problem: change

A digital self should not stay frozen forever.

Real people change.

But if the agent changes too quickly, it may stop feeling like the original person.

So another major research question is:

> How much can a digital self change while still remaining a plausible continuation of the same person?

---

## Current status

This is an early research prototype.

It currently includes:

- Generic Engine prototype
- Persona Package structure
- blind-test protocol
- frozen-prediction verification
- cross-person testing
- identity-continuity ideas
- privacy and anonymized contribution rules

It does **not** claim:

- consciousness transfer
- perfect personality reconstruction
- certain prediction of human behavior
- scientific validation

---

## Want to test yourself?

You do not need to be a programmer.

Start with:

- [NO_CODE_TESTING.md](NO_CODE_TESTING.md)
- [TESTING.md](TESTING.md)
- [PRIVACY.md](PRIVACY.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

Programmers can also use:

`tools/blind_test_cli.py`

---

## Privacy

Do not upload raw personal data.

Keep private Persona Packages on your own device.

This public repository contains no private Person A data.

---

## Long-term vision

The long-term goal is not a chatbot that merely knows facts about you.

It is a system that preserves enough of your:

- ways of thinking
- ways of deciding
- memories
- relationships
- emotional patterns
- uncertainty
- habits
- contradictions
- growth trajectory

that, when something new happens, its response still feels like:

> “Yes — that is probably how this person would respond.”

That is the goal of Digital Self Engine.
