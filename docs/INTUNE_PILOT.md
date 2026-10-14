# Microsoft Intune — proposed customer entry workflow

**Leaf Solutions — IT Operations Agent · Design only · No connector or upload service implemented**

## Customer experience

Two planned starting options:

1. **Report assessment:** the customer's administrator exports an agreed device report. The proposed importer checks columns, timestamps, device identifiers and missing values, then presents current conditions and data gaps. No permanent tenant connection is needed for this mode. Available export columns must be confirmed against the selected report.
2. **Connected observation:** an administrator authorizes the agreed Microsoft Graph access. A future service records selected device observations over time and shows collection status and last successful retrieval. End users review findings; they do not configure permissions.

Suggested product flow: choose report/connection → review data scope → validate available data → inspect findings and evidence → add historical incident outcomes → assess whether prediction is feasible. This flow is not available today. Intune's native administration and compliance reporting remain in place.

## Data feasibility

Microsoft documents managed-device properties including device ID, operating system/version, compliance state, last synchronization, encryption and storage information. Availability and meaning depend on the platform and reporting conditions; missing or default values must not be interpreted as device failure. [Managed device reference](https://learn.microsoft.com/en-us/graph/api/resources/intune-devices-manageddevice?view=graph-rest-1.0).

Start with an agreed field allowlist and pseudonymous device key. Collect observation time separately from last synchronization. Avoid user names, emails, phone numbers, serial numbers, recovery/bypass codes and unrelated fields unless independently justified and approved. A stable asset mapping must remain customer-controlled. Do not publish real exports or tenant identifiers in this repository.

A snapshot can describe current compliance or stale reporting; it cannot establish when an incident will happen. For prediction, link repeated pre-incident observations to timestamped incident outcomes, and include non-incident periods. A candidate target is a recurring endpoint disruption with sufficient labeled examples, to be chosen during discovery. Noncompliance is a condition, not automatically an outage. Ticket history or other approved signals may be required.

## Proposed integration boundary

The initial connected candidate is Microsoft Graph v1.0 `GET /deviceManagement/managedDevices`, with `DeviceManagementManagedDevices.Read.All`, an active Intune tenant license and appropriate authorization. Both delegated and application access are documented; choose the actual mode after reviewing the customer environment. [List managed devices](https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-list?view=graph-rest-1.0).

Application-wide permissions may allow reads across the tenant. Filtering collected devices does not itself narrow the token's authority. Explain effective access to the administrator before consent and verify the customer-required restrictions. Do not promise that an app inherits the user's Intune scope tags without validation. Store credentials server-side, support revocation, isolate customers and handle pagination, throttling and failed retrievals before claiming a functioning connector.

An important exception: the documented v1.0 endpoint for **creating report export jobs** requires one of the listed `ReadWrite.All` permissions. Therefore automated export-job creation is excluded from the initial read-only design. Use direct GET endpoints or customer-generated reports first. Any broader reporting workflow requires a separate endpoint and permission review; a reporting feature must not silently expand privileges. [Create export job](https://learn.microsoft.com/en-us/graph/api/intune-reporting-devicemanagementexportjob-create?view=graph-rest-1.0).

No write, wipe, retire, reboot, policy update or remediation operations are in scope. No tenant is connected and no consent has been granted by this documentation work.

## Pilot acceptance criteria

- Agree one report/schema or one read endpoint and verify field availability on authorized sample data.
- Reject malformed imports; mark incomplete records and stale observations instead of fabricating values.
- Display collection time, source and evidence for every finding.
- Verify actual token privileges and that the implementation has no device-modification path.
- Review native Intune reports as the assessment baseline; demonstrate what additional historical context adds.
- Evaluate predictive claims on later held-out periods with incident labels, missed incidents, false warnings and advance notice. Keep current-state findings distinct from validated predictions.
- Confirm retention, deletion, hosting, license prerequisites and support ownership before a customer pilot.

Initial implementation sequence: synthetic report schema and importer → repeated observations and incident labels → baseline evaluation → authorized read-only lab connector → supervised customer pilot. No dates, accuracy levels or savings are promised.

Sources checked 2026-10-13. Report import, user interface, connected collection and predictive evaluation are all planned work.
