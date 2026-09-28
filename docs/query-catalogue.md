# Query Catalogue

| File | Focus | Primary table |
| --- | --- | --- |
| identity/signin-hunting.kql | Authentication anomalies | EntraIdSignInEvents |
| endpoint/powershell-hunting.kql | Suspicious process execution | DeviceProcessEvents |
| endpoint/network-hunting.kql | Unusual outbound activity | DeviceNetworkEvents |
| email/phishing-hunting.kql | Suspicious email campaigns | EmailEvents |
| cloud/cloudapp-hunting.kql | Unusual SaaS/cloud actions | CloudAppEvents |

## Hunting versus detection

A hunting query is an analytical starting point. Before turning one into a scheduled detection:

- establish expected volume
- tune exclusions
- test representative benign activity
- define severity
- define ownership
- write investigation steps
- measure false positives
- review after environmental change
