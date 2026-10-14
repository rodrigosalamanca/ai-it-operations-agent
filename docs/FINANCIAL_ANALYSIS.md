# Financial analysis — planning model, 50 servers

> Scope notice, 2026-10-13: this document describes the earlier diagnostic MVP. The current direction is historical incident prediction, described in [the customer overview](CLIENT_OVERVIEW.md). The architecture, schedule, economics and competitive position below have not been validated for that predictive scope.

Baseline date: 2026-10-13. All amounts are USD, before tax, inflation and currency conversion. This is a feasibility scenario, not a quote, valuation, forecast or investment recommendation. No customer revenue or savings have been demonstrated. Vendor references are in [competitive analysis](COMPETITIVE_ANALYSIS.md); all North Maple Systems IT Operations Agent rates below are internal assumptions.

## Recurring cost model

Base workload: 100 briefs/day × 30 days = 3,000 briefs/month. At 4,000 input and 1,000 output tokens each, that is 12 million input and 3 million output tokens. Placeholder rates of USD 1 and USD 4 per million yield **USD 24/month**. Rates are deliberately vendor-neutral budget inputs, not published model prices. Replace them after provider selection. No call is made for every metric sample or every raw alert.

| Monthly cost | Low | Base | High |
| --- | ---: | ---: | ---: |
| Application compute, database, networking/storage envelope | 100.00 | 150.00 | 300.00 |
| Backups and ancillary services | 10.00 | 20.00 | 40.00 |
| Model inference | 12.00 | 24.00 | 120.00 |
| 20% contingency on the above cash costs | 24.40 | 38.80 | 92.00 |
| Maintenance labor at USD 50/hour (2 / 4 / 8 hours) | 100.00 | 200.00 | 400.00 |
| **Total economic operating cost** | **246.40** | **432.80** | **952.00** |

Low assumes 50 briefs/day; base 100; high 500, with the same token sizes/rates. These are workload/cost scenarios, not vendor hosting quotes. The base cash cost excluding maintenance labor is USD 232.80. Labor remains an economic cost even when performed by the founder without a cash payment.

Infrastructure budgets include a provisional 100 GB storage envelope and modest single-tenant traffic; confirm with a deployment quote. Existing monitoring licenses/hosting, telemetry expansion, 24/7 support, major incident handling, compliance/legal work, taxes, payment fees, sales, customer acquisition and provider overages are excluded. Add any incremental monitoring cost before approval. Local/self-hosted inference would require a different compute and operations model.

## Benefit sensitivity

Assume 100 actionable incidents/month and USD 50/hour loaded operator cost. Generated briefs and useful incidents are different counts: 3,000 briefs do not imply 3,000 time-saving incidents. The proposed design must investigate whether briefs can be restricted to useful events.

| Net minutes saved per incident, after review | Monthly labor capacity value | Net value after base operations |
| --- | ---: | ---: |
| 0 | 0.00 | -432.80 |
| 5 | 416.67 | -16.13 |
| 10 | 833.33 | 400.53 |
| 20 | 1,666.67 | 1,233.87 |

Formula: incidents × net minutes saved ÷ 60 × loaded hourly cost. This is reclaimed capacity, not necessarily a reduction in payroll or cash spend. Extra review time and incorrect advice can make savings negative. Avoid assigning downtime reduction revenue without incident evidence.

At 10 minutes saved, recurring-cost break-even is approximately **52 useful incidents/month**. At 100 incidents, the requirement is **5.19 net minutes saved/incident**. With high operating cost, the 10-minute scenario loses USD 118.67/month.

## Development and first-year total cost

Illustrative initial investment: 200 engineering hours × USD 50 = USD 10,000, plus 40 hours security review × USD 50 = USD 2,000, plus 40 hours onboarding/evaluation × USD 50 = USD 2,000: **USD 14,000** total. Scope changes and external review may materially increase this.

Base first-year project cost: USD 14,000 + 12 × USD 432.80 = **USD 19,193.60**, excluding the costs listed above. At the 10-minute benefit assumption, annual capacity value is USD 10,000, net first-year value is **-USD 9,193.60**, and simple first-year ROI is approximately **-47.9%**. Steady-state monthly net value is USD 400.53; simple payback on development is approximately **35 months**, assuming benefits and costs remain constant. There is no recurring-cost payback at 5 minutes saved. At 20 minutes it is approximately 11.35 months, excluding ramp-up and discounting.

## Commercial pricing hypothesis

An illustrative USD 699/month service price for one 50-server customer yields USD 266.20/month contribution after base operating cost, or about 38.1% before development, sales, overhead and tax. It has **not** been validated or offered. At high cost it loses USD 253/month. A 60% contribution margin would require USD 1,082/month at base cost, which exceeds the USD 833.33 customer capacity value in the 10-minute case. This tension argues for cost reduction, stronger measured value, or a narrower workflow before commercialization.

At base contribution, recovering USD 14,000 requires about 53 customer-months before other costs. Multi-customer economics cannot assume shared infrastructure or identical support hours: the design is single tenant and customer acquisition is unknown. No sales forecast is provided.

## Reproduce and revise

Run `python3 tools/financial_model.py`. Edit the clearly named inputs to test measured workloads, token usage, provider quotes, support hours and incident time. The script contains arithmetic only and has no model or infrastructure integration. Recalculate after discovery and monthly during pilot; never present an assumption as a measured result.


## 2026-10-14 — Current predictive pilot scope

The proposed first pilot is **next-backup failure prediction using Zabbix + Veeam**. Start with approved historical exports, including successful jobs and failures, then consider scoped read-only APIs. Compare simple rules with a small ML model on later held-out data; measure recall, precision, false warnings, advance notice and operator effort. Numerical probabilities require calibration. The optional LLM explains evidence; it does not calculate or validate the predictive model. No trained predictor or live connectors are implemented. Wazuh, Fortinet, Intune and other sources remain later candidates. See [the pilot design](PREDICTIVE_PILOT.md) for the source of truth.
