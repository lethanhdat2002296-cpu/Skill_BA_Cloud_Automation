# Lead and Contact Management

| Attribute | Value |
|---|---|
| Project | Busy Bees Asia CRM |
| Module | Lead and Contact Management |
| Feature | [FSD] Lead and Contact Management - Sprint 4 (ticket ID to be assigned) |
| Document ID | FSD-CRM-LCM-Sprint4 |
| Sprint | 4 |
| Version | 0.1 |
| Status | DRAFT FOR CONFIRMATION |
| Date | 9 November 2026 |
| Prepared by | Business Analysis |
| Reviewed by | HaiNguyen |
| Approved by | HaiNguyen |

## 1. Document Control

| Version | Date | Author | Change Summary | Approval |
|---|---|---|---|---|
| 0.1 | 9 November 2026 | Business Analysis | Initialize the document from BBA CRM SRS v0.1, excluding the scope already specified in Sprint 3 (BBA-40, BBA-41, BBA-42, BBA-44). | HaiNguyen |

**Readiness statement:** Lead list, Lead creation, Lead profile, Lead lifecycle status, Family relationships and the Contact master are defined. Ten decisions remain open in Section 7; the main one is the approved Lead status set (OQ-LCM-01).

## 2. Purpose and Background

This FSD specifies how authorised CRM users find, create, view and maintain Leads, how Family relationships and responsibility roles are kept at Lead scope, and how the reusable Contact master is maintained. A Lead is the reusable prospective-child identity record; it is distinct from an Enquiry and may be linked to multiple Enquiries (BR-CRM-001).

Behaviour already specified in Sprint 3 is referenced, not repeated: Inactive Lead (BBA-40), Centre Sharing (BBA-41), Lead and Enquiry duplicate detection and Reference Log creation for API duplicates (BBA-42), and the Lead aggregate Timeline (BBA-44).

**Source workflow and SRS references:** WF-CRM-P1 (Lead intake), WF-CRM-P3 (Lead lifecycle) · SRS: BBA_CRM_SRS v0.1 — §2 User Roles, §3 P1 and P3, §4 Module 2 (2.1 Lead Master, 2.2 Lead Detail, 2.4 Contact and Family Relationships), §5 BR-CRM-001 to BR-CRM-011 and BR-CRM-046 to BR-CRM-050, §6.1 Lead import validation notification, §6.2 Excel Lead import, §8 AC-CRM-017, AC-CRM-018, AC-CRM-022, AC-CRM-041 · WBS 2.1.1.03–2.1.1.05 (Phase 2 items in this FSD).

## 3. Scope and Phase Boundaries

| In Scope | Out of Scope |
|---|---|
| Lead list, search, status filter, export and navigation (Core Platform); Lead creation from staff, web and event channels (Core Platform); Lead profile view and edit; related Enquiries, converted Child and Reference Log display; Lead lifecycle status rules; Lead Family relationships and responsibility roles; Contact master list, search, duplicate check, reuse, creation, edit, identity-number merge and relationship usage (Core Platform); Bulk reassign Lead owner (WBS Phase 2, 2.1.1.04); Import Leads from Excel (WBS Phase 2, 2.1.1.05). | Inactive Lead and its read-only rules (BBA-40); Centre Sharing (BBA-41); Lead and Enquiry duplicate rules and API Reference Log creation (BBA-42); Lead Timeline (BBA-44); Merge with existing Lead (WBS Phase 2, 2.1.1.03 — separate FSD); Enquiry creation and Enquiry preferences (Enquiry and Customer Journey FSD); Child records after Enrolment (SMS Children and Families). |

Boundary: this feature creates and maintains Lead, Contact and Lead-scope relationship records. It does not create, move or overwrite Enquiry preferences, Journey runtime, Visit history or Child records.

## 4. Actors, Roles and Access

| Actor | Scope | Permission / Responsibility |
|---|---|---|
| Admissions / Customer Service | Leads and Contacts within the authorised Country, Brand and Centre scope and the Lead Centre Sharing list. | Creates and edits Leads, maintains Lead Family relationships and Contacts, sets Dead Lead when permitted. |
| Centre Administration | Leads and Contacts of authorised Centres. | Maintains Family and Contact information according to configured permissions. |
| HQ Admin | Configured cross-Centre visibility. | Bulk reassigns Lead owners and imports Leads when the role grants these actions. |
| Marketing | Authorised marketing scope. | Views Lead source and Reference Log information; imports Leads when the role grants the action. |
| System | Lead, Contact and relationship records. | Applies duplicate rules (BBA-42), initialises Centre Sharing (BBA-41), derives lifecycle statuses, validates imports and records audit history. |
| Unauthorised User | Outside the permitted role or data scope. | Does not see or change restricted Leads, Contacts or fields. |

