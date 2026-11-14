Busy Bees Asia

Customer Relationship Management (CRM)

# Software Requirements Specification (SRS)

**CRM Admissions**

Review baseline • 29 October 2026 • v0.1

# Document Control Information

| **Version** | **Date**        | **Prepared by** | **Description**         |
|-------------|-----------------|-----------------|-------------------------|
| 0.1         | 29 October 2026 | DOTB / BA       | Document initialization |

## Conventions

- A Feature is an individual action performed by a user or the system; a Function describes the detailed behaviour of each Feature.

- Business Rules are coded BR-CRM-NNN and Acceptance Criteria are coded AC-CRM-NNN. Implementation classifications are aligned with the current WBS: Core Platform (included), WBS Phase 1, WBS Phase 2, WBS Phase 3, or Not identified in the WBS.

- The following rules apply across all modules:

- Access and actions are governed by user permissions.

- All list screens support search, data filtering, column sorting, pagination with 20 / 50 / 100 rows, and data export.

- Records that have been used in the system are never deleted.

- Screen names and displayed content must follow the approved prototype design.

# 1. Purpose and Scope

This SRS defines the Busy Bees Asia CRM admissions capability for Singapore, Malaysia and Vietnam: Lead intake, Enquiry management, Journey follow-up, Visit booking, Waitlist and Offer, Registration and Enrolment confirmation, together with related Marketing and operational reporting. The document is organised by module and sub-module so Development and QA can verify the implementation against the prototype.

## 1.1 Phase 1 Scope

Phase allocation is applied at WBS feature level rather than at module level. A CRM module may therefore contain both Phase 1 features and features deferred to a later release.

- Leads and core Enquiry records: Centre sharing (2.1.1.01), Duplicate detection on create (2.1.1.02), Inactive Lead (2.1.1.00), Enquiry detail page (2.1.2.01), and View timeline (2.1.2.03).

- Enquiry list: Phase 1 provides the table-based Enquiry list noted under WBS item 2.2.1.02.

- Enquiry actions: Action framework (2.3.1.01), Mark visited (2.3.1.02), Log no-show (2.3.1.03), Parent is considering (2.3.1.04), Log follow-up (2.3.1.05), and Hold the space (2.3.1.09).

- Journey automation foundation: Journey assignment resolution (2.3.2.03), Event-key engine (2.3.2.05), Task assignment resolution (2.3.2.07), and Automated messages (2.3.2.08).

- Visit calendar and booking: Calendar views and filters (2.4.1.01-2.4.1.02), together with the Phase 1 Visit booking features (2.4.2.01-2.4.2.11), including configured and ad-hoc slots, hosts, confirmation, rescheduling, cancellation, Visit detail, soft deletion, parent self-booking, and multi-child scheduling.

- Open Day: create, edit or cancel, pre-select attendees, parent self-booking with capacity checks, and attendance recording (2.4.3.01-2.4.3.05).

- Conversion and Registration: convert or add to waitlist, create Child, Family and Enrolment records, and create the registration or deposit invoice (2.5.1.01-2.5.1.03); start and resume Registration, complete Registration detail actions, check payment, assign class, create invoices, and submit Registration (2.5.2.02-2.5.2.06 and 2.5.2.08); online Registration, Registration review, and parent onboarding (2.5.3.01, 2.5.3.03 and 2.5.3.04).

- CRM administration: Journey template versioning, visual Journey builder, Journey preview, and Activity Template runtime rules (2.8.1.01-2.8.1.04); Visit Slot Schedule CRUD, generation and review of dated Slot occurrences, and cancellation of a generated Slot (2.8.2.01-2.8.2.03).

## 1.2 Deferred to Phase 2 or Later Releases

The following CRM WBS features are excluded from Phase 1 and are planned for Phase 2 or a later release.

- Phase 2 - Lead and Enquiry enhancements: Merge with existing Lead, Bulk reassign owner, Lead import, and system-calculated Enquiry score (2.1.1.03-2.1.1.05 and 2.1.2.02).

- Phase 2 - Work queues and pipeline: My Work, Kanban Pipeline Board, SLA clocks, round-robin assignment, and age eligibility checks (2.2.1.01-2.2.1.05). The Phase 1 exception is the table-based Enquiry list stated in the WBS note for 2.2.1.02.

- Phase 2 - Enquiry actions and Journey work management: Schedule for later and Transfer Centre (2.3.1.06-2.3.1.07); Journey and Task checklist, Change Journey or apply the latest version, Add manual Task, and Task SLA handling (2.3.2.01-2.3.2.02, 2.3.2.04 and 2.3.2.06).

- Phase 2 - Visit Calendar side panels: Not confirmed, Needs reschedule, and Waiting to book (2.4.1.03). Calendar views and filters remain in Phase 1.

- Phase 2 - Trial management: class and capacity selection, Trial invoices and payment, free Trial handling, Trial session scheduling and updates, outcomes, parent confirmation, and Enquiry Trial status (2.4.4.01-2.4.4.09).

- Phase 2 - Waitlist and Registration extensions: Waitlist queue and fee or refund-window tracking (2.5.1.06 and 2.5.1.09); Registration and Enrolment list and multi-invoice fee collection (2.5.2.01 and 2.5.2.07); GIRO application within Registration (2.5.3.02).

- Phase 2 - Campaign and renewal extensions: Post-visit survey (2.6.1.02) and the complete Lead Renewal run capability (2.7.1.01-2.7.1.06).

- Phase 2 - Visit Slot Schedule governance: submit changes for approval, approve or reject changes, apply impact rules to existing bookings, and maintain Visit type duration settings and history (2.8.2.04-2.8.2.07).

- Phase 3 - Waitlist and Offer extensions: Slot available conversion, Places availability, Waitlist priority rules, and Offer processing (2.5.1.04-2.5.1.05 and 2.5.1.07-2.5.1.08).

- Phase 3 - Later CRM extensions: advertising-spend linkage for CPL and CPA reporting (2.6.1.01) and the e-Form 1 acknowledgement reminder and two-month trigger (2.5.3.05).

## 1.3 Outside CRM Scope and Undecided Items

- Outside CRM: post-enrolment attendance, classroom and learning operations, withdrawal or transfer after enrolment, re-enrolment, internal finance and banking processing, parent services, and regulatory systems.

- CRM Registration captures Child, Family, Document, Health and Consent context before Enrolment. Post-Enrolment records and processes belong to SMS Children & Families and other SMS SRS documents; implementation must align the ownership and handoff boundaries.

# 2. User Roles

| **Role or Actor**             | **Responsibilities and Access Limitations**                                                                                                                                                                                                                                      |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HQ Admin                      | Administers CRM configuration, permissions, Country, Brand and Centre settings, and cross-Centre visibility subject to permissions.                                                                                                                                              |
| Marketing                     | Manages supported Campaigns, intake attribution, and Marketing or Admissions reporting. Direct platform synchronisation and EDM are outside Phase 1.                                                                                                                             |
| Admissions / Customer Service | Captures Leads, handles Reference Logs and Enquiries, records Calls, performs Journey follow-up, manages Visits, Waitlist and Offers, and initiates Registration within authorised Centres.                                                                                      |
| Centre Director               | Oversees Centre admissions, hosts, capacity, Visits, Offers, and country-specific approval or Registration activities.                                                                                                                                                           |
| Centre Administration         | Maintains admissions records, Registration readiness, Family and Child information, Documents, and Centre handoffs according to configured permissions.                                                                                                                          |
| Finance                       | Views authorised payment or invoice references and receives handoff data; financial processing is not performed in CRM.                                                                                                                                                          |
| Parent / Public Visitor       | Submits supported intake or Registration information and cannot create ad-hoc Visits.                                                                                                                                                                                            |
| System                        | Performs duplicate checks, creates a Reference Log for a duplicate confirmed during intake, automatically adds Centre Sharing from a Reference Log for another Centre, creates Journey or Slot updates, and applies configured notifications, audit records, and status changes. |

Access principle: Preferred Centre is only a Lead attribute; the Centre Sharing list determines Centre-level visibility. Users at a shared Centre receive Centre-level access subject to role and object permissions. A Lead must be shared with a Centre before an Enquiry for that Centre can be created.

# 3. Process Overview

## P1. Lead Intake Duplicate Handling and Centre Sharing

1.  Capture a Lead through an authorised staff user, website or API, event, or import, and apply the approved Lead matching rules.

2.  If a duplicate is confirmed, reuse the existing Lead and create a Reference Log; do not create a duplicate Lead or merge automatically.

