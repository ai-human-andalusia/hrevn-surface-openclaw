# HREVN for OpenClaw - Verifiable Workflow State for Agent-First Flows

Thin OpenClaw-facing surface for the live HREVN runtime.

The helper uses only the Python standard library. No extra package install is
required for the first alpha tests.

## Quick Start

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-openclaw
cd hrevn-surface-openclaw
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
python3 scripts/hrevn_openclaw_api.py health-check
python3 scripts/hrevn_openclaw_api.py self-test
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/baseline_check_request.json
```

If the first test works, you should see a real `BaselineResult` from the live
managed runtime, including a real `check_id` and `checked_at`.

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

## What this surface gives OpenClaw
- a helper-first bridge to the live HREVN runtime
- machine-readable discovery assets for agent-first tooling
- baseline-first testing before deeper validation or bundle flows
- a compact way to inspect `missing_required_blocks`, `risk_flags`, and `remedy_payload`

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
- `docs/ALPHA_EXECUTION_TRACE.md`

The OpenClaw surface should expose compact, machine-readable examples against
the shared HREVN managed API rather than introducing a distinct backend.

Live managed endpoint:
- `https://api.hrevn.com`

Machine-readable entry assets:
- `openclaw_manifest.json`
- `scripts/hrevn_openclaw_api.py`

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

## Recommended alpha test sequence

1. `python3 scripts/hrevn_openclaw_api.py health-check`
2. `python3 scripts/hrevn_openclaw_api.py self-test`
3. `python3 scripts/hrevn_openclaw_api.py baseline-check --input examples/baseline_check_request.json`
4. `python3 scripts/hrevn_openclaw_api.py baseline-check --input examples/governance_gap_request.json`

The fourth step matters because it makes the HREVN value more concrete: the
runtime does not only say pass/fail. It returns structured guidance on what
governance evidence is still missing.

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
