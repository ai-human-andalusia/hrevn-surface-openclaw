# OpenClaw Alpha Testing

## Public repo

- `https://github.com/ai-human-andalusia/hrevn-surface-openclaw`

## Live backend

- `https://api.hrevn.com`

## Supported first path

OpenClaw-style entry docs -> local helper -> `https://api.hrevn.com`

This is the supported technical alpha path for this surface.

The helper uses only the Python standard library, so the first alpha tests do
not require extra package installation.

## Setup

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-openclaw
cd hrevn-surface-openclaw
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
```

## Preflight

Run this first to separate basic reachability from auth:

```bash
python3 scripts/hrevn_openclaw_api.py health-check
```

Expected result:
- `health_check: ok`
- `status: ok`

Then run auth + runtime validation:

```bash
python3 scripts/hrevn_openclaw_api.py self-test
```

Expected result:
- `self_test: ok`
- `health: ok`
- `auth: ok`
- a real `check_id`
- a real `checked_at`

## First test

```bash
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/baseline_check_request.json
```

Expected result:
- a real `BaselineResult`
- returned from the live managed runtime
- not a mock and not a textual explanation

## Governance gap demo

This is the best follow-up test if you want to see why HREVN is useful beyond
simple pass/fail style output:

```bash
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/governance_gap_request.json
```

Expected result:
- `missing_required_blocks`
- `risk_flags`
- `recommended_next_step`
- `remedy_payload`

## What to test next

After the baseline result is understood, you can move on to:
- `generate-bundle`
- `verify-bundle`
- `download-bundle`

## Important notes

- this is a technical alpha
- the runtime truth is in the managed API
- the helper is the supported bridge in this alpha
- do not commit live API keys into docs or manifests
- for a compact proof trail, see `docs/ALPHA_EXECUTION_TRACE.md`
