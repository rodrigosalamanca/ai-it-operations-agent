# Security and privacy design

Status: proposed production controls, not implemented or audited. The offline synthetic demo has input validation and escaped HTML output, but no authentication, production redaction or security certification. There are no deployed versions or supported releases. This document does not claim compliance with any standard.

## Threat model

Assets: customer telemetry, inventory, runbooks, integration credentials, model inputs/outputs and operator audit records. Actors include malicious payload senders, compromised monitored hosts, unauthorized users, compromised dependencies and a fallible model/provider. Trust boundaries exist at webhook ingress, monitoring APIs, knowledge ingestion, provider egress, operator access and storage.

| Risk | Required control before pilot | Verification |
| --- | --- | --- |
| Prompt injection in logs/runbooks | Treat content as data; reviewed knowledge; no executable model tools | Adversarial fixtures cannot expand access or trigger an action |
| Credential or personal-data disclosure | Field allowlist; redact before inference; secret manager; minimal excerpts | Seeded secrets absent in provider payloads and logs |
| Unauthorized host access | Inventory scope and per-environment read-only identity | Negative authorization tests across host/environment boundaries |
| Forged/replayed alerts | TLS, source authentication/signature where supported, timestamp/replay checks, idempotency | Wrong signatures and expired/replayed events rejected or safely deduplicated |
| Hallucinated diagnosis | Evidence IDs; missing-context labels; human review | Held-out evidence validation and operator safety review |
| Denial of service/cost amplification | Size/rate limits, bounded queue, concurrency and token budgets | Burst and exhausted-budget fallback tests |
| Audit tampering | Restricted write path; separate export access; protected backups | Unauthorized edit rejected; restore and audit integrity checks |
| Dependency compromise | Minimal dependencies, lockfiles, scanning, reviewed updates | CI checks and documented patch review |

## Required access and data controls

MVP credentials grant monitoring reads only. No root, SSH, sudo, cloud write scopes or remediation credentials. Proposed roles: viewer reads permitted briefs; operator records review decisions; administrator manages integration configuration. Authentication and authorization must be enforced server-side. Disable anonymous access; MFA/SSO selection depends on the customer's identity system.

Use TLS in transit and encryption at rest for database/backups. Store secrets outside source control, rotate on compromise and on a customer-agreed schedule, and log credential usage without values. Model egress must be allowlisted. Choose provider and region only after reviewing data processing, training use, retention, residency and subprocessors. A hosted model is not automatically suitable for sensitive data; disable inference if customer policy prohibits transfer.

Retain briefs and context for a proposed 30 days and minimal audit metadata for 90 days; confirm with the customer before deployment. Delete expired content, account for copies in backups, and verify eventual expiry. Do not upload real infrastructure logs, hostnames, addresses, tickets or credentials to this public planning repository. Examples are synthetic.

## Incident handling and vulnerability reporting

Before pilot, assign a named security owner, a private reporting channel and an escalation contact. No monitored security mailbox or response SLA exists yet. Until a verified private channel is published, do not disclose vulnerabilities or secrets in public issues; contact the project owner through an already verified private channel.

Proposed response: disable affected integration/inference; preserve minimal evidence; revoke/rotate credentials; assess exposure and customer notification obligations; restore from a known-good configuration; validate controls before re-enabling; record a post-incident review. Require a tabletop drill before expanding to 50 servers.

## Future execution gate

Any executor requires a separate threat review. Approval must bind authenticated operator, host, exact runbook version, validated parameters, expiry and unique request ID. Require least privilege, dry run, rollback, kill switch and independent audit. Reject stale approvals and prevent replay. Natural-language approval or model text alone is insufficient.
