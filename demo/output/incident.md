# North Maple Systems — IT Operations Agent

**Synthetic offline demo · No AI · No infrastructure actions**

## Observed facts

- Disk utilization was reported at 91% on lab-linux-01 at 2026-10-13T12:00:00Z. Evidence: synthetic-event-001.
- Disk utilization changed from 75% to 91% over 6 hours (+16 percentage points). Evidence: synthetic-metric-000, synthetic-metric-001.

## Time to next configured threshold

Next configured threshold: 95% (synthetic demo configuration). Observed growth: 2.67 percentage points/hour. Estimated time: 1.50 hours from the last sample (2026-10-13T12:00:00Z); projected crossing: 2026-10-13T13:30:00+00:00.

Linear scenario, not a guaranteed alert delivery time. Two points cannot establish normal background growth; longer history is required. No cleanup, capacity change or workload change is assumed.

Evidence: synthetic-event-001, synthetic-metric-000, synthetic-metric-001

## Unconfirmed hypotheses

- Log growth is one possible cause, but no supporting log-size evidence is available. Data growth or insufficient filesystem capacity are alternatives.

## Missing context

- Directory growth and log sizes are unknown.
- Service impact is unknown.
- Inode utilization is unknown.

## Suggested read-only checks

- Review disk utilization history in the existing monitoring tool.
- Review mount capacity and inode utilization using read-only monitoring views.
- Ask an authorized operator to inspect directory-size summaries without transmitting file contents.
- Confirm service impact before selecting any remediation.

Runbook: disk-triage@0.1 (demo-only)

**Actions executed: none.**

Review: pending (local demo annotation, not authenticated approval).

