Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Administration**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-ADM-NNN and acceptance criteria AC-ADM-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Administration module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes how BBA sets up its organisation, controls who can do what, manages templates and settings, keeps a full history of changes and moves data from Taidii.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/organisation. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Organisation: organisation tree (country, brand, cluster, centre), centres, legal entities, levels and their mapping to ECDA levels.

- Users & permissions: user accounts, roles, extra permissions granted by Centre Directors, approval routes, sign-in and security.

- Templates: financial documents, registration forms and T&C, handbooks, messages and letters.

- Settings: one place for every setting, inherited from country to brand to cluster to centre; feature switches; shared lists.

- History: change log, messages sent and integration log.

- Data migration tools used while moving data from Taidii and WeeBee.

## 1.2 Not in Phase 1

- Creating accounts or assigning roles automatically from Microsoft Entra groups (SCIM).

- Synchronisation with an HR system (HRMS).

- Fast user switching on shared devices.

- Free customisation of fields and screen layouts.

- Free-text variables in welcome letters.

- Sending logs to an external monitoring system.

- Data retention and anonymisation policies, and copying anonymised data to a test environment.

# 2. Who uses it

| **Role**                                                         | **What they do in this module**                                                                                                                                                                               |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HQ Admin (BBA IT)**                                            | Has every permission in every country, brand and centre, sees every field and cannot be restricted. Manages the organisation, users, roles, approval routes, sign-in, templates, settings and data migration. |
| **HQ Finance**                                                   | Maintains legal entities, bank accounts, PayNow and GST; edits financial document templates and fee settings when granted; reads the change log and integration log.                                          |
| **HQ Ops / Head of Brand, District Manager, Operations Manager** | Manage clusters and the centres in their scope; change the settings they are granted; act as approvers in approval routes.                                                                                    |
| **Centre Director**                                              | Grants extra permissions to staff of the centre; changes centre-level settings they are granted; views the history of the centre's records.                                                                   |
| **Centre Admin / School Admin**                                  | Views the history of the centre's records; adjusts messages slightly before sending them.                                                                                                                     |
| **External Auditor**                                             | Reads the change log and exports it. Cannot change anything.                                                                                                                                                  |
| **Parent (Parents App)**                                         | Acknowledges receipt of the brand handbook.                                                                                                                                                                   |

# 3. Process overview

## P1. Open a new centre

1\. HQ Admin opens the centre with its brand, cluster, legal entity, cost centre and POP status.

2\. HQ Admin sets the levels offered and the licensed capacity for each level.

3\. HQ Admin reviews the settings the centre inherits and overrides any that differ.

4\. HQ Admin creates the centre staff accounts and sets their scope to the centre.

5\. The centre appears immediately on every screen for HQ Admin and for users whose scope covers it.

## P2. Onboard and offboard a staff member

1\. HQ Admin creates the user with name, email, job title, role, scope and start date.

2\. The user signs in with the configured sign-in method.

3\. When the staff member moves centre, HQ Admin ends the old scope and opens the new one from an effective date.

4\. When the staff member leaves, HQ Admin deactivates the user; sign-in is blocked immediately and history is kept.

## P3. Create or change a role

1\. HQ Admin creates a role from scratch or duplicates an existing role.

2\. HQ Admin sets area permissions, special permissions and protected fields.

3\. HQ Admin reviews the list of changes and the number of people affected.

4\. HQ Admin publishes the role; the change applies at the users' next action and is written to the change log.

## P4. Grant an extra permission in a centre

1\. The Centre Director selects a staff member of the centre and a permission they hold themselves.

2\. The Centre Director gives a reason and an optional end date, and confirms.

3\. The staff member is notified and can use the permission at once.

4\. The permission ends when revoked or on its end date, and the staff member is notified.

## P5. Change a setting

1\. An authorised user opens the setting and sees the value and its source for every centre.

2\. The user picks the scope (country, brand, cluster or selected centres) and the new value.

3\. The system validates the value and shows the impact (children, invoices, pending requests).

4\. The user confirms; centres without their own override take the new value; the change is logged.

## P6. Publish a new template version

1\. HQ Admin (or Finance for financial documents) edits the template and previews it with sample data.

2\. The user publishes a new version with a summary of changes.

3\. New documents and messages use the new version; documents already issued keep their version.

## P7. Migrate data from Taidii

1\. HQ Admin maps identifiers and statuses from Taidii and WeeBee to the SMS.

2\. The system loads each batch and lists records received, errors, reasons and fixes.

3\. HQ Admin reviews possible duplicates and merges them or keeps them separate.

4\. The system derives the levels offered by each centre from the Taidii class list.

5\. After go-live, Data migration is hidden from the menu.

# 4. Modules, sub-modules, features and functions

## 1. Organisation

