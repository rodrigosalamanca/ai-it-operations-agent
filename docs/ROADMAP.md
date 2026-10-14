# MVP roadmap and acceptance gates

A preliminary offline synthetic demo is available with focused validation tests. It does not complete any production milestone below. Illustrative schedule: 8–10 weeks with one engineer at approximately 20 hours/week, plus operator/security review. This is a planning estimate, not a delivery commitment; the 200 engineering hours in the financial model exclude reviewer time.

| Milestone | Planned work | Evidence required to exit |
| --- | --- | --- |
| M0 Discovery, week 1 | Inventory, data classification, choose one adapter, label incidents, approve runbooks | Owner signs scope; 14-day alert baseline; data-transfer decision |
| M1 Ingestion, weeks 2–3 | Authentication, schema, durable acceptance, redaction, grouping, audit | Replay produces no duplicate processing; burst test has zero accepted-event loss; malformed/unauthorized payloads rejected |
| M2 Diagnostic prototype, weeks 4–5 | Read-only context, retrieval, bounded model gateway, schema validation, fallback | Evidence references resolve; model outage falls back; budgets/timeouts enforced |
| M3 Evaluation, weeks 6–7 | Operator review, labeled scenarios, injection and privacy tests | At least 50 held-out scenarios; at least 80% briefs rated useful by two operators; zero executable actions; zero exposed seeded secrets |
| M4 Supervised pilot, weeks 8–10 | 5 servers first, then 10, then 50 after review | At least 2 weeks pilot observation; p95 normal-load latency <60s; measured labor benefit and rejection rates; security and operations sign-off |

## Evaluation protocol

Split development and held-out scenarios before tuning. Include disk pressure, CPU saturation, service unavailability, stale telemetry, contradictory evidence, duplicate alerts, missing runbooks, model outage and malicious log content. Record baseline manual triage time and assisted time for comparable cases; include review time and failed recommendations. Report sample size, distributions, operator disagreement and incident mix. Do not extrapolate lab results to production savings without a customer pilot.

Every factual statement should have a valid evidence reference or be labeled as missing/unverified. Require zero unsupported high-impact recommendations in the held-out set; failing that gate blocks pilot expansion. Security tests include cross-host access, unauthorized role, prompt injection, source spoofing, oversized payload, secrets redaction and budget exhaustion. Required targets are ambitions, not existing results.

## Explicit exclusions

No shell execution, patching, reboot, destructive cleanup, autonomous remediation, Windows/Kubernetes adapter, multi-customer tenancy, billing system or 24/7 SLA in the MVP. Ticket creation, notifications and additional integrations require separately agreed scope and permissions.

## Beyond MVP

M5: approval-controlled execution of one reversible runbook in a lab, with rollback and replay prevention. M6: additional integrations only after usage evidence. M7: commercial readiness with support ownership, license, procurement, incident response drills and customer agreements. Stop or narrow the product if quality gates fail, privacy requirements cannot be met, or measured benefit does not justify full cost.
