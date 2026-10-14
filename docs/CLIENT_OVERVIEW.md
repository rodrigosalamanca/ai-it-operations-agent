# Leaf Solutions — IT Operations Agent
## Predictive Incident Intelligence

**Customer product overview · Proposed pilot · Product in development**

Leaf Solutions is developing an IT operations product designed to identify patterns that preceded past incidents and recognize similar warning signals in the current environment. The goal is to help operations teams investigate emerging risks earlier and choose preventive steps with supporting evidence.

**Current availability:** the predictive product and platform connectors are not implemented. An existing offline demonstration uses synthetic data and fixed diagnostic rules; it does not demonstrate learned incident prediction. This document describes the intended product and a proposed validation pilot, not a service already available for production.

## The business problem

Operational incidents often leave information across monitoring systems, tickets, change records, infrastructure and backup platforms. Teams may have the history of a failure but lack a practical way to relate that history to current conditions.

Leaf Solutions intends to bring those signals together: what happened before an incident, which assets and services were affected, and whether a comparable pattern is emerging again. Existing monitoring remains responsible for telemetry and its native alerting. The proposed product adds historical incident analysis and risk assessment across agreed data sources.

## Intended customer experience

An operator would receive a preventive risk brief showing:

- The incident category that may be developing and the affected assets or services.
- The current signals and relevant historical incidents, with source references.
- An estimated prediction horizon and risk level only where evaluation supports them.
- Missing or stale evidence and conditions that could weaken the assessment.
- Recommended verification steps and links to customer-approved preventive runbooks.

A matching historical pattern would be presented as evidence for investigation, not proof that an incident will occur. Numerical probabilities would be shown only after appropriate calibration and validation. The product would abstain when the available data does not support a useful assessment.

### Illustrative brief — not a measured result

> **Potential incident:** storage-related service interruption.  
> **Current signals:** backup failures and increased storage latency on related assets.  
> **Historical context:** similar signals preceded past storage incidents in the supplied example history.  
> **Next verification:** confirm backup status, storage health and relevant recent changes.  
> **Assessment:** a pattern warrants investigation; probability and time horizon are not established in this example.  
> **Action:** operator review required; no infrastructure change has been executed.

## Planned integration coverage

Connector priorities will be agreed during discovery. The following are candidates for the product roadmap; none is currently connected or certified.

| Data area | Candidate platforms | Intended information |
| --- | --- | --- |
| Monitoring and observability | Zabbix, Prometheus/Grafana, Datadog | Alerts, metric history, availability and operating conditions |
| Endpoint management | Microsoft Intune | Approved device reports and periodic inventory/compliance observations; report import and connected modes are planned |
| Cloud and infrastructure | AWS, Microsoft Azure, VMware | Asset inventory, resource events, changes and dependencies |
| Backup and recovery | Veeam and the customer's existing backup platform | Job outcomes, failure history and recovery-related events |
| Service management | ServiceNow, Jira Service Management | Incident records, impact, resolution and change history |
| Logs and security events | Customer-approved log platforms, Wazuh | Relevant event sequences and bounded diagnostic evidence |

Coverage depends on API availability, customer permissions, data quality and agreed scope. Platform names identify integration candidates, not vendor partnerships or endorsements. A first pilot would connect a small agreed subset rather than promise support for every platform.

## Microsoft Intune: a simpler entry point

For customers using Intune, the planned entry workflow is either uploading a selected device report or having an administrator authorize a scoped analysis connection. The user would see affected devices, supporting observations, missing information and recommended next checks without navigating API configuration. Neither workflow is implemented yet.

A single report supports current-state assessment. Prediction requires repeated observations linked to incident outcomes and comparable non-incident periods. Intune data alone may not contain enough information for the selected incident category. See the [Intune pilot design](INTUNE_PILOT.md) for data and access requirements.

## How the proposed product would work

1. **Connect approved sources.** Establish narrowly scoped read access to selected monitoring and incident records.
2. **Build a consistent history.** Relate incidents, assets, timestamps, changes and relevant signals; review incident labels with operators.
3. **Learn candidate patterns.** Compare periods before incidents with comparable periods where no incident occurred.
4. **Evaluate future risk.** Assess current signals against validated patterns for a defined incident category and prediction window.
5. **Present evidence and track outcomes.** Let operators review the brief and record whether an incident occurred and whether the warning was useful.

The initial model approach will be selected after inspecting the data. A language model may help summarize evidence, but a fluent explanation does not establish predictive accuracy.

## Data and access requirements

A useful pilot needs historical incidents with dates, affected assets, incident categories and operational outcomes, plus timestamped signals from before those incidents. It also needs representative non-incident periods to assess false alarms. Data after an incident begins cannot be used to claim that the incident was predicted beforehand.

Discovery will determine the history required, the number of usable incidents, missing records, time alignment and whether the proposed target is predictable with the available data. If evidence is insufficient, Leaf Solutions will recommend collecting additional data or narrowing the use case rather than claim validated prediction.

The original 50-server estate is an illustrative planning scenario, not a capacity guarantee. Pilot size and data volume will be defined with the customer.

## Customer control and security

The proposed initial pilot is advisory and read-only. It does not require unrestricted administrative control of customer systems. Broad visibility comes through approved integrations and agreed asset scopes.

Before connecting data, the parties would agree access roles, hosting location, data fields, retention, provider processing and incident reporting. Credentials should remain outside public repositories and client-side files. Only required operational data should be collected; sensitive information should be minimized before processing.

Any future remediation capability would require separately approved scope, least-privilege execution and explicit operator authorization. No autonomous remediation, compliance certification, production SLA or security audit is claimed today.

## Proposed pilot and success criteria

**Discovery:** select one recurring incident category, relevant assets and source systems; define the warning horizon and acceptable alert burden.

**Historical evaluation:** train or configure on earlier periods and test on later held-out periods. Compare against existing monitoring and simple baseline rules. Keep post-incident information out of prediction inputs and avoid counting many warnings for the same incident as independent successes.

**Shadow operation:** generate risk briefs without changing systems or replacing existing paging. Review usefulness and false alarms with operators.

**Go/no-go review:** decide whether to expand, collect more data, change the target or stop the pilot.

Agreed measures would include the proportion of incidents detected, the proportion of warnings followed by the defined incident, advance notice, false warnings per week, data coverage and operator investigation time. Existing threshold alarms remain the comparison baseline. No accuracy percentage, financial saving or commercial outcome is promised before evaluation.

## Responsibilities and commercial scope

Leaf Solutions would define the pilot workflow, prepare the agreed integration and evaluation plan, and report results and limitations. The customer would designate an operational owner, approve data access, confirm incident labels and review recommendations.

Pricing, deployment model, support hours and delivery dates will be proposed after discovery. Earlier internal cost calculations are exploratory and are not a customer quote for this predictive scope.

**Next step:** agree one incident category, identify the available history and select the first data sources for a feasibility review.

Document baseline: 2026-10-13. Prepared for customer review; capabilities described as intended remain subject to implementation and pilot validation.
