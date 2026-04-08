# HREVN OpenClaw Surface

Machine-readable and agent-first entry surface for HREVN.

## Why HREVN

AI agents and multi-step workflows fail in ambiguous ways. When a sequence is
interrupted, neither the user nor the system can always determine with
certainty what completed, what failed mid-execution, and where work can safely
resume. Without a verifiable record, context is reconstructed from memory or
chat history, wasting tokens, repeating work, and leaving no reliable trail.

HREVN adds a structured evidence layer: baseline checks before consequential
steps, tamper-evident receipts after execution, and manifests that allow
workflows to continue from the last verified point rather than restarting from
scratch.

For teams operating in regulated or high-stakes environments, HREVN also
supports evidentiary discipline: structured records of what ran, under what
authority, and when it stopped. This is particularly relevant for AI systems
that may fall within EU regulatory timelines in 2026 and beyond. HREVN does
not make a system legally compliant, but it provides structured, verifiable
evidence that compliance, audit, and governance processes can use.

OpenClaw gives agent-first workflows a verifiable action trail, so when
execution stops, the next call can resume from the last trusted point instead
of reconstructing state from scratch.

## Purpose
This surface gathers the OpenClaw-oriented entry documents:
- machine-readable orientation for agents and integrators
- Baseline Check as first entry point
- first-use-case decisions
- managed-access path
- a lightweight helper bridge to the live managed runtime

## What this is not
- not the HREVN core
- not the canonical home of schemas or baseline semantics
- not a replacement for the technical core
- not a separate backend

## Relationship with the core
This surface consumes the canonical HREVN core through the managed runtime and explains how an agent-first environment should enter it:
1. Baseline Check first
2. deeper validation second
3. generation / managed access later

## Direction
OpenClaw is now treated as a dedicated public-facing surface candidate.

Its job is to make HREVN easier to discover and use in agent-first environments while still calling the same managed API as the other public surfaces.

## Managed Runtime Bridge

See:
- `docs/integration/MANAGED_API_USAGE.md`
- `docs/OPENCLAW_ALPHA_TESTING.md`

The OpenClaw surface should expose compact, machine-readable examples against
the shared HREVN managed API rather than introducing a distinct backend.

Live managed endpoint:
- `https://api.hrevn.com`

Machine-readable entry assets:
- `openclaw_manifest.json`
- `scripts/hrevn_openclaw_api.py`

## Quick Start

```bash
export HREVN_API_KEY="replace-me"
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/baseline_check_request.json
```

The command above should return a real `BaselineResult` from the live managed runtime.

## Alpha runtime path

Current supported alpha path:

- OpenClaw-oriented repo and manifest
- local helper
- `https://api.hrevn.com`

This is intentional. The goal of this surface is to make HREVN easy to
discover and call from agent-first environments without introducing another
runtime layer.

## Recommended first use

Start with `baseline-check` first.
Only move on to bundle generation or verification once the baseline result is understood and the workflow profile is clear.

## Public cut

This public surface is intentionally thin. It keeps:
- machine-readable entry docs
- compact examples
- the OpenClaw manifest
- the lightweight API helper

It does not carry:
- internal handoff notes
- internal strategy memos
- a separate backend

## Current status
This is a thin public OpenClaw surface with a real technical alpha testing
path. It is meant for developers and agent operators who want a lightweight,
machine-readable bridge to the live HREVN runtime.