Access follows the existing role-based permission model and data scope. Preferred Centre is only a Lead attribute; the Centre Sharing list determines Centre-level visibility (SRS §2). All list screens support search, data filtering, column sorting, pagination with 20 / 50 / 100 rows and export within the user's scope. Records that have been used in the system are never deleted.

## 5. Feature Overview and Functional Decomposition

| Module | Feature | Function | User Story | WBS classification |
|---|---|---|---|---|
| Lead | Lead Master list | List, search, filter by status, sort, paginate, export and open Leads. | US-001 | Core Platform (included) |
| Lead | Create Lead | Capture a prospective-child Lead from a staff, web or event channel. | US-002 | Core Platform (included) |
| Lead | Lead Detail | View and edit Lead identity; view related Enquiries, converted Child and Reference Log. | US-003 | Core Platform (included) |
| Lead | Lead lifecycle status | Derive and change Lead status under the approved transition rules. | US-004 | Core Platform (included) |
| Family | Lead Family relationships | Maintain relationships and responsibility roles at Lead scope. | US-005 | Core Platform (included) |
| Contact | Contact master | List, search, duplicate check, reuse, create, edit and merge Contacts. | US-006 | Core Platform (included) |
| Lead | Bulk reassign Lead owner | Change the owner of selected Leads within the permitted scope. | US-007 | WBS Phase 2 (2.1.1.04) |
| Lead | Import Leads from Excel | Validate rows, apply duplicate rules and report row-level results. | US-008 | WBS Phase 2 (2.1.1.05) |

## 6. Functional Requirements by User Story

### 6.1 US-001 - Find and Open Leads

#### User Story

As an Admissions user, I want to list, search and filter Leads within my scope so that I can open the right prospective-child record without creating a duplicate.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-001 | The system shall list Leads as reusable prospective-child identity records within the user's Country, Brand, Centre and Centre Sharing scope. |
| FR-002 | The system shall search Leads by the approved Lead display data (OQ-LCM-02) and return only Leads within the user's scope. |
| FR-003 | The system shall filter Leads by Lead status, including every status in the approved status set (OQ-LCM-01). Inactive Leads remain searchable (BBA-40). |
| FR-004 | The system shall support column sorting, pagination of 20, 50 or 100 rows and export of the filtered list within the user's scope. |
| FR-005 | Selecting a Lead shall open Lead Detail without converting the Lead into an Enquiry. |

#### Functional Flow - Main

1. The user opens the Leads list (FR-001).
2. The system loads Leads within the user's scope, sorted by the default order of the approved prototype (FR-001; VAL-001).
3. The user enters a search value or selects a status filter (FR-002, FR-003).
4. The system returns the matching Leads in scope (FR-002, FR-003).
5. The user opens a Lead; the system shows Lead Detail (FR-005).

#### Functional Flow - Alternative

1. No Lead matches: the system shows the approved empty state; no Lead is created.
2. The user exports the list: the export contains only the filtered Leads within scope (FR-004; VAL-002).
3. The user changes the page size to 20, 50 or 100 rows; filters and sort order remain applied (FR-004).

#### Functional Flow - Exception

1. A Lead leaves the user's scope after the list loads: opening it applies the standard access-denied behaviour (VAL-001).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-001 | A Lead is a reusable prospective-child identity record, distinct from an Enquiry, and may be linked to multiple Enquiries (BR-CRM-001). |
| BR-002 | List, search, filter and export never return records outside the user's Country, Brand, Centre or Centre Sharing scope (AC-CRM-022). |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-001 | The Lead is outside the user's data scope. | Do not list or open it; apply the standard access-denied behaviour. |
| VAL-002 | The user exports a filtered list. | Export only the records returned by the active filters within scope. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-001 - Leads list | Prototype screen "Leads" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Search | Search field | No | Empty | Existing search rules. | Searches the approved Lead display data in scope. |
| Lead status filter | Filter | No | All statuses | Approved status set. | Narrows the list by status. |
| Lead list columns | Table | Yes | Prototype columns (OQ-LCM-02) | Permission-controlled fields. | Shows one row per Lead; masked fields follow the access model. |
| Page size | Selector | Yes | 20 | 20, 50, 100. | Changes the number of rows per page. |
| Export | Action | No | By permission | Export permission. | Exports the filtered list in scope. |
| Lead row | Link | Yes | — | Lead in scope. | Opens Lead Detail. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-001 | Listing, searching, filtering and exporting do not create or modify Lead records. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | a user limited to Centre A and Leads shared with Centres A and B | the user opens the Leads list | only Leads shared with Centre A are listed | FR-001; BR-002; VAL-001 |
| AC-002 | an Inactive Lead within scope | the user filters by the Inactive status | the Inactive Lead is returned | FR-003 |
| AC-003 | a filtered list of 35 Leads | the user selects page size 20 | page 1 shows 20 rows and page 2 shows 15 rows with the same filter | FR-004 |
| AC-004 | an active filter | the user exports the list | the file contains only the filtered Leads within scope | FR-004; VAL-002 |
| AC-005 | a Lead in the list | the user opens it | Lead Detail opens and no Enquiry is created | FR-005; BR-001 |