3.  If a Reference Log records contact from another Centre, the system adds that Centre to the Lead Centre Sharing list. This action does not automatically create an Enquiry in this backlog.

4.  An authorised user may add or remove a shared Centre according to approved permission and validity rules. Preferred Centre is independent of Centre Sharing.

## P2. Enquiry Intake Renewal and Attribution

5.  After the Lead is resolved, select a Brand and a Centre already shared with the Lead, then capture Level, preferred Start date and Session.

6.  Compare Enquiry duplicates independently from Lead identity. Do not recreate a fully matching active Enquiry; renew Enquiry when eligible; and create a new Enquiry where a permitted different context applies.

7.  Retain the immutable true-source or Reference Log snapshot separately from self-reported source, Campaign, Channel, UTM and Promotion code; assign the appropriate owner and Journey.

## P3. Lead Lifecycle and Audited Closure

8.  An authorised user may inactivate a Lead after previewing all linked Enquiries; the system inactive the Lead and affected Enquiries atomically and retains history.

9.  A Inactive Lead remains searchable but read-only and is excluded from the active Pipeline; no new Enquiry or Reference Log may be created for it.

## P4. Journey and Follow-up

10. An Enquiry receives the applicable versioned Journey, including Stages and Tasks; users record Calls, Tasks, Activities and Messages.

11. Configured events complete automatic Tasks without double counting; Enquiry operational status and the Journey runtime are separate concepts.

## P5. Visits Events and Trial

12. Booking from Calendar allows selection of a parent and eligible Enquiries at the same Centre, including a family Visit linked to multiple Enquiries. When booking from Enquiry Detail, the parent and Enquiry are preselected and locked.

13. Select an available generated Slot or create an ad-hoc booking when authorised; record attendance and Visit outcomes against the correct Enquiry and Visit. Trial is not displayed as a Book Visit type.

14. Manage Open House at Centre level or across a Brand where approved. Trial is managed separately in eligible countries, Malaysia and Vietnam, and is not a Book Visit option.

## P6. Waitlist Offer Registration and Enrolment

15. Parent is considering proposes the next follow-up date after 48 continuous hours but does not reserve capacity; where appropriate, the Enquiry may enter the Waitlist.

16. Create an Offer when a place is available. Offer Accepted opens Registration; Offer Declined or Expired moves the associated Waitlist entry to the end of the queue.

17. Save and resume readiness data; manage Child, Family, Contact, Health, Document, Consent and class assignment; then submit Registration and Enrolment explicitly. Payment alone does not complete Enrolment.

## P7. Monitoring and Administration

18. Administrators maintain Journeys, Slot Schedules and exclusions within the approved scope. Marketing and Admissions users use defined dashboards and reports; exports respect filters and permissions.

19. Notifications route recipients to the source record, and material changes are retained in audit history.

# 4. Modules Sub-modules Features and Functions

