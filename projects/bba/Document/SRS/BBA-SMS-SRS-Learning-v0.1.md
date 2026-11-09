Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Learning**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-LRN-NNN and acceptance criteria AC-LRN-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Learning module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes what the module must do so that HQ Curriculum, teachers and Centre Directors can share class moments, assess children and publish progress reports and portfolios to parents, and so that the Enrichment team can run enrichment classes and bill them each month without Taidii.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/learning. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Learning set-up by HQ: academic years and terms, rating scales, checklist templates, portfolio layouts, report frequency and release dates.

- Class updates: posting photos and videos, tagging, media consent checks, optional review before posting, recall.

- Gallery: albums built from class updates, retagging, downloads, recall.

- Progress reports: rating checklist objectives, comments, Centre Director approval, publishing to parents, recall, raw data export.

- Portfolios: building pages, photos and work samples, attached progress report, Centre Director approval, publishing, recall.

- Enrichment: classes, students in each class, attendance per session, monthly charges by class schedule and enrichment invoices sent to Fees & Payments.

- Learning overview: tasks waiting for each user.

- What parents see in the Parents App: class updates and photos of their own child and class, published progress reports and portfolios as PDF.

## 1.2 Not in Phase 1

- Lesson plans.

- Learning Management System (LMS), online quizzes and homework.

- Learning progress tracking for parents beyond published reports and portfolios.

- Resource library.

- Learning analytics dashboards (Phase 1 provides raw data export to Excel).

- Grammar check for portfolio and gallery text.

- Approving all progress reports of a class in one action.

- Downloading the progress reports of a whole class as one file.

- Scheduled publishing of portfolios.

- Creating or editing progress reports and portfolios on mobile (mobile is view only).

- Reminders to teachers to post photos, face recognition and per-child captions in the Gallery.

- Parent comments on class updates (parents can only react with a heart).

- Attendance data in progress reports.

- Enrichment: expression of interest, trial classes, make-up classes, rescheduling or cancelling sessions, enrolment or withdrawal through the Parents App, automatic emails, holiday camps for external children, revenue dashboards.

- Malaysia term-based enrichment billing will be detailed during sprint planning.

# 2. Who uses it

| **Role**                     | **What they do in this module**                                                                                                                                            |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HQ Curriculum**            | Sets up academic years, terms, rating scales, checklist templates, portfolio layouts and report schedules per brand; views learning data across centres; exports raw data. |
| **HQ Admin**                 | Has every permission in the module; configures review settings and roles.                                                                                                  |
| **Centre Director**          | Reviews class updates when review is switched on; starts portfolios; approves or returns progress reports and portfolios; publishes and recalls them.                      |
| **Teacher / Senior Teacher** | Posts class updates; rates objectives and writes comments; builds portfolios; submits to the Centre Director. A Senior Teacher can review class updates when delegated.    |
| **HQ Enrichment team**       | Creates and closes enrichment classes; adds and removes students; uploads student lists; reviews monthly charges and creates enrichment invoices.                          |
| **Enrichment trainer**       | Sees only the enrichment classes assigned to them; takes and edits attendance for their sessions.                                                                          |
| **HQ Finance**               | Bills and collects enrichment invoices in Fees & Payments.                                                                                                                 |
| **Parent (Parents App)**     | Views class updates and photos of their child and class; reacts with a heart; views published progress reports and portfolios as PDF.                                      |

# 3. Process overview

## P1. Learning set-up

1\. HQ Curriculum sets the academic year and terms for the brand.

2\. HQ Curriculum defines the rating scale and the report frequency and release dates.

3\. HQ Curriculum creates checklist templates per brand, level and language, or imports them from Excel.

4\. HQ Curriculum publishes each template to the selected centres; every class of that level uses it at once.

## P2. Class update

1\. A teacher posts photos or videos for a class and tags the class, children, learning domain and activity.

2\. The system blocks tagging any child without media consent.

3\. If review is switched on for the centre, the update goes to the Centre Director or a delegated Senior Teacher, who approves it or sends it back.

4\. The approved update is posted; parents of the tagged class or children are notified and can react with a heart.

