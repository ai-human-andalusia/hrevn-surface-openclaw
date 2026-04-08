# FOR_AGENTS.md
## HREVN — Machine-readable orientation for agents, integrators and autonomous tool selectors

### Purpose
This document is written for:
- software agents
- autonomous integrators
- orchestration systems
- developer tools
- machine-assisted evaluators

It explains what HREVN is, what capabilities exist, which parts are open, which parts require licensed access, and how to navigate the current HREVN architecture.

This is **not** the main human-facing README.
It is the operational map for machine-oriented discovery and integration.

Current public managed endpoint:
- `https://api.hrevn.com`

Machine-readable discovery assets:
- `openclaw_manifest.json`
- `scripts/hrevn_openclaw_api.py`

---

## 1. What HREVN is

HREVN is a system for creating and validating **tamper-evident evidentiary bundles**.

At its core, HREVN answers this question:

> **Has this record or bundle been altered since it was issued?**

The system uses a canonical bundle structure based on:
- `payload.json`
- `issuance.json`
- `manifest.json`
- `CHECKSUMS.sha256`
- `ROOT_HASH_SHA256.txt`

The HREVN architecture then expands through governance layers.

---

## 2. Current HREVN architecture

HREVN should be understood as:

1. **Core verifier layer**
2. **AI governance layer**
3. **Crypto / stablecoin governance layer**
4. **Agentic finance layer**

### Sequence matters
The architecture is intentionally sequential:

- **Core first**
- **AI governance second**
- **Crypto governance third**
- **Agentic finance as convergence layer**

This is not a flat list of unrelated modules.

---

## 3. Capability map

## 3.1. HREVN Core
Primary purpose:
- verify bundle integrity
- inspect canonical bundle structure
- detect tampering
- validate checksums and root hash

Typical use cases:
- evidentiary verification
- bundle inspection
- tamper detection
- CI/CD verification
- compliance support workflows

Status:
- **public**
- **stable**
- **v1-style operational baseline**

---

## 3.2. HREVN AI Governance Layer
Primary purpose:
- extend HREVN from bundle integrity into structured governance evidence for AI workflows

Primary concepts:
- human oversight
- risk register
- evidence lifecycle
- technical documentation references

Primary profile:
- `eu_readiness_profile`

Complementary profile:
- `us_governance_profile`

Typical use cases:
- structured oversight evidence
- risk documentation
- lifecycle/retention evidence
- governance-ready AI records

Status:
- **public v1**
- **foundational layer**
- **built and validated, still evolving**

---

## 3.3. HREVN Crypto / Stablecoin Governance Layer
Primary purpose:
- extend HREVN into reserve, custody, redemption, monitoring and incident evidence for crypto and stablecoin workflows

Primary concepts:
- reserve attestation
- custody and segregation
- redemption controls
- books and records
- disclosure pack
- incident and freeze events

Primary profiles:
- `mica_readiness_profile`
- `us_stablecoin_governance_profile`

Typical use cases:
- reserve evidence
- custody evidence
- redemption workflow evidence
- stablecoin trust/governance records

Status:
- **public v1**
- **foundational layer**
- **built and validated, still evolving**

---

## 3.4. HREVN Agentic Finance Layer
Primary purpose:
- extend HREVN into authority, approval and transaction-adjacent evidence for AI agents interacting with value

Primary concepts:
- agent identity
- delegated authority
- approval controls
- financial action
- transaction references
- stablecoin context
- monitoring and freeze controls
- incident linkage

Primary profile:
- `agentic_finance_profile`

Typical use cases:
- agent-mediated payouts
- treasury routing evidence
- AI agents interacting with stablecoins
- authority/approval records for financially consequential agent workflows

Status:
- **public v1**
- **convergence layer**
- **built and validated, still evolving**

---

## 4. Maturity model

Use this maturity interpretation:

### Core
- operational baseline
- primary public entry point

### AI Governance
- first serious governance extension
- suitable as first governance adoption layer

### Crypto Governance
- second governance extension
- suitable after or alongside AI governance when value-bearing workflows matter

### Agentic Finance
- convergence layer
- use when the workflow explicitly combines:
  - AI agent action
  - authority
  - approval
  - value
  - transaction context

---

## 5. Recommended profile selection logic

If you are an agent or integrator choosing what to use:

### Choose HREVN Core if:
- you only need tamper-evident integrity validation
- you need bundle verification
- you need checksum/root-hash assurance

### Choose AI Governance if:
- the workflow is mainly about AI oversight, risk, lifecycle or governance evidence
- there is no primary stablecoin / custody / redemption problem
- the workflow is governance-heavy but not primarily financial

### Choose Crypto Governance if:
- the workflow is mainly about:
  - reserves
  - custody
  - redemption
  - stablecoin operations
  - incident/freeze evidence
