Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**General Requirements**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

# 1. Purpose

This document describes the requirements that apply to every module of the Busy Bees Asia School Management System (SMS), Phase 1. Each module SRS describes only what is specific to that module and refers to this document for the common rules.

It is a baseline for discussion. The DOTB Business Analyst will update it with the details agreed during sprint planning.

## 1.1 Document set

| **Document**                            | **Covers**                                                                                                                                            |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SRS — General Requirements**          | This document: system overview, roles and access, common behaviour, non-functional requirements, glossary.                                            |
| **SRS — Children & Families**           | Children, families and guardians, health and allergies, documents, authorised pickup, classes.                                                        |
| **SRS — Communication**                 | Announcements, messages, inquiries, surveys and consents, notifications.                                                                              |
| **SRS — Daily Operations**              | Attendance, staff attendance, visitors, routines, leave requests, calendar, centre log, safety overview, bus services.                                |
| **SRS — Learning**                      | Learning set-up, class updates, gallery, progress reports, portfolios, enrichment.                                                                    |
| **SRS — Fees & Payments**               | Fee set-up, billing, payments and receipts, deposits and refunds, GSII, finance approvals, reports and month-end.                                     |
| **SRS — Joining & Leaving**             | Joining, withdrawals, temporary withdrawals, transfers, graduation, re-enrolment.                                                                     |
| **SRS — Administration**                | Organisation, users and permissions, templates, settings, history, data migration.                                                                    |
| **SRS — Parents App**                   | What parents and guardians see and do in the mobile app (prototype: https://bba-parents.lovable.app).                                                 |
| **SRS — Teacher App**                   | What teachers do in the mobile app (prototype: https://bba-teacher.lovable.app).                                                                      |
| **SRS — Attendance App**                | Check-in, check-out, temperatures, staff clock-in and visitors on the centre iPad (prototype: https://bba-attendance-visitor.lovable.app).            |
| **SRS — Centre Director App (Phase 2)** | The Centre Director mobile app planned for Phase 2; in Phase 1 the Centre Director uses SMS web (prototype: https://bba-centre-director.lovable.app). |

Prototype: [<u>https://bba-sms-crm.lovable.app</u>](https://bba-sms-crm.lovable.app)

# 2. System overview

## 2.1 Applications

| **Application**    | **Users**                              | **Purpose in Phase 1**                                                                                                                                                                                                                        |
|--------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SMS web**        | HQ and centre staff                    | All modules described in the SRS set. Works on desktop and tablet browsers.                                                                                                                                                                   |
| **Parents App**    | Parents and guardians                  | Child information, health and pickup updates, announcements, messages, inquiries, surveys and consents, class updates and gallery, progress reports and portfolios, invoices, receipts, PayNow, leave and withdrawal requests, notifications. |
| **Teacher App**    | Teachers                               | Class updates, routines, messages and progress report entry. No attendance taking.                                                                                                                                                            |
| **Attendance App** | Centre staff at the gate (centre iPad) | Child check-in and check-out with photo and temperature at the gate, once per child per day (attendance can also be taken on SMS web). Staff clock-in and visitor sign-in.                                                                    |

The Centre Director mobile app is not in Phase 1; Centre Directors use SMS web.

## 2.2 Countries and organisation

- Phase 1 serves Singapore and Malaysia centres. Vietnam is not in Phase 1.

- The organisation is Country → Brand → Cluster → Centre. Each centre belongs to one legal entity; a legal entity can have several centres.

- Country-specific features (for example GIRO, CDA and ECDA forms in Singapore) are shown only to centres of that country.

## 2.3 Main areas (navigation)

| **Area**                | **Purpose**                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| **Enquiries**           | Leads, visits, trials and booking fees, up to the booking fee payment (CRM; described separately).          |
| **Children & Families** | Records of children, families, health, documents, pickup and classes.                                       |
| **Communication**       | Announcements, messages, inquiries, surveys and consents with parents, and internal announcements to staff. |
| **Daily Operations**    | What happens in the centre each day, including the centre log and safety overview.                          |
| **Learning**            | Learning set-up, class updates, gallery, progress reports, portfolios and enrichment classes.               |
| **Fees & Payments**     | Billing, collection, refunds, subsidy reconciliation and month-end.                                         |
| **Joining & Leaving**   | From booking fee to first day, and withdrawals, transfers, graduation and re-enrolment.                     |
| **Administration**      | Organisation, users and permissions, templates, settings and history.                                       |

The SMS starts when a family pays the booking fee. Everything before that belongs to Enquiries.

# 3. Roles and access

## 3.1 Principles

- HQ Admin holds every permission of every role, in every country, brand and centre, and sees every field in full. HQ Admin is never blocked by a scope message. HQ Admin's permissions cannot be removed, and there is always at least one active HQ Admin.

- Every other role is a subset of HQ Admin's permissions, configured by HQ Admin in Administration › Users & permissions.

- Access has three layers: area permissions (View, Create, Edit, Delete, Approve, Export, Configure per area), special permissions (sensitive actions such as voiding attendance or approving refunds) and protected fields (Hidden, Masked, Read, Edit).

- Each user has a data scope: class, centre, several centres, cluster, brand, country or all. Users see and act only on records within their scope.

- A user can hold more than one role. Centre Directors can grant extra permissions to staff of their own centre, such as approving leave, voiding attendance or reviewing photos.

- Menus, buttons and data follow the permissions: what a user may not do is not shown.

## 3.2 Default roles

| **Role**                      | **Default scope**      | **Main responsibilities**                                                        |
|-------------------------------|------------------------|----------------------------------------------------------------------------------|
| **HQ Admin**                  | All                    | System administration; every permission.                                         |
| **HQ Finance**                | Country / legal entity | Fees, billing, collection, refunds, finance approvals, month-end.                |
| **HQ Curriculum**             | Brand                  | Learning set-up: terms, checklists, rating scales, portfolio layouts.            |
| **HQ Ops / Head of Brand**    | Brand                  | Oversight of a brand; approvals routed to Head of Brand.                         |
| **District Manager**          | Cluster                | Oversight of a cluster (Singapore); approvals routed to District Manager.        |
| **Operations Manager**        | Several centres        | Oversight of centres (Malaysia); approvals routed to Operations Manager.         |
| **Centre Director**           | Centre                 | Runs the centre; approves centre requests; publishes reports and portfolios.     |
| **Assistant Centre Director** | Centre                 | Supports the Centre Director (Malaysia).                                         |
| **Centre Admin**              | Centre                 | Registrations, records, attendance corrections, centre billing tasks.            |
| **Centralised Admin**         | Several centres        | Centre Admin work for a group of small centres.                                  |
| **Senior Teacher**            | Class                  | Teacher work; can receive extra permissions from the Centre Director.            |
| **Teacher**                   | Class                  | Attendance, routines, class updates, progress reports, messages for own classes. |
| **Enrichment Trainer**        | Enrichment classes     | Attendance of own enrichment classes.                                            |
| **Safeguarding officer**      | All                    | Centre log and safety overview of every centre.                                  |
| **External Auditor**          | As granted             | Read-only access for audits.                                                     |

The final list of roles and their permissions is configured by HQ Admin and can change without development work.

## 3.3 Approvals

- All approvals of a user appear in one Approvals inbox, with filters by type, centre and status.

- Who approves each type of request (up to two levels, with optional amount thresholds) is configured in Administration › Approval routes.

- Rejecting a request always requires a reason. Every decision records who decided and when, and the requester is notified.

# 4. Common behaviour

## 4.1 Lists

- Search: one search box with partial, case-insensitive matching on the fields named in each module.

- Filters: combinable, with a "Clear filters" action; the filters are kept when the user returns to the list.

- Sort: click a column header to sort ascending or descending; each list has a default sort.

- Paging: 20, 50 or 100 rows per page, showing for example "1–20 of 356".

- Export: Excel or CSV of the rows matching the current filters; protected fields are excluded for users who cannot see them.

- Bulk actions: available only where a module lists them; the user selects rows and confirms.

- Empty lists show a short message explaining what will appear and how to add the first item.

## 4.2 Records

- Records that have been used are never deleted. They are closed, voided, stopped, retired or deactivated, with a reason where the module requires one.

- Every record has a History tab: who created or changed it, what changed (old and new value), when, why, and who approved it where applicable.

- The history log is append-only: entries cannot be edited or deleted.

- Changes with a future effect have an effective date.

- Documents issued to parents or companies (invoices, receipts, credit notes, signed forms) keep the template version and organisation details that applied when they were issued.

## 4.3 Each kind of data has one home

| **Data**                                                       | **Managed in**                                                   | **Shown read-only in**                 |
|----------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------|
| **Centres, legal entities, levels offered**                    | Administration › Organisation                                    | All modules                            |
| **Classes**                                                    | Children & Families › Classes                                    | Administration › Organisation          |
| **Academic years and terms**                                   | Learning › Setup                                                 | Fees & Payments, Daily Operations      |
| **Centre closure days and public holidays**                    | Daily Operations › Calendar / Administration › Settings (import) | Attendance, Enrichment                 |
| **Approvers**                                                  | Administration › Approval routes                                 | Every approval                         |
| **Settings (billing days, notice periods, feature switches…)** | Administration › Settings                                        | The module that uses them              |
| **Document and message templates**                             | Administration › Templates                                       | Fees, Joining & Leaving, Communication |
| **Consents**                                                   | Communication › Surveys & consents                               | Child record                           |

## 4.4 Settings

- Values that may differ between countries, brands or centres are settings, not fixed values.

- A setting can be set at country, brand, cluster or centre level. A lower level inherits the higher level's value unless it overrides it.

- Changing a setting shows its impact before it is saved and is recorded in History.

## 4.5 Notifications

- Parents receive notifications in the Parents App (push and the in-app notification list). Each guardian has their own notifications and can switch categories on or off.

- Staff receive notifications in SMS (and in the Teacher App where relevant).

- Email is used only where a module says so (for example invoices to companies, registration emails).

- The system does not send SMS text messages or email digests in Phase 1.

- Every message sent is logged and can be reviewed in Administration › History › Messages sent.

## 4.6 Dates, money and language

- Dates are shown as DD MMM YYYY (for example 05 Oct 2026) in the local time of the centre's country.

- Amounts are shown in the currency of the centre's country (SGD or MYR) with two decimals.

- The SMS web screens are in English.

- Parent-facing content (registration form, selected messages and templates) can have Chinese versions; other languages are added as template versions.

## 4.7 Attachments

- Attachments accept PDF, images (JPG, PNG) and common office files. The maximum file size is a setting (default 10 MB per file; videos as set per brand).

- Attachments inherit the access rules of the record they belong to.

# 5. Non-functional requirements

| **Area**                 | **Requirement**                                                                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sign-in**              | Staff sign in with the method set by HQ Admin: Microsoft Entra single sign-on or password. Multi-factor authentication follows Busy Bees' Microsoft policy.                             |
| **Shared devices**       | The Attendance App runs on a shared tablet at the centre gate and shows only what is needed for check-in, check-out and visitors.                                                       |
| **Personal data**        | Personal data is shown only to users who need it; NRIC, bank account, medical and other protected fields are masked or hidden by role. Access to protected data and exports are logged. |
| **Audit**                | Changes to child, user, billing, credit and refund information are recorded with who, when, old and new value.                                                                          |
| **Performance**          | Lists and record pages open within 3 seconds for normal centre volumes; large exports and reports run in the background and notify the user when ready.                                 |
| **Availability**         | The system is available 24 hours a day; planned maintenance is announced in advance and scheduled outside centre operating hours.                                                       |
| **Browsers and devices** | Current versions of Chrome, Edge and Safari on desktop and tablet. Parents App and Teacher App on current iOS and Android versions.                                                     |
| **Accessibility**        | Clear labels, keyboard access on web, and readable text sizes.                                                                                                                          |
| **Data migration**       | Children, families, enrolments, classes, balances and required history are migrated from Taidii before go-live, with duplicate checks.                                                  |

# 6. Common business rules

| **ID**         | **Rule**                                                                                              |
|----------------|-------------------------------------------------------------------------------------------------------|
| **BR-GEN-001** | HQ Admin has every permission and is never restricted by scope.                                       |
| **BR-GEN-002** | Every other role is a subset of HQ Admin's permissions and is configured by HQ Admin.                 |
| **BR-GEN-003** | Users see and act only on records within their data scope.                                            |
| **BR-GEN-004** | Menus, buttons and data a user is not permitted to use are not shown.                                 |
| **BR-GEN-005** | Records that have been used are never deleted; they are closed, voided, stopped or deactivated.       |
| **BR-GEN-006** | Every change to a record is recorded in its history, which cannot be edited or deleted.               |
| **BR-GEN-007** | Every rejection of a request requires a reason.                                                       |
| **BR-GEN-008** | Approvers are configured only in Approval routes.                                                     |
| **BR-GEN-009** | Each kind of data is managed in one place and shown read-only elsewhere.                              |
| **BR-GEN-010** | Values that can differ by country, brand or centre are settings with inheritance and centre override. |
| **BR-GEN-011** | Issued documents keep the template version and organisation details that applied when issued.         |
| **BR-GEN-012** | Exports never include fields the user is not permitted to see.                                        |
| **BR-GEN-013** | Country-specific features are shown only to centres of that country.                                  |
| **BR-GEN-014** | The SMS does not send SMS text messages or email digests in Phase 1.                                  |

# 7. Common acceptance criteria

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Scenario</strong></th>
<th><strong>Given / When / Then</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AC-GEN-001</strong></td>
<td>HQ Admin access</td>
<td>Given a centre was opened today,<br />
when HQ Admin opens any module,<br />
then the new centre appears in filters and records, and no scope message is shown.</td>
</tr>
<tr class="even">
<td><strong>AC-GEN-002</strong></td>
<td>Permissions drive menus</td>
<td>Given HQ Admin removes "Learning › View" from the Teacher role,<br />
when a teacher signs in,<br />
then the Learning area is not shown to the teacher.</td>
</tr>
<tr class="odd">
<td><strong>AC-GEN-003</strong></td>
<td>Scope</td>
<td>Given a Centre Admin has scope Centre A,<br />
when they search for a child of Centre B,<br />
then the child is not found.</td>
</tr>
<tr class="even">
<td><strong>AC-GEN-004</strong></td>
<td>List standard</td>
<td>Given a list with 356 rows,<br />
when the user opens it,<br />
then 20 rows are shown with "1–20 of 356", columns can be sorted, and Export downloads the filtered rows.</td>
</tr>
<tr class="odd">
<td><strong>AC-GEN-005</strong></td>
<td>Protected export</td>
<td>Given a user cannot see NRIC,<br />
when they export a child list,<br />
then the export does not contain NRIC.</td>
</tr>
<tr class="even">
<td><strong>AC-GEN-006</strong></td>
<td>No delete</td>
<td>Given a fee item used on an invoice,<br />
when a user looks for a delete action,<br />
then only "Stop using" is offered.</td>
</tr>
<tr class="odd">
<td><strong>AC-GEN-007</strong></td>
<td>History</td>
<td>Given a Centre Admin changes a child's address,<br />
when the child's History tab is opened,<br />
then it shows the old and new address, who changed it and when.</td>
</tr>
<tr class="even">
<td><strong>AC-GEN-008</strong></td>
<td>Reject reason</td>
<td>Given any request in Approvals,<br />
when the approver rejects it without a reason,<br />
then the system does not allow it.</td>
</tr>
<tr class="odd">
<td><strong>AC-GEN-009</strong></td>
<td>Setting inheritance</td>
<td>Given the brand notice period is 1 month and Centre A overrides it to 2 months,<br />
when a withdrawal is submitted at Centre A,<br />
then the 2-month notice period is applied.</td>
</tr>
</tbody>
</table>

# 8. Glossary

| **Term**              | **Meaning**                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Area**              | A main section of the SMS navigation, such as Fees & Payments.                                |
| **Booking fee**       | Fee paid to secure a place; the point where a family enters the SMS.                          |
| **CD**                | Centre Director (also called Principal or Head of School).                                    |
| **CDA**               | Child Development Account (Singapore), usable for eligible fees.                              |
| **Cluster**           | A group of centres within a brand, overseen by a District Manager or Operations Manager.      |
| **ECDA**              | Early Childhood Development Agency (Singapore).                                               |
| **e-Form 1 / Form 3** | ECDA forms for enrolment and withdrawal.                                                      |
| **GIRO**              | Direct debit from a bank account (Singapore); collected in 1ST DD and 2ND DD runs.            |
| **GSII**              | Monthly ECDA subsidy report per centre.                                                       |
| **Legal entity**      | The company that issues invoices and holds the bank account for its centres.                  |
| **Level**             | A stage of the programme as named by each brand (for example Nursery), mapped to ECDA levels. |
| **PayNow**            | Singapore instant payment by QR code.                                                         |
| **Protected field**   | A field such as NRIC or bank account whose visibility is controlled by role.                  |
| **Scope**             | The part of the organisation a user can see and act on.                                       |
| **Setting**           | A configurable value with country, brand, cluster or centre level.                            |
