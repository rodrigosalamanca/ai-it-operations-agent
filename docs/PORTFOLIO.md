# Customer-facing portfolio copy

**North Maple Systems — IT Operations Agent**  
**Predictive Incident Intelligence · In development**

A proposed IT operations product designed to recognize patterns that preceded past incidents and identify similar warning signals in the current environment. The planned workflow combines approved monitoring and incident-history sources to produce preventive risk briefs with supporting evidence and operator-reviewed next steps.

The first pilot will focus on one incident category and measure advance notice, missed incidents and false alarms against existing monitoring. Predictive models and live connectors are not implemented; the existing synthetic diagnostic demonstration is an earlier experiment.

CTA: **Explore the product overview** → [Customer documentation](https://github.com/rodrigosalamanca/ai-it-operations-agent/blob/main/docs/CLIENT_OVERVIEW.md).

Use this copy in the existing North Maple Systems Projects page when website integration is authorized. Do not describe the experiment as a validated predictive agent or promise customer results.


## 2026-10-14 — Current predictive pilot scope

The proposed first pilot is **next-backup failure prediction using Zabbix + Veeam**. Start with approved historical exports, including successful jobs and failures, then consider scoped read-only APIs. Compare simple rules with a small ML model on later held-out data; measure recall, precision, false warnings, advance notice and operator effort. Numerical probabilities require calibration. The optional LLM explains evidence; it does not calculate or validate the predictive model. No trained predictor or live connectors are implemented. Wazuh, Fortinet, Intune and other sources remain later candidates. See [the pilot design](PREDICTIVE_PILOT.md) for the source of truth.
