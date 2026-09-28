# KQL Threat Hunting Library

![KQL library checks](https://github.com/WaleedWTR/kql-threat-hunting-library/actions/workflows/tests.yml/badge.svg)

A curated portfolio library of Microsoft security hunting queries organised by identity, endpoint, email and cloud activity.

> **Portfolio note:** Queries are designed for learning and portfolio demonstration. Table availability depends on connected Microsoft security data sources and licensing.

## Library goals

- keep hunting queries readable and reusable
- document what behaviour each query is looking for
- separate hunting from production alerting
- encourage baselining and tuning
- map queries to investigation questions
- version detection logic as code

## Structure

```text
.
├── cloud/
├── docs/
├── email/
├── endpoint/
├── identity/
└── tests/
```

## Categories

| Area | Examples |
| --- | --- |
| Identity | failed sign-ins, risky sign-ins, unusual sources |
| Endpoint | encoded PowerShell, Office child processes, admin tooling |
| Email | suspicious senders, malicious URLs, high-volume campaigns |
| Cloud | unusual application activity and high-risk actions |

## Usage

Open the appropriate `.kql` file in Microsoft Defender XDR Advanced Hunting, Microsoft Sentinel or Log Analytics as appropriate for the table used.

Always validate:

- data source availability
- time range
- environmental baseline
- false-positive rate
- user/device/application context

## Key documentation

- [Query catalogue](docs/query-catalogue.md)
- [Tuning guide](docs/tuning-guide.md)
- [Identity hunting](identity/signin-hunting.kql)
- [Endpoint hunting](endpoint/powershell-hunting.kql)
- [Email hunting](email/phishing-hunting.kql)
- [Technical references](docs/references.md)

## Skills demonstrated

**KQL · Threat Hunting · Microsoft Sentinel · Defender XDR · Detection Engineering · Security Analytics**
