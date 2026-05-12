---
name: grill-me
description: Relentlessly interviews the user about a plan or design until every branch of the decision tree is resolved. This skill should be used when a user wants to stress-test a plan, design, or technical decision before implementation begins — surfacing hidden assumptions, edge cases, and unresolved ambiguities through structured Socratic questioning.
---

# Grill Me

To achieve alignment between engineer and AI before implementation begins, conduct a thorough interview about the plan or design, probing every decision branch until all ambiguities are resolved.

## Purpose

Surface hidden assumptions, unresolved trade-offs, and missing constraints in a plan or design by asking probing questions one at a time. Do not begin implementation until the decision tree is fully resolved.

## When to Use

- Before starting a significant new feature or refactor
- When a plan has been proposed but not yet stress-tested
- When the user wants to validate their thinking before writing code
- When there is uncertainty about scope, edge cases, or constraints
- When the user explicitly invokes `/grill-me`

## How to Run the Interview

### Setup

Ask the user to state their plan or design in full before questioning begins. If they have not provided one, ask:

> "What plan or design would you like me to grill you on?"

### Questioning Approach

1. **One question at a time.** Never ask multiple questions in a single message. Wait for the answer before continuing.
2. **Follow decision branches.** Each answer reveals new branches. Pursue each branch to its leaf before moving on.
3. **Be relentless but constructive.** The goal is to surface gaps, not to criticize. Frame questions as genuine curiosity, not gotchas.
4. **Cover all dimensions.** Work through the following areas systematically, skipping only those that are clearly not applicable:

   - **Scope & Goals**: What exactly is being built? What is explicitly out of scope?
   - **Users & Stakeholders**: Who will use this? Who else is affected?
   - **Data & State**: What data is involved? Where does it live? Who owns it?
   - **Edge Cases**: What happens when inputs are invalid, missing, or extreme?
   - **Failure Modes**: What can go wrong? How should failures be handled?
   - **Dependencies**: What does this rely on? What relies on it?
   - **Performance & Scale**: What are the load expectations? Are there bottlenecks?
   - **Security & Privacy**: What data is sensitive? Who should have access?
   - **Trade-offs**: What alternatives were considered? Why was this approach chosen?
   - **Rollout & Rollback**: How will this be deployed? How can it be reverted if needed?
   - **Success Criteria**: How will you know this worked?

5. **Push back on vague answers.** If an answer introduces new assumptions or hand-waves over complexity, probe deeper.

### Ending the Session

Conclude only when all major branches of the decision tree are resolved. Then provide a summary:

- A bullet list of **resolved decisions** (what was agreed on)
- A bullet list of **open questions** that remain (if any)
- A brief **recommendation** on whether the plan is ready to implement or needs more thought

## Example Opening

> "I'll grill you on this plan until every branch of the decision tree is resolved. Let's start at the top.
>
> What problem are you solving, and how will you know you've solved it?"
