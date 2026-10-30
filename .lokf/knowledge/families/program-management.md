---
type: Sp80053Family
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/families/program-management
title: Program Management
description: "The SP 800-53 family PM, Program Management: 32 controls and 5 control enhancements in Release 5.2.0, none withdrawn."
family_id: PM
resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/references/sp-800-53
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-53/knowledge/glossary/control-family
sources:
  - id: nist_sp-800-53_rev5_catalog.json
    resource: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json
    title: the group pm
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Program Management (PM)

The catalog's group `pm`, labelled PM, holds 32 controls and 5 control enhancements in Release 5.2.0; 0 controls and 0 enhancements carry the status withdrawn.[^nist_sp-800-53_rev5_catalog.json]

The catalog gives this family alone an overview. It says that:

- FISMA, the Privacy Act and OMB Circular A-130 require federal agencies to run organization-wide information security and privacy programs;
- the PM controls are implemented at the organization level and are not directed at individual systems;
- they help organizations comply with federal laws, executive orders, directives, policies, regulations and standards;
- being independent of the FIPS 200 impact levels, they are not associated with the baselines of SP 800-53B.

Organizations document them in the information security and privacy program plans, which together with the system plans cover every control the organization employs.[^nist_sp-800-53_rev5_catalog.json]

Its controls, with the number of enhancements each holds:

- `PM-1` Information Security Program Plan
- `PM-2` Information Security Program Leadership Role
- `PM-3` Information Security and Privacy Resources
- `PM-4` Plan of Action and Milestones Process
- `PM-5` System Inventory: 1 enhancement
- `PM-6` Measures of Performance
- `PM-7` Enterprise Architecture: 1 enhancement
- `PM-8` Critical Infrastructure Plan
- `PM-9` Risk Management Strategy
- `PM-10` Authorization Process
- `PM-11` Mission and Business Process Definition
- `PM-12` Insider Threat Program
- `PM-13` Security and Privacy Workforce
- `PM-14` Testing, Training, and Monitoring
- `PM-15` Security and Privacy Groups and Associations
- `PM-16` Threat Awareness Program: 1 enhancement
- `PM-17` Protecting Controlled Unclassified Information on External Systems
- `PM-18` Privacy Program Plan
- `PM-19` Privacy Program Leadership Role
- `PM-20` Dissemination of Privacy Program Information: 1 enhancement
- `PM-21` Accounting of Disclosures
- `PM-22` Personally Identifiable Information Quality Management
- `PM-23` Data Governance Body
- `PM-24` Data Integrity Board
- `PM-25` Minimization of Personally Identifiable Information Used in Testing, Training, and Research
- `PM-26` Complaint Management
- `PM-27` Privacy Reporting
- `PM-28` Risk Framing
- `PM-29` Risk Management Program Leadership Roles
- `PM-30` Supply Chain Risk Management Strategy: 1 enhancement
- `PM-31` Continuous Monitoring Strategy
- `PM-32` Purposing

[^nist_sp-800-53_rev5_catalog.json]: src/nist_sp_800_53/schema/oscal-content/NIST_SP-800-53_rev5_catalog.json, the group pm