#### Dependencies

Existing role, Centre and data-scope model; Centre Sharing list (BBA-41); approved Lead status set (OQ-LCM-01); prototype "Leads".

### 6.2 US-002 - Create a Lead

#### User Story

As an Admissions user, I want to capture a new prospective-child Lead from a staff, web or event channel so that the family can be followed up through Enquiries.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-006 | The system shall capture a Lead from an authorised staff user, the website or API, or an event, with the Lead identity fields of the approved prototype (OQ-LCM-03). |
| FR-007 | Before saving, the system shall run the Lead duplicate check of BBA-42 and hand the result to the BBA-42 handling flow. |
| FR-008 | When no duplicate is found, the system shall save the Lead with status New and initialise its Centre Sharing list with the creator's Centre (BBA-41 FR-001). |
| FR-009 | The system shall record the immutable true source of the Lead at creation (BR-CRM-004). |
| FR-010 | The system shall assign the Lead owner according to the approved assignment rule (OQ-LCM-04). |

#### Functional Flow - Main

1. The user opens Create Lead and enters the Lead identity data (FR-006).
2. The user selects Save; the system validates required fields (VAL-003).
3. The system runs the BBA-42 duplicate check (FR-007).
4. No duplicate is found: the system saves the Lead with status New, initialises Centre Sharing, records the true source and assigns the owner (FR-008, FR-009, FR-010).
5. The system opens the new Lead Detail.

#### Functional Flow - Alternative

1. A duplicate is found: the BBA-42 manual result handling applies (Cancel, Save on the existing Lead, or Reopen Lead); no new Lead is created (FR-007).
2. The Lead arrives through the website or API: the same duplicate and Centre Sharing rules apply without a user screen (FR-006, FR-007).

#### Functional Flow - Exception

1. A required field is missing or invalid: the Lead is not saved and the field shows the standard validation message (VAL-003).
2. The save fails: no Lead, Centre Sharing entry or source record persists; the standard failure result is shown (VAL-004).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-003 | A new Lead is created only when no duplicate is confirmed under BBA-42; a confirmed duplicate reuses the existing Lead and no Leads are merged automatically (BR-CRM-002, BR-CRM-005). |
| BR-004 | The true source and Reference Log form an immutable intake snapshot. Later attribution edits do not overwrite it (BR-CRM-004). |
| BR-005 | Preferred Centre is a Lead attribute only; it does not grant Centre access (SRS §2). |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-003 | A required Lead identity field is missing or has an invalid format. | Do not save; show the standard field validation message. |
| VAL-004 | Any part of the Lead creation transaction fails. | Roll back the Lead, Centre Sharing and source records; show the standard failure result. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-002 - Create Lead | Prototype screen "Leads" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Lead identity fields | Form | Per OQ-LCM-03 | Empty | Field-level rules of the approved prototype. | Lead Full Name, Email and Date of Birth are the BBA-42 comparison fields. |
| Preferred Centre | Selector | No | Empty | Active Centre. | Stored as a Lead attribute only. |
| Save | Action | Yes | Enabled | VAL-003. | Runs the duplicate check, then saves. |
| Cancel | Action | Yes | Enabled | None. | Closes without creating a Lead. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-002 | Store the Lead creator, creation timestamp, true source and initial status New through the existing audit mechanism. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-006 | valid Lead data with no duplicate under BBA-42 | the user saves | the Lead is created with status New and the creator's Centre is first in Centre Sharing | FR-007; FR-008; BR-003 |
| AC-007 | Lead data that matches an existing Lead under BBA-42 | the user saves | no new Lead is created and the BBA-42 result actions are shown | FR-007; BR-003 |
| AC-008 | a required identity field is blank | the user saves | the Lead is not saved and the field shows the validation message | VAL-003 |
| AC-009 | a Lead created from the website | a user later edits the Lead's campaign attribution | the true source recorded at creation is unchanged | FR-009; BR-004 |
| AC-010 | Preferred Centre B and creator Centre A | the Lead is saved | Centre B is stored as Preferred Centre and is not added to Centre Sharing | BR-005 |
| AC-011 | the save transaction fails after the duplicate check | the result is shown | no Lead, Centre Sharing entry or source record exists | VAL-004 |