5\. Photos are added to the class, child and tag albums in the Gallery.

6\. A posted update can be recalled; parents no longer see it.

## P3. Progress report

1\. On the entry start date, reports open for children who have attended for at least 3 months.

2\. Teachers rate each objective on the brand's scale and write comments; in a shared class, each teacher rates their own language domains.

3\. The teacher submits the report to the Centre Director.

4\. The Centre Director approves it or returns it with a comment.

5\. The Centre Director publishes it now or on the release date; the parent views the PDF in the Parents App.

## P4. Portfolio

1\. Each semester the Centre Director starts portfolios from the brand layout and assigns teachers.

2\. The teacher builds the pages, adds photos and work samples, and attaches the approved progress report.

3\. The teacher submits the portfolio to the Centre Director, who approves or returns it.

4\. The Centre Director publishes it; the parent views the PDF in the Parents App.

## P5. Enrichment class and students

1\. The HQ Enrichment team creates a class with its weekdays, time, trainer and fee per session.

2\. The team adds students one by one or by uploading a list; each student has a start date.

3\. The trainer takes attendance at every session.

4\. When a student leaves, the team enters an end date; a child withdrawn from the centre is ended automatically.

## P6. Enrichment monthly charges

1\. On the last day of the month the system counts, for each student and class, the scheduled sessions in the month between the start date and the end date.

2\. Each count is multiplied by the class fee per session; public holidays are still charged and absences are not deducted.

3\. The HQ Enrichment team reviews the preview per centre.

4\. The team creates one enrichment invoice per child covering all enrichment classes.

5\. The invoices go to Fees & Payments, where Finance bills and collects them like any other invoice.

# 4. Modules, sub-modules, features and functions

## 1. Overview

