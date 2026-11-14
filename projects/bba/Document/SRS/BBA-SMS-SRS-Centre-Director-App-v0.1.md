Busy Bees Asia

School Management System (SMS) — Phase 2

**Software Requirements Specification**

**Centre Director App**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-CDP-NNN and acceptance criteria AC-CDP-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Centre Director App of the Busy Bees Asia School Management System (SMS). The Centre Director App is delivered in Phase 2.

In Phase 1 the Centre Director does all of this work on the SMS web. The app does not add a new process or new data. It is a mobile surface for the same records and the same rules as the SMS modules (Daily Operations, Children & Families, Joining & Leaving, Learning, Communication and Administration), so that a Centre Director can check the centre and make decisions from the floor, without waiting to reach a computer.

The app is a decision and oversight tool. Work that needs a desk, such as building portfolios, finance, set-up and exports, stays on the SMS web.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-centre-director.lovable.app. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Home: today's figures for the centre (checked in, checked out, still in the centre, absent, not in with no reason), items waiting for a decision, the calendar for today and the next three days, and a launcher of pinned features.

- Attendance oversight: today, this week and this month by class and bus; correcting and voiding records; deciding void requests.

- Approvals in one inbox: child leave, authorised pickup, withdrawals (retention and approval), class update photos, progress reports and attendance void requests.

- Children and classes: student list, centre-wide allergy list with staff notes, classes and teachers, staff, daily routines (view), portfolios (view only).

- Communication: announcements within the centre, messages (every thread of the centre, private chats with one family, bulk send), inquiries, survey and consent results.

- Learning: class updates and the photo gallery (view, review, recall), progress report review, editing and publishing.

- Calendar and centre log for the centre.

- Centre settings the Centre Director is allowed to change: extra permissions for centre staff and the photo review switch.

- Push notifications to the Centre Director for items that need attention.

## 1.2 Not in Phase 1

- Taking attendance (check in, check out, temperature) in this app. Attendance is taken once, on the Attendance app at the gate or on the SMS web.

- Creating, editing or approving portfolios (SMS web only; the app shows portfolios read only).

- Creating progress reports and managing report templates (SMS web and Teacher App).

- Creating or editing surveys and consent forms, and exporting their results (SMS web only).

- Exports, printing and report downloads of any kind (SMS web only).

- Fees, invoices, payments, refunds and deposits.

- Locking the last day, recording Form 3 and other admin steps of joining and leaving (SMS web only).

- Set-up work: classes and class changes, staff records and class assignments, bus routes, calendar import, approval routes, roles and organisation settings (SMS web only).

- Chat between staff members, including Centre Director and teacher.

- Seeing or acting on another centre's children, staff or records.

- Deadlines, scores, targets or service levels that Busy Bees has not defined.

- Staff attendance, staff leave, rosters and relief cover.

- Parent-teacher conference slot booking.

- Who reacted to or viewed a photo or album.

- Email delivery of announcements (the SMS sends push and in-app notifications only).

# 2. Who uses it

| **Role**                                  | **What they do in this module**                                                                                                                                                                                                                                                       |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Centre Director**                       | Main user. Sees only their own centre. Checks the centre's status, decides every approval routed to the Centre Director, corrects and voids attendance, communicates with families, posts announcements, keeps the calendar and centre log, grants extra permissions to centre staff. |
| **Senior Teacher with extra permission**  | Acts on the permissions the Centre Director granted (approve leave, approve class update photos, void attendance) in the Teacher App or on the SMS web. Does not use this app.                                                                                                        |
| **Teacher**                               | Sends progress reports and class updates for review; requests attendance voids from the Attendance app or the Teacher App; receives the Centre Director's decisions. Does not use this app.                                                                                           |
| **Centre Admin / School Admin**           | Works on the SMS web on the same records (for example authorised pickup approval, locking the last day). Sees decisions made in the app.                                                                                                                                              |
| **District Manager / Operations Manager** | Approves short-notice and mid-month withdrawals routed to them on the SMS web; sees the Centre Director's retention record.                                                                                                                                                           |
| **Parent (Parents App)**                  | Sends leave, pickup and withdrawal requests and inquiries; receives decisions, announcements and messages.                                                                                                                                                                            |
| **HQ Admin**                              | Configures approval routes, permissions, settings and categories on the SMS web. Has every permission and is never limited in scope.                                                                                                                                                  |

# 3. Process overview

## P1. Morning check of the centre

1\. The Centre Director opens Home before entering the centre.

2\. Home shows today's figures: checked in of expected, checked out, still in the centre, absent and not in with no reason from the family.

3\. The Centre Director taps a figure to see the list of children behind it, by class.

4\. The Centre Director opens "Waiting for you" and today's calendar, and follows up children not in with no reason.

## P2. Deciding an approval

1\. A request arrives (leave, pickup, withdrawal, class update photos, progress report or void request) and the Centre Director receives a push notification.

2\. The Centre Director opens it from Home or Approvals and sees everything needed to decide, including what happens next.

3\. The Centre Director approves, or declines or returns it with a reason.

4\. The requester (parent or staff member) is notified and the decision is recorded with who and when.

## P3. Withdrawal with retention

1\. A parent submits a withdrawal in the Parents App; the Centre Director is notified.

2\. The Centre Director talks to the family and records the retention attempt (date, outcome, notes).

3\. If the family stays, the Centre Director closes the request as retained and the parent is notified.

4\. If the family leaves, the admin locks the last day on the SMS web; the system compares the notice given with the notice required.