#### Dependencies

BBA-42 duplicate detection; BBA-41 Centre Sharing initialisation; owner assignment rule (OQ-LCM-04); approved Lead identity fields (OQ-LCM-03).

### 6.3 US-003 - View and Edit a Lead Profile

#### User Story

As an Admissions user, I want to view and edit the Lead profile and see its related Enquiries, converted Child and Reference Log so that I work from one accurate identity record.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-011 | Lead Detail shall show the prospective-child identity information at Lead scope, separately from Enquiry preferences and history. |
| FR-012 | An authorised user shall edit the approved Lead identity fields without overwriting Enquiry preferences, Journey execution or Visit history. |
| FR-013 | Lead Detail shall list every Enquiry linked to the Lead with its Brand and Centre, and open the selected Enquiry Detail (BBA-43) without moving its history onto the Lead. |
| FR-014 | When a converted Child exists, Lead Detail shall open the linked Child profile without replacing the Lead identity. |
| FR-015 | Lead Detail shall display the immutable Reference Log history, related Centre and original true source without changing Enquiry attribution. |
| FR-016 | Before saving an edit, the system shall run the BBA-42 duplicate check for manual Lead edits. |

#### Functional Flow - Main

1. The user opens Lead Detail (FR-011).
2. The system shows identity data, related Enquiries, Reference Logs and, when present, the converted Child link (FR-011, FR-013, FR-014, FR-015).
3. The user edits identity fields and selects Save (FR-012).
4. The system validates the fields and runs the BBA-42 edit duplicate check (VAL-005; FR-016).
5. No duplicate is found: the system saves the changes and records audit history (DATA-003).

#### Functional Flow - Alternative

1. The Lead has no Enquiry: the related Enquiry list shows the approved empty state.
2. No Child exists: the Child link is not shown.
3. The user opens a related Enquiry: Enquiry Detail (BBA-43) opens (FR-013).

#### Functional Flow - Exception

1. The edit creates a duplicate under BBA-42: the save is blocked and the BBA-42 edit result applies (FR-016).
2. The Lead is Inactive: editing is unavailable (BBA-40 BR-009).
3. Another user saved the Lead after it was opened: the save is rejected and the user reviews the refreshed data (VAL-006).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-006 | Lead-level Family relationships and Contact responsibility roles belong to the Lead, not to an Enquiry; Lead Detail shows related Enquiries without copying their operational history (BR-CRM-003). |
| BR-007 | Editing Lead identity never changes Enquiry preferences, Journey runtime or Visit history. |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-005 | An edited field is invalid or a required field is cleared. | Do not save; show the standard field validation message. |
| VAL-006 | The Lead changed after the user opened it. | Reject the save; refresh the Lead and ask the user to review before saving again. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-003 - Lead Detail | Prototype screen "Lead Detail" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Lead identity fields | Display / Form | Per OQ-LCM-03 | Persisted values | VAL-005. | Editable by permission; read-only when Inactive. |
| Related Enquiries | Table | Yes | Linked Enquiries / empty | Enquiries in scope. | Shows Enquiry, Brand, Centre and status; row opens Enquiry Detail. |
| Converted Child | Link | Conditional | Shown when a Child exists | Child access permission. | Opens the Child profile. |
| Reference Log | Table | Yes | Persisted entries / empty | Read-only. | Shows date, source, campaign, Centre and true source. |
| Edit / Save | Action | By permission | Enabled for editable Lead | VAL-005, VAL-006; BBA-42. | Saves identity changes. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-003 | Record the user, timestamp and before and after values for every saved Lead identity change. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-012 | a Lead with two Enquiries at different Centres | the user opens Lead Detail | both Enquiries are listed with Brand and Centre | FR-013; BR-006 |
| AC-013 | an Enquiry with preferred Level K1 | the user edits the Lead name and saves | the Enquiry preferred Level remains K1 | FR-012; BR-007 |
| AC-014 | a Lead with a converted Child | the user selects the Child link | the Child profile opens and the Lead identity is unchanged | FR-014 |
| AC-015 | a Lead with a Reference Log from an API intake | the user opens Lead Detail | the Reference Log shows its source, campaign and Centre read-only | FR-015 |
| AC-016 | an edit that matches another Lead under BBA-42 | the user saves | the save is blocked and the BBA-42 edit result is shown | FR-016 |
| AC-017 | another user saved the Lead after it was opened | the user saves | the save is rejected and refreshed data is shown | VAL-006 |
| AC-018 | a saved identity change | the change is committed | audit records the user, timestamp, old value and new value | DATA-003 |
| AC-019 | an editable Lead | the user clears a required identity field and saves | the change is not saved and the field shows the validation message | VAL-005 |

