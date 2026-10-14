# North Maple Systems — IT Operations Agent

**Predictive Incident Intelligence · Product in development**

A proposed product for anticipating operational incidents by learning from past incidents and the signals that preceded them. The intended result is an evidence-backed preventive risk brief: what may go wrong, which assets are affected, which historical patterns are relevant, and what an operator should verify.

**[Read the customer product overview](docs/CLIENT_OVERVIEW.md)** for the product vision, planned integrations, data requirements and proposed pilot.

## Current status

The predictive model, live platform connectors and production service are not implemented. No predictive accuracy, customer savings or supported platform coverage has been validated.

This repository contains an earlier offline, rules-based disk-triage demonstration and planning documents. That experiment does not learn from incident history or demonstrate the current predictive product. The standalone disk-threshold forecast is not the product's differentiator; native monitoring functions should be used where available.

## Intended workflow

Approved monitoring and incident-history sources → unified asset/event history → candidate pre-incident patterns → temporal validation → preventive risk briefs → operator review and outcome measurement.

The initial pilot would select one incident category and a limited set of sources. It would use scoped read access, preserve existing monitoring and assess false alarms and advance notice before expansion. Broad integrations are a roadmap goal, not a current support commitment.

## Documents

- [Customer overview](docs/CLIENT_OVERVIEW.md): current customer-facing product direction and proposed pilot.
- [Portfolio copy](docs/PORTFOLIO.md): concise presentation aligned with that direction.
- [Security design](SECURITY.md): earlier read-only design principles; production controls remain proposed.
- [Earlier experiment](demo/README.md): reproducible offline diagnostic demonstration, not incident prediction.

The architecture and roadmap now describe the predictive pilot. Earlier assumptions, competitive and financial calculations retain their diagnostic-scope notices and require reassessment. Their costs, schedules and model workload are not a predictive pilot quote or validated forecast.

## Reproduce the earlier experiment

Python 3 standard library only:

```sh
python3 demo/triage.py
python3 -m unittest discover -s tests -v
```

No model calls or infrastructure actions occur. Synthetic outputs are included for inspection. No license has been selected; establish rights and contribution terms before accepting external code. Project owner: Rodrigo Salamanca, North Maple Systems.


## 2026-10-14 — Current predictive pilot scope

The proposed first pilot is **next-backup failure prediction using Zabbix + Veeam**. Start with approved historical exports, including successful jobs and failures, then consider scoped read-only APIs. Compare simple rules with a small ML model on later held-out data; measure recall, precision, false warnings, advance notice and operator effort. Numerical probabilities require calibration. The optional LLM explains evidence; it does not calculate or validate the predictive model. No trained predictor or live connectors are implemented. Wazuh, Fortinet, Intune and other sources remain later candidates. See [the pilot design](docs/PREDICTIVE_PILOT.md) for the source of truth.
