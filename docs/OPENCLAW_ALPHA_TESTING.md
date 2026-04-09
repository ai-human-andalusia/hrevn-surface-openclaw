# OpenClaw Alpha Testing

## Public repo

- `https://github.com/ai-human-andalusia/hrevn-surface-openclaw`

## Live backend

- `https://api.hrevn.com`

## Supported first path

OpenClaw-style entry docs -> local helper -> `https://api.hrevn.com`

This is the supported technical alpha path for this surface.

The CLI uses only the Python standard library, so the first alpha tests do not
require extra runtime dependencies beyond Python and `pipx`.

Public package:

- `https://pypi.org/project/hrevn-openclaw-cli/`

## Setup

Preferred local-first setup:

```bash
pipx install hrevn-openclaw-cli
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
```

If you want to test from the repo checkout instead, use:

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-openclaw
cd hrevn-surface-openclaw
pipx install .
```

If `pipx` is not available, a local fallback is:

```bash
python3 -m pip install .
```

Fallback script-only setup:

```bash
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
```

## Preflight

Run this first to separate basic reachability from auth:

```bash
hrevn health-check
```

Expected result:
- `health_check: ok`
- `status: ok`

Then run auth + runtime validation:

```bash
hrevn self-test
```

Expected result:
- `self_test: ok`
- `health: ok`
- `auth: ok`
- a real `check_id`
- a real `checked_at`

## First test

```bash
hrevn baseline
```

Expected result:
- a real `BaselineResult`
- returned from the live managed runtime
- not a mock and not a textual explanation

## Governance gap demo

This is the best follow-up test if you want to see why HREVN is useful beyond
simple pass/fail style output:

```bash
hrevn governance-gap
```

Expected result:
- `missing_required_blocks`
- `risk_flags`
- `recommended_next_step`
- `remedy_payload`

## What to test next

After the baseline result is understood, you can move on to:
- `hrevn generate-bundle --input examples/generate_bundle_request.json`
- `hrevn verify-bundle --source /path/to/bundle.zip`
- `hrevn download-bundle --bundle-id <bundle_id> --output bundle.zip`

## Important notes

- this is a technical alpha
- the runtime truth is in the managed API
- the PyPI-distributed CLI is the preferred bridge in this alpha
- the helper scripts remain available for compatibility
- do not commit live API keys into docs or manifests
- for a compact proof trail, see `docs/ALPHA_EXECUTION_TRACE.md`