#### Dependencies

BBA-42 edit duplicate check; BBA-43 Enquiry Detail; BBA-40 Inactive restrictions; Child profile (SMS Children and Families).

### 6.4 US-004 - Maintain the Lead Lifecycle Status

#### User Story

As an Admissions user, I want the Lead status to reflect the Lead's progress so that lists, filters and reports show where each family stands.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-017 | The system shall set status New when a Lead is created. |
| FR-018 | The system shall change the status to Inprogress when the first Call is recorded for the Lead. |
| FR-019 | The system shall change the status to Converted when at least one linked Enquiry is converted. |
| FR-020 | An authorised user shall set Dead Lead manually. |
| FR-021 | The Inactive Lead action (BBA-40) shall set the inactive / closed status defined by OQ-LCM-01. |
| FR-022 | Every status change shall be permission-controlled and recorded in audit history. |

#### Functional Flow - Main

1. A Lead is created with status New (FR-017).
2. A user records the first Call for the Lead; the system sets Inprogress (FR-018).
3. An Enquiry of the Lead is converted; the system sets Converted (FR-019).
4. Each change is recorded in audit history (FR-022).

#### Functional Flow - Alternative

1. A permitted user sets Dead Lead with the reason required by OQ-LCM-06 (FR-020).
2. A user runs Inactive Lead: BBA-40 applies (FR-021).

#### Functional Flow - Exception

1. A user without the status permission tries to set Dead Lead: the action is unavailable (VAL-007).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-008 | Lead lifecycle statuses are New, Inprogress, Converted, Dead Lead and Closed (BR-CRM-008). Inprogress is set by the first Call; Converted requires at least one converted Enquiry; Dead Lead is selected by a user; Closed results from the Inactive Lead function. The final status names, including Inactive, are pending OQ-LCM-01. |
| BR-009 | Status changes remain permission-controlled and auditable (BR-CRM-008, BR-CRM-022). |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-007 | The user lacks permission to change the Lead status. | Do not show the status action; keep the status unchanged. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-004 - Lead status | Prototype screen "Lead Detail" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Lead status | Display | Yes | New | Approved status set. | Shows the current lifecycle status. |
| Set Dead Lead | Action | No | By permission | VAL-007. | Changes the status to Dead Lead. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-004 | Record the actor (user or System), timestamp, previous status and new status for every Lead status change. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-020 | a new Lead | the Lead is saved | its status is New | FR-017; BR-008 |
| AC-021 | a Lead with status New and no Call | a user records the first Call | the status becomes Inprogress and audit records System as actor | FR-018; DATA-004 |
| AC-022 | a Lead with two Enquiries | one Enquiry is converted | the Lead status becomes Converted | FR-019 |
| AC-023 | a user without the status permission | the user opens Lead Detail | Set Dead Lead is not shown | VAL-007; BR-009 |

#### Dependencies

Call logging (Enquiry and Customer Journey FSD); Enquiry conversion (Waitlist, Registration and Child Record Preparation FSD); BBA-40; OQ-LCM-01, OQ-LCM-06.

### 6.5 US-005 - Maintain Lead Family Relationships

#### User Story

As an Admissions user, I want to maintain the family members of a Lead and their responsibility roles so that the correct people are contacted and billed later.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-023 | Lead Detail shall show the Family relationships and the linked Contacts with their relationship roles at Lead scope. |
| FR-024 | An authorised user shall add, change or remove a relationship and its roles (Primary, Billing, Emergency, Authorised pickup) at Lead scope. |
| FR-025 | Adding a family member shall search the Contact master first and reuse an existing Contact (US-006). |
| FR-026 | Contact master data shall be edited in the Contact context; Lead Detail edits only the relationship. |

#### Functional Flow - Main

1. The user opens the Family area of Lead Detail (FR-023).
2. The user adds a family member; the system searches the Contact master (FR-025).
3. A matching Contact exists: the user links it and selects the roles (FR-024).
4. The system saves the relationship and records audit history (DATA-005).

#### Functional Flow - Alternative

