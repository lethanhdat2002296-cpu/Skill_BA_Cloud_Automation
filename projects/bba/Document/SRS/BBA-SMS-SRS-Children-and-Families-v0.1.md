Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Children & Families**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-CHF-NNN and acceptance criteria AC-CHF-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Children & Families module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes what the module must do so that centres and HQ keep one accurate record of every child, family, health condition, document, authorised pickup person and class, replacing Taidii and paper forms.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/records. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Children: child list, child profile, change records, class assignment, export.

- Families and guardians: guardian records, links to children, primary and billing contacts, Parents App invitations.

- Health and allergies: health information entered by parents, staff notes, allergy alerts, height and weight, growth chart, vaccination records and reminders.

- Documents: required documents per child, upload by staff and parents, review, versions, document requests.

- Authorised pickup: requests from parents in the Parents App, approval by the centre, removal, pickup lists for teachers.

- Classes: classes per centre within the levels offered, teachers, assignment and moves of children, annual promotion.

- What parents see and do in the Parents App for these areas: health information, documents, authorised pickup.

## 1.2 Not in Phase 1

- Medication declarations and medication administration records.

- One-time (temporary) pickup persons.

- Facial recognition at pickup.

- Blood type, swimming, vision, dental, BMI, family medical history and emergency medicine fields.

- Reminders for documents that expire (passport, work pass).

- Printing a full child profile.

- Managing consents (media / PDPA, field trips) in this module; consents are managed in Communication › Surveys & consents.

- Changing a child's status by hand; status changes come from Joining & leaving.

- Deleting children, guardians, documents or classes that hold records.

# 2. Who uses it

| **Role**                 | **What they do in this module**                                                                                                                                  |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HQ Admin**             | Has every permission in the module across all centres; configures required document types, health settings and the roles that see medical details.               |
| **HQ Enrolment**         | Child profiles are created from their enrolment work; views and corrects child and family records across centres.                                                |
| **Centre Director**      | Manages children, families and classes of the centre; reviews documents; approves authorised pickup requests; creates classes when the role has that permission. |
| **School Admin**         | Maintains child and family records of the centre; sends Parents App invitations and document requests; reviews documents; approves authorised pickup requests.   |
| **Teacher**              | Views children of own classes, allergy alerts and the approved pickup list; records height and weight; adds staff health notes.                                  |
| **HQ Finance**           | Views children and families; uses the billing contact set on each family.                                                                                        |
| **Parent (Parents App)** | Enters and updates the child's health information; uploads documents; adds and removes authorised pickup persons; edits own contact details.                     |

# 3. Process overview

## P1. Child profile from enrolment

1\. The enrolment is confirmed in Enrolment.

2\. The system creates the child profile, the guardians and the links between them from the registration data.

3\. The School Admin assigns the child to a class with an effective date.

4\. The School Admin sends the Parents App invitation to the guardians.

5\. The parent activates the app and completes health information, documents and authorised pickup.

## P2. Health information and allergy alerts

1\. The parent submits the health information in the Parents App: the Required part, then the Optional part.

2\. The child shows an allergy alert icon on the child list, attendance and the child profile.

3\. Roles allowed to see medical details open the health record; other roles see only the icon.

4\. Staff add their own notes without changing what the parent entered.

5\. The centre prints or exports the allergy list per class for the kitchen.

## P3. Document collection and review

1\. Each child has a list of required document types; missing ones show as Missing.

2\. The parent uploads in the Parents App, or staff upload at the centre.

3\. The Centre Director or School Admin accepts or rejects each document; a rejection needs a reason.

4\. A rejected document goes back to the parent to upload again.

5\. The centre sends document requests to families with missing documents.

## P4. Authorised pickup

1\. The parent adds a pickup person in the Parents App with photo, name, relationship, NRIC/FIN and phone number.

2\. The Centre Director and School Admin are notified of the pending request.

3\. One of them approves or rejects it; the parent is notified of the result.

4\. Teachers see approved pickup persons with their photos on the child profile and at pickup.

5\. The parent can remove a person at any time; the removal takes effect at once and the centre is notified.

## P5. Class set-up and assignment

1\. A user with permission creates the classes of the centre for the school year, only within the levels offered by the centre.

