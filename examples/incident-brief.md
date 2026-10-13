# Illustrative incident brief — hand-authored, synthetic

This is a design example, not output from a working agent.

**Observed fact:** `lab-linux-01` reported 91% disk utilization at 2026-10-13 12:00 UTC (`synthetic-metric-001`). A single point does not establish growth rate, inode exhaustion, affected mount or a root cause.

**Hypothesis:** application logs may be growing. Evidence is insufficient; no log size information has been supplied. Alternative causes include data growth or an undersized filesystem.

**Missing context:** mount point, utilization trend, free inodes, largest directories, service impact and approved runbook version.

**Suggested next checks:** an authorized operator should inspect recent disk trends and mount/inode summaries in existing monitoring, then locate the reviewed disk triage runbook. Do not send unredacted file contents to a model.

**Action status:** no action executed; no deletion, restart or infrastructure change authorized. Review status: pending operator review. Runbook: unavailable in this synthetic fixture.