1. No matching Contact exists: the user creates a Contact (US-006), then links it (FR-025).
2. The user changes the Primary role to another Contact: the previous Primary loses the Primary role (BR-011).

#### Functional Flow - Exception

1. The Lead is Inactive: relationship changes are unavailable (BBA-40 BR-009).
2. A second Primary is selected without removing the first: the system keeps one Primary as defined in BR-011.

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-010 | Relationship and responsibility roles (Primary, Billing, Emergency, Authorised pickup) exist at Lead and Child scope, not at Enquiry scope (BR-CRM-046, BR-CRM-047). |
| BR-011 | Only one Primary Contact is permitted per Lead. Changing the Child Primary Contact does not change the Lead Primary Contact (BR-CRM-049). |
| BR-012 | An existing Contact is reused and only the relationship is created (BR-CRM-048). |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-008 | A user selects Primary for a Contact while another Contact holds Primary on the Lead. | Move Primary to the selected Contact after user confirmation; the Lead keeps one Primary. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-005 - Lead Family | Prototype screen "Lead Detail" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Family members | Table | Yes | Linked Contacts / empty | Permission-controlled fields. | Shows name, relationship and roles. |
| Add family member | Action | No | By permission | Lead editable. | Searches the Contact master, then links or creates. |
| Roles | Multi-select | No | None | VAL-008. | Primary, Billing, Emergency, Authorised pickup. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-005 | Record the user, timestamp and before and after relationship and role values for every saved change. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-024 | an existing Contact matching the parent | the user adds the parent to a Lead | the existing Contact is linked and no new Contact is created | FR-025; BR-012 |
| AC-025 | a Lead whose Primary is Contact A | the user sets Primary on Contact B and confirms | Contact B is Primary and Contact A keeps its other roles | VAL-008; BR-011 |
| AC-026 | a linked Lead and Child with different Primary Contacts | the user changes the Child Primary | the Lead Primary is unchanged (AC-CRM-018) | BR-011 |
| AC-027 | an Enquiry of the Lead | the user opens the Enquiry | no relationship roles are shown or editable on the Enquiry | BR-010 |
| AC-028 | a saved relationship change | the change is committed | audit records the user, timestamp and old and new values | DATA-005 |

#### Dependencies

US-006 Contact master; BBA-40 Inactive restrictions; Child relationships (Waitlist, Registration and Child Record Preparation FSD).

### 6.6 US-006 - Maintain the Contact Master

#### User Story

As an Admissions or Centre Administration user, I want one reusable record per person so that parent details are entered once and stay consistent across Leads, Enquiries and Children.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-027 | The system shall list Contacts within the user's scope and search them by name, phone, email or Contact ID. |
| FR-028 | Before creating a Contact, the system shall check the Contact master for an exact match on Full name + Phone + Email and offer the matching Contact for reuse. |
| FR-029 | The system shall create a new Contact only when no existing Contact can be reused. |
| FR-030 | Editing the Contact master shall update the same person in every linked Lead, Enquiry and Child context. |
| FR-031 | When an identity number (NRIC / FIN / MyKad / Passport) matches another Contact, the system shall merge the accounts under OQ-LCM-05. |
| FR-032 | Contact Detail shall show the Contact's relationships to Leads and Children and route the user to the Lead or Child relationship for role maintenance. |

#### Functional Flow - Main

1. The user searches the Contact list (FR-027).
2. The user starts Create Contact and enters the details.
3. The system checks Full name + Phone + Email (FR-028; VAL-009).
4. No match: the system creates the Contact (FR-029).
5. The user links the Contact to a Lead or Child relationship (US-005).

#### Functional Flow - Alternative

1. An exact match exists: the system offers the existing Contact; the user reuses it (FR-028; BR-012).
2. The user edits a Contact: the change appears in every linked context (FR-030).
3. The identity number matches another Contact: the merge under OQ-LCM-05 applies (FR-031).

#### Functional Flow - Exception

