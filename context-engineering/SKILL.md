---
name: context-engineering
description: Library of structured reasoning and workflow protocols (e.g. systematic reasoning, extended thinking, self-reflection, explore-plan-code-commit, debugging, refactoring) adapted from the Context-Engineering project's "Cognitive Operating System". This skill should be used when a task is complex, ambiguous, or benefits from an explicit step-by-step protocol — such as deep debugging, architectural planning, code review, or multi-stage agent workflows — and a reusable named protocol template would help structure the approach.
source: https://github.com/davidkimai/Context-Engineering
---

# Context Engineering: Cognitive Protocols

This skill provides a library of named "protocol shells" — structured templates for reasoning,
workflows, and self-improvement — adapted from the Context-Engineering project.

## When to use

Reach for a protocol when a task matches one of the patterns below and following an explicit
structure would reduce the chance of skipping steps (e.g., diving into code before exploring,
or shipping without verification).

## How to use

1. Open `references/cognitive-protocols.md`.
2. Find the protocol whose `intent` matches the current task (e.g. `/workflow.explore_plan_code_commit`,
   `/reasoning.systematic`, `/self.reflect`, `/thinking.extended`, debugging or refactoring protocols).
3. Adapt the protocol's `process` steps as a checklist for the current task — fill in `input` fields
   with the actual problem, constraints, and context, and work through each `process` step in order.
4. Use the `output` fields as a guide for what the final response should contain (e.g. solution +
   reasoning trace + verification evidence).

These protocols are templates for organizing thought and communication, not literal commands to
execute — translate each `/protocol.name{...}` block into normal actions and prose.

## Reference

`references/cognitive-protocols.md` contains the full set of protocols, including:

- Context schemas (code understanding, troubleshooting)
- Reasoning protocols (`reasoning.systematic`, `thinking.extended`)
- Self-improvement protocol (`self.reflect`)
- Workflow protocols (explore-plan-code-commit, debugging, refactoring, and more)

Grep this file for `/<category>.<name>{` to locate a specific protocol.
