# HREVN OpenClaw -> Managed API

## Goal
Give OpenClaw-native users a direct, machine-readable way to call the HREVN backend.

## Entry rule
OpenClaw uses the same managed API as:
- Codex
- Anthropic
- Google / Genkit

It does not use a separate backend.

Public managed endpoint:
- `https://api.hrevn.com`

## First call
`POST /v1/baseline-check`

## Useful sequence
1. `POST /v1/baseline-check`
2. `POST /v1/generate-bundle`
3. `POST /v1/verify-bundle`
4. `GET /v1/bundles/{bundle_id}/download`

## Required headers

```http
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

## Minimal live example

```bash
curl -s -X POST "https://api.hrevn.com/v1/baseline-check" \
  -H "Authorization: Bearer ${HREVN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @examples/baseline_check_request.json
```

## Local helper for agents

This surface also includes:
- `scripts/hrevn_openclaw_api.py`
- `openclaw_manifest.json`

Minimal usage:

```bash
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-me"
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/baseline_check_request.json
```

## Recommendation
Keep examples compact and machine-readable so autonomous/local-agent workflows can use them directly.

For the supported technical alpha test flow, see:
- `docs/OPENCLAW_ALPHA_TESTING.md`
