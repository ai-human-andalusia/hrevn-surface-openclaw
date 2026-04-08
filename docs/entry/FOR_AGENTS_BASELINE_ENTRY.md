# FOR_AGENTS_ADDENDUM_BASELINE_CHECK.md
## HREVN — Addendum for agents
## Baseline Check as first entry point

### Purpose
This short addendum updates the machine-oriented entry path.

The recommended first interaction is no longer only full validation.
It is:

> **HREVN Baseline Check**

---

## Recommended first call
`POST /v1/baseline-check`

Purpose:
- detect profile fit
- detect missing required blocks
- estimate structural readiness
- recommend next step

---

## Why agents should start here
Because Baseline Check answers the question:

> **What am I missing before I attempt full validation or evidentiary generation?**

That is often more useful than immediate pass/fail validation.

---

## Expected output
Typical output includes:
- `profile_detected`
- `readiness_level`
- `missing_required_blocks`
- `risk_flags`
- `recommended_next_step`

---

## Escalation path
1. **Baseline Check** (free, limited)
2. **Profile Validation** (API key / deeper validation)
3. **Generation / Managed / Licensed access** (commercial path)

---

## Initial recommended use case
The first practical Baseline Check focus should be:

- **AI Governance**
- especially `eu_readiness_profile`

This keeps the first entry point aligned with the current HREVN product sequence.
