# {{Feature name}}

| Attribute | Value |
|---|---|
| Project | Busy Bees Asia {{CRM / SMS}} |
| Module | {{Lead / Enquiry / …}} |
| Feature | {{BBA-xx}} - {{Feature name}} |
| Document ID | {{BBA-xx}}-{{WBS}}_{{Feature_Name}} |
| Version | {{0.1}} |
| Status | DRAFT FOR CONFIRMATION |
| Date | {{DD Month YYYY}} |
| Prepared by | Business Analysis |
| Reviewed by | {{HaiNguyen}} |
| Approved by | {{HaiNguyen}} |

## 1. Document Control

| Version | Date | Author | Change Summary | Approval |
|---|---|---|---|---|
| {{0.1}} | {{DD Month YYYY}} | Business Analysis | Initialize the document. | {{HaiNguyen}} |

**Readiness statement:** {{One sentence: what is defined and which decisions remain open in Section 7.}}

## 2. Purpose and Background

{{What the feature does, for whom, and what it deliberately does not do.}}

**Source workflow and SRS references:** {{WF-CRM-P1, WF-CRM-P2}} · SRS: {{BBA_CRM_SRS v0.1 — §4 2.3 Reference Log and Centre Sharing; BR-CRM-006, BR-CRM-007; AC-CRM-028}} · WBS {{2.1.1.01}}.

## 3. Scope and Phase Boundaries

| In Scope | Out of Scope |
|---|---|
| {{…}} | {{… (state the phase or owning FSD when known)}} |

Boundary: {{What data or objects this feature creates, changes or never touches.}}

## 4. Actors, Roles and Access

| Actor | Scope | Permission / Responsibility |
|---|---|---|
| {{Authorised User}} | {{…}} | {{…}} |
| System | {{…}} | {{…}} |
| Unauthorised User | {{Outside the permitted role or data scope.}} | {{Must not see or execute restricted actions.}} |

{{Access principle sentence — existing role / Centre / object permission model.}}

## 5. Feature Overview and Functional Decomposition

| Module | Feature | Function | User Story |
|---|---|---|---|
| {{…}} | {{…}} | {{…}} | {{BBA-xx}}: US-001 |

## 6. Functional Requirements by User Story

### 6.1 {{BBA-xx}}: US-001 - {{User Story Title}}

#### User Story

As {{a role}}, I want {{capability}} so that {{business value}}.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-001 | {{The system shall …}} |

#### Functional Flow - Main

1. {{Actor action (FR-001).}}
2. {{System response (FR-002; VAL-001).}}

#### Functional Flow - Alternative

1. {{Condition: behaviour (FR / VAL reference).}}

#### Functional Flow - Exception

1. {{Condition: behaviour without data change (VAL reference).}}

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-001 | {{…}} |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-001 | {{…}} | {{…}} |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| {{BBA-xx}}: UI-US-001 - {{Screen name}} | {{Figma link}} |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| {{…}} | {{Display / Action / Link / …}} | {{Yes / No / Conditional}} | {{…}} | {{…}} | {{…}} |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-001 | {{…}} |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | {{…}} | {{…}} | {{…}} | {{FR-001; BR-001}} |

#### Dependencies

{{Owning services, other FSDs (BBA-xx), master data, permission model.}}

## 7. Open Questions

| Question ID | Decision Needed | Owner | Priority | Decision BBA |
|---|---|---|---|---|
| {{OQ-XX-01}} | {{…}} | {{Business Owner}} | {{High / Medium / Low}} | |

## 8. Glossary

| Term | Definition in This FRS |
|---|---|
| {{…}} | {{…}} |
