# Offline synthetic incident demonstration

This is working deterministic demo code, not an AI agent or production integration. It reads only local JSON files and writes an incident report. It makes no model calls, network requests, shell executions or changes to servers. Python 3 standard library only.

## Run

From the repository root:

```sh
python3 demo/triage.py
python3 -m unittest discover -s tests -v
```

Open `demo/output/incident.html` in a browser or read `incident.md` and `incident.json`. Outputs are overwritten on each run. Use `--output` for a separate directory if you want to retain multiple reviews. The checked-in outputs are reproducible examples, not customer results.

## Inputs and flow

- [Alert](../examples/disk-alert.json): explicitly synthetic host and 91% disk reading.
- [Context](fixtures/disk-context.json): synthetic 75% and 91% readings six hours apart.
- [Runbook](runbooks/disk-triage.json): local version 0.1, approved for this demonstration only.

Validation → evidence consistency checks → fixed runbook match → deterministic brief → HTML/Markdown/JSON export.

The report cites source event/metric IDs and displays raw synthetic evidence. It reports +16 **percentage points**, not a 16% relative change. Possible log growth is unconfirmed: no log-size evidence exists. Suggested checks are displayed only; nothing is executed.

## Local operator annotation

```sh
python3 demo/triage.py --review useful --note "The evidence and next checks are clear." --output demo/output-reviewed
python3 demo/triage.py --review needs-correction --note "Need inode and service-impact information." --output demo/output-correction
```

Review states are local annotations, not authenticated approvals or append-only audit records. This demo never authorizes an action. No browser interaction or review database is implemented.

## Failure behavior and scope

Use `--alert`, `--context`, `--runbook` and `--output` to select local fixtures. Explicit synthetic flags are required; they do not detect or anonymize real data, so only hand-authored examples should be used. No customer telemetry belongs here.

Missing history, stale context (>15 minutes relative to alert time), conflicting readings or unavailable/unapproved runbooks produce an explicit gap rather than a fabricated trend or runbook. Invalid percentages, missing timezone, future metrics, duplicate IDs and another host's context reject input with exit code 2. On rejection no new report is generated: older reports in the output folder remain and must not be mistaken for a successful new run.

Runbooks are trusted local demo configuration, not cryptographically signed documents. The `demo-only` label is not a production approval mechanism. Unknown input fields are not treated as instructions. HTML output escapes text; JSON evidence retains all supplied synthetic alert fields for inspection. There is no production privacy filter, inference, retrieval search, webhook, paging, queue, telemetry collector, access control or deployment. The 50-server scenario has not been tested.

Next: obtain the missing operational context, evaluate on additional synthetic incident cases, then select an approved model/provider and read-only lab monitoring adapter separately.

## Time to next configured threshold

The synthetic alert explicitly configures 90% and 95% thresholds. At 91%, the next is 95%. The 75% → 91% rise over six hours yields 2.67 percentage points/hour and a linear crossing estimate of 1.5 hours after the last sample: 2026-10-13 13:30 UTC. This is a scenario based on recent growth, not established normal background growth or guaranteed alert delivery; monitoring duration/hysteresis are not modeled. The timestamp is historical fixture time, not a live countdown.

Missing thresholds or invalid/stale/conflicting trend data produce no ETA. Flat or declining net usage yields no projected crossing. Already reached thresholds are labeled. Edit `configured_thresholds_percent` in the synthetic alert to change the target; the tool selects the smallest threshold strictly above current usage. The model assumes unchanged filesystem capacity and workload; long-term baseline and uncertainty estimation remain future work.
