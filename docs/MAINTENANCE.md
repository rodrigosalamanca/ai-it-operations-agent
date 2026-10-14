# Maintenance and operations plan

Design only. No production service or active support obligation exists. Before a pilot, assign primary and backup owners for application, monitoring integration, security, runbooks and customer escalation. Rodrigo Salamanca is the proposed project owner, not an assumed 24/7 responder.

| Cadence | Proposed work | Record |
| --- | --- | --- |
| Daily during pilot | Check ingestion failures, queue age, provider errors, costs and unresolved critical alerts | Pilot health log and escalations |
| Weekly | Review rejected briefs, stale runbooks, alert grouping and sampled evidence accuracy | Quality trend and approved corrections |
| Monthly | Dependency/model changes, API compatibility, access review, cost versus benefit | Change record and updated financial inputs |
| Quarterly | Restore drill, incident tabletop, retention/deletion test, permission review | Drill results and remediation owners |
| On monitoring/model changes | Run held-out regression and privacy/security checks before rollout | Versioned evaluation report |

## Reliability and recovery

Monitor accepted/rejected event counts, queue oldest age, retries, dead-letter volume, model latency/failure, token spend, valid evidence rate and operator rejection rate. Set customer-specific alerts; proposed queue-age trigger is 5 minutes and spend warnings at 80% of the approved cap. These thresholds need calibration.

Take encrypted daily database/configuration backups with an initial 7-day backup retention, separate credentials and an off-host copy. Confirm data deletion implications. Proposed pilot recovery targets: RPO 24 hours and RTO 4 hours; neither is validated. Keep existing monitoring and paging independent. Test restoration before pilot and quarterly thereafter. Recovery steps: stop processing, restore verified snapshot, validate inventory/roles/secrets, replay retained source events idempotently, compare counts and re-enable with owner approval.

## Changes and maintenance

Version application, schemas, prompts, runbooks and evaluation data separately. Require pull request review, release notes, pinned dependencies and rollback instructions once code exists. Stage changes on synthetic data, then limited pilot hosts. Revert model/prompt changes if evidence accuracy or safety gates regress. Back up before schema migrations; prove restore compatibility. Prioritize critical security findings immediately with an owner and a risk-based mitigation deadline; no unsupported patch SLA is promised.

Budget 4 hours/month routine maintenance in the base financial case, excluding major incidents and upgrades. Track actual time and revise the estimate. If costs, queue failures or quality deteriorate, disable inference and use deterministic alert/runbook output. Document support hours, escalation, handover and end-of-life policy before any paid deployment.


## 2026-10-14 — Current predictive pilot scope

The proposed first pilot is **next-backup failure prediction using Zabbix + Veeam**. Start with approved historical exports, including successful jobs and failures, then consider scoped read-only APIs. Compare simple rules with a small ML model on later held-out data; measure recall, precision, false warnings, advance notice and operator effort. Numerical probabilities require calibration. The optional LLM explains evidence; it does not calculate or validate the predictive model. No trained predictor or live connectors are implemented. Wazuh, Fortinet, Intune and other sources remain later candidates. See [the pilot design](PREDICTIVE_PILOT.md) for the source of truth.

Pilot maintenance must track input freshness, missingness, label quality, feature drift, delayed outcomes, calibration and false-warning burden. Retraining requires a reviewed dataset, temporal evaluation and versioned approval; never auto-promote a new model. Preserve rollback to the prior model or suspend scoring. Assign separate ownership for data pipelines, prediction quality and optional LLM processing.