Prototype: [<u>https://drive.google.com/file/d/1hANMGPB86NQreaBQcQI9NsVDSk1IqvrQ/view?usp=drive_link</u>](https://drive.google.com/file/d/1hANMGPB86NQreaBQcQI9NsVDSk1IqvrQ/view?usp=drive_link)

## 1. Admissions Workspace

### 1.1 My Work

*Prototype screen: My Work*

| **Object**   | **Feature**                 | **Function**                                                                                                               | **Implementation Classification** |
|--------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Enquiry      | View assigned Enquiry work  | Lists Enquiries assigned to the current user or role with due state.                                                       | WBS Phase 2                       |
| Enquiry      | Open assigned Enquiry       | Opens the selected Enquiry admissions context from My Work.                                                                | Core Platform (included)          |
| Journey Task | View assigned Journey Tasks | Shows Task name, Enquiry, Journey Stage, assignee and due / overdue state. The Task remains owned by the selected Enquiry. | WBS Phase 2                       |
| Notification | Open CRM Notification       | Shows an actionable assignment or due alert and routes the user to its owning record.                                      | Core Platform (included)          |

### 1.2 Pipeline

*Prototype screen: Pipeline.*

| **Object** | **Feature**                   | **Function**                                                                                                                             | **Implementation Classification** |
|------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Enquiry    | View Enquiry pipeline board   | Displays active Enquiries by configured admissions status / Journey context and excludes closed or dormant records from the live board.  | WBS Phase 2                       |
| Enquiry    | Filter Enquiry pipeline       | Filters the board by authorised Centre, owner, status, date and other supported list dimensions without changing the underlying Enquiry. | WBS Phase 2                       |
| Lead       | Open linked Lead              | Opens the associated Lead identity from a pipeline card while keeping Lead data separate from the Enquiry admissions context.            | Core Platform (included)          |
| Journey    | View Enquiry Journey progress | Displays the current Enquiry-specific Journey State and completion information; a pipeline column is not a Journey template definition.  | WBS Phase 2                       |

## 2. Lead and Contact Management

### 2.1 Lead Master

*Prototype screen: Leads*

| **Object** | **Feature**              | **Function**                                                                                                                                                                                             | **Implementation Classification** |
|------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Lead       | List Leads               | Shows reusable prospective-child identity records.                                                                                                                                                       | Core Platform (included)          |
| Lead       | Search Leads             | Searches Lead records by approved Lead display data within authorised scope.                                                                                                                             | Core Platform (included)          |
| Lead       | Duplicate check Lead     | Applies the configured Lead identity-matching rules. A confirmed duplicate reuses the master Lead and creates a Reference Log; an ambiguous match is routed for review; no automatic merge is performed. | WBS Phase 1                       |
| Lead       | Create Lead              | Captures a prospective-child Lead from a supported staff, web, event or import channel; identity matching rules remain TBD.                                                                              | Core Platform (included)          |
| Lead       | Open Lead detail         | Opens the Lead profile and its related Enquiry, Family and Contact context without making the Lead an Enquiry.                                                                                           | Core Platform (included)          |
| Lead       | Bulk reassign Lead owner | Authorised users change the owner of selected Leads within their permitted scope.                                                                                                                        | WBS Phase 2                       |
| Lead       | Inactivate Lead          | Previews all linked Enquiries; inactive the Lead and affected Enquiries in one atomic transaction; retains the status snapshot and history; and does not delete records.                                 | WBS Phase 1                       |
| Lead       | Filter Leads by status   | Supports New, Inprogress, Converted, Closed Lead and Inactive according to the approved status-transition rules; Inactive Leads remain searchable.                                                       | Core Platform (included)          |
| Lead       | Import Leads from Excel  | Validates each row, applies duplicate checks, and creates either a new Lead or a Reference Log for a confirmed duplicate; ambiguous cases are routed for review.                                         | WBS Phase 2                       |
| Lead       | View Inactive Lead       | Opens a Inactive Lead in read-only mode and excludes it from active Pipeline metrics.                                                                                                                    | Core Platform (included)          |

### 2.2 Lead Detail

*Prototype screen: Lead Detail*

| **Object** | **Feature**                          | **Function**                                                                                                                      | **Implementation Classification** |
|------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Lead       | View Lead profile                    | Shows prospective-child identity information at Lead scope without combining it with Enquiry preferences or history.              | Core Platform (included)          |
| Lead       | Edit Lead profile                    | Updates approved Lead identity fields without overwriting Enquiry preferences, Journey execution or Visit history.                | Core Platform (included)          |
| Lead       | View Lead related Enquiries          | Shows every Enquiry linked to this Lead by Brand and Centre.                                                                      | Core Platform (included)          |
| Enquiry    | Open Lead linked Enquiry             | Opens the selected Enquiry detail without moving its admissions history onto the Lead.                                            | Core Platform (included)          |
| Family     | View Lead Family relationships       | Shows relationships at Lead scope, not on the Enquiry.                                                                            | Core Platform (included)          |
| Family     | Edit Lead Family relationships       | Updates relationships at Lead scope without creating Family relationship roles on the Enquiry.                                    | Core Platform (included)          |
| Contact    | View Lead linked Contacts            | Displays linked reusable Contacts and their Lead relationship roles. Contact master edits are made in the Contact context.        | Core Platform (included)          |
| Activity   | View Lead aggregate Activity history | Shows a Lead-level timeline of linked Enquiry Activities for navigation and audit; each Activity retains its owning Enquiry.      | WBS Phase 1                       |
| Child      | Open converted Child                 | When a Child exists, opens the linked Child profile without replacing the original Lead identity.                                 | Core Platform (included)          |
| Lead       | Manage Centre Sharing                | Allows an authorised user to add or remove a Centre within the permitted data scope.                                              | WBS Phase 1                       |
| Lead       | View Reference Log                   | Displays the immutable intake or referral history, related Centre, and original true source without changing Enquiry attribution. | Core Platform (included)          |
| Lead       | Open Inactive Lead confirmation      | Displays linked Enquiries with ID, name, status and Centre, and provides two actions: Cancel or Close Lead and Enquiries.         | WBS Phase 1                       |
| Lead       | View Closed Lead audit history       | Displays the saved pre-closure state, closure action, and history in read-only mode.                                              | Core Platform (included)          |

### 2.3 Reference Log and Centre Sharing

*Prototype screen: Lead Detail / Reference Log / Centre Sharing.*

| **Object**     | **Feature**                                  | **Function**                                                                                                                                      | **Implementation Classification** |
|----------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Reference Log  | Create Reference Log for confirmed duplicate | When an intake is confirmed as a duplicate of an existing Lead, adds a Reference Log to the master Lead instead of creating another Lead.         | Core Platform (included)          |
| Centre Sharing | Automatically add Centre from Reference Log  | The system adds the originating Centre when it is not already shared; this action does not create an Enquiry.                                     | WBS Phase 1                       |
| Centre Sharing | Manually add shared Centre                   | An authorised user selects a Centre and grants Centre-level Lead access subject to role and object permissions.                                   | WBS Phase 1                       |
| Centre Sharing | Remove shared Centre                         | An authorised user may remove a shared Centre, including one added automatically, subject to approved permissions and linked-Enquiry constraints. | WBS Phase 1                       |
| Lead           | Check Centre access before Enquiry creation  | The Lead must be shared with the target Centre before an Enquiry for that Centre is created.                                                      | WBS Phase 1                       |

### 2.4 Contact and Family Relationships

*Prototype screen: Contacts / Contact Detail.*

| **Object** | **Feature**                     | **Function**                                                                                                                                | **Implementation Classification** |
|------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Contact    | List Contacts                   | Shows reusable person-master records within authorised scope.                                                                               | Core Platform (included)          |
| Contact    | Search Contacts                 | Searches Contacts by authorised name, phone, email or Contact ID.                                                                           | Core Platform (included)          |
| Contact    | Duplicate check Contact         | Checks the Contact master using exact Full name + Phone + Email before creating a new person record.                                        | Core Platform (included)          |
| Contact    | Merge the accounts              | Use NRIC / FIN / MyKad / Passport number as the identifier. If a duplicate identity is found, merge the accounts.                           | Core Platform (included)          |
| Contact    | Reuse Contact                   | Links an existing Contact to the required Lead or Child relationship instead of creating a second person master.                            | Core Platform (included)          |
| Contact    | Create Contact                  | Creates a new person master only where an existing Contact cannot be reused for the required relationship.                                  | Core Platform (included)          |
| Contact    | Edit Contact master             | Edits common person data once and propagates it to every linked Lead, Enquiry and Child context.                                            | Core Platform (included)          |
| Contact    | View Contact relationship usage | Shows relationships to Leads and Children while preserving that responsibility roles belong to the Lead or Child, not to the Contact alone. | Core Platform (included)          |
| Family     | Open Lead Family relationship   | Routes a user to the Lead relationship for Primary, Billing, Emergency or Authorised pickup role maintenance.                               | Core Platform (included)          |
| Family     | Open Child Family relationship  | Routes a user to the Child relationship for Primary, Billing, Emergency or Authorised pickup role maintenance.                              | Core Platform (included)          |

## 3. Enquiry and Customer Journey

### 3.1 Enquiry List

*Prototype screen: Enquiries.*

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 24%" />
<col style="width: 47%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Object</strong></th>
<th><strong>Feature</strong></th>
<th><strong>Function</strong></th>
<th><strong>Implementation Classification</strong></th>
</tr>
<tr class="odd">
<th>Enquiry</th>
<th>List Enquiries</th>
<th>Shows one row per admissions context with Lead, Brand, Centre, Level, preferred Start date, Session, owner and status context.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="header">
<th>Enquiry</th>
<th>Search Enquiries</th>
<th>Searches Enquiries within authorised Country, Brand and Centre scope without returning out-of-scope records.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="odd">
<th>Enquiry</th>
<th>Filter Enquiries</th>
<th>Applies supported Country, Brand, Centre, owner, status and date filters without changing Enquiry records.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="header">
<th>Lead</th>
<th>Select Lead for Enquiry</th>
<th>Selects the reusable prospective-child Lead identity for the new admissions context; it does not create a second Lead.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="odd">
<th>Enquiry</th>
<th>Duplicate check Enquiry</th>
<th><p>First compares Lead + Brand + Centre to determine whether the admissions context already exists.</p>
<p>For the same Lead + Brand + Centre, compares Level + Start date + Session to distinguish a new context, an active duplicate and a closed full match.</p></th>
<th>WBS Phase 1</th>
</tr>
<tr class="header">
<th>Enquiry</th>
<th>Create Enquiry</th>
<th>Creates a new admissions context only when the Enquiry comparison permits it; Lead identity matching follows its own rule.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="odd">
<th>Enquiry</th>
<th>Export Enquiry list</th>
<th>Exports the authorised, filtered Enquiry dataset and retains the current filter context.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="header">
<th>Lead</th>
<th>Open Lead master</th>
<th>Opens the shared prospective-child Lead record linked to the selected Enquiry without merging the two objects.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="odd">
<th>Enquiry</th>
<th>Use quick filters</th>
<th>Supports All, My, Created this week, Need attention, Visit booked, Renewal and Waitlisted filters within the authorised scope.</th>
<th>Core Platform (included)</th>
</tr>
<tr class="header">
<th>Enquiry</th>
<th>Select multiple Enquiries for Renewal</th>
<th>Supports selecting multiple eligible Enquiries and confirming before the permitted Renewal action is performed.</th>
<th>WBS Phase 2</th>
</tr>
<tr class="odd">
<th>Enquiry</th>
<th>Save optional admissions preferences</th>
<th>Stores Level, Session and preferred Start date separately from Lead identity fields.</th>
<th>Core Platform (included)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 3.2 Enquiry Detail

*Prototype screen: Enquiry Detail*

| **Object**   | **Feature**                      | **Function**                                                                                                                                             | **Implementation Classification** |
|--------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Enquiry      | View Enquiry admissions header   | Shows the owning Lead, Brand, Centre, Level, preferred Start date, Session, owner and operational status for this admissions context.                    | WBS Phase 1                       |
| Enquiry      | Assign Enquiry owner             | Allows an authorised user to assign the Enquiry owner within the permitted scope.                                                                        | Core Platform (included)          |
| Enquiry      | Update Enquiry status            | Changes the operational Enquiry status without rewriting the saved Journey definition.                                                                   | WBS Phase 1                       |
| Enquiry      | View Enquiry intake source       | Shows the immutable true-source / Reference Log snapshot without making it an editable attribution field.                                                | WBS Phase 1                       |
| Enquiry      | Set Enquiry self-reported source | Maintains the editable self-reported source independently of the immutable intake snapshot.                                                              | Core Platform (included)          |
| Enquiry      | Set Enquiry campaign attribution | Maintains the Enquiry campaign or event attribution independently of the immutable intake snapshot.                                                      | Core Platform (included)          |
| Enquiry      | Capture Enquiry Promotion code   | Stores a supplied Promotion code on the Enquiry as a separate attribution value.                                                                         | WBS Phase 1                       |
| Enquiry      | View Enquiry duplicate result    | Shows the Enquiry duplicate outcome: different scope, active full duplicate, or closed full match renewed. Lead identity matching is handled separately. | WBS Phase 1                       |
| Journey      | View Enquiry Journey runtime     | Displays the Journey version, current State and history assigned to this Enquiry; a different Enquiry has its own runtime.                               | WBS Phase 2                       |
| Journey Task | View Enquiry Journey Tasks       | Add manual task, Change Journey / Apply latest version on an enquiry, Task SLA: due-after, reminder before due, escalate after overdue to role           | WBS Phase 2                       |
| Call         | Log Enquiry Call                 | Records a Call and its notes against the Enquiry with performer and timestamp.                                                                           | Core Platform (included)          |
| Activity     | View Enquiry Activity history    | Shows messages, Calls, Visits and system actions as separate Enquiry Activity entries with audit context.                                                | WBS Phase 1                       |
| Visit        | View Enquiry linked Visits       | Shows appointments belonging to this Enquiry.                                                                                                            | WBS Phase 1                       |
| Visit        | Open Enquiry linked Visit        | Opens the selected Visit for booking, outcome, cancellation or history.                                                                                  | WBS Phase 1                       |
| Contact      | View Enquiry contacting parent   | Shows contacting-parent details for the Enquiry but does not assign Family relationship or responsibility roles there.                                   | WBS Phase 1                       |
| Enquiry      | View Enquiry score               | Displays the read-only Enquiry score separately from Journey progress score or Lead score.                                                               | WBS Phase 2                       |
| Enquiry      | View linked family Visit         | Displays Visits linked to the Enquiry, including a family Visit shared with other Enquiries at the same Centre.                                          | WBS Phase 1                       |

### 3.3 Journey Setup

*Prototype screen: Journey Settings.*

| **Object**       | **Feature**                                 | **Function**                                                                                                                                            | **Implementation Classification** |
|------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Journey Template | List Journey Templates                      | Shows scoped, versioned Journey Templates available to the authorised user.                                                                             | Core Platform (included)          |
| Journey Template | Create Journey Template                     | Creates a scoped Journey Template without changing existing Enquiry runs.                                                                               | Core Platform (included)          |
| Journey Stage    | Configure Journey Stage                     | Maintains ordered States, phase, base score and non-overlapping tier ranges for one Journey Template.                                                   | Core Platform (included)          |
| Journey Activity | Create Journey Activity                     | Adds a Task or sub-task definition with sequence, manual / automatic type, owner, progress points and score points.                                     | Core Platform (included)          |
| Journey Activity | Edit Journey Activity                       | Updates an existing Task or sub-task definition without silently changing saved Enquiry runs.                                                           | Core Platform (included)          |
| Journey Activity | Configure Journey Activity completion event | Associates automatic Task completion with an approved record-state or event key; Calls, Meetings and Applications remain outside the Journey hierarchy. | Core Platform (included)          |
| Journey Template | Preview Journey Template                    | Shows the configured Stage and Activity structure without changing any Enquiry-specific runtime.                                                        | WBS Phase 1                       |
| Journey Scoring  | View Journey scoring tiers                  | Displays the configured tier ranges and Journey progress score.                                                                                         | Core Platform (included)          |
| Lead             | View Lead score                             | Displays Lead score separately from Journey progress. Score is not awarded twice for repeated automatic-event processing.                               | Not identified in the WBS         |

### 3.4 Enquiry Renewal

*Prototype screen: Enquiry Renewal / Run History.*

| **Object**          | **Feature**                             | **Function**                                                                                                           | **Implementation Classification** |
|---------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Enquiry             | Configure Enquiry renewal eligibility   | Defines the eligible Enquiry statuses, inactivity / last-contact timing and assignment context for renewal processing. | WBS Phase 2                       |
| Enquiry             | Preview eligible Enquiries              | Shows Enquiries matching the configured rule before a scheduled or manual renewal run is performed.                    | WBS Phase 2                       |
| Enquiry             | Run Enquiry renewal                     | For a closed full match, reopens the same Enquiry rather than creating a new one.                                      | WBS Phase 2                       |
| Journey             | Apply latest Journey to renewed Enquiry | Uses the latest applicable Journey version for the renewed Enquiry and preserves previous Journey-run history.         | WBS Phase 2                       |
| Enquiry Renewal Run | View Enquiry renewal run history        | Shows the run trigger, performer, eligible / renewed / skipped counts and resulting audit evidence.                    | WBS Phase 2                       |

## 4. Visits and Events

### 4.1 Visit Calendar

*Prototype screen: Visit Calendar.*

| **Object** | **Feature**                      | **Function**                                                                                                                                                                | **Implementation Classification** |
|------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Visit      | View Visit calendar              | Displays booked Visits and their date/time, centre, host and status in the calendar context.                                                                                | WBS Phase 1                       |
| Visit      | View Visit calendar: Side panels | Side panels: Not confirmed / Needs reschedule / Waiting to book                                                                                                             | WBS Phase 2                       |
| Visit Slot | View available Visit Slots       | Displays generated Slots as availability only when they are active, valid, non-excluded and have capacity.                                                                  | WBS Phase 1                       |
| Visit      | Filter Visit calendar            | Filters calendar entries by authorised Centre, date, Visit type and other supported dimensions without changing booking data.                                               | WBS Phase 1                       |
| Open Day   | View Open Day occurrence         | Displays an Open Day as an event and opens attendee management without treating it as one shared Visit outcome.                                                             | WBS Phase 1                       |
| Trial      | View Trial sessions              | Displays Trial session calendar items separately from standard Visits and keeps their Trial linkage.                                                                        | WBS Phase 2                       |
| Visit      | Select family Visit context      | When booking from Calendar, the parent selector shows the number of linked Leads and Enquiries; multiple Enquiries at the same Centre may be selected for one family Visit. | WBS Phase 1                       |

### 4.2 Book and Edit Visit

*Prototype screen: Visit Booking / Edit Visit.*

| **Object** | **Feature**                    | **Function**                                                                                                                                                                              | **Implementation Classification** |
|------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Visit Slot | Select standard Visit Slot     | Lists selectable generated Slots for a standard Visit; booked, excluded, invalid or unavailable occurrences cannot be selected.                                                           | WBS Phase 1                       |
| Visit      | Create standard Visit          | Creates a Visit from an available Slot, linked to one Enquiry or to multiple Enquiries at the same Centre for an approved family Visit; displays it in Calendar and each Enquiry history. | WBS Phase 1                       |
| Visit      | Create ad-hoc Visit            | Allows a non-parent user with Book Visit permission to create an appointment outside a generated Slot. Parents cannot use this action.                                                    | WBS Phase 1                       |
| Visit      | Set Visit hosts                | Initialises hosts from the selected Slot and permits the booking user to change or add hosts.                                                                                             | WBS Phase 1                       |
| Visit      | Edit Visit booking details     | Allows authorised update to the selected Visit date, time, centre, host and notes subject to the available validation rules.                                                              | WBS Phase 1                       |
| Enquiry    | Resolve Visit linked Enquiries | From Enquiry Detail, the parent and Enquiry are locked. From Calendar, multiple Enquiries may be linked only when all belong to the same Centre.                                          | WBS Phase 1                       |
| Visit      | Book Visit                     | Completes the booking by selecting the appointment context, eligible family or Enquiries, time, and host.                                                                                 | WBS Phase 1                       |

### 4.3 Visit Detail and Outcome

*Prototype screen: Visit Detail.*

| **Object** | **Feature**             | **Function**                                                                                                               | **Implementation Classification** |
|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Visit      | View Visit detail       | Displays date and time, Centre, linked Enquiries, host, Slot, notes, status, and audit history for the Visit.              | WBS Phase 1                       |
| Visit      | Record Visit attendance | Records Held, No-show, Cancelled or other approved attendance state for this Visit only.                                   | WBS Phase 1                       |
| Visit      | Mark parent confirmed   | Records that the parent has confirmed the Visit appointment.                                                               | WBS Phase 1                       |
| Visit      | Cancel individual Visit | Cancels one booked Visit without scheduled-Slot deletion approval and records the chosen cancellation or rebooking result. | WBS Phase 1                       |
| Visit      | Rebook Visit            | Creates a replacement Visit while retaining the original occurrence and its cancellation / no-show history.                | WBS Phase 1                       |

### 4.4 Visit Slot Schedule

*Prototype screen: Visit Slot Settings.*

| **Object**          | **Feature**                         | **Function**                                                                                                                               | **Implementation Classification** |
|---------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Visit Slot Schedule | List Visit Slot Schedules           | Lists recurring schedule configurations with Centre, Visit type, weekday / times, host(s), effective period and Active / Inactive status.  | WBS Phase 1                       |
| Visit Slot Schedule | Create Visit Slot Schedule          | Creates a recurring availability configuration with Visit type, times, hosts, effective dates and exclusion settings.                      | WBS Phase 1                       |
| Visit Slot Schedule | View Slots from Visit Slot Schedule | Opens the list of Slots generated by the selected configuration when the user selects the row or View slots.                               | WBS Phase 1                       |
| Visit Slot Schedule | Edit Visit Slot Schedule            | Updates an authorised configuration directly; schedule configuration does not use an approval lifecycle.                                   | WBS Phase 1                       |
| Visit Slot Schedule | Activate Visit Slot Schedule        | Sets the configuration to Active so valid future Slots may be offered.                                                                     | WBS Phase 1                       |
| Visit Slot Schedule | Inactivate Visit Slot Schedule      | Sets the configuration to Inactive so it creates no new available Slots.                                                                   | WBS Phase 1                       |
| Visit Slot Schedule | Delete Visit Slot Schedule          | Deletes the schedule configuration directly. This action is not the same as deleting one generated Slot and has no configuration approval. | WBS Phase 1                       |

### 4.5 Generated Slots and Deletion Approval

*Prototype screen: Schedule Slots / Generated Slots.*

| **Object** | **Feature**                                | **Function**                                                                                                                                                                | **Implementation Classification** |
|------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Visit Slot | List generated Visit Slots                 | Shows future Slots created by the selected schedule with date/time, Visit type, hosts, Slot status and booking / deletion-request context.                                  | WBS Phase 1                       |
| Visit Slot | Open booked Visit from Slot                | Opens the Visit linked to a booked Slot without changing the Slot or booking state.                                                                                         | WBS Phase 1                       |
| Visit Slot | Request Visit Slot deletion                | Requests deletion of one individual generated Slot. The Malaysia workflow currently requires configurable approval and stops new bookings while pending.                    | WBS Phase 1                       |
| Visit Slot | Approve Visit Slot deletion                | Allows only the configured approver to approve a pending Slot deletion. When deletion takes effect, a booked Visit is cancelled as Centre cancelled and remains in history. | WBS Phase 1                       |
| Visit Slot | Reject Visit Slot deletion                 | Allows the configured approver to reject a pending deletion request, retaining the Slot when it remains valid.                                                              | WBS Phase 1                       |
| Visit Slot | Restore Visit Slot after withdrawn request | Restores booking availability when a deletion request is withdrawn and the Slot remains valid.                                                                              | WBS Phase 1                       |

### 4.7 Open House and Open Day

*Prototype screen: Open Day.*

| **Object**          | **Feature**                         | **Function**                                                                                                                                              | **Implementation Classification** |
|---------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Open Day            | Create Open House or Open Day event | Creates an event with a date and either Centre scope or an approved Brand-wide option across eligible Centres; each attendee outcome remains independent. | WBS Phase 1                       |
| Lead                | Select Open Day Lead attendees      | Searches and selects eligible Lead attendees. Each attendee keeps the associated Lead identity and context.                                               | WBS Phase 1                       |
| Open Day Attendance | Record Open Day attendee attendance | Records Held, No-show or other outcome independently for each attendee; one outcome does not update another attendee.                                     | WBS Phase 1                       |
| Enquiry             | Open Open Day attendee Enquiry      | Routes a selected attendee to the relevant Enquiry for follow-up without assigning Family roles to the event attendance.                                  | WBS Phase 1                       |

### 4.8 Trial Management

*Prototype screen: Trial.*

| **Object** | **Feature**                     | **Function**                                                                                                          | **Implementation Classification** |
|------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Trial      | List Trial batches              | Lists Trial records and their Enquiry, Child / admissions context, session dates and current state.                   | WBS Phase 2                       |
| Trial      | Arrange Trial sessions          | Creates separate linked session records for selected days and groups them as one Trial batch.                         | WBS Phase 2                       |
| Trial      | Record Trial session attendance | Records each session outcome independently; mixed-session aggregate-state behaviour remains TBD until approved.       | WBS Phase 2                       |
| Trial      | Apply Trial country eligibility | Exposes pre-enrolment Trial for Malaysia and Vietnam according to configuration and does not expose it for Singapore. | WBS Phase 2                       |
| Trial      | View Trial payment context      | Shows any linked Trial product / payment evidence without treating payment as Registration creation or Enrolment.     | WBS Phase 2                       |

## 5. Waitlist Registration and Child Record Preparation

### 5.1 Waitlist and Offer

*Prototype screen: Waitlist and Offers.*

| **Object**   | **Feature**                                                  | **Function**                                                                                                                                                                                        | **Implementation Classification** |
|--------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Waitlist     | List Waitlist queue                                          | Shows Waiting records by Centre, Level, preferred start, entry time, fee context and queue status.                                                                                                  | WBS Phase 2                       |
| Waitlist     | Review Waitlist availability                                 | Displays capacity, enrolled / waiting totals and places left where supplied before an Offer is made.                                                                                                | WBS Phase 3                       |
| Waitlist     | View Waitlist fee information                                | Allows users to view related fee information.                                                                                                                                                       | WBS Phase 2                       |
| Offer        | Create Offer                                                 | Creates an Offer for an eligible Waitlist record and stores the creator-entered valid-until date.                                                                                                   | WBS Phase 3                       |
| Offer        | Accept Offer                                                 | Records an Accepted response and opens the Registration path without enrolling the child.                                                                                                           | WBS Phase 3                       |
| Offer        | Decline Offer                                                | Records a Declined response and moves the linked Waitlist entry to the end of the queue.                                                                                                            | WBS Phase 3                       |
| Offer        | Expire Offer                                                 | Records an Expired outcome and moves the linked Waitlist entry to the end of the queue.                                                                                                             | WBS Phase 3                       |
| Registration | Start Registration (from converted enquiry / accepted offer) | Registration started' when an enquiry converts to Enrollment or an offer is accepted (child record created if needed, status Registration); draft can be saved and resumed later ('Draft – saved'). | WBS Phase 1                       |

### 5.2 Registration and Enrolment List

*Prototype screen: Registration and Enrolment.*

| **Object**   | **Feature**                            | **Function**                                                                                                             | **Implementation Classification** |
|--------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Registration | List Registrations in progress         | Shows active Registration records, readiness state, Child, Centre, Level and remaining operational context.              | Core Platform (included)          |
| Registration | List completed Registration enrolments | Shows records whose explicit CRM Enrolment submission has completed; payment alone does not place a record in this list. | WBS Phase 2                       |
| Enquiry      | List conversion-ready Enquiries        | Shows authorised Enquiries ready to start Registration without treating every Visit, Trial or payment as a prerequisite. | WBS Phase 2                       |
| Registration | Open Registration detail               | Opens the selected Registration workspace and preserves its independent readiness areas.                                 | WBS Phase 1                       |
| Child        | Open Child detail                      | Opens the Child record linked to the Registration without converting the Child profile into an Enquiry.                  | Core Platform (included)          |

### 5.3 Registration Detail

*Prototype screen: Registration Detail.*

| **Object**       | **Feature**                             | **Function**                                                                                                                      | **Implementation Classification** |
|------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Registration     | View Registration summary               | Shows Registration ID, Child, Centre, Level, intended start date, status, source Enquiry where present and operational readiness. | WBS Phase 1                       |
| Registration     | Save Registration                       | Saves partial Registration information and its incomplete-work state.                                                             | WBS Phase 1                       |
| Child            | Maintain Child profile                  | Maintains Child profile information required for Registration separately from the original Lead identity and Enquiry preferences. | Core Platform (included)          |
| Family           | Maintain Child Family relationships     | Maintains Family relationships at Child scope without creating relationship roles on the Enquiry.                                 | Core Platform (included)          |
| Contact          | Add Child Contact                       | Adds or reuses a Contact for the Child relationship without creating a second person master when a matching Contact exists.       | Core Platform (included)          |
| Registration     | Maintain Registration payment reference | Records registration / deposit evidence without completing Registration or Enrolment solely because payment exists.               | WBS Phase 1                       |
| Class Assignment | Assign Registration Class               | Requires authorised capacity and a start date and prevents full-class assignment.                                                 | WBS Phase 1                       |
| Class Assignment | Change Registration Class               | Permits authorised Class changes for all children during Registration, subject to capacity and start-date checks.                 | WBS Phase 1                       |
| Registration     | Submit Registration                     | Executes the Registration submission action.                                                                                      | WBS Phase 1                       |

### 5.4 Documents and Consents

*Prototype screen: Documents and Consents.*

| **Object**   | **Feature**                          | **Function**                                                                                                             | **Implementation Classification** |
|--------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Document     | List Documents                       | Shows authorised Child / Registration document entries with category, status, expiry and owning context.                 | Core Platform (included)          |
| Document     | Search Documents                     | Searches authorised Document entries by supported fields within their owning Child or Registration context.              | Core Platform (included)          |
| Document     | Upload Document                      | Adds a Document file reference, category, status and expiry without silently changing Registration submission readiness. | Core Platform (included)          |
| Document     | Update Document                      | Edits a Document entry within its authorised Child or Registration context.                                              | Core Platform (included)          |
| Consent      | List Consent requirements            | Shows Consent type and collection state separately from Document and Health objects.                                     | WBS Phase 1                       |
| Consent      | Record Consent collection            | When a Consent becomes Collected, records the collecting user and collection date.                                       | WBS Phase 1                       |
| Registration | Show Registration Document readiness | Displays Documents as an independent Registration area.                                                                  | WBS Phase 1                       |
| Registration | Show Registration Consent readiness  | Displays Consents as an independent Registration area.                                                                   | WBS Phase 1                       |

### 5.5 Allergies and Health

*Prototype screen: Allergies and Health.*

| **Object**   | **Feature**                        | **Function**                                                                                                  | **Implementation Classification** |
|--------------|------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Health       | List Child Health information      | Shows authorised health notes and clinical / care information for the selected Child or Registration context. | Core Platform (included)          |
| Allergy      | Create Child Allergy record        | Creates allergy information separately from general Child Health notes.                                       | Core Platform (included)          |
| Allergy      | Update Child Allergy record        | Updates an existing allergy record separately from general Child Health notes.                                | Core Platform (included)          |
| Health       | Maintain Child Health notes        | Records health notes with appropriate sensitive-data access scope and audit context.                          | Core Platform (included)          |
| Registration | Show Registration Health readiness | Shows Health as an independent readiness area; completion definition and submission effect remain TBD.        | WBS Phase 1                       |

### 5.6 Child and Family Links

*Prototype screen: Children / Child Detail*

| **Object** | **Feature**                     | **Function**                                                                                                                                              | **Implementation Classification** |
|------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Child      | List Children                   | Lists Child profiles created from Enrolment conversion or independently, with centre, status, parent / guardian and source-Enquiry context where present. | Core Platform (included)          |
| Child      | View Child detail               | Shows Child identity, class, Registration / Enrolment state and source admissions context without changing the Lead record.                               | Core Platform (included)          |
| Child      | Create independent Child        | Allows Child creation without a linked Lead and maintains Family and Contacts at Child scope in that case.                                                | Core Platform (included)          |
| Family     | View Child Family relationships | Shows Family relationships shared with a linked Lead while keeping relationship roles at Child scope.                                                     | Core Platform (included)          |
| Contact    | Set Child Primary Contact       | Sets the Child-specific Primary Contact without changing the linked Lead Primary Contact.                                                                 | Core Platform (included)          |

## 6. Marketing Dashboard and Reports

### 6.1 Campaigns

*Prototype screen: Campaigns.*

| **Object** | **Feature**                     | **Function**                                                                                                                                                                          | **Implementation Classification** |
|------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Campaign   | List Campaigns                  | Shows Campaign records within authorised marketing scope.                                                                                                                             | Core Platform (included)          |
| Campaign   | Search Campaigns                | Searches Campaign records by supported attributes within authorised marketing scope.                                                                                                  | Core Platform (included)          |
| Campaign   | Create Campaign                 | Creates approved Campaign context, planning and related-record fields where the release scope supports them.                                                                          | Core Platform (included)          |
| Campaign   | Edit Campaign                   | Updates approved Campaign context without changing linked Lead identity or Enquiry attribution.                                                                                       | Core Platform (included)          |
| Campaign   | View Campaign related records   | Shows supported related Lead, Contact and Child records while keeping the Campaign separate from their source identities.                                                             | Core Platform (included)          |
| Lead       | View Lead immutable true source | Displays the Lead true-source and Reference Log snapshot without allowing Campaign or event attribution to overwrite it.                                                              | WBS Phase 1                       |
| Enquiry    | View Enquiry Promotion code     | Shows supplied Promotion code in its Enquiry attribution context; Campaign updates do not overwrite it.                                                                               | WBS Phase 1                       |
| Enquiry    | Capture attribution from API    | Phase 1 may store source, channel, campaign, UTM Source, and advertising or page identifiers supplied by the intake API; this does not imply direct advertising-platform integration. | WBS Phase 2                       |

### 6.2 Dashboard

*Prototype screen: Dashboard.*

| **Object**   | **Feature**                              | **Function**                                                                                                          | **Implementation Classification** |
|--------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Dashboard    | Choose CRM department dashboard          | Opens the authorised department workspace and does not present an undefined data source as a populated KPI dashboard. | WBS Phase 2                       |
| Dashboard    | View Marketing and Admissions EVESW KPIs | Shows primary cards for Enquiries, Visits, Enrolments, Starts and Withdrawn using the defined supporting dataset.     | WBS Phase 2                       |
| Dashboard    | Filter CRM dashboard                     | Applies report-defined filters to the selected dashboard without changing CRM source records.                         | WBS Phase 2                       |
| Enquiry      | Open Enquiry from dashboard              | Routes an authorised Enquiry KPI or detail row to the supporting Enquiry where drill-through is configured.           | WBS Phase 2                       |
| Visit        | Open Visit from dashboard                | Routes an authorised Visit KPI or detail row to the supporting Visit where drill-through is configured.               | WBS Phase 2                       |
| Registration | Open Enrolment from dashboard            | Routes an authorised Enrolment KPI or detail row to the supporting Registration where drill-through is configured.    | WBS Phase 2                       |

###  

## 7. Notifications and Follow-up Alerts

### 7.1 Notification Centre

*Prototype screen: Notifications.* Direct URL: TBD (not available in the source SRS). [<u>Open shared prototype workspace</u>](https://bba-sms-crm.lovable.app/)

| **Object**   | **Feature**                       | **Function**                                                                                                                       | **Implementation Classification** |
|--------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Notification | List CRM Notifications            | Lists assignment, due, Visit, Slot-deletion approval, Offer, Registration and Consent notifications available to the current user. | Core Platform (included)          |
| Notification | Open Notification owning record   | Routes the user to the Enquiry, Task, Visit, Slot request, Offer, Registration or Consent that generated the alert.                | Core Platform (included)          |
| Notification | Mark Notification read            | Maintains the Notification read state without changing the business status of the linked CRM object.                               | Core Platform (included)          |
| Notification | Filter notifications              | Filters by status or unread state while preserving navigation to the source record.                                                | Core Platform (included)          |
| Notification | Display unread notification count | Displays the number of unread items and opens the Notification detail screen.                                                      | Core Platform (included)          |

# 5. Business Rules

## Lead Object Rules

| **ID**     | **Business Rule**                                                                                                                                                                                                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BR-CRM-001 | A Lead is a reusable prospective-child identity record. It is distinct from an Enquiry and may be linked to multiple Enquiries.                                                                                                                                                                                      |
| BR-CRM-002 | When a Lead duplicate is identified under the approved rules, CRM creates a Reference Log instead of a duplicate Lead and does not merge Leads automatically.                                                                                                                                                        |
| BR-CRM-003 | Lead-level Family relationships and Contact responsibility roles belong to the Lead, not to an Enquiry. A Lead may display related Enquiries without copying their operational history.                                                                                                                              |
| BR-CRM-004 | True source and the Reference Log are retained as an immutable intake audit snapshot viewable from the Lead or linked Enquiry. Editing Enquiry attribution must not overwrite this snapshot.                                                                                                                         |
| BR-CRM-005 | In Phase 1, a duplicate Lead is handled by reusing the master Lead during intake or by an authorised user manually inactivating a duplicate identified later. Automatic merge or redirect is deferred to a later phase and must preserve history.                                                                    |
| BR-CRM-006 | When a new Reference Log identifies an originating Centre that is not already shared, the system automatically adds that Centre to the Lead Centre Sharing list. This Centre Sharing backlog item does not create an Enquiry.                                                                                        |
| BR-CRM-007 | An authorised user may add or remove a shared Centre, including one added automatically, subject to approved permission and linked-data constraints.                                                                                                                                                                 |
| BR-CRM-008 | The Lead lifecycle statuses are New, Inprogress, Converted, Dead Lead and Closed. Inprogress is associated with the first Call; Converted requires at least one converted Enquiry; Dead Lead is selected by a user; and Closed results from the Inactive Lead function. Status changes remain permission-controlled. |
| BR-CRM-009 | Inactive Lead closes the Lead and linked Enquiries atomically. An Enquiry already Closed remains Closed and receives no new status-change history. The confirmation preview lists the ID, name, status and Centre of affected Enquiries.                                                                             |
| BR-CRM-010 | A Closed Lead remains searchable but read-only. Users cannot create a new Enquiry or Reference Log, edit the Lead, or change Family or Contact links. A Closed Lead is excluded from the active Pipeline.                                                                                                            |
| BR-CRM-011 | Excel Lead import applies the same duplicate and ambiguous-match rules as standard intake. Import errors must be reported by row and must not be silently skipped.                                                                                                                                                   |

## Enquiry and Journey Rules

| **ID**     | **Business Rule**                                                                                                                                                                                                                 |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BR-CRM-012 | An Enquiry is the Centre-specific admissions context for a Lead and belongs to only one Centre. It owns admissions preferences, owner, status, Journey and operational history; the Lead must already be shared with that Centre. |
| BR-CRM-013 | The Enquiry duplicate check first compares Lead + Brand + Centre. When that combination differs, CRM may create a separate Enquiry for the different admissions context.                                                          |
| BR-CRM-014 | For the same Lead + Brand + Centre, CRM compares Brand + Centre + Level + Start date + Session. A full match with an active Enquiry does not create another Enquiry and records a Duplicate Activity on the existing Enquiry.     |
| BR-CRM-015 | Where all Enquiry matching fields match a Closed Enquiry, CRM renews that Enquiry instead of creating another.                                                                                                                    |
| BR-CRM-016 | Renewal uses the latest applicable Journey Template version and preserves previous Journey runtime history.                                                                                                                       |
| BR-CRM-017 | An Enquiry displays the immutable intake true source and stores self-reported source, Campaign, Event and supplied Promotion code separately. Editing these values must not overwrite the intake snapshot.                        |
| BR-CRM-018 | An Enquiry stores contacting-parent information but does not own Family relationship or responsibility-role assignments.                                                                                                          |
| BR-CRM-019 | Journey Task completion triggers are configured in the Activity Template. A status change is one possible trigger, not the only trigger.                                                                                          |
| BR-CRM-020 | If an automatic Task completion condition occurred before the Task started, the Task becomes Completed and no due-date calculation or evaluation is performed.                                                                    |
| BR-CRM-021 | Changing Enquiry status does not change the saved Journey definition. Executing a configured Action may change status.                                                                                                            |
| BR-CRM-022 | Material CRM actions and changes record the actor, timestamp and relevant before-and-after context where applicable.                                                                                                              |

## Visit Scheduling Visits and Trial

| **ID**     | **Business Rule**                                                                                                                                                               |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BR-CRM-023 | A standard Visit uses a generated Slot from an Active Centre schedule unless an authorised non-parent user creates an ad-hoc Visit.                                             |
| BR-CRM-024 | Only a non-parent user with Book Visit permission may create an ad-hoc Visit. Parents may not create ad-hoc Visits.                                                             |
| BR-CRM-025 | A new Visit inherits the host configured on the Slot. The booking user may change or add hosts.                                                                                 |
| BR-CRM-026 | Public-holiday and Centre-event exclusion ranges prevent matching Slots from being offered.                                                                                     |
| BR-CRM-027 | A Visit Slot Schedule has only Active and Inactive operational statuses and has no configuration approval lifecycle.                                                            |
| BR-CRM-028 | Creating, editing, activating, inactivating or deleting a Visit Slot Schedule is saved directly and does not require approval.                                                  |
| BR-CRM-029 | Deleting an individual scheduled Slot may require a configured approval workflow. This currently applies in Malaysia, while the workflow and approver role remain configurable. |
| BR-CRM-030 | While scheduled-Slot deletion approval is pending, the Slot stops accepting new bookings.                                                                                       |
| BR-CRM-031 | When a Slot with a booked Visit is deleted and the deletion takes effect, the Visit becomes Cancelled with reason Centre cancelled and remains in Calendar history.             |
| BR-CRM-032 | Cancelling an individual booked Visit is separate from scheduled-Slot deletion and does not require deletion approval.                                                          |
| BR-CRM-033 | Open House or Open Day is configured for a Centre or, when enabled, across a Brand. Each attending Lead has an independent attendance outcome.                                  |
| BR-CRM-034 | Singapore does not expose a pre-enrolment Trial flow. Malaysia and Vietnam may use it according to the configured process.                                                      |
| BR-CRM-035 | Calendar booking may link one family Visit to multiple Enquiries only when all belong to the same Centre. Booking from Enquiry Detail locks the Parent and Enquiry.             |
| BR-CRM-036 | The separate Trial module may be used in Malaysia and Vietnam according to the approved country configuration.                                                                  |

## Considering Waitlist Offer and Registration

| **ID**     | **Business Rule**                                                                                                                                                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BR-CRM-037 | Parent is considering is a business term, not a capacity hold. It proposes next action = execution timestamp plus 48 continuous elapsed hours, which the user may edit. |
| BR-CRM-038 | Parent is considering does not reduce available places.                                                                                                                 |
| BR-CRM-039 | Initial Waitlist order is based on the time of entry into the queue. No sibling or staff-child priority is applied.                                                     |
| BR-CRM-040 | The Offer creator enters the expiry or valid-until date; no configuration-driven default is required.                                                                   |
| BR-CRM-041 | When an Offer is declined or expires, the outcome is recorded and the linked Waitlist entry moves to the end of the queue.                                              |
| BR-CRM-042 | Accepting an Offer opens Registration. The Child is enrolled only after explicit Registration and Enrolment submission.                                                 |
| BR-CRM-043 | Registration readiness areas are independent. A rule requiring all seven areas before submission has not been approved and remains TBD.                                 |
| BR-CRM-044 | Class changes are permitted for all Children during Registration, subject to authorised capacity and operational checks.                                                |
| BR-CRM-045 | Payment or fee recording alone does not complete Registration or Enrolment.                                                                                             |

## Child Family Contact Document and Consent

| **ID**     | **Business Rule**                                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| BR-CRM-046 | Relationship and responsibility roles such as Primary, Billing, Emergency and Authorised pickup exist at Lead and Child scope, not Enquiry scope.        |
| BR-CRM-047 | An Enquiry stores contacting-parent information but does not own Family relationship or responsibility roles.                                            |
| BR-CRM-048 | When an existing Contact is found, CRM reuses it and creates only the relationship. A new Contact is created only when no existing Contact is available. |
| BR-CRM-049 | Only one Primary Contact is permitted per Lead or Child. Changing the Child Primary Contact does not change the Primary Contact of the linked Lead.      |
| BR-CRM-050 | Editing the Contact master updates the same person across linked Lead, Enquiry and Child contexts.                                                       |
| BR-CRM-051 | A Child may be created independently without a linked Lead, with Family and Contacts managed at Child scope.                                             |
| BR-CRM-052 | Health notes are stored independently from allergy information.                                                                                          |
| BR-CRM-053 | Changing a Consent to Collected records the collecting user and collection date.                                                                         |

## Campaign Reporting and Configuration

| **ID**     | **Business Rule**                                                                                                                                                                                   |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BR-CRM-054 | Dashboard data can be filtered by time period, Brand, Country and Centre.                                                                                                                           |
| BR-CRM-055 | Report and dashboard data is displayed according to user permissions.                                                                                                                               |
| BR-CRM-056 | Phase 1 stores Source, Campaign, UTM and Promotion code supplied by supported forms or APIs. Direct advertising-platform synchronisation, bulk EDM and the Promotion Engine belong to later phases. |

# 6. Notifications and Documents

## 6.1 Notifications

| **Notification**                 | **Recipient**                              | **Channel**                                      | **When Triggered**                                                       |
|----------------------------------|--------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------|
| New assigned work                | Assigned CRM user or role                  | In-application                                   | A Task, Enquiry, Visit or Action is assigned or becomes due.             |
| Journey Task due                 | Task assignee                              | In-application                                   | A configured Task reaches its due state.                                 |
| Visit booking or change          | Relevant staff and family where configured | Configured channel                               | A Visit is created, moved, rebooked or cancelled.                        |
| Scheduled-Slot deletion approval | Configured approver                        | In-application                                   | A scheduled Slot enters a configured approval workflow.                  |
| Offer response                   | Offer owner                                | In-application                                   | An Offer is accepted, declined or expires.                               |
| Registration handoff             | Country-configured role                    | In-application                                   | Registration is submitted or requires review or follow-up.               |
| Consent collection               | Relevant authorised user                   | In-application or Task                           | A required Consent remains incomplete or is collected, where configured. |
| Lead import validation           | User authorised to perform the import      | In-application result or downloadable error file | A row is rejected, flagged as ambiguous, or matched to an existing Lead. |

## 6.2 Documents and Generated Data

- Registration and Child documents: retain file reference, type, status, expiry, and permitted audit information.

- Consent collection: retain the collection date, collecting user, and independent readiness state.

- Finance and payment references: CRM retains agreed links and evidence; it does not process accounting or collections and does not infer Enrolment from payment alone.

- Excel Lead import: includes template fields, validation errors, duplicate Lead or Reference Log outcomes, and row-level feedback; the detailed template mapping remains TBD.

- Exports and reports: apply the authorised Country, Brand, Centre and role scope together with the active filters.

# 7. Reports and Exports

| **Report or Export**                                  | **Content**                                                                                                                                                      | **Used By**                       |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Marketing and Admissions Dashboard                    | EVESW KPI cards: Enquiries, Visits, Enrolments, Starts and Withdrawn.                                                                                            | Marketing, Admissions, Leadership |
| EVESW Detail Report                                   | ACT, OP and OP Variance using the defined supporting dataset.                                                                                                    | Marketing, Admissions             |
| Operational Enquiry Export                            | Authorised Enquiry list and selected filter dimensions.                                                                                                          | Admissions, Centre teams          |
| Visit and Calendar Export                             | Visit schedule, occurrence, attendance and outcome data within the authorised scope.                                                                             | Admissions, Centre teams          |
| Waitlist and Offer Export                             | Queue, Offer status, expiry and supporting operational data.                                                                                                     | Admissions, Centre teams          |
| Conversion Time by Stage, pending metric confirmation | Enquiry to Visit Held to first deposit to Start, filtered by Owner, Host, Centre, Brand and creation date; the official schema and event definitions remain TBD. | Marketing and Admissions          |

# 8. Acceptance Criteria

| **ID**     | **Criterion**                              | **Acceptance Condition**                                                                                                                                                                                                                                                 |
|------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC-CRM-001 | New Enquiry by scope                       | Given a Lead already has an Enquiry for Brand A and Centre X, when a user creates an Enquiry for Brand B or Centre Y, then CRM creates a separate Enquiry rather than overwriting the original.                                                                          |
| AC-CRM-002 | Renewal                                    | Given the Lead, Brand, Centre, Level, Start date and Session match a closed Enquiry, when the user starts the same admissions request, then CRM reopens that Enquiry, keeps prior Journey history and uses the latest applicable Journey template.                       |
| AC-CRM-004 | Automatic Journey task                     | Given an automatic task is configured to complete on a defined event, when the event occurred before the task starts, then the task is Completed and no due-date calculation is run.                                                                                     |
| AC-CRM-005 | Live call notes                            | Given an authorised user starts a click-to-call interaction, when the user types notes before ending it, then the notes remain available for the saved call log.                                                                                                         |
| AC-CRM-006 | Standard Visit availability                | Given a standard Visit user opens booking, when a slot is booked, excluded or unavailable, then it cannot be selected as available.                                                                                                                                      |
| AC-CRM-008 | Schedule status                            | Given an authorised user creates or edits a Visit-slot schedule, when the user saves it as Active or Inactive, then the schedule is saved directly without an approval status or approval action.                                                                        |
| AC-CRM-009 | Scheduled-slot deletion in Malaysia        | Given a Malaysia scheduled slot has future availability, when an authorised user requests its deletion, then CRM creates the configured approval request and stops new bookings for that slot while the request is pending.                                              |
| AC-CRM-010 | Booked Visit on deleted slot               | Given a scheduled slot containing a booked Visit is deleted after any required approval, when deletion takes effect, then the Visit is Cancelled with reason Centre cancelled and remains in Calendar history.                                                           |
| AC-CRM-011 | Individual Visit cancellation              | Given a booked Visit is cancelled by an authorised user, when the user chooses an individual Visit cancellation action, then CRM records that cancellation without requiring scheduled-slot deletion approval.                                                           |
| AC-CRM-012 | Considering                                | Given a user applies Parent is considering, when the action is saved, then CRM proposes a next action date 48 continuous hours after execution and does not reduce available places.                                                                                     |
| AC-CRM-013 | Offer expiry                               | Given a Waitlist Offer expires, when its expiry is processed, then the outcome is recorded and the Waitlist entry is moved to the end of the queue.                                                                                                                      |
| AC-CRM-014 | Offer acceptance                           | Given a family accepts an Offer, when the user records Accepted, then CRM opens Registration and does not mark the child enrolled before explicit submission.                                                                                                            |
| AC-CRM-016 | Payment is not Enrolment                   | Given a payment reference is recorded, when no explicit Registration and Enrolment submission has occurred, then CRM does not show the child as enrolled solely because payment exists.                                                                                  |
| AC-CRM-017 | Contact reuse                              | Given a contacting parent already has a matching Contact, when staff adds the relationship, then CRM reuses the Contact and creates only the relationship.                                                                                                               |
| AC-CRM-018 | Primary independence                       | Given a linked Lead and Child have different authorised Primary contacts, when a user changes Primary on the Child, then the Lead Primary remains unchanged.                                                                                                             |
| AC-CRM-019 | Consent audit                              | Given a consent is changed to Collected, when it is saved, then CRM records the collecting user and collection date.                                                                                                                                                     |
| AC-CRM-022 | Authorised scope                           | Given a user is limited to a Country, Brand or Centre scope, when the user searches, filters or exports a CRM list, then records outside that scope are not returned.                                                                                                    |
| AC-CRM-024 | Active Enquiry full duplicate              | Given Lead, Brand, Centre, Level, Start date and Session all match an active Enquiry, when matching intake is processed, then CRM does not create another Enquiry and records a Duplicate Activity against the active Enquiry.                                           |
| AC-CRM-025 | Promotion code attribution                 | Given an intake provides a Promotion code and staff later changes campaign or self-reported source, when the Enquiry is saved, then the Promotion code remains a separate captured attribution value and the original true-source / Reference Log snapshot is unchanged. |
| AC-CRM-026 | Duplicate Lead intake                      | Given a confirmed duplicate Lead is identified during intake, when an authorised channel submits the data, then CRM does not create a new Lead and adds a Reference Log to the existing Lead.                                                                            |
| AC-CRM-028 | Automatic Centre Sharing                   | Given a new Reference Log originates from Centre B and the Lead is not shared with Centre B, when the Reference Log is created, then the system adds Centre B to Centre Sharing and does not create an Enquiry through this action.                                      |
| AC-CRM-029 | Centre-level visibility                    | Given a Lead is shared with Centre B, when a Centre B user with the required object permissions opens Leads, then the Lead is accessible at Centre level.                                                                                                                |
| AC-CRM-030 | Centre prerequisite for Enquiry            | Given a Lead is not shared with Centre B, when a user attempts to create an Enquiry for Centre B, then CRM blocks creation until the permitted sharing action is completed.                                                                                              |
| AC-CRM-031 | Inactive Lead confirmation                 | Given an active Lead has linked Enquiries, when the user selects Inactive, then the confirmation lists Enquiry ID, name, status and Centre and provides Cancel and Close Lead and Enquiries actions.                                                                     |
| AC-CRM-032 | Atomic inactivation                        | Given active linked Enquiries and one already Closed Enquiry, when inactivation is confirmed, then the Lead and affected active Enquiries become Closed atomically and the already Closed Enquiry remains unchanged.                                                     |
| AC-CRM-033 | Closed Lead is read-only                   | Given a Lead is Closed, when a user opens it, then the record is visible but editing, new Enquiry or Reference Log creation, and relationship changes are unavailable.                                                                                                   |
| AC-CRM-036 | Family Visit from Calendar                 | Given two eligible Enquiries belong to the same Centre, when a family Visit is booked from Calendar, then one Visit may link both Enquiries and an Enquiry from another Centre cannot be selected.                                                                       |
| AC-CRM-037 | Locked booking context from Enquiry Detail | Given a Visit is booked from Enquiry Detail, when the booking form opens, then the Parent and Enquiry are preselected and cannot be changed.                                                                                                                             |
| AC-CRM-039 | Brand-wide Open House                      | Given Brand-wide Open House is enabled, when an Open House is created, then the event may apply across the Brand in addition to a single-Centre configuration.                                                                                                           |
| AC-CRM-040 | Phase 1 attribution                        | Given a website or API supplies Campaign, UTM Source and Promotion code, when the Enquiry is saved, then CRM stores these values separately from the immutable true source without requiring direct advertising-platform integration.                                    |
| AC-CRM-041 | Excel import with duplicate Lead           | Given an Excel row matches an existing Lead, when the row is imported, then CRM creates a Reference Log instead of a duplicate Lead and records the row outcome in the import result.                                                                                    |