### 1.1 Structure

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/units</u>](https://bba-sms-crm.lovable.app/organisation/units)

| **Feature**                        | **Function**                                                                                                       |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **View organisation tree**         | Country, brand, cluster, centre. Brands are set per country (for example, Small Wonder Malaysia is its own brand). |
| **Search units**                   | Name, unit code.                                                                                                   |
| **Create brand**                   | Name, country, logo.                                                                                               |
| **Edit brand**                     | Name, logo; logged.                                                                                                |
| **Deactivate brand**               | Allowed only when the brand has no active centre.                                                                  |
| **Create cluster**                 | Name, brand, manager (District Manager or Operations Manager).                                                     |
| **Edit cluster**                   | Name, manager; logged.                                                                                             |
| **Deactivate cluster**             | Allowed only when the cluster has no centre.                                                                       |
| **Move centre to another cluster** | Within the same brand; logged.                                                                                     |
| **View history**                   | Every change to brands and clusters.                                                                               |

### 1.2 Centres

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/units</u>](https://bba-sms-crm.lovable.app/organisation/units)

| **Feature**                        | **Function**                                                                                                                                                                    |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View centre list**               | Name, centre code, brand, cluster, legal entity, cost centre, POP / Non-POP, status, licensed capacity, Centre Director.                                                        |
| **Search**                         | Name, centre code.                                                                                                                                                              |
| **Filter**                         | Country, brand, cluster, POP, status.                                                                                                                                           |
| **Sort**                           | Default by name, A to Z.                                                                                                                                                        |
| **Paging**                         | 20 / 50 / 100 rows.                                                                                                                                                             |
| **View centre detail**             | Government centre code, address, phone, email, Centre Director, legal entity, NetSuite cost centre, POP, PT Code (GSII).                                                        |
| **Open a centre**                  | Name, brand, cluster, legal entity, cost centre and POP are required; address and Centre Director optional. HQ Admin sees the new centre on every screen at once.               |
| **Edit centre**                    | All centre fields; logged.                                                                                                                                                      |
| **Map cost centre**                | Centre name to NetSuite cost centre, including centres whose names differ.                                                                                                      |
| **Set levels offered**             | Choose the levels the centre teaches from the brand's level list (for example, centre A: Pre-Nursery, Nursery, Pre-K, K; centre B: Pre-K, K).                                   |
| **Set licensed capacity by level** | Per centre and level; a warning shows when enrolment exceeds it.                                                                                                                |
| **View classes**                   | Read-only tab: classes of the centre and headcount against capacity, with a link to Children & Families › Classes.                                                              |
| **Close centre permanently**       | Reason, closing date and an impact check (children, staff, classes, unpaid invoices, GIRO accounts). Different from a closure day, which is set in Daily Operations › Calendar. |
| **Reopen centre**                  | The closed period stays in the history.                                                                                                                                         |
| **Bulk transfer children**         | Move children to another centre when a centre closes, or from a junior to a senior campus at year end (Malaysia).                                                               |
| **Export**                         | Centre list.                                                                                                                                                                    |
| **View history**                   | Every change to the centre.                                                                                                                                                     |

### 1.3 Legal entities

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/units</u>](https://bba-sms-crm.lovable.app/organisation/units)

| **Feature**           | **Function**                                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------------------------|
| **View entity list**  | Name, country, registration number (UEN), GST registration number, NetSuite code, number of centres.          |
| **Search**            | Name, registration number.                                                                                    |
| **Filter**            | Country.                                                                                                      |
| **Create entity**     | Name, country, registration number, NetSuite code, address.                                                   |
| **Edit entity**       | All entity fields; logged.                                                                                    |
| **Set bank account**  | One bank account per entity. The full account number shows only to users with the protected-field permission. |
| **Set PayNow**        | PayNow UEN of the entity. GIRO files and PayNow QR codes use the entity's details.                            |
| **Set GST**           | GST rate and effective date per entity.                                                                       |
| **Assign centres**    | One entity has many centres; one centre has one entity.                                                       |
| **Deactivate entity** | An entity that has been used is never deleted.                                                                |
| **Export**            | Entity list.                                                                                                  |
| **View history**      | Every change to the entity.                                                                                   |

### 1.4 Levels

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/units</u>](https://bba-sms-crm.lovable.app/organisation/units)

| **Feature**            | **Function**                                                                                              |
|------------------------|-----------------------------------------------------------------------------------------------------------|
| **View brand levels**  | Levels with the names each brand uses (for example Pre-Nursery, Nursery, Pre-Kindergarten, Kindergarten). |
| **Create level**       | Name, order, age range.                                                                                   |
| **Edit level**         | Name, order, age range; logged.                                                                           |
| **Deactivate level**   | A level that has classes is never deleted.                                                                |
| **Map to ECDA levels** | Each brand level maps to one of the 6 ECDA levels: Infant, PG, N1, N2, K1, K2.                            |
| **Export**             | Levels and ECDA mapping.                                                                                  |

## 2. Users & permissions

### 2.1 Users

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/users</u>](https://bba-sms-crm.lovable.app/organisation/users)

| **Feature**                | **Function**                                                                          |
|----------------------------|---------------------------------------------------------------------------------------|
| **View user list**         | Name, email, job title, roles, scope, status (Invited / Active / Left), last sign-in. |
| **Search**                 | Name, email, job title.                                                               |
| **Filter**                 | Role, country, brand, centre, status.                                                 |
| **Saved views**            | "Left but still active", "Starting soon, no account".                                 |
| **Sort**                   | Name, date created.                                                                   |
| **Paging**                 | 20 / 50 / 100 rows.                                                                   |
| **Create user**            | Name, email, job title, role, scope, start date. Users can be created at any level.   |
| **Send invitation**        | Activation email that matches the sign-in method.                                     |
| **Assign role**            | One or more roles, including roles created by BBA.                                    |
| **Set data scope**         | Class, centre, several centres (Centralised Admin), cluster, brand, country or all.   |
| **Edit user**              | Details, roles and scope, with an effective date.                                     |
| **Move to another centre** | Ends the old scope and opens the new one; history kept.                               |
| **Deactivate user**        | Blocks sign-in immediately; history kept; confirmation required.                      |
| **Reactivate user**        | For rehired staff; default role and scope from before can be reused.                  |
| **Reset password**         | Available only when the sign-in method is password.                                   |
| **Bulk change role**       | For several selected users.                                                           |
| **Bulk deactivate**        | For several selected users.                                                           |
| **Import users**           | From an Excel template for the initial set-up; row-by-row errors before confirming.   |
| **View user access**       | Combined permissions from roles, extra permissions and scope.                         |
| **Export**                 | User list.                                                                            |
| **View history**           | Who created the user and changed roles, scope or status.                              |

### 2.2 Roles

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation</u>](https://bba-sms-crm.lovable.app/organisation)

| **Feature**                  | **Function**                                                                                                                                                                                                                                                                     |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View role list**           | Name, number of holders, default scope, number of permissions, status (Draft / In use / Retired).                                                                                                                                                                                |
| **Search**                   | Role name.                                                                                                                                                                                                                                                                       |
| **Filter**                   | Status.                                                                                                                                                                                                                                                                          |
| **Sort**                     | Name, number of holders.                                                                                                                                                                                                                                                         |
| **Create role**              | From scratch.                                                                                                                                                                                                                                                                    |
| **Duplicate role**           | "Save as" from an existing role.                                                                                                                                                                                                                                                 |
| **Edit area permissions**    | Grid of areas and actions: View, Create, Edit, Delete, Approve, Export, Configure.                                                                                                                                                                                               |
| **Edit special permissions** | One grouped list of specific actions (for example void attendance, approve photos, view full NRIC).                                                                                                                                                                              |
| **Edit protected fields**    | NRIC, medical information, date of birth, bank account, deposit, internal notes: Hidden / Masked / Read / Edit.                                                                                                                                                                  |
| **Review before saving**     | List of changes and the number of people affected.                                                                                                                                                                                                                               |
| **Publish role**             | Draft to In use.                                                                                                                                                                                                                                                                 |
| **Rename role**              | Logged.                                                                                                                                                                                                                                                                          |
| **Compare two roles**        | Shows only the differences.                                                                                                                                                                                                                                                      |
| **Assign people**            | Assign the role to several users from the role screen.                                                                                                                                                                                                                           |
| **Retire role**              | Allowed only when nobody holds the role.                                                                                                                                                                                                                                         |
| **Delete role**              | Allowed only for a Draft role that was never used.                                                                                                                                                                                                                               |
| **Lock HQ Admin role**       | No permission can be removed from HQ Admin; at least one active HQ Admin always exists.                                                                                                                                                                                          |
| **Load default roles**       | HQ Admin, HQ Finance, HQ Curriculum, HQ Ops / Head of Brand, District Manager, Operations Manager, Centre Director, Assistant Centre Director, Centre Admin, Centralised Admin, Senior Teacher, Teacher, Enrichment Trainer, Safeguarding officer, External Auditor (read only). |
| **Export permission matrix** | Excel, for BBA review.                                                                                                                                                                                                                                                           |
| **View history**             | Who changed which permission, when, old value and new value.                                                                                                                                                                                                                     |

### 2.3 Extra permissions

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/delegations</u>](https://bba-sms-crm.lovable.app/organisation/delegations)

| **Feature**                  | **Function**                                                                                                                                                                            |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View granted permissions** | Who holds it, permission, granted by, start date, end date, status (Active / Expired / Revoked).                                                                                        |
| **Search**                   | User name.                                                                                                                                                                              |
| **Filter**                   | Permission, centre, status.                                                                                                                                                             |
| **Grant permission**         | Centre Director grants a staff member of the centre a permission they hold themselves (for example approve leave, void attendance, approve photos); reason required; end date optional. |
| **Revoke permission**        | Takes effect immediately.                                                                                                                                                               |
| **Auto-expire**              | The permission ends automatically on its end date.                                                                                                                                      |
| **Notify**                   | The staff member is notified when a permission is granted, revoked or expires.                                                                                                          |
| **Export**                   | Granted permissions.                                                                                                                                                                    |
| **View history**             | Every grant, revoke and expiry.                                                                                                                                                         |

### 2.4 Approval routes

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/approvals</u>](https://bba-sms-crm.lovable.app/organisation/approvals)

| **Feature**             | **Function**                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------|
| **View routes**         | By request type, country and brand: level-1 approver, level-2 approver, amount threshold. |
| **Filter**              | Request type, country, brand.                                                             |
| **Edit route**          | Choose the approver role for each level; up to 2 levels; optional amount threshold.       |
| **Load default routes** | Pre-filled routes for every request type (see business rules), editable by HQ Admin.      |
| **Export**              | All routes.                                                                               |
| **View history**        | Every route change.                                                                       |

### 2.5 Sign-in & security

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/security</u>](https://bba-sms-crm.lovable.app/organisation/security)

| **Feature**            | **Function**                                                                 |
|------------------------|------------------------------------------------------------------------------|
| **Set sign-in method** | The sign-in method is a setting: Microsoft Entra single sign-on or password. |
| **Enforce MFA**        | Multi-factor authentication follows Microsoft Entra policies.                |
| **View sign-in log**   | User, date and time, success or failure.                                     |
| **Filter sign-in log** | User, result, date range.                                                    |
| **Export sign-in log** | Filtered list.                                                               |

## 3. Templates

### 3.1 Financial documents

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/templates</u>](https://bba-sms-crm.lovable.app/organisation/templates)

| **Feature**             | **Function**                                                                                                                                                                               |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View templates**      | Type (invoice: monthly, registration, enrichment, ad hoc; receipt: payment, GIRO, deposit; credit note), brand, legal entity, version, status (Draft / Active / Retired).                  |
| **Search**              | Template name.                                                                                                                                                                             |
| **Filter**              | Type, brand, status.                                                                                                                                                                       |
| **Preview**             | With sample data.                                                                                                                                                                          |
| **Edit template**       | Logo, title, information blocks, footer notes; merge fields (centre name, address, phone, email; GST registration number; company registration number; document number). Fits on one page. |
| **Publish new version** | Summary of changes required. Documents already issued keep their version.                                                                                                                  |
| **Compare versions**    | Shows the differences between two versions.                                                                                                                                                |
| **Retire template**     | No longer used for new documents.                                                                                                                                                          |
| **View history**        | Who edited, which version, how many documents issued per version.                                                                                                                          |

### 3.2 Registration forms & T&C

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/templates</u>](https://bba-sms-crm.lovable.app/organisation/templates)

| **Feature**          | **Function**                                                                                                                             |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **View forms**       | Per brand; Odyssey Orchard has its own form.                                                                                             |
| **Preview form**     | As the parent sees it.                                                                                                                   |
| **Edit form fields** | Required / optional / hidden, per brand.                                                                                                 |
| **Edit T&C**         | One standard T&C plus a lookup table per brand and centre (deposit months with or without GIRO, notice period) that the system fills in. |
| **Set signatures**   | Two signature boxes on every form.                                                                                                       |
| **Publish version**  | Parents who already signed are not asked to sign again.                                                                                  |
| **View history**     | Every version and who published it.                                                                                                      |

### 3.3 Handbooks

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/templates</u>](https://bba-sms-crm.lovable.app/organisation/templates)

| **Feature**                 | **Function**                                                         |
|-----------------------------|----------------------------------------------------------------------|
| **View handbooks**          | Brand, version, publish date.                                        |
| **Upload handbook**         | One PDF per brand; a warning shows for large files.                  |
| **Replace handbook**        | Creates a new version; the version each parent acknowledged is kept. |
| **View acknowledgements**   | Parents who have and have not acknowledged receipt.                  |
| **Export acknowledgements** | Excel.                                                               |

### 3.4 Messages & letters

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/templates</u>](https://bba-sms-crm.lovable.app/organisation/templates)

| **Feature**                             | **Function**                                                                                                                                                                                                    |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View message templates**              | Registration emails (registration link with handbook and fee table; receipt with e-Form 1 and GIRO instructions; e-Form 1 submitted), welcome letter per brand, registration completion reminder, fee reminder. |
| **Search**                              | Template name.                                                                                                                                                                                                  |
| **Filter**                              | Type, brand.                                                                                                                                                                                                    |
| **Preview**                             | With sample data.                                                                                                                                                                                               |
| **Edit template**                       | Content and merge fields (parent name, child name, centre, start date, class, due date).                                                                                                                        |
| **Add language version**                | English, Chinese (registration forms) and Bahasa Malaysia.                                                                                                                                                      |
| **Allow small edits when sending**      | Admin can adjust the text before sending one message.                                                                                                                                                           |
| **Turn off welcome letter for a brand** | For brands that opt out (for example Odyssey).                                                                                                                                                                  |
| **Publish version**                     | New messages use the new version.                                                                                                                                                                               |
| **View history**                        | Every version and who published it.                                                                                                                                                                             |

## 4. Settings

### 4.1 Settings by level

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/features</u>](https://bba-sms-crm.lovable.app/organisation/features)

| **Feature**                         | **Function**                                                                                          |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| **View settings**                   | Grouped by Fees, Joining & leaving, Daily operations, Learning, Communication.                        |
| **Search**                          | Setting name.                                                                                         |
| **View one setting across centres** | Value for each centre and its source (default, country, brand, cluster, centre), who set it, when.    |
| **Filter centres**                  | Country, brand, cluster, "different from default", "not confirmed".                                   |
| **Change a setting**                | Choose the scope (country, brand, cluster or selected centres) and the value; the value is validated. |
| **See impact**                      | Number of children, invoices and pending requests affected.                                           |
| **Override for a centre**           | The centre value replaces the inherited value.                                                        |
| **Remove override**                 | The centre goes back to the inherited value.                                                          |
| **Mark as confirmed**               | A default value shows "To confirm" until a user confirms it.                                          |
| **Export**                          | Settings and values per centre.                                                                       |
| **View history**                    | One line per change.                                                                                  |

### 4.2 Feature switches

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/features</u>](https://bba-sms-crm.lovable.app/organisation/features)

| **Feature**          | **Function**                                                                                                                                             |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View switches**    | Feature, scope, status for each centre.                                                                                                                  |
| **Turn feature on**  | Per centre or brand: School bus, Enrichment, Photo review, Temporary withdrawal, Admin message check.                                                    |
| **Turn feature off** | Hides the feature from the menu. Blocked while work is still open (for example photos waiting for review, children on the bus), with links to that work. |
| **View history**     | Every switch change.                                                                                                                                     |

### 4.3 Shared lists

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/features</u>](https://bba-sms-crm.lovable.app/organisation/features)

| **Feature**         | **Function**                                                                                                           |
|---------------------|------------------------------------------------------------------------------------------------------------------------|
| **View lists**      | Withdrawal reasons, calendar event types, centre log categories, enquiry categories, public holidays and closure days. |
| **Add item**        | Name, order, scope.                                                                                                    |
| **Edit item**       | Name, order; logged.                                                                                                   |
| **Deactivate item** | An item that has been used is never deleted.                                                                           |
| **Import items**    | From Excel (public holidays, closure days).                                                                            |
| **Export**          | List items.                                                                                                            |

## 5. History

### 5.1 Change log

*Prototype:* [<u>https://bba-sms-crm.lovable.app/history</u>](https://bba-sms-crm.lovable.app/history)

| **Feature**                  | **Function**                                                                                                                                                              |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View changes**             | Date and time, user and their role at the time, type (field change, approval step, owner change, action, integration), record, old value, new value, reason, approved by. |
| **Search**                   | User, record, reason.                                                                                                                                                     |
| **Filter**                   | Area, type, user, date range, centre.                                                                                                                                     |
| **Sort**                     | Default newest first.                                                                                                                                                     |
| **Paging**                   | 20 / 50 / 100 rows.                                                                                                                                                       |
| **Open record**              | Opens the record from the log line.                                                                                                                                       |
| **Mask sensitive fields**    | Old and new values follow the viewer's protected-field permission.                                                                                                        |
| **Export**                   | Exactly the filtered list, for audit.                                                                                                                                     |
| **View history on a record** | History tab on child, invoice, withdrawal and other records.                                                                                                              |

### 5.2 Messages sent

*Prototype:* [<u>https://bba-sms-crm.lovable.app/history</u>](https://bba-sms-crm.lovable.app/history)

| **Feature**            | **Function**                                                    |
|------------------------|-----------------------------------------------------------------|
| **View sent messages** | Emails and notifications: what, to whom, when, channel, status. |
| **Search**             | Recipient, content.                                             |
| **Filter**             | Type, channel, date range, centre.                              |
| **Open message**       | Shows the content as sent.                                      |
| **Export**             | Filtered list.                                                  |

### 5.3 Integration log

*Prototype:* [<u>https://bba-sms-crm.lovable.app/history</u>](https://bba-sms-crm.lovable.app/history)

| **Feature**        | **Function**                                                                                                                                         |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View exchanges** | System (DBS GIRO and PayNow files, GSII, NetSuite export, e-Form 1, Malaysia e-invoice), record, status (Sent / Accepted / Failed / Waiting), error. |
| **Search**         | Record.                                                                                                                                              |
| **Filter**         | System, status, date range.                                                                                                                          |
| **Retry**          | For failed lines, with permission.                                                                                                                   |
| **View payload**   | With permission; viewing is logged.                                                                                                                  |
| **Export**         | Filtered list.                                                                                                                                       |

## 6. Data migration

### 6.1 Data migration

*Prototype:* [<u>https://bba-sms-crm.lovable.app/organisation/migration</u>](https://bba-sms-crm.lovable.app/organisation/migration)

| **Feature**               | **Function**                                                                                 |
|---------------------------|----------------------------------------------------------------------------------------------|
| **Map identifiers**       | Taidii and WeeBee keys and registration numbers to SMS records.                              |
| **Review duplicates**     | Children and parents that may be the same person.                                            |
| **Merge duplicates**      | Confirmation required.                                                                       |
| **Keep as separate**      | "Two different children".                                                                    |
| **View batches**          | Records received, errors, reason and fix for each error.                                     |
| **Re-run batch**          | After fixes.                                                                                 |
| **Map statuses**          | Old status to new status.                                                                    |
| **Derive levels offered** | From the Taidii class list, suggests the levels each centre teaches for HQ Admin to confirm. |
| **Hide after go-live**    | Data migration is removed from the menu.                                                     |

# 5. Business rules

## Access and HQ Admin

| **ID**         | **Rule**                                                                                                                                                                                                                   |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-001** | HQ Admin has every permission of every role, in every country, brand and centre, including centres opened after the role was set up. HQ Admin sees every field in full and is never blocked as "Outside where you work".   |
| **BR-ADM-002** | No permission can be removed from the HQ Admin role. At least one active HQ Admin must exist at all times; the last one cannot be deactivated or have the role removed.                                                    |
| **BR-ADM-003** | Every other role is a subset of HQ Admin's permissions, configured by HQ Admin.                                                                                                                                            |
| **BR-ADM-004** | Only users with the Administration permission can open Administration screens. A custom role with that permission can open them in the same way as HQ Admin.                                                               |
| **BR-ADM-005** | Permissions have three layers: area permissions (View, Create, Edit, Delete, Approve, Export, Configure per area), special permissions (one list of specific actions) and protected fields (Hidden, Masked, Read or Edit). |
| **BR-ADM-006** | Data scope is set per user (class, centre, several centres, cluster, brand, country or all), not per role. A user sees only records inside their scope.                                                                    |
| **BR-ADM-007** | A user can hold several roles. Their access is the combination of all roles, extra permissions and scope.                                                                                                                  |
| **BR-ADM-008** | Role and scope changes take effect at the user's next action and are written to the change log.                                                                                                                            |

## Users and sign-in

| **ID**         | **Rule**                                                                                                                                                     |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-009** | User accounts are created manually by HQ Admin or imported from Excel for the initial set-up.                                                                |
| **BR-ADM-010** | Deactivating a user blocks sign-in immediately. The user's records and history are kept.                                                                     |
| **BR-ADM-011** | Moving a user to another centre ends the old scope and opens the new one from the effective date.                                                            |
| **BR-ADM-012** | The sign-in method is a setting: Microsoft Entra single sign-on or password (default: Microsoft Entra single sign-on). MFA follows Microsoft Entra policies. |
| **BR-ADM-013** | Every sign-in attempt, successful or failed, is recorded in the sign-in log.                                                                                 |

## Roles and extra permissions

| **ID**         | **Rule**                                                                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-014** | A role is Draft until published. Only a Draft role that was never used can be deleted; a role in use can be retired only when nobody holds it.    |
| **BR-ADM-015** | Before a role change is saved, the system lists the changes and the number of people affected.                                                    |
| **BR-ADM-016** | A Centre Director can grant extra permissions only to staff of their own centre, and only permissions they hold themselves. A reason is required. |
| **BR-ADM-017** | An extra permission ends when it is revoked or on its end date. The staff member is notified either way.                                          |

## Approval routes

| **ID**         | **Rule**                                                                                                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-018** | Approvers are configured only in Approval routes. No other screen sets who approves a request.                                                                                                                                                                                                   |
| **BR-ADM-019** | A route has up to 2 levels and an optional amount threshold above which level 2 is required.                                                                                                                                                                                                     |
| **BR-ADM-020** | Default routes: withdrawal with full notice, Centre Director. Withdrawal with short notice, District Manager (Singapore), Operations Manager (Malaysia), Centre Director (Odyssey), Head of Brand (Brighton). Mid-month withdrawal, Centre Director then District Manager or Operations Manager. |
| **BR-ADM-021** | Default routes: temporary withdrawal, Centre Director then Operations Manager (Malaysia); Centre Director (Singapore). Transfer with short notice, District Managers of both centres.                                                                                                            |
| **BR-ADM-022** | Default routes: discount, Centre Director then Finance. Registration fee waiver, Finance. Retention fee waiver (Malaysia), Centre Director then Operations Manager then Finance.                                                                                                                 |
| **BR-ADM-023** | Default routes: void attendance, leave, pickup changes, photos, reports and portfolios, Centre Director. Credit note, refund and notice waiver, Finance (default: no amount threshold).                                                                                                          |

## Organisation

| **ID**         | **Rule**                                                                                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-024** | The organisation tree is Country, Brand, Cluster, Centre. Brands are set per country.                                                                                    |
| **BR-ADM-025** | A brand or cluster can be deactivated only when it has no active centre.                                                                                                 |
| **BR-ADM-026** | Opening a centre requires a legal entity, a cost centre and a POP / Non-POP status.                                                                                      |
| **BR-ADM-027** | Each centre belongs to one legal entity. Each legal entity has one bank account and one PayNow UEN.                                                                      |
| **BR-ADM-028** | Each centre teaches only the levels set in "levels offered". Classes can be created only for those levels, and a level that still has open classes cannot be turned off. |
| **BR-ADM-029** | Each brand level maps to exactly one of the 6 ECDA levels.                                                                                                               |
| **BR-ADM-030** | Closing a centre permanently never deletes it. The centre can be reopened and the closed period stays in the history.                                                    |
| **BR-ADM-031** | Bank account numbers show in full only to users with Read or Edit access to the protected field.                                                                         |

## One place for each type of data

| **ID**         | **Rule**                                                                                                                           |
|----------------|------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-032** | Classes are managed only in Children & Families › Classes. Organisation shows them read-only.                                      |
| **BR-ADM-033** | School years and terms are managed only in Learning › Setup.                                                                       |
| **BR-ADM-034** | Centre holidays and closure days are managed only in Daily Operations › Calendar; the public holiday list is kept in Shared lists. |
| **BR-ADM-035** | Settings is the only place where configuration is stored. Fees › Billing settings and Learning › Setup open the same values.       |

## Settings

| **ID**         | **Rule**                                                                                                                                                                                                                                                  |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-036** | Setting values are inherited from country to brand to cluster to centre. A lower level can override the inherited value, and removing the override restores it.                                                                                           |
| **BR-ADM-037** | Every setting change is validated, shows its impact before saving and is logged with the old value, new value, user and time.                                                                                                                             |
| **BR-ADM-038** | Country settings: GIRO, CDA and ECDA apply only to Singapore; DuitNow and e-invoice apply only to Malaysia; GST for Singapore and SST for Malaysia.                                                                                                       |
| **BR-ADM-039** | Brand settings: notice period by month of withdrawal (default for Malaysia: 1 month for January to September, 3 months for October to December), temporary withdrawal on or off, welcome letter and when it is sent, booking fee, resource fee on or off. |
| **BR-ADM-040** | Centre settings: deposit months (default 1, with 3 for Odyssey Orchard and 2 for Odyssey Dempsey), late cut-off time, operating hours, class update approval and its approver, admin check of teacher messages, visit slots.                              |
| **BR-ADM-041** | HQ settings: invoice draft day, fee reminder days, parent account kept for 6 months after withdrawal, maximum video length, PayNow QR validity (default 48 hours).                                                                                        |
| **BR-ADM-042** | Turning a feature off is blocked while related work is still open, and the system links to that work.                                                                                                                                                     |

## Templates

| **ID**         | **Rule**                                                                                                                                                         |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-043** | Financial document templates are controlled by HQ Admin. Finance can edit them only when granted.                                                                |
| **BR-ADM-044** | Publishing a template version requires a summary of changes.                                                                                                     |
| **BR-ADM-045** | An issued invoice, receipt or credit note keeps the template version and the legal entity details that applied when it was issued. Later changes never alter it. |
| **BR-ADM-046** | Registration forms always have two signature boxes. Publishing new T&C does not ask parents who already signed to sign again.                                    |
| **BR-ADM-047** | The system records which handbook version each parent acknowledged.                                                                                              |

## History

| **ID**         | **Rule**                                                                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ADM-048** | History is append-only. No log line can be edited or deleted.                                                                                                        |
| **BR-ADM-049** | Changes to users, children, billing, credit notes and refunds are always logged.                                                                                     |
| **BR-ADM-050** | Sensitive values in the log follow the viewer's protected-field permission.                                                                                          |
| **BR-ADM-051** | History screens are open to HQ Admin, HQ Finance and External Auditor by default. Centre Directors and Centre Admins see history on the records of their own centre. |
| **BR-ADM-052** | Viewing an integration payload is itself logged.                                                                                                                     |

## Data migration

| **ID**         | **Rule**                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------|
| **BR-ADM-053** | Data migration is available only to HQ Admin and is hidden after go-live.                        |
| **BR-ADM-054** | Possible duplicates are never merged automatically; HQ Admin merges them or keeps them separate. |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                        | **Recipient**        | **Channel**  | **When**                                          |
|-----------------------------------------|----------------------|--------------|---------------------------------------------------|
| **Account invitation**                  | New user             | Email        | When a user is created or reactivated             |
| **Password reset**                      | User                 | Email        | When a reset is requested (password sign-in only) |
| **Extra permission granted**            | Staff member         | In-app (web) | When a Centre Director grants a permission        |
| **Extra permission revoked or expired** | Staff member         | In-app (web) | When revoked or on the end date                   |
| **Role changed**                        | User                 | In-app (web) | When the user's roles or scope change             |
| **Handbook to acknowledge**             | Parent               | In-app       | When a handbook version is published or replaced  |
| **Integration failure**                 | HQ Admin, HQ Finance | In-app (web) | When an exchange fails                            |
| **Data migration batch finished**       | HQ Admin             | In-app (web) | When a batch finishes, with the number of errors  |

## 6.2 Documents

- Templates for invoices, receipts and credit notes per brand and legal entity, with versions.

- Registration form and T&C per brand, with a lookup table per brand and centre.

- Handbook PDF per brand, with versions.

- Message and letter templates (registration emails, welcome letter, reminders) in English, Chinese and Bahasa Malaysia.

- Excel templates to import users and shared list items.

# 7. Reports & exports

| **Report**                    | **Content**                                                                | **Used by**                            |
|-------------------------------|----------------------------------------------------------------------------|----------------------------------------|
| **Centre list**               | Centres with brand, cluster, legal entity, cost centre, POP and capacity   | HQ Admin, HQ Finance                   |
| **Legal entity list**         | Entities with registration, GST and NetSuite codes and centres             | HQ Finance                             |
| **Level mapping**             | Brand levels and their ECDA levels                                         | HQ Admin, HQ Curriculum                |
| **User list**                 | Users with roles, scope, status and last sign-in                           | HQ Admin                               |
| **Permission matrix**         | Every role with area permissions, special permissions and protected fields | HQ Admin                               |
| **Extra permissions**         | Granted permissions with grantor, dates and status                         | HQ Admin, Centre Director              |
| **Approval routes**           | Every route with approvers and thresholds                                  | HQ Admin, HQ Finance                   |
| **Sign-in log**               | Sign-in attempts and results                                               | HQ Admin                               |
| **Settings by centre**        | Each setting's value and source per centre                                 | HQ Admin                               |
| **Handbook acknowledgements** | Parents who have and have not acknowledged each version                    | HQ Admin, Centre Director              |
| **Change log**                | Filtered audit trail                                                       | HQ Admin, HQ Finance, External Auditor |
| **Messages sent**             | Emails and notifications sent                                              | HQ Admin                               |
| **Integration log**           | Exchanges with external systems and their status                           | HQ Admin, HQ Finance                   |

Every list in the module can also be exported to Excel or CSV with the filters applied.

# 8. Acceptance criteria

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
<td><strong>AC-ADM-001</strong></td>
<td>New centre visible to HQ Admin</td>
<td>Given HQ Admin opens centre "Busy Bees Tampines",<br />
when HQ Admin opens the child list and the invoice list,<br />
then Busy Bees Tampines is available in both lists and never shows "Outside where you work".</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-002</strong></td>
<td>Last HQ Admin</td>
<td>Given only one active user holds the HQ Admin role,<br />
when someone tries to deactivate that user or remove the role,<br />
then the system blocks it and explains that at least one HQ Admin is required.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-003</strong></td>
<td>HQ Admin role locked</td>
<td>Given HQ Admin opens the HQ Admin role,<br />
when they try to untick any permission,<br />
then the permission cannot be changed.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-004</strong></td>
<td>Protected field</td>
<td>Given the Teacher role has NRIC set to Masked,<br />
when a teacher opens a child profile,<br />
then the NRIC shows masked, while HQ Admin sees it in full.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-005</strong></td>
<td>Data scope</td>
<td>Given a Centre Director has scope Centre A,<br />
when they search for a child of Centre B,<br />
then the child is not returned.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-006</strong></td>
<td>Deactivate user</td>
<td>Given a teacher leaves on 31 October,<br />
when HQ Admin deactivates the user,<br />
then the teacher cannot sign in from that moment and their past records and history remain.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-007</strong></td>
<td>Extra permission limits</td>
<td>Given a Centre Director does not hold "approve refunds",<br />
when they try to grant it to a staff member,<br />
then the permission is not offered.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-008</strong></td>
<td>Extra permission expiry</td>
<td>Given a Senior Teacher was granted "approve leave" until 30 November,<br />
when 1 December starts,<br />
then the permission is Expired and the Senior Teacher is notified.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-009</strong></td>
<td>Two-level route</td>
<td>Given the discount route is Centre Director then Finance,<br />
when a discount request is submitted at Centre A,<br />
then it goes to the Centre Director first and to Finance only after level 1 approves.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-010</strong></td>
<td>Single place for approvers</td>
<td>Given the withdrawal approver is changed in Approval routes,<br />
when a new withdrawal with short notice is submitted in Singapore,<br />
then it is routed to the role now set in Approval routes.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-011</strong></td>
<td>Levels offered</td>
<td>Given Centre B offers only Pre-K and K,<br />
when a user creates a class at Centre B,<br />
then only Pre-K and K can be chosen.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-012</strong></td>
<td>Level with open classes</td>
<td>Given Centre A has an open Nursery class,<br />
when HQ Admin turns off Nursery in levels offered,<br />
then the system blocks it and lists the open classes.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-013</strong></td>
<td>Setting inheritance</td>
<td>Given the brand notice period is 1 month and Centre A has no override,<br />
when HQ Admin changes the brand value to 2 months,<br />
then Centre A shows 2 months with source Brand, while a centre with its own override keeps its value.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-014</strong></td>
<td>Remove override</td>
<td>Given Centre A overrides the late cut-off time to 9:30,<br />
when HQ Admin removes the override,<br />
then Centre A shows the brand value again and the change is logged.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-015</strong></td>
<td>Feature switch blocked</td>
<td>Given Centre A has 5 photos waiting for review,<br />
when HQ Admin turns Photo review off for Centre A,<br />
then the system blocks it and links to the 5 photos.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-016</strong></td>
<td>Template version on issued documents</td>
<td>Given invoice INV-0001 was issued with template version 3 and entity address X,<br />
when Finance publishes version 4 and edits the entity address,<br />
then INV-0001 still shows version 3 and address X.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-017</strong></td>
<td>Handbook acknowledgement</td>
<td>Given version 2 of the brand handbook is published,<br />
when a parent acknowledges it in the Parents App,<br />
then the acknowledgement list shows the parent against version 2.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-018</strong></td>
<td>Append-only history</td>
<td>Given a change log line exists,<br />
when any user tries to edit or delete it,<br />
then no edit or delete action is available.</td>
</tr>
<tr class="odd">
<td><strong>AC-ADM-019</strong></td>
<td>Export change log</td>
<td>Given the change log is filtered to Centre A for September,<br />
when an External Auditor exports it,<br />
then the file contains exactly the filtered lines with sensitive values masked as for the auditor.</td>
</tr>
<tr class="even">
<td><strong>AC-ADM-020</strong></td>
<td>Duplicate review</td>
<td>Given two migrated child records have the same name and date of birth,<br />
when HQ Admin marks them "Two different children",<br />
then both records stay separate and are not suggested again.</td>
</tr>
</tbody>
</table>