### 1.1 Learning overview

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning</u>](https://bba-sms-crm.lovable.app/learning)

| **Feature**               | **Function**                                                                                                                                                                                                         |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View "Waiting on you"** | Tasks for the user's role: class updates waiting for review, returned progress reports and portfolios, reports and portfolios waiting for approval, checklist templates still in Draft. Each opens the right screen. |
| **Filter**                | Centre, class.                                                                                                                                                                                                       |

## 2. Learning set-up

### 2.1 Learning setup

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/setup</u>](https://bba-sms-crm.lovable.app/learning/setup)

| **Feature**                           | **Function**                                                                                                                      |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Manage academic year**              | Per brand; the year starts on 1 January. Centres cannot edit it.                                                                  |
| **Manage terms**                      | Per brand; default 4 terms with start and end dates.                                                                              |
| **Create rating scale**               | Per brand; stars or levels, with a name for each level.                                                                           |
| **Edit rating scale**                 | Level names and order.                                                                                                            |
| **Set display of unrated objectives** | Per brand: show or hide objectives skipped with a remark in the parent PDF.                                                       |
| **View template list**                | Brand, level, language, version, status (Draft / Published).                                                                      |
| **Search**                            | Template name.                                                                                                                    |
| **Filter**                            | Brand, level, language, status.                                                                                                   |
| **Create checklist template**         | Brand, level, language; domains, optional sub-domains and objectives. Chinese is a separate domain, not a translation of English. |
| **Edit checklist template**           | Domains, sub-domains, objectives while Draft; editing a published template creates a new version.                                 |
| **Import template from Excel**        | Download sample, upload, row-by-row errors, then create a new template or overwrite a Draft.                                      |
| **Reorder objectives**                | Move an objective up or down within its domain.                                                                                   |
| **Publish template**                  | Draft to Published; choose the receiving centres; every class of the level uses it at once.                                       |
| **Manage portfolio layouts**          | Per brand; all classes of a brand use the same layout.                                                                            |
| **Set report frequency**              | Per brand: monthly, termly or by semester.                                                                                        |
| **Set entry and release dates**       | Separate entry start date, entry end date and release date for each report period.                                                |
| **View history**                      | Template versions, who, when.                                                                                                     |

## 3. Class updates

### 3.1 Class updates

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/updates</u>](https://bba-sms-crm.lovable.app/learning/updates)

| **Feature**                     | **Function**                                                                                                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View feed**                   | Posts per class and date, newest first.                                                                                                                   |
| **Search**                      | Caption text.                                                                                                                                             |
| **Filter**                      | Class, academic year, tag, posted by, status.                                                                                                             |
| **Post a moment**               | Photos and videos (no audio); video length limit is a setting (default: 2 minutes). Covers class and event updates; an event can include several classes. |
| **Tag class**                   | Default tag; one or more classes.                                                                                                                         |
| **Tag children**                | Optional; children of the selected classes.                                                                                                               |
| **Tag learning domain**         | From the brand's checklist domains.                                                                                                                       |
| **Tag activity or event**       | Pick from the list or create a new tag.                                                                                                                   |
| **Check media consent**         | Children without media consent cannot be tagged and are shown greyed out with the reason.                                                                 |
| **Submit for review**           | When review is switched on for the centre.                                                                                                                |
| **Approve update**              | Centre Director, or a Senior Teacher delegated by the Centre Director.                                                                                    |
| **Send back update**            | Comment required; the teacher edits and resubmits.                                                                                                        |
| **Set review per centre**       | On or off per centre (default: off in Singapore, on in Malaysia).                                                                                         |
| **Notify parents**              | In-app notification to parents of the tagged class or children when posted.                                                                               |
| **React with a heart (parent)** | Parents can react; they cannot comment.                                                                                                                   |
| **Recall update**               | Removes the post and its photos for all parents.                                                                                                          |
| **View history**                | Posted, reviewed, sent back, recalled, who, when.                                                                                                         |

## 4. Gallery

### 4.1 Gallery

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/gallery</u>](https://bba-sms-crm.lovable.app/learning/gallery)

| **Feature**           | **Function**                                                                                                                      |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **View albums**       | Built automatically from class updates: class album, album per child, album per tag. Albums belong to the class, not the teacher. |
| **Search**            | Child, tag, caption.                                                                                                              |
| **Filter**            | Class, academic year, learning domain, activity, date range.                                                                      |
| **Sort**              | Date, newest first by default.                                                                                                    |
| **Retag photo**       | Change class, child, domain or activity tags; media consent check applies.                                                        |
| **Bulk retag**        | Apply tags to several selected photos.                                                                                            |
| **Download photo**    | Single photo.                                                                                                                     |
| **Download selected** | Several selected photos as one file.                                                                                              |
| **Download all**      | All photos of an album; the download link expires after 7 days.                                                                   |
| **Recall photo**      | Removes the photo for all parents.                                                                                                |
| **Preview as parent** | Shows the albums a parent of the selected child sees.                                                                             |
| **Parent view**       | Parents see only photos of their own child and class.                                                                             |

## 5. Progress reports

### 5.1 Progress reports

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/reports</u>](https://bba-sms-crm.lovable.app/learning/reports)

| **Feature**                   | **Function**                                                                                                       |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **View report list**          | Child, class, period, teacher, status (Not started / Draft / Submitted / Returned / Approved / Published).         |
| **Search**                    | Child name.                                                                                                        |
| **Filter**                    | Class, period, status, teacher.                                                                                    |
| **Sort**                      | Child name A to Z by default.                                                                                      |
| **Paging**                    | 20 / 50 / 100 rows.                                                                                                |
| **Track progress**            | Per class: number of reports not started, in Draft, submitted, approved and published.                             |
| **Start report**              | Only for children who have attended for at least 3 months.                                                         |
| **Rate objectives**           | Each objective on the brand's scale.                                                                               |
| **Skip objective**            | Remark required, for example "Not taught yet".                                                                     |
| **Rate by language domain**   | In a class with several teachers, each teacher rates the domains assigned to them, for example English or Chinese. |
| **Rate whole class**          | Grid of children and objectives for quick rating.                                                                  |
| **Write comments**            | Per domain; the text box grows with the text, with no character limit; Chinese text is never cut.                  |
| **Write summary**             | Overall summary; no character limit.                                                                               |
| **Save draft**                |                                                                                                                    |
| **Submit to Centre Director** | All rated objectives or remarks completed.                                                                         |
| **Approve report**            | Centre Director only; one level.                                                                                   |
| **Return report**             | Comment required; the teacher edits and resubmits.                                                                 |
| **Show last editor**          | Shows who made the last edit, including Centre Director edits.                                                     |
| **Publish now**               | Parents are notified and see the PDF in the Parents App.                                                           |
| **Publish on release date**   | Approved reports are published automatically on the release date.                                                  |
| **Recall report**             | Parents no longer see it; the report goes back to Approved for editing and republishing.                           |
| **Send reminder to teachers** | Centre Director sends an in-app reminder to teachers with reports not yet submitted.                               |
| **Download PDF**              | One child's report.                                                                                                |
| **View child history**        | Past reports of the child, including those written by previous teachers.                                           |
| **Parent view**               | PDF in the Parents App, showing only the names and photos of the class teachers.                                   |
| **Export raw data**           | Ratings to Excel by class, level, centre or brand.                                                                 |

## 6. Portfolios

### 6.1 Portfolios

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/portfolios</u>](https://bba-sms-crm.lovable.app/learning/portfolios)

| **Feature**                         | **Function**                                                                                                 |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **View portfolio list**             | Child, class, semester, teacher, status (Not started / Draft / Submitted / Returned / Approved / Published). |
| **Search**                          | Child name.                                                                                                  |
| **Filter**                          | Class, semester, status.                                                                                     |
| **Paging**                          | 20 / 50 / 100 rows.                                                                                          |
| **Start portfolios**                | Centre Director, each semester, from the brand layout; assigns a teacher per class.                          |
| **Build pages**                     | Cover, About me (name, date of birth, class, height, weight), domain pages, Chinese page, Summary.           |
| **Add page**                        |                                                                                                              |
| **Remove page**                     |                                                                                                              |
| **Reorder pages**                   |                                                                                                              |
| **Add photos from Gallery**         | From the child's and class albums.                                                                           |
| **Upload photos and work samples**  | Images from the computer.                                                                                    |
| **Attach approved progress report** | Only an Approved or Published report of the same period.                                                     |
| **Upload external PDF portfolio**   | A ready-made PDF instead of built pages.                                                                     |
| **Save draft**                      |                                                                                                              |
| **Submit to Centre Director**       |                                                                                                              |
| **Approve portfolio**               | Centre Director only; one level.                                                                             |
| **Return portfolio**                | Comment required.                                                                                            |
| **Publish portfolio**               | Parents are notified and see the PDF in the Parents App.                                                     |
| **Recall portfolio**                | Parents no longer see it.                                                                                    |
| **Republish portfolio**             | After edits and approval.                                                                                    |
| **Download PDF**                    | One child's portfolio.                                                                                       |
| **View history**                    | Created, submitted, returned, approved, published, recalled, who, when.                                      |

## 7. Enrichment

### 7.1 Enrichment classes

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/enrichment</u>](https://bba-sms-crm.lovable.app/learning/enrichment)

| **Feature**               | **Function**                                                                                                                        |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **View class list**       | Class name, programme, centre, weekdays, time, trainer, fee per session, number of students, status (Active / Closed).              |
| **Search**                | Class name, programme.                                                                                                              |
| **Filter**                | Centre, brand, weekday, status.                                                                                                     |
| **Sort**                  | Class name A to Z by default.                                                                                                       |
| **Paging**                | 20 / 50 / 100 rows.                                                                                                                 |
| **Create class**          | Name, programme, centre, weekdays, start and end time, trainer, fee per session.                                                    |
| **View class detail**     | Class details, students, attendance history.                                                                                        |
| **Edit class**            | All details; a new fee applies only to months not yet invoiced.                                                                     |
| **Delete class**          | Only when the class has no attendance recorded.                                                                                     |
| **Close class**           | For a class with attendance; stops new sessions and students, keeps all history; active students get an end date of the close date. |
| **Restrict trainer view** | A trainer sees only the classes assigned to them.                                                                                   |
| **View history**          | Created, edited, closed, who, when.                                                                                                 |
| **Export**                | Class list.                                                                                                                         |

### 7.2 Enrichment students

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/enrichment</u>](https://bba-sms-crm.lovable.app/learning/enrichment)

| **Feature**                       | **Function**                                                                                                                                               |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View students in class**        | Child name, home centre, start date, end date, status (Active / Left).                                                                                     |
| **Search**                        | Child name.                                                                                                                                                |
| **Filter**                        | Status.                                                                                                                                                    |
| **Sort**                          | Child name A to Z by default.                                                                                                                              |
| **Add student**                   | Pick an existing child and enter the start date (required). A child can join several enrichment classes.                                                   |
| **Show on child profile**         | The child's enrichment classes appear on the child profile.                                                                                                |
| **Upload student list**           | Download template (child ID, class, start date), upload, row-by-row errors (child not found, already in class, missing start date), confirm before saving. |
| **Edit enrolment**                | Start date, end date.                                                                                                                                      |
| **Remove student**                | End date required; no charges after the end date; attendance and invoices are kept.                                                                        |
| **Auto-end on centre withdrawal** | When a child withdraws from the centre, all enrichment classes end on the child's last day.                                                                |
| **View history**                  | Added, edited, removed, who, when.                                                                                                                         |
| **Export**                        | Students of the class.                                                                                                                                     |

### 7.3 Enrichment attendance

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/enrichment</u>](https://bba-sms-crm.lovable.app/learning/enrichment)

| **Feature**                            | **Function**                                                                                 |
|----------------------------------------|----------------------------------------------------------------------------------------------|
| **View sessions**                      | Sessions of the month, generated from the class weekdays.                                    |
| **Take attendance**                    | Present or Absent for each active student (on or after the start date, before the end date). |
| **Mark all present**                   | Marks the whole class Present; the trainer then changes individual children.                 |
| **Edit attendance**                    | Reason required; does not change the amount charged.                                         |
| **Keep separate from main attendance** | Enrichment attendance is not counted in the child's centre attendance.                       |
| **Filter**                             | Class, month, centre.                                                                        |
| **View history**                       | Taken by, edited by, when, reason.                                                           |
| **Export register**                    | Per class and month.                                                                         |

### 7.4 Enrichment monthly charges

*Prototype:* [<u>https://bba-sms-crm.lovable.app/learning/enrichment</u>](https://bba-sms-crm.lovable.app/learning/enrichment)

| **Feature**                  | **Function**                                                                                                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Generate monthly charges** | On the last day of the month (setting), per child and class: scheduled sessions in the month from the start date to the end date, times the fee per session. |
| **Charge public holidays**   | Sessions on public holidays are charged.                                                                                                                     |
| **Ignore absences**          | Absences do not reduce the charge.                                                                                                                           |
| **Preview before invoicing** | Per centre: child, class, sessions charged, sessions attended (for reference), amount; drill down to the sessions charged.                                   |
| **Filter**                   | Centre, brand, month.                                                                                                                                        |
| **Create invoices**          | One enrichment invoice per child covering all enrichment classes, separate from the tuition invoice.                                                         |
| **Send to Fees & Payments**  | Invoices are created as Draft in Fees & Payments and follow the Draft to Billed flow; collected by PayNow, GIRO or CDA like other invoices.                  |
| **Block duplicate charges**  | A child, class and month can be invoiced only once.                                                                                                          |
| **Export**                   | Sessions and revenue by class, centre and brand.                                                                                                             |

# 5. Business rules

## Learning set-up

| **ID**         | **Rule**                                                                                                                                                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-LRN-001** | Academic years, terms, rating scales, checklist templates, portfolio layouts and report schedules are set per brand by HQ Curriculum. Centres and teachers cannot edit them. |
| **BR-LRN-002** | The academic year starts on 1 January and has 4 terms by default.                                                                                                            |
| **BR-LRN-003** | A checklist template belongs to one brand, one level and one language. Chinese is a separate domain with its own objectives.                                                 |
| **BR-LRN-004** | A published template applies at once to every class of its level in the selected centres. Editing it creates a new version; reports already started keep their version.      |
| **BR-LRN-005** | Report frequency is monthly, termly or by semester per brand. Each period has an entry start date, an entry end date and a release date.                                     |
| **BR-LRN-006** | All classes of a brand use the same portfolio layout.                                                                                                                        |

## Class updates and Gallery

| **ID**         | **Rule**                                                                                                                                                                             |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-LRN-007** | A class update contains photos and videos only. Audio is not supported. The video length limit is a setting (default: 2 minutes).                                                    |
| **BR-LRN-008** | Every class update is tagged with at least one class. Child, learning domain and activity tags are optional.                                                                         |
| **BR-LRN-009** | A child without media consent cannot be tagged in any update or photo.                                                                                                               |
| **BR-LRN-010** | Review before posting is switched on or off per centre (default: off in Singapore, on in Malaysia). When on, the Centre Director or a delegated Senior Teacher approves each update. |
| **BR-LRN-011** | Sending an update back requires a comment.                                                                                                                                           |
| **BR-LRN-012** | Parents can react with a heart. Parents cannot comment.                                                                                                                              |
| **BR-LRN-013** | Parents see only updates and photos tagged with their own child or class.                                                                                                            |
| **BR-LRN-014** | Albums belong to the class, not to the teacher, and stay available when a teacher leaves.                                                                                            |
| **BR-LRN-015** | A recalled update or photo disappears for all parents at once. Recall is recorded in the history.                                                                                    |
| **BR-LRN-016** | Bulk download links expire after 7 days.                                                                                                                                             |

## Progress reports

| **ID**         | **Rule**                                                                                                                                             |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-LRN-017** | A report can be started only for a child who has attended the centre for at least 3 months on the entry start date (default: 3 months, setting).     |
| **BR-LRN-018** | Each objective is rated on the brand's scale or skipped with a remark. Skipped objectives look different from rated ones in the parent PDF.          |
| **BR-LRN-019** | In a class with several teachers, each teacher rates the language domains assigned to them, for example one teacher for English and one for Chinese. |
| **BR-LRN-020** | Comment and summary boxes have no character limit.                                                                                                   |
| **BR-LRN-021** | Only the Centre Director approves reports. There is one approval level.                                                                              |
| **BR-LRN-022** | Returning a report requires a comment.                                                                                                               |
| **BR-LRN-023** | The system records the last editor of each report, including edits by the Centre Director.                                                           |
| **BR-LRN-024** | An approved report is published at once or automatically on the release date.                                                                        |
| **BR-LRN-025** | Parents view published reports as PDF in the Parents App. The PDF shows only the names and photos of the class teachers.                             |
| **BR-LRN-026** | A recalled report is hidden from parents and can be edited, approved and published again.                                                            |
| **BR-LRN-027** | A new teacher of the class can view the child's past reports.                                                                                        |
| **BR-LRN-028** | Raw rating data can be exported to Excel by class, level, centre or brand. There is no dashboard in Phase 1.                                         |

## Portfolios

| **ID**         | **Rule**                                                                                                     |
|----------------|--------------------------------------------------------------------------------------------------------------|
| **BR-LRN-029** | Portfolios are started by the Centre Director each semester from the brand layout.                           |
| **BR-LRN-030** | Only an Approved or Published progress report of the same period can be attached.                            |
| **BR-LRN-031** | Only the Centre Director approves portfolios. Returning a portfolio requires a comment.                      |
| **BR-LRN-032** | Portfolios are created and edited on the web only. The Parents App and staff mobile app show them read only. |

## Enrichment classes and students

| **ID**         | **Rule**                                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| **BR-LRN-033** | The HQ Enrichment team manages enrichment classes and students. A trainer sees only the classes assigned to them. |
| **BR-LRN-034** | A class can be deleted only if no attendance has been recorded. Otherwise it is closed and its history is kept.   |
| **BR-LRN-035** | Every student in an enrichment class has a start date. Removing a student requires an end date.                   |
| **BR-LRN-036** | A child can attend several enrichment classes. The classes appear on the child profile.                           |
| **BR-LRN-037** | When a child withdraws from the centre, all enrichment classes end on the child's last day.                       |
| **BR-LRN-038** | An uploaded student list is saved only after the user reviews the errors and confirms.                            |
| **BR-LRN-039** | Enrichment attendance is for tracking only. It is separate from centre attendance and never changes the charge.   |

## Enrichment charges

| **ID**         | **Rule**                                                                                                                                        |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-LRN-040** | Monthly charge per child and class = number of scheduled class sessions in the month between the start date and the end date × fee per session. |
| **BR-LRN-041** | A child who starts mid-month is charged for the scheduled sessions remaining from the start date.                                               |
| **BR-LRN-042** | Sessions on public holidays are charged. Absences are not deducted.                                                                             |
| **BR-LRN-043** | A fee change applies only to months not yet invoiced.                                                                                           |
| **BR-LRN-044** | Each child receives one enrichment invoice per month covering all enrichment classes. It is separate from the tuition invoice.                  |
| **BR-LRN-045** | Enrichment invoices are created in Fees & Payments and follow its billing, payment, reminder and month-end rules.                               |
| **BR-LRN-046** | A child, class and month can be invoiced only once.                                                                                             |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                    | **Recipient**                              | **Channel**               | **When**                                               |
|-------------------------------------|--------------------------------------------|---------------------------|--------------------------------------------------------|
| **New class update**                | Parents of the tagged class or children    | In-app                    | When an update is posted                               |
| **Class update waiting for review** | Centre Director / delegated Senior Teacher | In-app (web)              | When a teacher submits an update for review            |
| **Class update sent back**          | Teacher                                    | In-app (web)              | When the reviewer sends it back                        |
| **Progress report submitted**       | Centre Director                            | In-app (web)              | When a teacher submits a report                        |
| **Progress report returned**        | Teacher                                    | In-app (web)              | When the Centre Director returns a report              |
| **Report reminder**                 | Teachers with reports not submitted        | In-app (web)              | When the Centre Director sends a reminder              |
| **Progress report published**       | Parent                                     | In-app                    | When a report is published or reaches its release date |
| **Portfolio submitted**             | Centre Director                            | In-app (web)              | When a teacher submits a portfolio                     |
| **Portfolio returned**              | Teacher                                    | In-app (web)              | When the Centre Director returns a portfolio           |
| **Portfolio published**             | Parent                                     | In-app                    | When a portfolio is published or republished           |
| **Enrichment charges ready**        | HQ Enrichment team                         | In-app (web)              | When monthly charges are generated                     |
| **Enrichment invoice**              | Parent                                     | Per Fees & Payments rules | When the enrichment invoice is Billed                  |

## 6.2 Documents

- Progress report: PDF per child from the brand template, showing the class teachers' names and photos.

- Portfolio: PDF per child from the brand layout, or the uploaded external PDF.

- Checklist template import file and enrichment student upload file: Excel templates downloaded from the system.

- Enrichment invoice: created in Fees & Payments from its invoice template.

# 7. Reports & exports

| **Report**                          | **Content**                                                                | **Used by**                    |
|-------------------------------------|----------------------------------------------------------------------------|--------------------------------|
| **Progress report raw data**        | Ratings per child and objective by class, level, centre or brand           | HQ Curriculum, Centre Director |
| **Report completion**               | Reports not started, in Draft, submitted, approved and published per class | Centre Director, HQ Curriculum |
| **Enrichment class list**           | Classes with trainer, schedule, fee and number of students                 | HQ Enrichment team             |
| **Enrichment students**             | Students of a class with start and end dates                               | HQ Enrichment team             |
| **Enrichment attendance register**  | Attendance per session for a class and month                               | HQ Enrichment team, trainer    |
| **Enrichment sessions and revenue** | Sessions charged and amount by class, centre and brand for a month         | HQ Enrichment team, HQ Finance |

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
<td><strong>AC-LRN-001</strong></td>
<td>Publish template</td>
<td>Given HQ Curriculum has a Draft K1 English template for brand A,<br />
when it is published to centres X and Y,<br />
then every K1 class in centres X and Y uses the template at once and centre users cannot edit it.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-002</strong></td>
<td>Media consent</td>
<td>Given child Mia has no media consent,<br />
when a teacher tags Mia in a class update,<br />
then Mia cannot be selected and the reason is shown.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-003</strong></td>
<td>Review switched on</td>
<td>Given review is on for centre X,<br />
when a teacher posts an update,<br />
then the update waits for the Centre Director and parents see nothing until it is approved.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-004</strong></td>
<td>Review switched off</td>
<td>Given review is off for centre Y,<br />
when a teacher posts an update for class K1A,<br />
then the update is posted at once and parents of K1A are notified.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-005</strong></td>
<td>Parent reaction</td>
<td>Given a parent opens a posted update,<br />
when the parent looks for actions,<br />
then the parent can react with a heart and there is no comment box.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-006</strong></td>
<td>Recall update</td>
<td>Given an update was posted to class K1A by mistake,<br />
when the teacher recalls it,<br />
then the update and its photos disappear for all K1A parents and the recall is in the history.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-007</strong></td>
<td>Gallery visibility</td>
<td>Given a photo is tagged with class K1A only,<br />
when a parent of class K2B opens the Gallery,<br />
then the photo is not shown.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-008</strong></td>
<td>Three-month rule</td>
<td>Given child Leo started on 1 August and the entry start date is 1 October,<br />
when the teacher tries to start Leo's report,<br />
then the system does not allow it because Leo has attended for less than 3 months.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-009</strong></td>
<td>Shared class rating</td>
<td>Given class K2A has an English teacher and a Chinese teacher,<br />
when both open the same child's report,<br />
then each can rate only the domains assigned to them.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-010</strong></td>
<td>Skip with remark</td>
<td>Given a teacher skips an objective,<br />
when the teacher saves without a remark,<br />
then the system asks for a remark.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-011</strong></td>
<td>No character limit</td>
<td>Given a teacher writes a 4,000-character Chinese summary,<br />
when the report is published,<br />
then the full summary appears in the parent PDF without being cut.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-012</strong></td>
<td>Return report</td>
<td>Given a report is Submitted,<br />
when the Centre Director returns it without a comment,<br />
then the system does not allow it.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-013</strong></td>
<td>Scheduled release</td>
<td>Given a report is Approved and the release date is 15 November,<br />
when 15 November arrives,<br />
then the report is published and the parent is notified.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-014</strong></td>
<td>Parent PDF</td>
<td>Given a report is Published,<br />
when the parent opens it in the Parents App,<br />
then the PDF shows only the class teachers' names and photos.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-015</strong></td>
<td>Delete or close class</td>
<td>Given enrichment class Art Explorers has attendance recorded,<br />
when the Enrichment team tries to delete it,<br />
then deletion is blocked and the team can close the class instead.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-016</strong></td>
<td>Start date required</td>
<td>Given the Enrichment team adds a child to a class,<br />
when no start date is entered,<br />
then the child is not added.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-017</strong></td>
<td>Upload errors</td>
<td>Given an uploaded student list has one row with an unknown child ID,<br />
when the file is checked,<br />
then that row is listed with the error and nothing is saved until the user confirms.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-018</strong></td>
<td>Monthly charge</td>
<td>Given a class runs every Wednesday at SGD 30 per session, October 2026 has 4 Wednesdays and the child was absent once,<br />
when October charges are generated,<br />
then the child is charged 4 sessions, SGD 120.</td>
</tr>
<tr class="odd">
<td><strong>AC-LRN-019</strong></td>
<td>Mid-month start</td>
<td>Given a Wednesday class and a child with start date 15 October 2026,<br />
when October charges are generated,<br />
then the child is charged for the 2 remaining Wednesdays, 21 and 28 October.</td>
</tr>
<tr class="even">
<td><strong>AC-LRN-020</strong></td>
<td>One enrichment invoice</td>
<td>Given a child attends two enrichment classes,<br />
when the Enrichment team creates invoices for the month,<br />
then one Draft enrichment invoice with both classes is created in Fees &amp; Payments, separate from the tuition invoice.</td>
</tr>
</tbody>
</table>