2\. Each class gets a class code (for example Nursery 1), a class name (for example Mickey), a session, teachers, a room and a maximum size.

3\. The School Admin assigns children to classes; the system warns when the maximum size is exceeded.

4\. Moving a child to another class takes an effective date and opens the new class thread in Communication.

## P6. Annual promotion

1\. At the end of the school year the user opens annual promotion for the centre.

2\. The system proposes the next level and a target class for each child.

3\. The user unticks children who stay (for example children repeating K2) and changes target classes where needed.

4\. The user confirms; children move with the new school year as the effective date and old classes can be closed.

## P7. Height and weight

1\. The teacher opens the class screen for height and weight.

2\. The teacher enters height and weight for each child present and saves once.

3\. The values are recorded directly, with no approval.

4\. The growth chart on the child profile updates with the new point.

# 4. Modules, sub-modules, features and functions

## 1. Children & families

### 1.1 Children

*Prototype:* [<u>https://bba-sms-crm.lovable.app/records</u>](https://bba-sms-crm.lovable.app/records)

| **Feature**                             | **Function**                                                                                                                                     |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **View child list**                     | Photo, name, age, centre, class, level, status, allergy alert icon; total number of records; click a row to open the profile.                    |
| **Search**                              | Partial, case-insensitive match on child name, name on IC, parent name, phone number and student ID; includes withdrawn children.                |
| **Filter**                              | Centre, brand, level, class, status (Enrolled / Temporary withdrawal / Withdrawn / Graduated), has allergy alert; filters combine; Clear button. |
| **Sort**                                | Name (default A to Z), age, start date.                                                                                                          |
| **Paging**                              | 20 / 50 / 100 rows; "1-20 of 356".                                                                                                               |
| **Create child profile from enrolment** | Created automatically when the enrolment is confirmed, with the guardians and their links.                                                       |
| **Create child profile manually**       | Required: full name, date of birth (or expected birth date), gender, centre, level, start date.                                                  |
| **Create profile for an unborn child**  | Expected birth date instead of date of birth; documents, health information and authorised pickup are not required until the child is born.      |
| **Warn about duplicates**               | Warns when a child with the same name and date of birth exists; the user can open it or continue.                                                |
| **View child profile**                  | Tabs: Overview, Family, Health, Documents, Pickup, Class history, Consents (read-only), Billing (read-only).                                     |
| **Edit child profile**                  | Each edit creates a change record.                                                                                                               |
| **Record change details**               | Updated by, approved by, effective date, optional attachment.                                                                                    |
| **Upload child photo**                  | Profile photo; a new photo replaces the old one.                                                                                                 |
| **Assign class**                        | Class with an effective date.                                                                                                                    |
| **Change class**                        | New class with an effective date; the child joins the new class thread in Communication.                                                         |
| **Bulk assign class**                   | Select several children with checkboxes and assign one class.                                                                                    |
| **View status**                         | Status is set by Joining & leaving (temporary withdrawal, withdrawal, graduation); no manual edit here.                                          |
| **View consents**                       | Media / PDPA and field trip consents from Communication › Surveys & consents, read-only.                                                         |
| **View change history**                 | All change records of the child over time.                                                                                                       |
| **Export child list**                   | Excel or CSV of the filtered list; NRIC hidden for roles not allowed to see it.                                                                  |
| **Send message to parents**             | From the profile or from selected rows; opens Communication › Messages with the parents selected.                                                |
| **Apply access scope**                  | HQ sees all centres; centre staff see their centre; teachers see their own classes.                                                              |

### 1.2 Families & guardians

*Prototype:* [<u>https://bba-sms-crm.lovable.app/records/families</u>](https://bba-sms-crm.lovable.app/records/families)

| **Feature**                        | **Function**                                                                            |
|------------------------------------|-----------------------------------------------------------------------------------------|
| **View guardian list**             | Name, relationship, phone number, email, children, Parents App status, billing contact. |
| **Search**                         | Name, phone number, email, last 4 characters of NRIC.                                   |
| **Filter**                         | Centre, has Parents App account, is billing contact.                                    |
| **Sort**                           | Name (default A to Z).                                                                  |
| **Paging**                         | 20 / 50 / 100 rows; "1-20 of N".                                                        |
| **Create guardian**                | From the child profile; name, relationship, phone number, email, NRIC/FIN.              |
| **Warn about duplicates**          | Warns when the phone number or email already exists; does not block.                    |
| **Link guardian to child**         | One guardian can be linked to several children (siblings).                              |
| **Unlink guardian**                | Removes the link to a child; the guardian record is kept.                               |
| **Edit guardian (staff)**          | Every change is recorded in the history.                                                |
| **Edit own details (parent, app)** | The parent updates own phone number, email and address in the Parents App.              |
| **Set primary contact**            | One primary contact per child.                                                          |
| **Set billing contact**            | One billing contact per child; used by Fees & Payments.                                 |
| **Send app invitation**            | Invitation to activate the Parents App; sent by email (default) or SMS.                 |
| **Resend invitation**              | For guardians who have not activated the app.                                           |
| **View history**                   | Who created, who edited, what changed.                                                  |
| **Export contact list**            | Excel of the filtered list.                                                             |

### 1.3 Health & allergies

*Prototype:* [<u>https://bba-sms-crm.lovable.app/records/allergies</u>](https://bba-sms-crm.lovable.app/records/allergies)

| **Feature**                                 | **Function**                                                                                                                                          |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View health list**                        | By centre and class: child name, allergies, medical conditions, severity.                                                                             |
| **Search**                                  | Child name, allergen.                                                                                                                                 |
| **Filter**                                  | Centre, class, type (allergy / medical condition / dietary).                                                                                          |
| **Sort**                                    | Severity, most severe first (default).                                                                                                                |
| **Paging**                                  | 20 / 50 / 100 rows; "1-20 of N".                                                                                                                      |
| **Submit health information (parent, app)** | Two parts: Required and Optional; allergies in 4 free-text fields plus a family note; severity per allergy.                                           |
| **Edit health information (parent, app)**   | Only the parent edits what the parent entered.                                                                                                        |
| **Upload health attachment (parent, app)**  | Medical letters or reports attached to the health record.                                                                                             |
| **Add staff note**                          | Staff add their own notes; parent entries are not changed.                                                                                            |
| **Show allergy alert**                      | Warning icon beside the child's name on the child list, attendance and the profile.                                                                   |
| **Restrict medical details**                | Only roles allowed in Roles & permissions see the details (default: Centre Director, Teacher, School Admin, HQ Admin); other roles see only the icon. |
| **Record height and weight**                | For one child, any age; no approval.                                                                                                                  |
| **Bulk record height and weight**           | One screen for a whole class.                                                                                                                         |
| **View growth chart**                       | Height and weight against percentile curves.                                                                                                          |
| **Upload vaccination record (parent, app)** | Vaccination record file.                                                                                                                              |
| **Send vaccination reminder**               | Automatic reminder to the parent before a vaccination is due.                                                                                         |
| **Export allergy list**                     | Per class, for the kitchen.                                                                                                                           |
| **Print allergy list**                      | Per class.                                                                                                                                            |
| **View history**                            | Parents and staff see who changed what and when.                                                                                                      |

### 1.4 Documents

*Prototype:* [<u>https://bba-sms-crm.lovable.app/records/documents</u>](https://bba-sms-crm.lovable.app/records/documents)

| **Feature**                       | **Function**                                                                    |
|-----------------------------------|---------------------------------------------------------------------------------|
| **View document list**            | Per child: document type, status, upload date.                                  |
| **Search**                        | Child name, document name.                                                      |
| **Filter**                        | Centre, document type, status (Missing / Pending review / Accepted / Rejected). |
| **Sort**                          | Newest first (default).                                                         |
| **Paging**                        | 20 / 50 / 100 rows; "1-20 of N".                                                |
| **Upload document (staff)**       | Choose the document type and upload the file.                                   |
| **Upload document (parent, app)** | The parent uploads missing or rejected documents.                               |
| **Accept document**               | Centre Director or School Admin; status becomes Accepted.                       |
| **Reject document**               | Reason required; status becomes Rejected and the parent is notified.            |
| **Replace document**              | A new file replaces the current one; earlier versions are kept.                 |
| **View document**                 | Open in the browser, including the signed registration form.                    |
| **Download document**             | PDF or the original file.                                                       |
| **Send document request**         | Asks one family to upload missing documents.                                    |
| **Bulk send document request**    | Asks several selected families at once.                                         |
| **Export missing-documents list** | Excel by centre and class.                                                      |
| **View history**                  | Versions, uploaded by, reviewed by, when.                                       |

### 1.5 Authorised pickup

*Prototype:* [<u>https://bba-sms-crm.lovable.app/records/pickup</u>](https://bba-sms-crm.lovable.app/records/pickup)

| **Feature**                            | **Function**                                                                                                         |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **View pickup list**                   | Per child: photo, name, relationship, phone number, status.                                                          |
| **Search**                             | Pickup person name, child name, phone number.                                                                        |
| **Filter**                             | Centre, status (Pending / Approved / Rejected / Removed).                                                            |
| **Sort**                               | Oldest first (default).                                                                                              |
| **Paging**                             | 20 / 50 / 100 rows; "1-20 of N".                                                                                     |
| **Add pickup person (parent, app)**    | Photo, full name, relationship, NRIC/FIN, phone number; accept the terms by tick; no limit on the number of persons. |
| **Notify centre of new request**       | Centre Director and School Admin see the pending request.                                                            |
| **Approve request**                    | Centre Director or School Admin.                                                                                     |
| **Reject request**                     | Reason required; the parent can add the person again.                                                                |
| **Bulk approve**                       | Approve several pending requests at once.                                                                            |
| **Notify parent of result**            | When a request is approved or rejected.                                                                              |
| **Remove pickup person (parent, app)** | No approval; takes effect at once.                                                                                   |
| **Notify centre of removal**           | Centre Director and School Admin are informed.                                                                       |
| **View pickup persons at pickup**      | Teachers see approved persons with photos on the child profile and the pickup screen.                                |
| **Export pickup list**                 | Per class.                                                                                                           |
| **View history**                       | Who added, approved, rejected or removed, and when.                                                                  |

### 1.6 Classes

*Prototype:* [<u>https://bba-sms-crm.lovable.app/classes</u>](https://bba-sms-crm.lovable.app/classes)

| **Feature**                  | **Function**                                                                                                                                    |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **View class list**          | Centre, level, class code (for example Nursery 1), class name (for example Mickey), school year, session, form teacher, size / maximum, status. |
| **Search**                   | Class code, class name, teacher.                                                                                                                |
| **Filter**                   | Centre, level, school year, session, status (Active / Closed).                                                                                  |
| **Sort**                     | Level, then class code (default).                                                                                                               |
| **Paging**                   | 20 / 50 / 100 rows.                                                                                                                             |
| **Create class**             | Level (only levels offered by the centre), class code, class name, school year, session, form teacher, assistant teachers, room, maximum size.  |
| **Edit class**               | Class name, teachers, room, maximum size; changes recorded in the history.                                                                      |
| **Close class**              | At the end of the year or when classes merge; history is kept.                                                                                  |
| **Assign children**          | Select several children with checkboxes; warns when the maximum size is exceeded.                                                               |
| **Move children**            | To another class with an effective date; infants move to playgroup at 18 months.                                                                |
| **Run annual promotion**     | Moves children to the next level and target class for the new school year, with a preview and untick option.                                    |
| **Assign teachers**          | Form teacher and assistant teachers; one teacher can teach several classes.                                                                     |
| **View class detail**        | Children, teachers, size, history.                                                                                                              |
| **View history**             | Who created, edited, assigned or moved children, and when.                                                                                      |
| **Export class list**        | Excel.                                                                                                                                          |
| **Export children by class** | Excel.                                                                                                                                          |

# 5. Business rules

## Child records

| **ID**         | **Rule**                                                                                                                                                                                           |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CHF-001** | A child profile is created automatically when the enrolment is confirmed. Manual creation needs 6 fields: full name, date of birth (or expected birth date), gender, centre, level and start date. |
| **BR-CHF-002** | A profile can be created for an unborn child. Documents, health information and authorised pickup are not required until the child is born.                                                        |
| **BR-CHF-003** | The School Admin is reminded to contact the family of an unborn child before the start date (default: 30 days before).                                                                             |
| **BR-CHF-004** | The system warns when a child with the same name and date of birth exists; it does not block.                                                                                                      |
| **BR-CHF-005** | Every edit of a child profile creates a change record with updated by, approved by, effective date and an optional attachment.                                                                     |
| **BR-CHF-006** | Child status (Enrolled, Temporary withdrawal, Withdrawn, Graduated) is changed only by Joining & leaving.                                                                                          |
| **BR-CHF-007** | Withdrawn and graduated children stay searchable.                                                                                                                                                  |
| **BR-CHF-008** | Children are never deleted.                                                                                                                                                                        |
| **BR-CHF-009** | NRIC is hidden in screens and exports for roles not allowed to see it.                                                                                                                             |
| **BR-CHF-010** | Consents are shown on the child profile read-only; they are managed in Communication › Surveys & consents.                                                                                         |

## Access scope

| **ID**         | **Rule**                                         |
|----------------|--------------------------------------------------|
| **BR-CHF-011** | HQ roles see children of all centres.            |
| **BR-CHF-012** | Centre staff see children of their own centre.   |
| **BR-CHF-013** | Teachers see children of their own classes only. |

## Families and guardians

| **ID**         | **Rule**                                                                                                                                  |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CHF-014** | A guardian can be linked to several children. Unlinking removes the link, not the guardian.                                               |
| **BR-CHF-015** | A guardian still linked to a child cannot be deleted.                                                                                     |
| **BR-CHF-016** | The system warns when a phone number or email already belongs to another guardian; it does not block.                                     |
| **BR-CHF-017** | Each child has one primary contact and one billing contact. Fees & Payments uses the billing contact.                                     |
| **BR-CHF-018** | Guardians who are not parents get no Parents App account by default. An account is created only on request and with the parent's consent. |
| **BR-CHF-019** | Parents App invitations are sent by email by default; the channel (email or SMS) is a setting.                                            |
| **BR-CHF-020** | Parents can edit their own contact details in the Parents App; staff edits are recorded in the history.                                   |

## Health and allergies

| **ID**         | **Rule**                                                                                                                                                              |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CHF-021** | Health information has a Required part and an Optional part. Allergies are entered in 4 free-text fields plus a family note.                                          |
| **BR-CHF-022** | Each allergy has a severity: Mild, Moderate or Severe (default scale, configurable by HQ Admin).                                                                      |
| **BR-CHF-023** | Only the parent changes what the parent entered. Staff add separate staff notes.                                                                                      |
| **BR-CHF-024** | A child with an allergy or medical condition shows a warning icon wherever the child's name appears in the child list, attendance and the profile.                    |
| **BR-CHF-025** | Only roles allowed in Roles & permissions see medical details (default: Centre Director, Teacher, School Admin, HQ Admin). Other roles see the icon only.             |
| **BR-CHF-026** | Height and weight are recorded directly by staff, with no approval.                                                                                                   |
| **BR-CHF-027** | Parents upload the vaccination record even when SingPass shows vaccinations as complete.                                                                              |
| **BR-CHF-028** | Vaccination reminders follow the national schedule set by HQ Admin and are sent before each due date (default: 14 days before).                                       |
| **BR-CHF-029** | The parent is the source of health information. When the parent changes allergy information, the Centre Director, School Admin and the child's teachers are notified. |

## Documents

| **ID**         | **Rule**                                                                                                                                       |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CHF-030** | HQ Admin sets the required document types per country and brand (for example birth certificate, vaccination record, signed registration form). |
| **BR-CHF-031** | A required document that has not been uploaded shows as Missing.                                                                               |
| **BR-CHF-032** | Document statuses are Missing, Pending review, Accepted and Rejected.                                                                          |
| **BR-CHF-033** | The Centre Director or School Admin reviews each uploaded document. Rejecting requires a reason.                                               |
| **BR-CHF-034** | A new upload replaces the current file; earlier versions are kept.                                                                             |
| **BR-CHF-035** | Documents are never deleted.                                                                                                                   |

## Authorised pickup

| **ID**         | **Rule**                                                                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CHF-036** | Parents add authorised pickup persons in the Parents App with photo, full name, relationship, NRIC/FIN and phone number. There is no limit on the number of persons. |
| **BR-CHF-037** | Each new person needs approval by the Centre Director or the School Admin. Rejecting requires a reason.                                                              |
| **BR-CHF-038** | Only Approved persons appear on the pickup list used by teachers.                                                                                                    |
| **BR-CHF-039** | A parent can remove a person at any time without approval; the centre is notified.                                                                                   |
| **BR-CHF-040** | A person who was rejected or removed can be added again as a new request.                                                                                            |
| **BR-CHF-041** | One-time pickup persons are not supported; every pickup person goes through approval.                                                                                |

## Classes

| **ID**         | **Rule**                                                                                                                                            |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CHF-042** | A class belongs to one centre and one level. A centre can create classes only for the levels that Organisation has turned on for the centre.        |
| **BR-CHF-043** | A class has a class code (for example Nursery 1) and a class name (for example Mickey). The class code is unique within the centre and school year. |
| **BR-CHF-044** | Who can create, edit and close classes is a permission in Roles & permissions (default: Centre Director and HQ Admin).                              |
| **BR-CHF-045** | The system warns when assigning children would exceed the maximum size; the user can continue.                                                      |
| **BR-CHF-046** | A class change takes an effective date. The child leaves the old class thread and joins the new one in Communication.                               |
| **BR-CHF-047** | Infants move to playgroup at 18 months.                                                                                                             |
| **BR-CHF-048** | Annual promotion moves children to the next level for the new school year. Children repeating a level are unticked by the user before confirming.   |
| **BR-CHF-049** | A class that has had children is closed, not deleted; its history is kept.                                                                          |
| **BR-CHF-050** | Organisation › Centres shows the same classes in a read-only Classes tab.                                                                           |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                | **Recipient**                                 | **Channel**            | **When**                                         |
|---------------------------------|-----------------------------------------------|------------------------|--------------------------------------------------|
| **Parents App invitation**      | Guardian                                      | Email (default) or SMS | When staff send or resend the invitation         |
| **Document request**            | Parent                                        | Push + in-app          | When staff send a request, one family or in bulk |
| **Document rejected**           | Parent                                        | Push + in-app          | When a document is rejected, with the reason     |
| **Vaccination reminder**        | Parent                                        | Push + in-app          | Before a vaccination is due                      |
| **Allergy information changed** | Centre Director, School Admin, class teachers | In-app                 | When the parent changes allergy information      |
| **New pickup request**          | Centre Director, School Admin                 | In-app (web)           | When a parent adds a pickup person               |
| **Pickup request result**       | Parent                                        | Push + in-app          | When the request is approved or rejected         |
| **Pickup person removed**       | Centre Director, School Admin                 | In-app (web)           | When a parent removes a pickup person            |
| **Unborn child start date**     | School Admin                                  | In-app (web)           | Before the start date of an unborn child         |

## 6.2 Documents

- Allergy list per class for the kitchen: printable and exportable.

- Child documents: uploaded files and the signed registration form, viewable and downloadable as PDF.

# 7. Reports & exports

| **Report**                | **Content**                                                     | **Used by**                                     |
|---------------------------|-----------------------------------------------------------------|-------------------------------------------------|
| **Child list**            | Filtered list of children with class, level and status          | Centre Director, School Admin, HQ               |
| **Guardian contact list** | Guardians with contact details, app status and billing contact  | School Admin, HQ                                |
| **Allergy list by class** | Children with allergies, conditions and severity per class      | Centre Director, School Admin, Teacher, kitchen |
| **Missing documents**     | Children with missing or rejected documents by centre and class | Centre Director, School Admin                   |
| **Pickup list by class**  | Approved pickup persons per child                               | Teacher, School Admin                           |
| **Class list**            | Classes with teachers, size and maximum                         | Centre Director, HQ                             |
| **Children by class**     | Children in each class                                          | Centre Director, School Admin, Teacher          |

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
<td><strong>AC-CHF-001</strong></td>
<td>Profile from enrolment</td>
<td>Given the enrolment of Emma Tan at centre A is confirmed,<br />
when the system processes the confirmation,<br />
then a child profile for Emma is created with her two guardians linked and status Enrolled.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-002</strong></td>
<td>Manual create</td>
<td>Given a School Admin creates a child without a date of birth,<br />
when the user saves,<br />
then the system does not save and marks date of birth as required.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-003</strong></td>
<td>Duplicate child</td>
<td>Given Ryan Lim born 3 March 2023 already exists,<br />
when a user creates another Ryan Lim born 3 March 2023,<br />
then the system warns about the existing profile and lets the user open it or continue.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-004</strong></td>
<td>Change record</td>
<td>Given a School Admin changes a child's programme from half day to full day effective 1 November 2026,<br />
when the user saves,<br />
then a change record shows the user, the approver, 1 November 2026 and any attachment.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-005</strong></td>
<td>Status not editable</td>
<td>Given a child is Enrolled,<br />
when a Centre Director opens the child profile,<br />
then there is no option to change the status; status changes only through Joining &amp; leaving.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-006</strong></td>
<td>Teacher scope</td>
<td>Given a teacher teaches Nursery 1 at centre A,<br />
when the teacher opens the child list,<br />
then only children of Nursery 1 are listed.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-007</strong></td>
<td>Search withdrawn child</td>
<td>Given Mia Wong was withdrawn in June 2026,<br />
when a user searches "mia",<br />
then Mia appears in the results with status Withdrawn.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-008</strong></td>
<td>Billing contact</td>
<td>Given a child has two guardians,<br />
when the School Admin sets the mother as billing contact,<br />
then the father stops being billing contact and Fees &amp; Payments uses the mother.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-009</strong></td>
<td>Parent-entered allergy</td>
<td>Given a parent entered "peanut, severe" in the Parents App,<br />
when a School Admin opens the health record,<br />
then the parent's entry is read-only and the School Admin can only add a staff note.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-010</strong></td>
<td>Medical details restricted</td>
<td>Given a child has a severe peanut allergy and HQ Finance is not allowed to see medical details,<br />
when an HQ Finance user opens the child list,<br />
then the warning icon is shown but the allergy details are not.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-011</strong></td>
<td>Bulk height and weight</td>
<td>Given class Nursery 1 has 18 children,<br />
when the teacher enters height and weight for 17 present children and saves,<br />
then 17 records are saved at once with no approval and each growth chart shows the new point.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-012</strong></td>
<td>Document rejected</td>
<td>Given a parent uploaded a blurred birth certificate,<br />
when the School Admin rejects it without a reason,<br />
then the system does not allow it until a reason is entered, then the status becomes Rejected and the parent is notified.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-013</strong></td>
<td>Document version</td>
<td>Given a birth certificate was rejected,<br />
when the parent uploads a new file,<br />
then the status becomes Pending review and the rejected file stays in the history.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-014</strong></td>
<td>Pickup approval</td>
<td>Given a parent adds the grandmother as a pickup person,<br />
when the Centre Director approves the request,<br />
then the parent is notified and teachers see the grandmother with her photo on the pickup list.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-015</strong></td>
<td>Pickup pending</td>
<td>Given a pickup request is Pending,<br />
when a teacher opens the pickup list of the child,<br />
then the pending person is not shown.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-016</strong></td>
<td>Pickup removal</td>
<td>Given the grandmother is an Approved pickup person,<br />
when the parent removes her in the Parents App,<br />
then she disappears from the pickup list at once and the Centre Director and School Admin are notified.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-017</strong></td>
<td>Level not offered</td>
<td>Given centre C offers only Nursery,<br />
when a Centre Director creates a class,<br />
then only Nursery can be selected as the level.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-018</strong></td>
<td>Class code unique</td>
<td>Given centre A has class Nursery 1 "Mickey" for 2027,<br />
when a user creates another Nursery 1 for 2027 at centre A,<br />
then the system blocks it and names the existing class.</td>
</tr>
<tr class="odd">
<td><strong>AC-CHF-019</strong></td>
<td>Over capacity</td>
<td>Given class Nursery 1 has a maximum of 20 and 20 children,<br />
when the School Admin assigns one more child,<br />
then the system warns that the maximum is exceeded and the user can continue.</td>
</tr>
<tr class="even">
<td><strong>AC-CHF-020</strong></td>
<td>Class change</td>
<td>Given Emma moves from Nursery 1 to Nursery 2 effective 1 November 2026,<br />
when the move is saved,<br />
then from 1 November Emma appears in Nursery 2 and her parents are in the Nursery 2 class thread instead of Nursery 1.</td>
</tr>
</tbody>
</table>
