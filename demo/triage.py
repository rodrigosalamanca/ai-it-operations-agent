"""Offline synthetic triage demo. No AI, network access or command execution."""
import argparse
from datetime import datetime
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError('Timestamp must be a string with a timezone.')
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('Timestamp requires a timezone.')
    return parsed


def percentage(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 100:
        raise ValueError('Disk percentage must be a finite number between 0 and 100.')
    return value


def triage(alert, context, runbook):
    if alert.get('synthetic') is not True or context.get('synthetic') is not True:
        raise ValueError('This demo accepts explicitly synthetic data only.')
    if alert.get('signal') != 'disk_used_percent' or alert.get('unit') != 'percent':
        raise ValueError('Only disk_used_percent alerts in percent are supported.')
    for field in ('event_id', 'host_id'):
        if not isinstance(alert.get(field), str) or not alert[field].strip():
            raise ValueError(f'Missing or invalid {field}.')
    if context.get('host_id') != alert['host_id']:
        raise ValueError('Context belongs to a different host.')
    occurred = timestamp(alert.get('occurred_at'))
    value = percentage(alert.get('value'))
    facts = [{'text': f"Disk utilization was reported at {value:g}% on {alert['host_id']} at {alert['occurred_at']}.",
              'evidence': [alert['event_id']]}]
    gaps = ['Directory growth and log sizes are unknown.', 'Service impact is unknown.', 'Inode utilization is unknown.']
    samples = context.get('samples', [])
    if not isinstance(samples, list):
        raise ValueError('Samples must be a list.')
    ids = set()
    for sample in samples:
        if not isinstance(sample, dict) or not isinstance(sample.get('id'), str) or not sample['id']:
            raise ValueError('Every metric requires an evidence ID.')
        if sample['id'] in ids or sample['id'] == alert['event_id']:
            raise ValueError('Duplicate evidence ID.')
        ids.add(sample['id'])
        percentage(sample.get('used_percent'))
        if timestamp(sample.get('at')) > occurred:
            raise ValueError('Metric timestamp is later than the alert.')
    samples = sorted(samples, key=lambda s: timestamp(s['at']))
    if not samples:
        gaps.append('No metric history is available; growth cannot be calculated.')
    else:
        latest = samples[-1]
        age = (occurred - timestamp(latest['at'])).total_seconds()
        if age > 900:
            gaps.append('Metric context is stale relative to the alert (>15 minutes); trend is withheld.')
        elif latest['used_percent'] != value:
            gaps.append('Alert and latest metric disagree; trend is withheld pending verification.')
        elif len(samples) < 2:
            gaps.append('Only one metric is available; growth cannot be calculated.')
        else:
            first = samples[0]
            hours = (timestamp(latest['at']) - timestamp(first['at'])).total_seconds() / 3600
            if hours <= 0:
                gaps.append('Metric timestamps do not define a positive interval; trend is withheld.')
            else:
                change = latest['used_percent'] - first['used_percent']
                facts.append({'text': f"Disk utilization changed from {first['used_percent']:g}% to {latest['used_percent']:g}% over {hours:g} hours ({change:+g} percentage points).",
                              'evidence': [first['id'], latest['id']]})
    approved = (isinstance(runbook, dict) and runbook.get('id') == 'disk-triage'
                and runbook.get('version') == '0.1' and runbook.get('approval') == 'demo-only'
                and runbook.get('signal') == alert['signal'])
    if approved:
        checks = runbook.get('checks')
        if not isinstance(checks, list) or not checks or not all(isinstance(c, str) for c in checks):
            raise ValueError('Invalid runbook checks.')
    else:
        checks = []
        gaps.append('No matching demo-approved runbook is available.')
    return {
        'incident_id': alert['event_id'], 'mode': 'synthetic deterministic demo — no AI',
        'facts': facts,
        'hypotheses': ['Log growth is one possible cause, but no supporting log-size evidence is available. Data growth or insufficient filesystem capacity are alternatives.'],
        'missing_context': gaps, 'suggested_read_only_checks': checks,
        'runbook': 'disk-triage@0.1 (demo-only)' if approved else None,
        'actions_executed': [], 'review': {'status': 'pending', 'note': ''},
        'evidence_catalog': {alert['event_id']: alert, **{s['id']: s for s in samples}},
    }


def markdown(report):
    lines = ['# Leaf Solutions — IT Operations Agent', '', '**Synthetic offline demo · No AI · No infrastructure actions**', '', '## Observed facts', '']
    lines += [f"- {f['text']} Evidence: {', '.join(f['evidence'])}." for f in report['facts']]
    for title, key in [('Unconfirmed hypotheses', 'hypotheses'), ('Missing context', 'missing_context'), ('Suggested read-only checks', 'suggested_read_only_checks')]:
        lines += ['', f'## {title}', ''] + [f'- {v}' for v in report[key]]
    lines += ['', f"Runbook: {report['runbook'] or 'unavailable'}", '', '**Actions executed: none.**', '', f"Review: {report['review']['status']} (local demo annotation, not authenticated approval).", report['review']['note']]
    return '\n'.join(lines) + '\n'


def html(report):
    def items(values):
        return '<ul>' + ''.join('<li>' + escape(v) + '</li>' for v in values) + '</ul>'
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Leaf Solutions — Synthetic incident demo</title>',
             '<style>body{font:17px/1.65 system-ui;margin:auto;padding:40px 24px;max-width:880px;background:#f5f2ea;color:#232f32}h1{font-size:32px;line-height:1.2}h2{font-size:22px}section{background:white;padding:18px 24px;margin:20px 0;border-radius:12px}.badge{color:#944e31;font-weight:700}li{margin:8px 0}small{display:block;color:#555}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}</style>',
             '<body><p class="badge">LEAF SOLUTIONS / LOCAL DEMONSTRATION</p><h1>IT Operations Agent</h1><p>Synthetic data · Deterministic rules · No AI connection</p><section><h2>Observed facts</h2>',
             items([f["text"] + ' Evidence: ' + ', '.join(f['evidence']) for f in report['facts']]), '</section>']
    for title, key in [('Unconfirmed hypotheses', 'hypotheses'), ('Missing context', 'missing_context'), ('Suggested read-only checks', 'suggested_read_only_checks')]:
        parts += ['<section><h2>' + title + '</h2>', items(report[key]), '</section>']
    parts += ['<section><h2>Operator review</h2><p>Actions executed: <strong>none</strong>.</p><p>Runbook: ' + escape(report['runbook'] or 'unavailable') + '</p><p>Status: ' + escape(report['review']['status']) + '</p><p>' + escape(report['review']['note']) + '</p><small>Review is a local annotation, not an authenticated approval. No actions are authorized.</small></section>',
              '<details><summary>Inspect synthetic evidence</summary><pre>' + escape(json.dumps(report['evidence_catalog'], indent=2)) + '</pre></details></body></html>']
    return ''.join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--alert', type=Path, default=ROOT / 'examples/disk-alert.json')
    parser.add_argument('--context', type=Path, default=ROOT / 'demo/fixtures/disk-context.json')
    parser.add_argument('--runbook', type=Path, default=ROOT / 'demo/runbooks/disk-triage.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'demo/output')
    parser.add_argument('--review', choices=['pending', 'useful', 'needs-correction'], default='pending')
    parser.add_argument('--note', default='')
    args = parser.parse_args()
    try:
        alert = json.loads(args.alert.read_text())
        context = json.loads(args.context.read_text())
        runbook = json.loads(args.runbook.read_text()) if args.runbook.exists() else None
        report = triage(alert, context, runbook)
        report['review'] = {'status': args.review, 'note': args.note}
        args.output.mkdir(parents=True, exist_ok=True)
        for name, content in [('incident.json', json.dumps(report, indent=2) + '\n'), ('incident.md', markdown(report)), ('incident.html', html(report))]:
            (args.output / name).write_text(content)
    except (ValueError, OSError, TypeError, KeyError, AttributeError) as exc:
        parser.exit(2, f'Demo input/output error: {exc}\n')
    print(f"Created synthetic incident report: {args.output / 'incident.html'}")
    print('No AI calls, monitoring queries or server actions were performed.')


if __name__ == '__main__':
    main()