1. A required Contact field is missing or invalid: the Contact is not saved (VAL-010).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-013 | Editing the Contact master updates the same person across linked Lead, Enquiry and Child contexts (BR-CRM-050). |
| BR-014 | Responsibility roles belong to the Lead or Child relationship, not to the Contact alone. |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-009 | Full name, Phone and Email exactly match an existing Contact. | Do not create a second Contact; offer the existing Contact for reuse. |
| VAL-010 | A required Contact field is missing or has an invalid format. | Do not save; show the standard field validation message. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-006 - Contacts / Contact Detail | Prototype screens "Contacts" and "Contact Detail" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Search | Search field | No | Empty | Name, phone, email, Contact ID. | Searches Contacts in scope. |
| Full name, Phone, Email | Form | Yes | Empty | VAL-009, VAL-010. | Used for the duplicate check. |
| Identity number | Form | No | Empty | NRIC / FIN / MyKad / Passport format. | Used for merge (OQ-LCM-05). |
| Relationship usage | Table | Yes | Linked Leads and Children | Read-only. | Opens the Lead or Child relationship. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-006 | Record the user, timestamp and before and after values for every Contact change and merge; a merged Contact keeps its history. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-029 | a Contact "Nguyen Thu Ha", 0901 234 567, ha.nguyen@example.com | a user creates a Contact with the same three values | the existing Contact is offered and no second Contact is created (AC-CRM-017) | FR-028; VAL-009 |
| AC-030 | a Contact linked to one Lead and one Child | the user changes the Contact phone | the new phone shows on the Lead and the Child | FR-030; BR-013 |
| AC-031 | the same values except a different email | the user saves | a new Contact is created | FR-029 |
| AC-032 | a Contact linked to a Lead | the user opens Contact Detail | the Lead relationship is listed and opens the Lead relationship | FR-032; BR-014 |
| AC-033 | Create Contact with a blank phone | the user saves | the Contact is not saved and the phone field shows the validation message | VAL-010 |

#### Dependencies

Contact identity-number merge decision (OQ-LCM-05); US-005; Child relationships.

### 6.7 US-007 - Bulk Reassign Lead Owner (WBS Phase 2)

#### User Story

As an HQ Admin, I want to change the owner of several Leads at once so that work is redistributed when staff change.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-033 | An authorised user shall select multiple Leads in the list and assign one new owner within the permitted scope. |
| FR-034 | The system shall save each Lead independently, keep successful changes and identify each failed Lead. |

#### Functional Flow - Main

1. The user selects Leads in the list and chooses Reassign owner (FR-033).
2. The user selects the new owner and confirms.
3. The system updates each Lead and shows the result (FR-034; DATA-007).

#### Functional Flow - Alternative

1. Some Leads fail validation: successful Leads keep the new owner; failed Leads are listed (FR-034).

#### Functional Flow - Exception

1. The new owner is outside the Lead's scope or inactive: that Lead is not reassigned (VAL-011).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-015 | Bulk reassignment changes the Lead owner only; Enquiry owners change only under OQ-LCM-08. |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-011 | The selected owner is inactive or has no access to the Lead. | Skip that Lead and list it as failed with the reason. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-007 - Bulk reassign | Prototype screen "Leads" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Row selection | Checkbox | No | Unselected | Leads in scope. | Selects Leads to reassign. |
| New owner | Selector | Yes | Empty | VAL-011. | Lists active users in scope. |
| Result message | Message | Yes | System standard | Actual result. | Shows success, failure or partial success. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-007 | Record the user, timestamp and previous and new owner for each reassigned Lead. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-034 | 10 selected Leads, one outside the new owner's scope | the user confirms reassignment | 9 Leads have the new owner and 1 is listed as failed with the reason | FR-034; VAL-011 |
| AC-035 | a reassigned Lead | the change is committed | audit records previous and new owner | DATA-007 |
| AC-036 | a reassigned Lead with an Enquiry | the reassignment completes | the Enquiry owner follows OQ-LCM-08 | BR-015 |

#### Dependencies

User and scope data; OQ-LCM-08.

### 6.8 US-008 - Import Leads from Excel (WBS Phase 2)

#### User Story

As an authorised Marketing or Admissions user, I want to import Leads from an Excel file so that event and campaign lists enter the CRM without manual typing.

#### Functional Requirements

| FR ID | Functional Requirement |
|---|---|
| FR-035 | The system shall accept an Excel file in the approved template (OQ-LCM-07) and validate each row. |
| FR-036 | Each valid row shall apply the same duplicate and ambiguous-match rules as standard intake (BBA-42): a new Lead for no match, a Reference Log on the existing Lead for a confirmed duplicate, and review routing for an ambiguous match. |
| FR-037 | The system shall report the outcome of every row (created, Reference Log, ambiguous, rejected with reason) in the import result and a downloadable error file. |
| FR-038 | The importing user shall receive the in-application import result notification. |

#### Functional Flow - Main

1. The user uploads the Excel file (FR-035).
2. The system validates each row (VAL-012).
3. The system applies duplicate rules to each valid row (FR-036).
4. The system shows the row results and notifies the user (FR-037, FR-038).

#### Functional Flow - Alternative

