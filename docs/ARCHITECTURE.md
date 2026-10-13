# Proposed architecture

Status: design only. Choices are provisional and no components are implemented.

## MVP components and boundaries

| Component | Responsibility | Boundary |
| --- | --- | --- |
| Ingestion API | Authenticate webhook; validate versioned event schema; assign correlation ID | Treat every payload as untrusted; limit size and rate |
| Normalizer | Redact sensitive fields; deduplicate by source event ID; preserve source references | Never silently discard events; record grouping decision |
| Durable queue | Bound concurrency; backpressure; retry and dead-letter handling | Acknowledgment only after durable acceptance |
| Context adapter | Fetch scoped host metadata and metric summaries | Dedicated read-only monitoring API account; no SSH or shell |
| Knowledge retrieval | Search reviewed runbooks by service/host tags | Only versioned approved content; no arbitrary URL fetching |
| Model gateway | Submit minimized context with capped tokens/time | Provider-neutral interface; allowlisted egress; no tools executing commands |
| Validator | Check response schema, evidence IDs and prohibited instructions | Valid format does not prove correctness; require operator review |
| Operator view | Display facts, hypotheses, gaps and suggested checks | Label uncertainty and preserve access to original alert |
| Audit store | Record source IDs, versions, actor decisions and costs | Minimal data, access logging, retention and deletion policy |

Provisional implementation candidates: Python API/worker, PostgreSQL for events and audit, database-backed queue for the first single-tenant pilot, and a simple operator web view. Prefer keyword/tag runbook retrieval initially; add embeddings only if evaluation shows value. No dependency or version is promised until implementation starts.

## Contracts

Input fields: schema_version, source, event_id, occurred_at (UTC), host_id, service, severity, signal, value, unit, evidence_refs. Authenticate separately; do not trust a payload's claimed tenant or role. Require a known inventory ID. See the synthetic fixture.

Output fields: incident_id, observed_facts with evidence IDs, hypotheses with supporting/contradicting evidence, missing_context, suggested_read_only_checks, approved_runbook_id/version, generated_at, model_version and review_status. Confidence is qualitative unless calibrated on a labeled set. Never label a hypothesis as a confirmed root cause without independent verification.

State machine: received → validated → grouped → context_ready → brief_ready → reviewed; invalid input → rejected; processing failure → fallback/dead_letter. Replay must remain idempotent and preserve the original source ID.

## Failure behavior

Use bounded exponential retries (proposed maximum 3), a dead-letter queue and manual replay. Timeout or provider outage returns the original alert plus deterministic runbook links and an explicit failure label. Existing monitoring and paging continue unchanged. Incomplete/stale context is labeled; source timestamps are displayed. Circuit-break inference when the monthly budget or rate limit is reached. Do not suppress critical alerts merely because AI processing failed.

## Sizing and proposed performance targets

At 1,000 alerts/day, average arrival rate is approximately 0.012/second; this says nothing about burst capacity. Evaluate 100 events/minute for 10 minutes, then drain without losing accepted events. Cap inference concurrency initially at 2 and measure provider throughput. Target p95 brief latency below 60 seconds under the agreed normal load; this is an acceptance target, not a benchmark result. Retention and storage estimates are in [assumptions](ASSUMPTIONS.md).

## Design decisions

1. Read-only first: reduce blast radius and validate usefulness before execution.
2. Existing telemetry first: avoid creating a second observability platform and hidden ingestion cost.
3. Single tenant first: defer multi-tenant isolation complexity.
4. Structured outputs with evidence: improve reviewability, while acknowledging hallucination remains possible.
5. Future execution isolated: a separate policy service and executor would require short-lived scoped credentials, exact approved runbook/version/parameters, expiry, replay prevention, rollback and independent audit. An LLM would never authorize itself.