5\. A withdrawal with enough notice comes to the Centre Director to approve; a short-notice or mid-month withdrawal goes to the approver set in Approval routes.

## P4. Correcting attendance

1\. The Centre Director finds a wrong record in Attendance, or a teacher sends a void request from the Attendance app.

2\. The Centre Director corrects the time, or voids the record with a reason after a warning that the parent may already have seen it.

3\. For a void request, the Centre Director voids the record or rejects the request with a reason.

4\. The record keeps an audit trail: who requested, who acted, when and why.

## P5. Progress report review

1\. A teacher submits a progress report from the Teacher App or the SMS web.

2\. The Centre Director opens it and sees, per learning domain, the objectives rated, the objectives skipped with their remarks, and the comments.

3\. The Centre Director approves and chooses to publish now or on the release date, or returns it with a comment.

4\. Parents are notified when the report is published.

## P6. Sharing extra permissions

1\. The Centre Director opens Who can approve and picks a staff member who currently works at the centre.

2\. The Centre Director grants approve leave, approve class update photos or void attendance, with a reason and an optional end date.

3\. The staff member is notified and can act on that permission in the Teacher App or the SMS web.

4\. The permission ends when the Centre Director revokes it or on its end date; every change is logged.

## P7. Daily centre log

1\. During the day, the Centre Director or a staff member adds centre log entries (Incident, Accident, Deviation, Menu).

2\. When nothing happened, one "Nothing to report" entry closes the day.

3\. The Centre Director reads each entry and marks it as read.

# 4. Modules, sub-modules, features and functions

## 1. Home

### 1.1 Home

