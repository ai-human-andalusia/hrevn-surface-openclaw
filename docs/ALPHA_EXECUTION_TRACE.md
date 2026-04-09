# OpenClaw Alpha Execution Trace

This surface is intentionally thin:

- OpenClaw-oriented entry docs
- local helper
- live HREVN managed runtime behind `https://api.hrevn.com`

## First checks

### 1. Health check

```bash
python3 scripts/hrevn_openclaw_api.py health-check
```

Expected:
- `health_check: ok`
- `status: ok`

### 2. Self-test

```bash
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="<issued-alpha-key>"
python3 scripts/hrevn_openclaw_api.py self-test
```

Expected:
- `self_test: ok`
- `health: ok`
- `auth: ok`
- `baseline_result`
- `check_id`
- `checked_at`

### 3. Baseline check

```bash
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/baseline_check_request.json
```

Expected:
- real `BaselineResult`
- real `check_id`
- real `checked_at`

### 4. Governance gap demo

```bash
python3 scripts/hrevn_openclaw_api.py baseline-check \
  --input examples/governance_gap_request.json
```

Expected:
- `missing_required_blocks`
- `risk_flags`
- `recommended_next_step`
- `remedy_payload`

This matters because it shows that HREVN does not only return pass/fail style output.
It returns structured guidance on what evidence is still missing before a deeper workflow proceeds.
