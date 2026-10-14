# Proposed predictive architecture

Updated 2026-10-14. Design only; no production connectors or trained predictor.

The first pilot uses Zabbix telemetry and Veeam job history. Approved exports → timestamp normalization and asset/job mapping → central history → features available before job start → baseline rules and a small ML model → temporal evaluation → advisory risk briefs → dashboard and optional LLM explanation.

Use a scheduled Python process and a central database initially. PostgreSQL and scikit-learn are implementation candidates, not deployed dependencies. Separate ingestion, training and scoring. Version datasets, labels, feature definitions, training periods, models and thresholds. Keep immutable source references and an audit trail of reviews. See [pilot design](PREDICTIVE_PILOT.md) for data contracts and validation.

Read-only scoped credentials stay server-side in a secret store; browser files contain no credentials or customer telemetry. Minimize exported fields, encrypt stored/transferred data and agree retention and deletion. Treat source text as untrusted, including when an LLM summarizes it. No shell access or autonomous remediation.

Missing/stale data, connector failures or invalid features produce an explicit unavailable assessment. Existing monitoring and paging continue. Optional LLM failure leaves the structured risk brief accessible. Uncalibrated scores must not appear as trustworthy probabilities.

For a potential 50-server estate, measure job frequency, sampling, retention and actual row size before sizing storage or compute. No GPU is assumed. Review source-specific API permissions and licenses before implementing adapters. Intune, Wazuh, Fortinet, cloud and ticket systems remain later integration candidates.