*Prototype:* [<u>https://bba-centre-director.lovable.app/</u>](https://bba-centre-director.lovable.app/)

| **Feature**                       | **Function**                                                                                         |
|-----------------------------------|------------------------------------------------------------------------------------------------------|
| **View "Waiting for you"**        | Every item waiting for the Centre Director's decision, oldest first; each opens the item in one tap. |
| **View count waiting**            | Total number of items waiting; opens Approvals.                                                      |
| **View checked in**               | Children checked in of the number expected today.                                                    |
| **View checked out**              | Children checked in today who have gone home.                                                        |
| **View still in the centre**      | Children checked in and not yet checked out.                                                         |
| **View absent**                   | Children marked absent or on leave today.                                                            |
| **View not in, nothing reported** | Children not checked in and with no leave or absence reason; highlighted.                            |
| **Open list from a figure**       | Every figure opens the list of children behind it, with their class.                                 |
| **View today's calendar**         | Centre events of today.                                                                              |
| **View next three days**          | Centre events of the next three days, grouped by day.                                                |
| **View no attendance this month** | Count of children with no attendance day this month; opens the list.                                 |
| **View open surveys**             | Surveys and consents still waiting for responses; opens Survey & Consent.                            |
| **Open pinned feature**           | Tiles for the pinned features.                                                                       |
| **Pin feature**                   | From the full feature list; between 4 and 8 features.                                                |
| **Unpin feature**                 | At least 4 features stay pinned.                                                                     |
| **Reset pinned features**         | Back to the default set (Attendance, Approvals, Messages, Calendar, Student list, Routines).         |
| **Open More**                     | All features of the app and the list of work that stays on the SMS web.                              |

## 2. Attendance

### 2.1 Attendance today

*Prototype:* [<u>https://bba-centre-director.lovable.app/attendance</u>](https://bba-centre-director.lovable.app/attendance)

| **Feature**                       | **Function**                                                                                                                              |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **View centre figures**           | Checked in of expected, still in the centre, checked out, not yet in, absent, enrolled.                                                   |
| **Open list from a figure**       | Children behind each figure, with their class.                                                                                            |
| **View by class**                 | Per class: level and class name, teachers, checked in of expected, checked out, still in.                                                 |
| **Filter**                        | Class, bus service.                                                                                                                       |
| **Open class**                    | Children of the class with status, check-in and check-out times, the adult who brought or collected them, photo and temperature readings. |
| **View child attendance detail**  | All events of the day for one child, including every temperature reading and the late flag.                                               |
| **View allergy alert**            | Warning icon beside children with an allergy or medical condition.                                                                        |
| **View not in, nothing reported** | Children not in with no reason from the family; each opens the class.                                                                     |
| **View fever flags**              | Readings at or above the fever threshold, highlighted.                                                                                    |

### 2.2 This week and this month

*Prototype:* [<u>https://bba-centre-director.lovable.app/attendance</u>](https://bba-centre-director.lovable.app/attendance)

| **Feature**                       | **Function**                                         |
|-----------------------------------|------------------------------------------------------|
| **View attendance by day**        | Children present each day of the current week.       |
| **View no attendance this month** | Children with no attendance day in the month so far. |
| **View days attended**            | Days attended this month per child, fewest first.    |
| **Filter**                        | Class.                                               |

### 2.3 Attendance corrections

*Prototype:* [<u>https://bba-centre-director.lovable.app/attendance</u>](https://bba-centre-director.lovable.app/attendance)

| **Feature**                | **Function**                                                                            |
|----------------------------|-----------------------------------------------------------------------------------------|
| **Correct check-in time**  | Reason required; the original time is kept in history.                                  |
| **Correct check-out time** | Reason required; the original time is kept in history.                                  |
| **Mark absent**            | For a child who did not come; reason optional.                                          |
| **Void record**            | Reason required; a warning first says that the parent may already have seen the record. |
| **View void requests**     | Requests sent by teachers from the Attendance app; also shown in Approvals.             |
| **Void from a request**    | Voids the record; the request and the void are recorded as two separate events.         |
| **Reject void request**    | Reason required; the requester is notified.                                             |
| **View corrections log**   | Child, class, record, what changed, requested by, done by, when, why.                   |

## 3. Approvals

### 3.1 Approvals inbox

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**             | **Function**                                                                                     |
|-------------------------|--------------------------------------------------------------------------------------------------|
| **View waiting items**  | Type, child or staff member, class, submitted date; oldest first.                                |
| **Filter**              | Type (Leave, Authorised pickup, Withdrawal, Class update photos, Progress report, Void request). |
| **View decided items**  | Approved, declined and closed items with who decided and when.                                   |
| **View count per type** | Number of waiting items per type.                                                                |
| **Open item**           | Detail screen with all the information needed to decide and what happens after the decision.     |

### 3.2 Child leave

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**            | **Function**                                                  |
|------------------------|---------------------------------------------------------------|
| **View leave request** | Child, type (Personal / Medical), dates, reason, attachment.  |
| **Approve leave**      | The days show On leave in attendance; the parent is notified. |
| **Reject leave**       | Reason required; the parent is notified.                      |

### 3.3 Authorised pickup

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**               | **Function**                                                                               |
|---------------------------|--------------------------------------------------------------------------------------------|
| **View pickup request**   | Photo, full name, relationship, NRIC/FIN (masked), phone number, child.                    |
| **Approve pickup person** | The person is added to the approved pickup list used at check out; the parent is notified. |
| **Reject pickup person**  | Reason required; the parent can add the person again as a new request.                     |
| **View removal notice**   | A parent's removal of a pickup person, shown for information; no decision needed.          |

### 3.4 Withdrawals

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**                  | **Function**                                                                                                              |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **View withdrawal**          | Child, reason, requested last day, locked last day, notice given, notice required, status, approver from Approval routes. |
| **View family balance**      | Outstanding amount of the whole family, including siblings.                                                               |
| **Record retention attempt** | Date, outcome and notes.                                                                                                  |
| **Close as retained**        | The request ends, the child stays active and the parent is notified.                                                      |
| **Approve withdrawal**       | When notice is enough and the last day is the calendar month-end; records who and when.                                   |
| **Reject withdrawal**        | Reason required; the request returns to the admin.                                                                        |
| **View approval route**      | Shows who decides when the Centre Director is not the approver, for example the District Manager.                         |

### 3.5 Class update photos

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**                | **Function**                                                                                   |
|----------------------------|------------------------------------------------------------------------------------------------|
| **View update for review** | Photos and videos, caption, class, tagged children, learning domain and event tags, posted by. |
| **Approve update**         | The update reaches the parents of the tagged class or children.                                |
| **Send back update**       | Comment required; the teacher edits and resubmits.                                             |

### 3.6 Progress reports

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**                             | **Function**                                                                                                                 |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **View report for review**              | Per learning domain: objectives rated out of total, skipped objectives with remarks, comments and summary; last editor.      |
| **Edit report**                         | The Centre Director can correct ratings, comments and the summary before approving; the change is recorded as the last edit. |
| **Approve and publish now**             | Parents are notified and see the PDF in the Parents App.                                                                     |
| **Approve and publish on release date** | The report is published automatically on the release date of the period.                                                     |
| **Return report**                       | Comment required; the teacher edits and resubmits.                                                                           |

### 3.7 Void requests

*Prototype:* [<u>https://bba-centre-director.lovable.app/approvals</u>](https://bba-centre-director.lovable.app/approvals)

| **Feature**           | **Function**                                                |
|-----------------------|-------------------------------------------------------------|
| **View void request** | Child, record, requested by, reason.                        |
| **Void record**       | Records who voided and when, separately from who requested. |
| **Reject request**    | Reason required; the requester is notified.                 |

## 4. Children and classes

### 4.1 Student list

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/students</u>](https://bba-centre-director.lovable.app/more/students)

| **Feature**                | **Function**                                                                  |
|----------------------------|-------------------------------------------------------------------------------|
| **View enrolled children** | Grouped by class, with a count.                                               |
| **View waiting list**      | Children with a place held who have not started, with a count.                |
| **Search**                 | Child name.                                                                   |
| **Filter**                 | Level, class.                                                                 |
| **View child summary**     | Class, guardians and contact numbers, approved pickup persons, allergy alert. |

### 4.2 Allergies

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/allergies</u>](https://bba-centre-director.lovable.app/more/allergies)

| **Feature**                  | **Function**                                                                                            |
|------------------------------|---------------------------------------------------------------------------------------------------------|
| **View centre allergy list** | Every child of the centre with an allergy or medical condition: allergies, conditions, severity, class. |
| **Search**                   | Child name, allergen.                                                                                   |
| **Filter**                   | Class, type (allergy / medical condition / dietary).                                                    |
| **Sort**                     | Severity, most severe first (default).                                                                  |
| **View child health record** | The family's entries (read only) and staff notes, shown separately.                                     |
| **Add staff note**           | Text; records author, date and the app used.                                                            |
| **Edit own staff note**      | Changes are kept in history.                                                                            |

### 4.3 Classes and teachers

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/classes</u>](https://bba-centre-director.lovable.app/more/classes)

| **Feature**      | **Function**                                                             |
|------------------|--------------------------------------------------------------------------|
| **View classes** | Level, class name, head teacher, assistant teachers, number of children. |
| **Open class**   | Children of the class and today's attendance.                            |

### 4.4 Staff

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/staff</u>](https://bba-centre-director.lovable.app/more/staff)

| **Feature**           | **Function**                                              |
|-----------------------|-----------------------------------------------------------|
| **View staff list**   | Name, role, classes, working status.                      |
| **Search**            | Staff name.                                               |
| **View staff record** | Role, classes and the extra permissions the person holds. |

### 4.5 Routines

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/routines</u>](https://bba-centre-director.lovable.app/more/routines)

| **Feature**             | **Function**                                                                                |
|-------------------------|---------------------------------------------------------------------------------------------|
| **View class routines** | Today's routines per child of a class, with required items missing.                         |
| **View child routines** | Meals, milk, nap, nappy and toilet, mood, note from home; who recorded each entry and when. |
| **Filter**              | Class, date.                                                                                |

### 4.6 Portfolio

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/portfolio</u>](https://bba-centre-director.lovable.app/more/portfolio)

| **Feature**             | **Function**                                       |
|-------------------------|----------------------------------------------------|
| **View portfolio list** | Child, class, semester, status.                    |
| **Search**              | Child name.                                        |
| **Filter**              | Class, semester.                                   |
| **Open portfolio**      | Published or approved portfolio as PDF, read only. |

## 5. Communication

### 5.1 Announcements

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/announcements</u>](https://bba-centre-director.lovable.app/more/announcements)

| **Feature**                     | **Function**                                                                                   |
|---------------------------------|------------------------------------------------------------------------------------------------|
| **View announcement list**      | Title, recipient type, audience, category, posted by, date, status, read count.                |
| **Search**                      | Title.                                                                                         |
| **Filter**                      | Recipient type, status (Draft / Scheduled / Sent / Recalled).                                  |
| **Create announcement**         | Title, content, category, attachments. Only with the "Create announcement" permission.         |
| **Select recipient type**       | Parents or Staff.                                                                              |
| **Select audience**             | Whole centre, level or class of the Centre Director's centre; for staff, the centre or a role. |
| **Attach files**                | Images and documents.                                                                          |
| **Require acknowledgement**     | Optional.                                                                                      |
| **Link to a survey or consent** | Adds a button that opens the form.                                                             |
| **Save draft**                  | Keeps the announcement as Draft.                                                               |
| **Schedule send**               | Date and time; can be edited or cancelled until sent.                                          |
| **Publish**                     | Sends now with a push notification.                                                            |
| **Edit announcement**           | After publishing; an "Edited" label is shown; "Notify recipients again" option (default: off). |
| **Recall announcement**         | Removes it from the Parents App and staff views; the record is kept.                           |
| **Track read and acknowledged** | Counts and the list of who has not read or acknowledged.                                       |
| **Send reminder**               | To recipients who have not read or acknowledged.                                               |

### 5.2 Messages

*Prototype:* [<u>https://bba-centre-director.lovable.app/messages</u>](https://bba-centre-director.lovable.app/messages)

| **Feature**                           | **Function**                                                                                                                        |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **View conversations**                | Every thread of the centre: class threads, private threads and groups, with last message, unread mark and the people in the thread. |
| **Search**                            | Parent name, child name, message text.                                                                                              |
| **Filter**                            | Class, thread type (Class / Private / Group), Read / Unread, Unanswered.                                                            |
| **Sort**                              | Latest message first (default) or longest unanswered first.                                                                         |
| **View Unanswered mark**              | "Unanswered N days" when the last message is from a parent and no staff reply has been sent for 2 days (setting).                   |
| **Open thread**                       | Full history; opening marks the messages as read on every device.                                                                   |
| **Reply in thread**                   | Text in a class, private or group thread.                                                                                           |
| **Send attachment**                   | Images, videos and documents within the size limits.                                                                                |
| **Recall own message**                | Within 15 minutes (setting); the thread shows "Message removed".                                                                    |
| **Start private chat**                | With one family, chosen by child; both parents chosen by default, one can be unticked; teachers are not included.                   |
| **Bulk send to families**             | Choose children by class or by family, review exactly who will receive it, then send; each family receives it in its own thread.    |
| **Fold bulk send**                    | A bulk send shows as one line ("Sent to 40 families") until a parent replies.                                                       |
| **Group parents in one conversation** | Only with the "Group parents in one conversation" permission; a title is required and every member sees who is in it.               |
| **View archived threads**             | Read-only threads of previous classes.                                                                                              |

### 5.3 Inquiries

*Prototype:* [<u>https://bba-centre-director.lovable.app/messages</u>](https://bba-centre-director.lovable.app/messages)

| **Feature**                   | **Function**                                                                            |
|-------------------------------|-----------------------------------------------------------------------------------------|
| **View inquiry list**         | Subject, child, category, status, assignee by name and role, waiting time.              |
| **Search**                    | Subject, child name, parent name.                                                       |
| **Filter**                    | Status (Open / In progress / Closed), category, assignee.                               |
| **Sort**                      | Longest waiting first (default).                                                        |
| **Open inquiry**              | Details, attachments, replies, assignee, history.                                       |
| **Reply**                     | Text and attachments; the parent is notified.                                           |
| **Change status**             | Open, In progress, Closed.                                                              |
| **Reassign**                  | To a staff member of the centre; only with the "Reassign inquiries" permission; logged. |
| **View reassigned inquiries** | Inquiries passed to a teacher leave the Centre Director's list and stay readable.       |

### 5.4 Survey & Consent

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/survey</u>](https://bba-centre-director.lovable.app/more/survey)

| **Feature**                         | **Function**                                                                                                                    |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **View survey and consent list**    | Survey tab (default) and Consent tab: title, audience, deadline, status, response rate.                                         |
| **Filter**                          | Status (Open / Closed), class.                                                                                                  |
| **View responses**                  | Responded and not responded, per class.                                                                                         |
| **Show only who has not responded** | One tap filter.                                                                                                                 |
| **View results**                    | Yes / no and choice answers as counts and shares; text answers with child and class; consent responses with signature and date. |
| **Send reminder**                   | To parents who have not responded.                                                                                              |
| **Close early**                     | Answers received are kept.                                                                                                      |

## 6. Learning

### 6.1 Class updates

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/class-updates</u>](https://bba-centre-director.lovable.app/more/class-updates)

| **Feature**       | **Function**                                                                    |
|-------------------|---------------------------------------------------------------------------------|
| **View feed**     | Updates of the centre per class and date, newest first, with review status.     |
| **Filter**        | Class, status, posted by.                                                       |
| **Open update**   | Photos, videos, caption, tags, posted by, review history.                       |
| **Recall update** | Removes the update and its photos for all parents at once; recorded in history. |

### 6.2 Photo gallery

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/gallery</u>](https://bba-centre-director.lovable.app/more/gallery)

| **Feature**                     | **Function**                              |
|---------------------------------|-------------------------------------------|
| **View class albums**           | One album per class, always present.      |
| **View child albums**           | Only photos the child is tagged in.       |
| **View learning domain albums** | Photos grouped by learning domain tag.    |
| **View event albums**           | Photos grouped by event or activity tag.  |
| **Filter**                      | Class, child, learning domain, event tag. |

## 7. Calendar and centre log

### 7.1 Calendar

*Prototype:* [<u>https://bba-centre-director.lovable.app/calendar</u>](https://bba-centre-director.lovable.app/calendar)

| **Feature**                                | **Function**                                                                                                                                                                                      |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View calendar**                          | Month view and list of entries for the selected day.                                                                                                                                              |
| **Switch view**                            | Events or Centre log, on the same screen.                                                                                                                                                         |
| **Filter**                                 | Event type, audience.                                                                                                                                                                             |
| **Create event**                           | Type (Event, Centre closure, Fire drill, Parent-teacher conference, Learning journey, Excursion, Other), title, date and time, classes, audience (staff only, or staff and parents), description. |
| **Edit event**                             | Any field until the event date.                                                                                                                                                                   |
| **Cancel event**                           | Reason required; parents who could see it are notified.                                                                                                                                           |
| **View birthdays**                         | Created automatically from each child's date of birth.                                                                                                                                            |
| **View public holidays and school visits** | Created automatically.                                                                                                                                                                            |
| **View allergy warning**                   | Birthday and food events show the allergies of the children in the class.                                                                                                                         |

### 7.2 Centre log

*Prototype:* [<u>https://bba-centre-director.lovable.app/calendar</u>](https://bba-centre-director.lovable.app/calendar)

| **Feature**                    | **Function**                                                                                                                              |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **View log**                   | Entries of the centre by date: type, category, time, author, read status.                                                                 |
| **Filter**                     | Type, date, read status.                                                                                                                  |
| **Create entry**               | Type (Incident, Accident, Deviation, Menu), category, date and time, children involved (optional), description, photo or file (optional). |
| **Answer category prompts**    | Each category shows its prompt questions.                                                                                                 |
| **Record "Nothing to report"** | One entry that closes the day.                                                                                                            |
| **View missing day flag**      | A day with no entry is flagged.                                                                                                           |
| **Edit entry**                 | Every edit is kept in history and shown on the entry.                                                                                     |
| **Mark as read**               | The Centre Director acknowledges each entry; there is no approval.                                                                        |

## 8. Centre settings

### 8.1 Who can approve

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/approvers</u>](https://bba-centre-director.lovable.app/more/approvers)

| **Feature**                  | **Function**                                                                                                                                          |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View granted permissions** | Staff member, permission, granted by, start date, end date, status (Active / Expired / Revoked).                                                      |
| **Grant permission**         | Approve leave, approve class update photos or void attendance, to a staff member currently working at the centre; reason required; end date optional. |
| **Show void warning**        | Explains what voiding does before the void permission is granted.                                                                                     |
| **Revoke permission**        | Takes effect immediately.                                                                                                                             |
| **Auto-expire**              | The permission ends on its end date.                                                                                                                  |
| **Notify staff member**      | When a permission is granted, revoked or expires.                                                                                                     |
| **View permission log**      | Every grant, revoke and expiry in plain words, with who and when.                                                                                     |

### 8.2 Photo review

*Prototype:* [<u>https://bba-centre-director.lovable.app/more/photo-approval</u>](https://bba-centre-director.lovable.app/more/photo-approval)

| **Feature**                   | **Function**                                                                                                |
|-------------------------------|-------------------------------------------------------------------------------------------------------------|
| **View photo review setting** | On or off for the centre, with what happens to a photo in each case.                                        |
| **Switch photo review on**    | Only when the Centre Director is granted this centre setting; confirmation required; logged.                |
| **Switch photo review off**   | Confirmation required; logged.                                                                              |
| **View reviewers**            | Staff who hold the approve class update photos permission.                                                  |
| **Show missing reviewer**     | When review is on and only the Centre Director can review, the screen says so and links to Who can approve. |

### 8.3 Notifications

*Prototype:* [<u>https://bba-centre-director.lovable.app/</u>](https://bba-centre-director.lovable.app/)

| **Feature**                   | **Function**                                                     |
|-------------------------------|------------------------------------------------------------------|
| **Receive push notification** | For the events listed in Section 7; each opens the exact record. |
| **View notification list**    | All notifications, newest first, with unread count.              |

# 5. Business rules

## Scope and access

| **ID**         | **Rule**                                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-001** | The Centre Director App is delivered in Phase 2. In Phase 1 the Centre Director does the same work on the SMS web.                                                            |
| **BR-CDP-002** | The app uses the same records, statuses, permissions and approval routes as the SMS web. A change made in the app is visible on the SMS web at once, and the other way round. |
| **BR-CDP-003** | The Centre Director sees and acts on their own centre only.                                                                                                                   |
| **BR-CDP-004** | The app shows a feature only when the user holds the matching permission in Roles & permissions.                                                                              |
| **BR-CDP-005** | Creating portfolios, finance, set-up and exports stay on the SMS web. The app lists them under More as web-only work.                                                         |
| **BR-CDP-006** | The app shows no deadline, score, timer or target that Busy Bees has not defined.                                                                                             |
| **BR-CDP-007** | Every decision, correction, void and permission change is recorded with who, when and the reason where one is required.                                                       |

## Home

| **ID**         | **Rule**                                                                                                                                    |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-008** | For every class, children expected = checked in + absent + not yet in.                                                                      |
| **BR-CDP-009** | Children checked out are a subset of children checked in, never added on top.                                                               |
| **BR-CDP-010** | Every figure on Home and Attendance opens the list of children behind it.                                                                   |
| **BR-CDP-011** | The Centre Director pins between 4 and 8 features; the default set is Attendance, Approvals, Messages, Calendar, Student list and Routines. |
| **BR-CDP-012** | Every item waiting for the Centre Director appears in "Waiting for you" and opens in one tap.                                               |

## Attendance

| **ID**         | **Rule**                                                                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-013** | Attendance is taken once per child per day, on the Attendance app at the gate or on the SMS web. The app does not check children in or out.                                     |
| **BR-CDP-014** | Temperature readings are shown as recorded; a reading at or above the fever threshold (default 37.5°C, setting per country) is highlighted and notified to the Centre Director. |
| **BR-CDP-015** | A wrong record is voided, not checked out. A voided record no longer counts as attendance and stays in history.                                                                 |
| **BR-CDP-016** | The Centre Director voids directly, with a required reason and without approval. A warning first says that the parent may already have seen the record.                         |
| **BR-CDP-017** | A void request from a teacher is decided by the Centre Director, a Centre Admin or a Senior Teacher with the void permission. Rejecting requires a reason.                      |
| **BR-CDP-018** | Who requested a void and who voided it are recorded as two separate events.                                                                                                     |
| **BR-CDP-019** | Corrections to check-in or check-out time require a reason and keep the original value in history.                                                                              |

## Approvals

| **ID**         | **Rule**                                                                                                                                                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-020** | All items waiting for the Centre Director are in one Approvals inbox, oldest first.                                                                                          |
| **BR-CDP-021** | Every item is Waiting, Approved, Declined or Closed.                                                                                                                         |
| **BR-CDP-022** | Declining, rejecting, returning or sending back always requires a reason or comment, and the requester is notified.                                                          |
| **BR-CDP-023** | Leave is approved by the Centre Director or a Senior Teacher with the approve leave permission. Approved leave days show On leave in attendance. Leave does not reduce fees. |
| **BR-CDP-024** | Adding an authorised pickup person needs approval by the Centre Director or the School Admin. Removing one needs no approval; the centre is notified.                        |
| **BR-CDP-025** | One-time pickup persons are not supported. Every pickup person goes through approval.                                                                                        |
| **BR-CDP-026** | Only the Centre Director approves progress reports, in one level. An approved report is published at once or on the release date.                                            |
| **BR-CDP-027** | Class update photos wait for review only when photo review is on for the centre. Nothing reaches parents until it is approved.                                               |

## Withdrawals

| **ID**         | **Rule**                                                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-028** | The Centre Director records a retention attempt before the admin can lock the last day.                                                                                                                                                          |
| **BR-CDP-029** | Only the admin locks the last day, on the SMS web. Every calculation uses the locked last day.                                                                                                                                                   |
| **BR-CDP-030** | A withdrawal with enough notice and a last day at the calendar month-end is approved by the Centre Director.                                                                                                                                     |
| **BR-CDP-031** | A short-notice or mid-month withdrawal goes to the approver set in Approval routes (default: District Manager in Singapore, Operations Manager in Malaysia, Centre Director for Odyssey, Head of Brand for Brighton). The app shows who decides. |
| **BR-CDP-032** | The Centre Director cannot change who approves a withdrawal.                                                                                                                                                                                     |
| **BR-CDP-033** | Before approval the app shows the outstanding balance of the whole family, including siblings.                                                                                                                                                   |

## Children, health and learning records

| **ID**         | **Rule**                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-034** | Allergy and health details written by the family are read only in the app. Staff add separate staff notes that never replace the family's words. |
| **BR-CDP-035** | The allergy list covers every child of the centre with an allergy, a medical condition or a dietary need.                                        |
| **BR-CDP-036** | Medical details are shown only to roles allowed in Roles & permissions (default: Centre Director, Teacher, School Admin, HQ Admin).              |
| **BR-CDP-037** | Portfolios are read only in the app.                                                                                                             |
| **BR-CDP-038** | Albums are never created by hand. They follow the class, child, learning domain and event tags on the photos.                                    |
| **BR-CDP-039** | A recalled update or photo disappears for all parents at once and the recall is recorded.                                                        |

## Communication

| **ID**         | **Rule**                                                                                                                                                |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-040** | The Centre Director creates announcements only with the "Create announcement" permission (default: on) and only for audiences in their own centre.      |
| **BR-CDP-041** | An announcement goes to Parents or to Staff, never both. Parents cannot reply to an announcement.                                                       |
| **BR-CDP-042** | A scheduled announcement can be edited or cancelled until it is sent.                                                                                   |
| **BR-CDP-043** | The Centre Director reads and replies in every thread of the centre.                                                                                    |
| **BR-CDP-044** | A private chat is between the Centre Director and one family. Teachers do not see it. Parents cannot start one.                                         |
| **BR-CDP-045** | There is no chat between staff members. Written communication to staff goes through staff announcements.                                                |
| **BR-CDP-046** | In a bulk send each family receives the message in its own thread and families never see each other.                                                    |
| **BR-CDP-047** | Reassigning an inquiry needs the "Reassign inquiries" permission (default: on for Centre Director) and is recorded with who passed it to whom and when. |
| **BR-CDP-048** | Survey and consent results can be viewed in the app; exporting them stays on the SMS web.                                                               |

## Calendar and centre log

| **ID**         | **Rule**                                                                                                                                                         |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-049** | The Centre Director creates every event type for their centre, including Centre closure. Teachers see the calendar and create only events for their own classes. |
| **BR-CDP-050** | Birthdays, public holidays and school visits are created automatically and are not entered by hand.                                                              |
| **BR-CDP-051** | Every event states its audience before it is saved: staff only, or staff and parents.                                                                            |
| **BR-CDP-052** | Centre log entries are visible to centre staff only and never to families.                                                                                       |
| **BR-CDP-053** | Each centre needs at least one centre log entry per day; "Nothing to report" counts as an entry.                                                                 |
| **BR-CDP-054** | The Centre Director marks centre log entries as read. Entries are not approved or rejected, and never deleted.                                                   |

## Centre settings

| **ID**         | **Rule**                                                                                                                                                                                  |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-CDP-055** | The Centre Director holds every permission of the centre and cannot remove their own permissions.                                                                                         |
| **BR-CDP-056** | The Centre Director grants extra permissions only to staff currently working at their centre, and only permissions they hold themselves. A reason is required.                            |
| **BR-CDP-057** | Several staff members can hold the same permission.                                                                                                                                       |
| **BR-CDP-058** | An extra permission ends when revoked or on its end date. A staff member who leaves the centre loses it automatically.                                                                    |
| **BR-CDP-059** | Photo review is a centre setting (default: off in Singapore, on in Malaysia). The Centre Director changes it only when granted this setting, with confirmation, and the change is logged. |
| **BR-CDP-060** | Company-level settings, such as approval routes and notice periods, cannot be changed in the app.                                                                                         |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                      | **Recipient**                                           | **Channel**                    | **When**                                                                                     |
|---------------------------------------|---------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------|
| **New item waiting for approval**     | Centre Director                                         | Push                           | When a leave, pickup, withdrawal, class update, progress report or void request is submitted |
| **Fever reading**                     | Centre Director                                         | Push                           | When a temperature at or above the fever threshold is recorded                               |
| **No attendance this month (day-18)** | Centre Director                                         | Push                           | On the run day (default the 18th), Singapore citizen children with no attendance day         |
| **Pickup person removed**             | Centre Director                                         | Push                           | When a parent removes an authorised pickup person                                            |
| **Allergy information changed**       | Centre Director                                         | Push                           | When a parent changes a child's allergy information                                          |
| **New message**                       | Centre Director                                         | Push                           | When a parent writes in a thread the Centre Director is in                                   |
| **Inquiry assigned**                  | Centre Director                                         | Push                           | When an inquiry is routed or reassigned to the Centre Director                               |
| **New centre log entry**              | Centre Director                                         | Push                           | When a staff member adds an Incident or Accident entry                                       |
| **Leave decision**                    | Parent                                                  | In-app and push (Parents App)  | When leave is approved or rejected                                                           |
| **Pickup decision**                   | Parent                                                  | In-app and push (Parents App)  | When a pickup person is approved or rejected                                                 |
| **Withdrawal outcome**                | Parent                                                  | In-app and push (Parents App)  | When a withdrawal is closed as retained, approved or rejected                                |
| **Progress report published**         | Parent                                                  | In-app and push (Parents App)  | When a report is published                                                                   |
| **Class update posted**               | Parents of tagged class or children                     | In-app and push (Parents App)  | When an update is approved                                                                   |
| **Announcement**                      | Parents or staff in the audience                        | In-app and push                | On publish; again on edit only when "Notify recipients again" is ticked                      |
| **Announcement or survey reminder**   | Recipients who have not read, acknowledged or responded | In-app and push                | When the Centre Director sends a reminder                                                    |
| **Message or inquiry reply**          | Parent                                                  | In-app and push (Parents App)  | On each reply or inquiry status change                                                       |
| **Event cancelled**                   | Parents who could see the event                         | In-app and push (Parents App)  | When an event is cancelled                                                                   |
| **Decision returned to staff**        | Teacher or requester                                    | In-app (Teacher App / SMS web) | When a report is returned, an update is sent back or a void request is rejected              |
| **Extra permission changed**          | Staff member                                            | In-app (Teacher App / SMS web) | When a permission is granted, revoked or expires                                             |

## 6.2 Documents

- Progress report and portfolio PDFs: opened read only in the app, generated by the SMS.

- No document is created, exported or printed in the app.

# 7. Reports & exports

| **Report**                       | **Content**                                                                                    | **Used by**     |
|----------------------------------|------------------------------------------------------------------------------------------------|-----------------|
| **Today's attendance**           | Checked in, checked out, still in the centre, not yet in, absent, by class and bus (on screen) | Centre Director |
| **This week's attendance**       | Children present per day of the current week (on screen)                                       | Centre Director |
| **Days attended this month**     | Days attended per child and children with no attendance this month (on screen)                 | Centre Director |
| **Attendance corrections**       | Corrections and voids with who, when and why (on screen)                                       | Centre Director |
| **Survey and consent responses** | Responded and not responded per class (on screen; export on the SMS web)                       | Centre Director |
| **Announcement reach**           | Read and acknowledged counts and who has not read (on screen)                                  | Centre Director |

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
<td><strong>AC-CDP-001</strong></td>
<td>Own centre only</td>
<td>Given the Centre Director of Small Wonder Tampines is signed in,<br />
when they open the Student list,<br />
then only children of Small Wonder Tampines are listed and no other centre can be selected.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-002</strong></td>
<td>Home figures reconcile</td>
<td>Given Nursery 2 expects 18 children, 15 are checked in, 2 are absent and 1 is not yet in,<br />
when the Centre Director opens Home,<br />
then the class figures add up to 18 and the checked-out count is included in the 15 checked in.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-003</strong></td>
<td>Figure opens list</td>
<td>Given 4 children are still in the centre at 6:30 pm,<br />
when the Centre Director taps "still in the centre",<br />
then the list shows those 4 children with their classes.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-004</strong></td>
<td>Pinned features limit</td>
<td>Given 8 features are pinned,<br />
when the Centre Director tries to pin a ninth,<br />
then the app blocks it and asks to remove one first.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-005</strong></td>
<td>No check in from the app</td>
<td>Given a child arrives at the gate,<br />
when the Centre Director opens the class in the app,<br />
then there is no check-in or check-out action; the record comes from the Attendance app or the SMS web.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-006</strong></td>
<td>Direct void</td>
<td>Given a check-in for Ryan Tan was recorded by mistake on 16 September,<br />
when the Centre Director voids it,<br />
then the app first warns that the parent may have seen it, requires a reason, removes the record from attendance and logs who voided it and when.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-007</strong></td>
<td>Void request</td>
<td>Given a teacher sends a void request from the Attendance app,<br />
when the Centre Director rejects it without a reason,<br />
then the app does not allow it.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-008</strong></td>
<td>Void request events</td>
<td>Given a teacher requested a void and the Centre Director voided the record,<br />
when the corrections log is opened,<br />
then the request and the void appear as two separate events with two names.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-009</strong></td>
<td>Leave approval</td>
<td>Given a parent requests Medical leave for 21 to 23 September,<br />
when the Centre Director approves it,<br />
then those days show On leave in attendance and the parent is notified.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-010</strong></td>
<td>Decline needs a reason</td>
<td>Given a pickup request is waiting,<br />
when the Centre Director rejects it with no reason,<br />
then the app does not allow it.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-011</strong></td>
<td>Pickup removal</td>
<td>Given a parent removes a pickup person in the Parents App,<br />
when the change is saved,<br />
then no approval item is created and the Centre Director receives a notice.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-012</strong></td>
<td>Retention before lock</td>
<td>Given a withdrawal has no retention attempt recorded,<br />
when the admin tries to lock the last day on the SMS web,<br />
then the system blocks it until the Centre Director records the retention attempt.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-013</strong></td>
<td>Short-notice withdrawal</td>
<td>Given a Small Wonder withdrawal with a last day of 15 December and one month of notice,<br />
when the Centre Director opens it,<br />
then the app shows the District Manager as the approver and offers the Centre Director no approve button.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-014</strong></td>
<td>Progress report publish</td>
<td>Given a Term 3 report for Chloe Ng is submitted,<br />
when the Centre Director approves it and chooses the release date,<br />
then the report is Approved and is published to the parent automatically on the release date.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-015</strong></td>
<td>Photo review off</td>
<td>Given photo review is off at a Singapore centre,<br />
when a teacher posts a class update,<br />
then the update reaches parents at once and nothing appears in Approvals.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-016</strong></td>
<td>Family health entries</td>
<td>Given a parent entered a peanut allergy,<br />
when the Centre Director opens the child's health record,<br />
then the family's entry is read only and the Centre Director can only add a staff note.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-017</strong></td>
<td>Private chat</td>
<td>Given the Centre Director starts a private chat with the parents of Nadia Osman,<br />
when the class teacher opens Messages,<br />
then the teacher does not see the private chat.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-018</strong></td>
<td>No staff chat</td>
<td>Given the Centre Director opens New message,<br />
when they look for a teacher as recipient,<br />
then only families can be chosen.</td>
</tr>
<tr class="odd">
<td><strong>AC-CDP-019</strong></td>
<td>Centre log hidden from parents</td>
<td>Given an Accident entry is recorded for 16 September,<br />
when a parent opens the Parents App calendar,<br />
then the entry is not shown.</td>
</tr>
<tr class="even">
<td><strong>AC-CDP-020</strong></td>
<td>Extra permission</td>
<td>Given Ms Janet Lee works at the centre,<br />
when the Centre Director grants her the void permission with an end date of 31 December,<br />
then a warning is shown first, a reason is required, Ms Lee is notified, the log records the grant and the permission ends on 31 December.</td>
</tr>
</tbody>
</table>