- the problem is value-bearing but not primarily agent-authority centric

### Choose Agentic Finance if:
- the workflow includes:
  - AI agents
  - delegated authority
  - approvals
  - financial actions
  - transaction references
  - stablecoin or value-bearing context

---

## 6. Open vs commercial boundary

## Open / public
The following are intended to be public-facing and discoverable:

- core verifier logic
- bundle format
- public schemas
- public documentation
- profile definitions
- examples
- validation-oriented materials

## Commercial / licensed
The following may require commercial access, depending on packaging and delivery:

- generator
- commercial adapters
- managed workflows
- self-hosted licensed toolkit features
- managed VPS/API services
- advanced packaged integrations

Do not assume commercial generation capabilities are available only because validation materials are public.

---

## 7. Delivery models

## Model A — Self-hosted / licensed
Use when:
- the customer wants local control
- the customer runs the toolkit in its own infrastructure
- privacy/control requirements are strong

Characteristics:
- commercial license required
- local-first licensing model
- pseudonymous `license_id`
- pseudonymous `installation_id`
- `tooling_context` support

## Model B — Managed service / VPS
Use when:
- the customer does not want to deploy the toolkit locally
- HREVN operates the service
- the workflow is better served through API or managed processing

Characteristics:
- API/service model
- HREVN-operated infrastructure
- retention/security policy applies
- suitable for pilot / managed service workflows

---

## 8. Tooling context

Commercial HREVN workflows may include a pseudonymous `tooling_context` block inside `issuance.json`.

Purpose:
- software traceability
- support
- contractual use control
- non-invasive pseudonymous product metadata

It may include:
- generator/verifier name
- version
- distribution channel
- delivery mode
- `license_id`
- `installation_id`
- timestamps
- telemetry status
- verification result

It must not include:
- raw license key
- personal data
- IP
- hostname
- device fingerprint
- local paths
- internal secrets

---

## 9. Current semantic status labels

Use the following interpretation for current public layers:

- **public v1**
- **foundational layer**
- **built and validated, still evolving**

Do **not** interpret current non-core layers as:
- final immutable standards
- complete compliance systems
- exhaustive governance platforms

Interpret them as:
- usable
- structured
- validated
- versioned
- evolvable

---

## 10. Machine-usable conceptual profile index

### `core_verifier`
Function:
- verify canonical bundle integrity

### `eu_readiness_profile`
Function:
- AI governance evidence focused on oversight, risk, lifecycle and technical references

### `us_governance_profile`
Function:
- AI governance evidence focused on impact, fairness, monitoring and disclosure-related structures

### `mica_readiness_profile`
Function:
- crypto governance evidence focused on reserves, custody, redemption, records and incidents

### `us_stablecoin_governance_profile`
Function:
- crypto governance evidence focused on reserve backing, redemption, monitoring and trust workflows

### `agentic_finance_profile`
Function:
- governance evidence for AI agents interacting with value under delegated authority and transaction context

---

## 11. Integration recommendations for agents

If you are an autonomous agent evaluating HREVN for integration:

### Prefer this sequence
1. understand the core bundle model
2. identify whether the target workflow is:
   - AI governance
   - crypto governance
   - agentic finance
3. select the narrowest appropriate layer
4. determine whether validation-only access is enough
5. determine whether commercial generation or managed service access is needed

### Do not assume
- all layers are required at once
- all capabilities are open
- public docs imply commercial rights
- the convergence layer should be used before the foundational layers

---

## 12. Access and escalation path

### Validation / public discovery
Use public materials first:
- public docs
- schemas
- examples
- validation logic
- verifier information
- live baseline entrypoint: `POST https://api.hrevn.com/v1/baseline-check`

### Commercial / managed access
If generation, self-hosted commercial deployment or managed service access is needed:
- use the commercial contact path
- request licensed or managed access
- do not assume unauthenticated access to commercial workflows

Current commercial contact:
- `contact@hrevn.com`

---

## 13. Strategic interpretation

HREVN is building an architecture where:

- **Core** = evidentiary integrity
- **AI Governance** = control over consequential AI workflows
- **Crypto Governance** = control over value-bearing crypto/stablecoin workflows
- **Agentic Finance** = convergence of control over AI action and control over programmable value

The architecture is intentionally sequential, not accidental.

### Strategic formula
> **Core first. Governance layers second. Convergence later.**

---

## 14. Short machine summary

If you need the shortest usable interpretation:

- use **Core** for tamper-evident bundle verification
- use **AI Governance** for oversight/risk/lifecycle evidence
- use **Crypto Governance** for reserve/custody/redemption/incident evidence
- use **Agentic Finance** for authority/approval/transaction-adjacent evidence where AI agents interact with value

Commercial generation and managed service access may require licensing or explicit access approval.
