# Planning assumptions — 50 servers

> Scope notice, 2026-10-13: this document describes the earlier diagnostic MVP. The current direction is historical incident prediction, described in [the customer overview](CLIENT_OVERVIEW.md). The architecture, schedule, economics and competitive position below have not been validated for that predictive scope.

Status: unvalidated planning inputs, 2026-10-13. No discovery session or workload benchmark has been completed.

| Input | Baseline assumption | Validation required |
| --- | --- | --- |
| Estate | 50 continuously monitored Linux VMs, one customer/environment | Inventory, OS versions, virtualization and network boundaries |
| Operators | 3 people; no new 24/7 coverage included | Team roles and escalation schedule |
| Existing monitoring | Already deployed; one adapter selected after discovery | Choose Zabbix or Prometheus Alertmanager; do not build both initially |
| Alert volume | 1,000 raw alerts/day across the estate | Measure at least 14 days; identify bursts and duplicates |
| Diagnostic volume | 100 briefs/day after rule-based grouping | Validate grouping; a 90% reduction is a workload assumption, not measured performance |
| Useful incidents | 100 actionable incidents/month | Label separately from raw alerts and generated briefs |
| Model workload | 4,000 input + 1,000 output tokens/brief, 30-day month | Includes retrieved context; retries and repeated calls add cost |
| Model unit costs | USD 1/million input and USD 4/million output tokens | Budget placeholders, not a vendor quote or chosen model |
| Metrics | Query bounded summaries from the existing stack | No full telemetry duplication in initial scope |
| Logs | Redacted excerpts only; 100 GB application storage envelope | Measure payload sizes; no bulk log indexing included |
| Retention | 30 days brief/context; 90 days minimal audit metadata | Customer/legal requirements; deletion and backup expiry tests |
| Labor | USD 50/hour loaded operations cost | Local compensation, overhead, currency and opportunity cost |
| Benefit | 5 / 10 / 20 minutes saved per actionable incident | Timed pilot and quality review; benefits may be zero or negative |
| Deployment | Single-tenant, private network, hosted model only after data approval | Residency, provider terms, egress and customer policy |
| Availability | Best-effort pilot; existing monitoring continues independently | No contractual SLA before operational readiness |

Windows, Kubernetes, multi-tenant SaaS, autonomous remediation, full log search, model training, and replacement of existing on-call systems are outside the MVP.

## Before estimating a customer pilot

Collect an inventory, 14-day alert sample, incident sample with operator time, data sensitivity classification, approved runbooks, integration API limits, hosting constraints, and a customer owner. Confirm whether 50 servers means physical hosts, VMs, or billed monitoring hosts. Get permission for telemetry transfer and retention. Replace each assumption with a measured value or explicitly keep it provisional.

Open decisions: hosting region, model/provider, monitoring adapter, ticketing workflow, business legal identity, public license, support hours, and customer willingness to pay. None is established by this planning pack.
