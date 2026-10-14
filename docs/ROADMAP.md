# Predictive MVP roadmap and acceptance gates

Updated 2026-10-14. Planned work; no stage below is implemented. Delivery dates and pricing require discovery.

| Stage | Work | Exit evidence |
| --- | --- | --- |
| Discovery | Define next-backup failure, pre-start cutoff, asset/job scope and warning burden | Agreed labels, horizon, access and baseline |
| Historical dataset | Approved Zabbix + Veeam exports; successes and failures; timestamp/asset mapping | Usable history, missingness report and leakage review |
| Offline evaluation | Simple rules, logistic regression and small tree candidate | Later untouched test; recall, precision, false warnings and lead time |
| Shadow pilot | Read-only scoring and operator-reviewed briefs on a small subset | Useful warnings, acceptable burden, cost and security review |
| Controlled expansion | Expand toward 50 servers only after gates pass | Measured workload and operating ownership |
| Later integrations | Wazuh, Fortinet, Intune, cloud and tickets as evidence supports | Scoped data access and demonstrable added usefulness |

Numerical probabilities require calibration and reliability evaluation. Insufficient evidence means collect more history, narrow scope or stop. Optional LLM explanations follow the prediction baseline; they do not replace evaluation. Autonomous remediation, unrestricted control and production SLA are excluded. See [pilot design](PREDICTIVE_PILOT.md).
