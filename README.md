# HREVN for OpenClaw - Verified Resume for Agent-First Workflows

Thin OpenClaw-facing surface for the live HREVN runtime.

The installable CLI uses only the Python standard library. No extra runtime
dependencies are required for the first alpha tests.

Public package:

- `https://pypi.org/project/hrevn-openclaw-cli/`

## Quick Start

Recommended local-first path:

```bash
pipx install hrevn-openclaw-cli
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
hrevn health-check
hrevn self-test
hrevn baseline
```

If you want the local repo version instead, use:

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-openclaw
cd hrevn-surface-openclaw
pipx install .
```

If `pipx` is not available, you can still install locally with:

```bash
python3 -m pip install .
```

If you prefer not to install the CLI yet, the script path still works:

```bash
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

OpenClaw-style workflows are often local-first, but they still break in costly
ways. A task can stop after partial execution, after calling external APIs, or
after building up context that is tedious to reconstruct. The problem is not
only cloud token spend. The real problem is that a broken workflow often forces
you to repeat steps you did not need to repeat.

HREVN helps OpenClaw workflows resume from a verified point after interruption.
Instead of guessing from memory or chat history, the workflow gets a structured
result that shows what happened, what is still missing, and what needs to be
corrected before moving on.

That matters in three layers:

1. verified resume for interrupted workflows
2. avoiding re-running costly external calls or tool steps
3. preserving a verifiable record of what happened and under what authority

For teams operating in regulated or high-stakes environments, HREVN also
supports evidentiary discipline: structured records of what ran, under what
authority, and when it stopped. HREVN does not make a system legally compliant,
but it provides structured, verifiable evidence that compliance, audit, and
governance processes can use.

## What this surface gives OpenClaw
- a CLI-first bridge to the live HREVN runtime
- a verified-resume path for interrupted agent workflows
- a way to avoid re-running costly external calls unnecessarily
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

Its job is to make HREVN easier to discover and use in agent-first environments
where local orchestration may still trigger costly external work. The point is
not only to save cloud spend, but to preserve a trustworthy resume point and
avoid re-running steps that did not need to be repeated.

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
- installable CLI via PyPI and `pyproject.toml`

## Alpha runtime path

Current supported alpha path:

- OpenClaw-oriented repo and manifest
- installable CLI first
- local helper as fallback
- `https://api.hrevn.com`

This is intentional. The goal of this surface is to make HREVN easy to
discover and call from agent-first environments without introducing another
runtime layer.

## Recommended first use

Start with `baseline-check` first.
Only move on to bundle generation or verification once the baseline result is understood and the workflow profile is clear.

## Recommended alpha test sequence

1. `hrevn health-check`
2. `hrevn self-test`
3. `hrevn baseline`
4. `hrevn governance-gap`

The fourth step matters because it makes the HREVN value more concrete: the
runtime does not only say pass/fail. It returns structured guidance on what
governance evidence is still missing.

## Public cut

This public surface is intentionally thin. It keeps:
- machine-readable entry docs
- compact examples
- the OpenClaw manifest
- an installable local-first CLI
- the lightweight API helper as compatibility path

It does not carry:
- internal handoff notes
- internal strategy memos
- a separate backend

## Current status
This is a thin public OpenClaw surface with a real technical alpha testing
path. It is meant for developers and agent operators who want a lightweight,
machine-readable bridge to the live HREVN runtime, especially for local-first
workflows that need a verified resume point after interruption.