1. A row matches an existing Lead: a Reference Log is added; no Lead is created (FR-036).
2. A row has an ambiguous match: it is routed for review and not created (FR-036).

#### Functional Flow - Exception

1. The file is not in the approved template: the import stops before any row is processed (VAL-013).
2. A row fails validation: that row is rejected with its reason; other rows continue (VAL-012).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-016 | Excel import applies the same duplicate and ambiguous-match rules as standard intake; import errors are reported by row and are never skipped silently (BR-CRM-011). |

#### Validation Rules

| VAL ID | Condition | System Response |
|---|---|---|
| VAL-012 | A row has a missing required value or an invalid format. | Reject the row with the reason in the result and the error file. |
| VAL-013 | The file does not match the approved template. | Stop the import; process no rows; show the template error. |

#### UI Reference

| Screen ID / Version | Reference / Link |
|---|---|
| LCM: UI-US-008 - Import Leads | Prototype screen "Leads" — Figma link to be provided (OQ-LCM-09) |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Validation | Behaviour |
|---|---|---|---|---|---|
| Upload file | File input | Yes | Empty | VAL-013. | Accepts the approved Excel template. |
| Row result table | Table | Yes | After processing | — | Shows row number, outcome and reason. |
| Download error file | Action | Conditional | Shown when rows are rejected or ambiguous | — | Downloads the row-level result. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-008 | Keep the import run, the importing user, the timestamp and the row outcomes. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-037 | an Excel row that matches an existing Lead | the row is imported | a Reference Log is created on the existing Lead and the row outcome is recorded (AC-CRM-041) | FR-036; BR-016 |
| AC-038 | a file with 50 rows, 2 missing the required name | the import completes | 48 rows are processed, 2 rows are rejected with the reason, and the error file lists both | FR-037; VAL-012 |
| AC-039 | a file not in the approved template | the user uploads it | no row is processed and the template error is shown | VAL-013 |
| AC-040 | a completed import | the result is ready | the importing user receives the in-application import notification | FR-038 |

#### Dependencies

Approved import template and field mapping (OQ-LCM-07); BBA-42 duplicate rules; review queue for ambiguous matches.

## 7. Open Questions

| Question ID | Decision Needed | Owner | Priority | Decision BBA |
|---|---|---|---|---|
| OQ-LCM-01 | Confirm the Lead status set. SRS BR-CRM-008 lists New, Inprogress, Converted, Dead Lead and Closed; SRS 2.1 lists New, Inprogress, Converted, Closed Lead and Inactive; BBA-40 sets Inactive and BBA-42 reopens Closed to New. | Business Owner | High | |
| OQ-LCM-02 | Which Lead fields are list columns and searchable "approved Lead display data"? | Business Owner / Design | Medium | |
| OQ-LCM-03 | Which Lead identity fields are required at creation (SRS: identity fields TBD; BBA-42 compares Lead Full Name, Email and Date of Birth)? | Business Owner | High | |
| OQ-LCM-04 | How is the Lead owner assigned at creation (creator, Centre default, round robin)? | Business Owner | Medium | |
| OQ-LCM-05 | Identity-number merge of Contacts: automatic or user-confirmed, who may merge, and which values win when the two Contacts differ? | Business Owner | High | |
| OQ-LCM-06 | Dead Lead: is a reason required, can it be reversed, and does it affect linked Enquiries? | Business Owner | Medium | |
| OQ-LCM-07 | Excel import template, mandatory columns, maximum rows per file and the owner of the ambiguous-match review queue. | Business Owner / Marketing | Medium | |
| OQ-LCM-08 | Does bulk reassignment of a Lead owner also reassign the Lead's Enquiry owners? | Business Owner | Medium | |
| OQ-LCM-09 | Figma links for the Sprint 4 Lead and Contact screens. | Design | Medium | |
| OQ-LCM-10 | When the only converted Enquiry is later withdrawn, does the Lead leave Converted status? | Business Owner | Low | |

## 8. Glossary

| Term | Definition in This FSD |
|---|---|
| Lead | A reusable prospective-child identity record, linked to one or more Enquiries. |
| Contact | A reusable person-master record (parent, guardian, other family member). |
| Family relationship | The link between a Contact and a Lead or Child, with responsibility roles. |
| Responsibility role | Primary, Billing, Emergency or Authorised pickup, held at Lead or Child scope. |
| True source | The immutable intake source recorded when the Lead was created. |
| Reference Log | An immutable intake record on an existing Lead for a confirmed duplicate intake (BBA-42). |
| Core Platform (included) | SRS implementation classification: part of the platform baseline. |
