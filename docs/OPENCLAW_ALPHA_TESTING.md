# OpenClaw Alpha Testing

## Public repo

- `https://github.com/ai-human-andalusia/hrevn-surface-openclaw`

## Live backend

- `https://api.hrevn.com`

## Supported first path

OpenClaw-style entry docs -> local helper -> `https://api.hrevn.com`

This is the supported technical alpha path for this surface.

## Setup

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-openclaw
cd hrevn-surface-openclaw
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
```

## First test

```bash
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/baseline_check_request.json
```

Expected result:
- a real `BaselineResult`
- returned from the live managed runtime
- not a mock and not a textual explanation

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
