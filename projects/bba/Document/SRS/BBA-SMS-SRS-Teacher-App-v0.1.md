Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Teacher App**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-TCH-NNN and acceptance criteria AC-TCH-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Teacher App of the Busy Bees Asia School Management System (SMS), Phase 1. The Teacher App is the mobile app teachers use in the classroom. It lets them record each child's day as it happens, share class moments, mark progress reports and talk to families without leaving the room.

A teacher records and reports; the Centre Director decides. Approving, publishing and changing records that belong to the family stay with the centre and the SMS web.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-teacher.lovable.app. Each feature in Section 4 links to the prototype screen. The rules of the matching SMS web modules (Daily Operations, Learning, Communication, Children & Families) apply to the same records in the Teacher App.

## 1.1 In scope for Phase 1

- Account and classes: sign in, profile, class switcher (one class or all my classes), read-only view of rights given by the Centre Director.

- Home: reminders, "Needs you today", quick actions, pinned features.

- Children: student list, child profile, health record and staff notes, allergy view, authorised pickup persons, attendance void requests.

- Routines: meals, bottles, naps, nappy and toilet, and mood, recorded for the class and adjusted per child; notes from home.

- Class updates: posting moments with photos and videos, tagging, review where the centre requires it, recall; photo gallery.

- Progress reports: rating objectives and writing comments on mobile, submitting to the Centre Director. Portfolios: view only.

- Messages with families of the teacher's own classes, inquiries assigned to the teacher, announcements, survey and consent responses, calendar.

- Approvals for Senior Teachers who hold delegated rights: child leave requests and class update review.

## 1.2 Not in Phase 1

- Taking attendance (check in and check out). Attendance is taken on the Attendance app at the gate or on the SMS web.

- Recording temperature readings in the Teacher App.

- Approving or voiding attendance in the Teacher App (approvers use the SMS web).

- Centre log on mobile (Phase 1 is on the SMS web only).

- Teacher leave requests, shift swaps and overtime claims (Phase 2).

- Emergency roll-call.

- Creating, editing or deleting portfolios on mobile (SMS web only).

- Chat between staff members, including teacher and Centre Director.

- Sending one message to families of more than one class.

- Creating calendar events in the Teacher App (teachers create class events on the SMS web).

- Seeing who reacted to a photo or who has viewed an album (later release).

- Enrichment attendance by enrichment trainers (SMS web, Learning module).

- Withdrawal, authorised pickup approval and other centre-wide approvals.

- Exporting data from the Teacher App (exports are on the SMS web).

# 2. Who uses it

| **Role**                        | **What they do in this module**                                                                                                                                                                                                                                                    |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Teacher**                     | Sees only the classes they are assigned to; records routines; posts class updates; rates progress reports and writes comments; replies to families of their classes; answers inquiries assigned to them; requests attendance voids; reads announcements, surveys and the calendar. |
| **Senior Teacher**              | Everything a Teacher can do; approves child leave requests and reviews class updates when the Centre Director has delegated that right.                                                                                                                                            |
| **Centre Director**             | Assigns teachers to classes and delegates rights; reviews class updates and approves progress reports; passes inquiries to teachers; reads every thread of the centre. Works in the SMS web and the Centre Director app.                                                           |
| **Centre Admin / School Admin** | Decides attendance void requests on the SMS web; in Malaysia, is notified when a teacher messages a parent.                                                                                                                                                                        |
| **HQ Admin**                    | Has every permission; configures centre settings and the Teacher permissions (for example "Create announcement").                                                                                                                                                                  |
| **Parent (Parents App)**        | Receives routines, class updates, messages and published reports; writes notes from home; owns the child's health record and pickup list.                                                                                                                                          |

# 3. Process overview

## P1. Recording routines for a class

1\. The teacher opens Routines and selects "Record for the class".

2\. The teacher chooses the routine (meal, bottle, nap, nappy and toilet, or mood) and fills the form once.

3\. Every child checked in today is ticked; the teacher unticks children it does not apply to and adjusts the children who differ.

4\. The teacher saves; one private entry is created per child with the teacher's name as "Logged by".

5\. Each parent sees only their own child's entry in the Parents App.

## P2. Posting a moment

1\. The teacher opens "Post a moment" and chooses Class update or Event update.

2\. The teacher adds photos and videos, then tags the class, children, learning domains and an activity.

3\. Children without media consent cannot be tagged.

4\. The teacher writes a caption and chooses an album, then posts.

5\. If review is on for the centre, the update waits for the Centre Director or a delegated Senior Teacher; otherwise parents see it at once and the photos are filed into albums.

## P3. Progress report

1\. Reports open on the entry start date for children who have attended for at least 3 months.

2\. The teacher rates each objective in the room, a bit at a time, or skips it with a reason, and writes a summary for each learning domain.

3\. Work is saved as it goes; the teacher can stop and return.

4\. The teacher submits the report to the Centre Director.

5\. The Centre Director approves and publishes it, or returns it with a comment; a returned report opens again for the teacher to edit and resubmit.

## P4. Messaging families

1\. Each child has a class thread for their guardians, the class teachers and the Centre Director.

2\. The teacher replies in the thread, or starts a message by choosing one class and then the children.

3\. Choosing a child selects both parents, or the one contact set at enrolment; the teacher can untick a parent.

4\. With several families, the message goes to each family separately.

5\. In Malaysia centres, the School Admin is notified of what was sent and to whom.

## P5. Inquiry passed to a teacher

1\. A parent raises an inquiry in the Parents App.

2\. The inquiry is assigned by category (Birthday goes to the class teachers) or passed to the teacher by the Centre Director.

3\. The teacher sees it in Inquiries with the waiting time and who passed it.

4\. The teacher replies and moves it to In progress or Closed; the parent is notified.

## P6. Attendance void request

1\. The teacher sees a wrong check in or check out on the child's attendance for today.

2\. The teacher requests a void with a reason.

3\. A Centre Admin, the Centre Director or a delegated Senior Teacher decides the request on the SMS web.

4\. The teacher is notified of the decision.

## P7. Delegated approvals (Senior Teacher)

1\. The Centre Director gives a Senior Teacher the right to approve leave requests, review class updates, or both.

2\. Requests appear in Approvals in the Teacher App; teachers without a right do not see Approvals.

3\. The Senior Teacher approves, or rejects or sends back with a reason.

4\. The parent or the teacher who posted is notified.

# 4. Modules, sub-modules, features and functions

## 1. Home & account

### 1.1 Sign in & profile

*Prototype:* [<u>https://bba-teacher.lovable.app/profile</u>](https://bba-teacher.lovable.app/profile)

| **Feature**         | **Function**                                                                                             |
|---------------------|----------------------------------------------------------------------------------------------------------|
| **Sign in**         | Staff account with the Teacher role; the app opens on Home.                                              |
| **View profile**    | Name, role (Teacher or Senior Teacher), centre.                                                          |
| **View my classes** | Classes the teacher is assigned to, including enrichment classes, with level and room.                   |
| **View my rights**  | Read-only list of rights given by the Centre Director, with "The centre director gave you these rights." |
| **Sign out**        |                                                                                                          |

### 1.2 Class switcher

*Prototype:* [<u>https://bba-teacher.lovable.app/</u>](https://bba-teacher.lovable.app/)

| **Feature**               | **Function**                                                    |
|---------------------------|-----------------------------------------------------------------|
| **Choose one class**      | Every screen shows only that class.                             |
| **Choose all my classes** | Every list is grouped by class.                                 |
| **Remember choice**       | The last choice is kept when the teacher moves between screens. |

### 1.3 Home

*Prototype:* [<u>https://bba-teacher.lovable.app/</u>](https://bba-teacher.lovable.app/)

| **Feature**                      | **Function**                                                                                                                             |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **View reminders**               | Reminders from the Centre Director or HQ, with sender, role and time, for example "17 progress reports for Nursery 2 are due on 14 Sep". |
| **Open reminder**                | Opens that class's progress reports filtered to the ones not finished.                                                                   |
| **Clear reminder automatically** | A reminder disappears when nothing is outstanding.                                                                                       |
| **View "Needs you today"**       | Built from real work: unanswered messages, waiting inquiries, children with no routine recorded, returned reports, updates sent back.    |
| **Open task**                    | Each item opens the right screen.                                                                                                        |
| **Use quick actions**            | Progress reports, Post a moment, Record routines.                                                                                        |
| **View "Your features"**         | Grid of pinned features; More features lists all of them.                                                                                |
| **Pin feature**                  | Add a feature to the Home grid.                                                                                                          |
| **Reorder features**             | Change the order of the Home grid.                                                                                                       |
| **View notifications**           | In-app notifications, newest first; each opens the related record.                                                                       |

## 2. Children

### 2.1 Student list

*Prototype:* [<u>https://bba-teacher.lovable.app/students</u>](https://bba-teacher.lovable.app/students)

| **Feature**            | **Function**                                                                            |
|------------------------|-----------------------------------------------------------------------------------------|
| **View student list**  | Children of the teacher's classes: photo, name, class, date of birth, medical icon.     |
| **Search**             | Child name.                                                                             |
| **Filter**             | Class.                                                                                  |
| **Sort**               | By name (default) or date of birth.                                                     |
| **Show medical icon**  | Next to the name of every child with an allergy or condition, on every list in the app. |
| **Open child profile** |                                                                                         |

### 2.2 Child profile

*Prototype:* [<u>https://bba-teacher.lovable.app/students</u>](https://bba-teacher.lovable.app/students)

| **Feature**                      | **Function**                                                                                     |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| **View child details**           | Photo, name, class, room, date of birth.                                                         |
| **View parents**                 | Name, relationship, phone, email.                                                                |
| **View health record**           | Allergies, conditions, medical history, note from the family, last updated by and on; read only. |
| **View declaration**             | Shows that the parent ticked the declaration that the health record is correct and complete.     |
| **Add note from staff**          | What the teacher observed; shown beside the family's text and attributed to the staff member.    |
| **Edit note from staff**         | The author edits their own note; changes kept in history.                                        |
| **View today's routines**        | Entries by type, with a link to record a routine.                                                |
| **View updates the child is in** | Moments the child is tagged in.                                                                  |

### 2.3 Allergy view

*Prototype:* [<u>https://bba-teacher.lovable.app/allergies</u>](https://bba-teacher.lovable.app/allergies)

| **Feature**                         | **Function**                                                                                                                                |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **View allergy list**               | Every child with an allergy in the selected classes: photo, class, allergy, severity and reaction, what to do, diet, underlying conditions. |
| **Select classes**                  | One class or several of the teacher's classes.                                                                                              |
| **Show count**                      | Heading states what is shown, for example "Nursery 2 and K1 Blue · 7 children".                                                             |
| **Search**                          | Child name, allergy.                                                                                                                        |
| **Filter**                          | Class, allergy, severity.                                                                                                                   |
| **Sort**                            | By severity, most severe first (default), or by name.                                                                                       |
| **View conditions without allergy** | Children with a condition and no allergy, listed separately.                                                                                |
| **Open child profile**              |                                                                                                                                             |

### 2.4 Authorised pickup

*Prototype:* [<u>https://bba-teacher.lovable.app/students</u>](https://bba-teacher.lovable.app/students)

| **Feature**                | **Function**                                                           |
|----------------------------|------------------------------------------------------------------------|
| **View pickup list**       | Approved pickup persons of a child, with photo, name and relationship. |
| **View class pickup list** | Approved pickup persons for every child of the class.                  |

### 2.5 Attendance void request

*Prototype:* [<u>https://bba-teacher.lovable.app/students</u>](https://bba-teacher.lovable.app/students)

| **Feature**                 | **Function**                                                                                       |
|-----------------------------|----------------------------------------------------------------------------------------------------|
| **View today's attendance** | Check in and check out times of a child today, with who brought or collected the child; read only. |
| **Request void**            | Choose the record and give a reason (required).                                                    |
| **View request status**     | Pending, Voided or Rejected, with the reason for a rejection.                                      |

## 3. Daily care

### 3.1 Routines

*Prototype:* [<u>https://bba-teacher.lovable.app/routines</u>](https://bba-teacher.lovable.app/routines)

| **Feature**                             | **Function**                                                                                                                         |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **View class routines**                 | Per class: children checked in today and what has been recorded for each.                                                            |
| **Show children with nothing recorded** | "To do" on each child and a count per class.                                                                                         |
| **Show missing required routines**      | For levels where routines are required (default: Infant and Playgroup).                                                              |
| **Record for the class**                | Fill the form once, then choose who it applies to.                                                                                   |
| **Choose children**                     | Every child checked in today is ticked; untick children it does not apply to.                                                        |
| **Adjust one child**                    | Change the value on the child's row or open the full form for that child.                                                            |
| **Record meal**                         | Time, meal type (Breakfast, Morning snack, Lunch, Afternoon snack, Late snack), amount eaten (All / Most / Some / None), meal items. |
| **Record bottle**                       | Time, millilitres prepared, millilitres drunk (required).                                                                            |
| **Record nap**                          | Start time, end time, quality (Slept well / Disrupted sleep); the duration is calculated.                                            |
| **Set default nap time**                | Per class, for example 12:00 to 14:00; new nap entries start from it.                                                                |
| **Record nappy / toilet**               | Diaper, Potty or Accident; Wet, BM or Dry.                                                                                           |
| **Record mood**                         | Happy, Settled, Quiet, Tired, Unsettled or Upset.                                                                                    |
| **Show time since last entry**          | For example "3h 10m since the last bottle"; calculated, never entered.                                                               |
| **Add note**                            | Free text the parent reads.                                                                                                          |
| **Add photo**                           | Warns that the photo also appears in the child's album in the Parents App.                                                           |
| **Fill "Logged by"**                    | Automatically the signed-in teacher.                                                                                                 |
| **Edit entry**                          | Change time or details; who edited is recorded.                                                                                      |
| **Remove entry**                        | Confirmation required; hidden from the parent and kept in history.                                                                   |
| **View child's day**                    | One child's entries in time order.                                                                                                   |
| **View note from home**                 | Under "From the family", with who wrote it and when; read only.                                                                      |
| **Show unread note from home**          | Marker on the child's row until the teacher opens it.                                                                                |

## 4. Learning

### 4.1 Class updates

*Prototype:* [<u>https://bba-teacher.lovable.app/updates</u>](https://bba-teacher.lovable.app/updates)

| **Feature**                | **Function**                                                                                                                            |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **View update list**       | Updates of the teacher's classes: photos, caption, class, posted by, date, status (Waiting for review / Sent back / Posted / Recalled). |
| **Filter**                 | Class, status.                                                                                                                          |
| **View update detail**     | Photos, videos, tags, captions, albums it is filed in.                                                                                  |
| **View sent-back comment** | Reviewer's comment, name and time.                                                                                                      |
| **Edit sent-back update**  | Change photos, tags or captions.                                                                                                        |
| **Resubmit update**        | Goes back to review.                                                                                                                    |
| **Recall update**          | Own updates; removes the update and its photos for all parents.                                                                         |

### 4.2 Post a moment

*Prototype:* [<u>https://bba-teacher.lovable.app/updates/new</u>](https://bba-teacher.lovable.app/updates/new)

| **Feature**                  | **Function**                                                                              |
|------------------------------|-------------------------------------------------------------------------------------------|
| **Choose kind**              | Class update (one class) or Event update (several of the teacher's classes).              |
| **Choose class**             | Teacher's own classes, including enrichment classes.                                      |
| **Take photo**               | Camera.                                                                                   |
| **Pick from library**        | Device photo library.                                                                     |
| **Add video**                | No audio-only files; length limit per brand (default: 2 minutes).                         |
| **Remove item**              | Before posting.                                                                           |
| **Tag class**                | Automatic; every parent of the class sees the update in the class album.                  |
| **Tag children**             | Children of the chosen class; for an Event update, children across the chosen classes.    |
| **Check media consent**      | Children without media consent are greyed out with the reason and cannot be tagged.       |
| **Tag one photo**            | Change the children, domains or activity on a single photo.                               |
| **Tag learning domain**      | From the brand's list; framework domains first, centre-added domains listed separately.   |
| **Tag activity**             | Existing activity tags, most used first.                                                  |
| **Add activity tag**         | A new tag becomes an album.                                                               |
| **Write caption**            | For the whole update.                                                                     |
| **Write line for one child** | Optional; only that child's parents read it.                                              |
| **Choose album**             | An existing album or a new named album.                                                   |
| **Review before posting**    | Photos, captions, audience, number of children tagged and the albums it will be filed in. |
| **Post update**              | Parents see it at once when review is off for the centre.                                 |
| **Send for review**          | When review is on; the screen says who reviews it.                                        |

### 4.3 Photo gallery

*Prototype:* [<u>https://bba-teacher.lovable.app/gallery</u>](https://bba-teacher.lovable.app/gallery)

| **Feature**     | **Function**                                                                                |
|-----------------|---------------------------------------------------------------------------------------------|
| **View albums** | Class album, child albums, learning domain albums, event and activity albums, named albums. |
| **Filter**      | Class, album kind.                                                                          |
| **Open album**  | Photos and videos in date order.                                                            |
| **View photo**  | Full screen with its tags, caption and update.                                              |
| **Play video**  |                                                                                             |

### 4.4 Progress reports

*Prototype:* [<u>https://bba-teacher.lovable.app/progress</u>](https://bba-teacher.lovable.app/progress)

| **Feature**                   | **Function**                                                                             |
|-------------------------------|------------------------------------------------------------------------------------------|
| **View report list**          | Per class: child, objectives rated out of total, summaries written out of total, status. |
| **Show only not finished**    | Filter used by reminders.                                                                |
| **View class progress**       | Children done out of total and the due date; overdue shown in red.                       |
| **View returned reports**     | Shown first, with the Centre Director's comment, name, role and time.                    |
| **Open report**               | Only for children who have attended for at least 3 months on the entry start date.       |
| **Rate objective**            | On the brand's scale (for example Emerging / Developing / Achieved).                     |
| **Rate assigned domains**     | In a class with several teachers, each teacher rates the domains assigned to them.       |
| **Skip objective**            | Reason required: "Not taught yet" or "Taught, not yet achieved".                         |
| **Add skip remark**           | Required with a skip.                                                                    |
| **Write domain summary**      | One per learning domain; no character limit.                                             |
| **Save draft**                | Saved as the teacher goes; the teacher can stop after any objective and return.          |
| **Submit to Centre Director** | Allowed when every objective has a rating or a skip and every domain has a summary.      |
| **Edit returned report**      | The teacher changes ratings and summaries and resubmits.                                 |
| **View submitted report**     | Read only while with the Centre Director or after publishing.                            |
| **View child's past reports** | Including reports written by previous teachers.                                          |

### 4.5 Portfolios

*Prototype:* [<u>https://bba-teacher.lovable.app/progress</u>](https://bba-teacher.lovable.app/progress)

| **Feature**             | **Function**                                         |
|-------------------------|------------------------------------------------------|
| **View portfolio list** | Children of the teacher's classes, semester, status. |
| **View portfolio**      | PDF; read only.                                      |

## 5. Communication

### 5.1 Messages

*Prototype:* [<u>https://bba-teacher.lovable.app/messages</u>](https://bba-teacher.lovable.app/messages)

| **Feature**                      | **Function**                                                                                                       |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **View conversations**           | Threads of the teacher's classes: child, parent, class, last message, time, unread marker.                         |
| **Search**                       | Parent, child, message text.                                                                                       |
| **Filter by class**              | Only the teacher's classes; hidden when the teacher has one class.                                                 |
| **Filter by type**               | Class thread, sent separately, group.                                                                              |
| **Sort**                         | Most recent (default) or longest unanswered.                                                                       |
| **Show unanswered**              | "Unanswered N days" when the last message is from a parent and no staff reply for 2 days (default).                |
| **Open thread**                  | Marks messages as read; shows who is in the thread.                                                                |
| **Reply**                        | Text.                                                                                                              |
| **Send attachment**              | Images, videos and documents (default limits: 25 MB per file, 3 minutes per video).                                |
| **Recall message**               | Own message within 15 minutes (default); the thread shows "Message removed".                                       |
| **Translate message**            | On demand, Chinese to English; the original is kept.                                                               |
| **Start new message**            | Choose one class first, then the recipients.                                                                       |
| **Choose by child**              | Selects both parents, or the one contact set at enrolment.                                                         |
| **Choose by family**             | Groups brothers and sisters in the same class.                                                                     |
| **Select whole class**           | Every family of the class.                                                                                         |
| **Untick a parent**              | Write to one parent only.                                                                                          |
| **Send separately**              | Each family receives the message in its own thread; families never see each other.                                 |
| **Start group conversation**     | Only with the "Group parents in one conversation" permission (default: off for Teacher); a group must have a name. |
| **Add member to group**          | Parents of the same class only.                                                                                    |
| **View read-only thread**        | Thread of a class the child has left: "You can read this conversation but not write in it."                        |
| **Show admin notice (Malaysia)** | Before sending: "The centre admin is notified that you sent this, and who it went to."                             |
| **View message check status**    | On or off for the centre; read only.                                                                               |
| **Open child profile**           | From the thread.                                                                                                   |

### 5.2 Inquiries

*Prototype:* [<u>https://bba-teacher.lovable.app/inquiries</u>](https://bba-teacher.lovable.app/inquiries)

| **Feature**             | **Function**                                                                            |
|-------------------------|-----------------------------------------------------------------------------------------|
| **View my inquiries**   | Only inquiries assigned to the teacher: subject, child, category, status, waiting time. |
| **Sort**                | Longest waiting first (default).                                                        |
| **Filter**              | Status (Open / In progress / Closed), class.                                            |
| **View inquiry detail** | Details, attachments, replies, history.                                                 |
| **Show who passed it**  | "The centre director passed this to you."                                               |
| **Reply**               | Text and attachments; the parent is notified.                                           |
| **Change status**       | Open, In progress, Closed.                                                              |

### 5.3 Announcements

*Prototype:* [<u>https://bba-teacher.lovable.app/announcements</u>](https://bba-teacher.lovable.app/announcements)

| **Feature**             | **Function**                                                                                                     |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **View announcements**  | Staff announcements sent to the teacher and parent announcements of the teacher's centre and classes; read only. |
| **Filter**              | Category (Closure, General, Event, Payment, Health and safety).                                                  |
| **Open announcement**   | Text, images, attachments, scope, sender, date.                                                                  |
| **Mark as read**        | Automatically when opened; the sender sees the read count.                                                       |
| **Acknowledge**         | When the sender requires acknowledgement.                                                                        |
| **Create announcement** | Only with the "Create announcement" permission (default: off for Teacher); to the teacher's own classes only.    |

### 5.4 Survey & consent

*Prototype:* [<u>https://bba-teacher.lovable.app/survey-consent</u>](https://bba-teacher.lovable.app/survey-consent)

| **Feature**                   | **Function**                                                                  |
|-------------------------------|-------------------------------------------------------------------------------|
| **View surveys and consents** | Those sent to the teacher's classes: title, deadline, responded out of total. |
| **Open responses**            | Answers per child.                                                            |
| **Show only not responded**   | Children whose parents have not answered.                                     |
| **View consent status**       | Agree, Disagree or not answered per child; read only.                         |

### 5.5 Calendar

*Prototype:* [<u>https://bba-teacher.lovable.app/calendar</u>](https://bba-teacher.lovable.app/calendar)

| **Feature**       | **Function**                                                   |
|-------------------|----------------------------------------------------------------|
| **View calendar** | Centre and class events, public holidays, closures, birthdays. |
| **Switch view**   | Day, week, month.                                              |
| **Open event**    | Date, time, type, classes, details.                            |

## 6. Approvals

### 6.1 Approvals

*Prototype:* [<u>https://bba-teacher.lovable.app/approvals</u>](https://bba-teacher.lovable.app/approvals)

| **Feature**                | **Function**                                                     |
|----------------------------|------------------------------------------------------------------|
| **Show Approvals**         | Only to a Senior Teacher who holds at least one delegated right. |
| **View approval inbox**    | Request type, child or class, requested by, date, status.        |
| **Filter**                 | Type (Leave request, Class update).                              |
| **View leave request**     | Child, type (Personal / Medical), dates, reason, attachment.     |
| **Approve leave**          | Records who and when; the parent is notified.                    |
| **Reject leave**           | Reason required; the parent is told the outcome.                 |
| **View update for review** | All photos and videos, tags and captions.                        |
| **Approve update**         | Parents see it and the photos are filed into albums.             |
| **Send back update**       | Comment required; the teacher edits and resubmits.               |

# 5. Business rules

## Access and scope

| **ID**         | **Rule**                                                                                                                                                                           |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-001** | A teacher sees only the classes they are assigned to. A class can have several teachers, and a teacher can have several classes.                                                   |
| **BR-TCH-002** | When a teacher is assigned to a class, they see its children, threads, updates and past reports; when they are removed, they no longer see them.                                   |
| **BR-TCH-003** | A teacher's rights are given by the Centre Director in the SMS web and are read only in the Teacher App.                                                                           |
| **BR-TCH-004** | Approvals appears only for a Senior Teacher who holds at least one delegated right. The only rights available in the Teacher App are child leave approval and class update review. |
| **BR-TCH-005** | Withdrawals, authorised pickup approvals and the centre-wide approval queue never appear in the Teacher App.                                                                       |
| **BR-TCH-006** | Centre settings (review of class updates, message check, required routines) are set on the SMS web. A teacher sees their state, never the switch.                                  |
| **BR-TCH-007** | In "All my classes" mode, every list is grouped by class.                                                                                                                          |

## Home

| **ID**         | **Rule**                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-008** | "Needs you today" is built from outstanding work and is never a fixed list.                                                   |
| **BR-TCH-009** | A reminder from the Centre Director or HQ shows who sent it, their role and when, and disappears when nothing is outstanding. |
| **BR-TCH-010** | The three quick actions are fixed: Progress reports, Post a moment, Record routines.                                          |

## Children and health

| **ID**         | **Rule**                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-011** | The parent owns the health record and writes it in the Parents App. No field of it can be edited in the Teacher App. |
| **BR-TCH-012** | A teacher adds observations under "Note from staff", which sits beside the family's text and never replaces it.      |
| **BR-TCH-013** | If the family's information looks wrong, the teacher tells the Centre Director.                                      |
| **BR-TCH-014** | A medical icon appears next to the name of every child with an allergy or condition on every list.                   |
| **BR-TCH-015** | Children with a condition and no allergy are listed separately in the allergy view.                                  |
| **BR-TCH-016** | Only approved pickup persons are shown. Pending or removed persons are never shown.                                  |

## Attendance

| **ID**         | **Rule**                                                                                                                                                                                        |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-017** | Teachers do not take attendance in the Teacher App. Attendance is taken once per child per day at the gate on the Attendance app or on the SMS web.                                             |
| **BR-TCH-018** | A teacher can request a void of a wrong check in or check out of a child in their class. A reason is required.                                                                                  |
| **BR-TCH-019** | Void requests are decided on the SMS web by a Centre Admin, the Centre Director or a Senior Teacher assigned by the Centre Director. Every void keeps who requested, who decided, when and why. |

## Routines

| **ID**         | **Rule**                                                                                                            |
|----------------|---------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-020** | Routines are recorded once for the class and adjusted per child. Each child gets a separate entry.                  |
| **BR-TCH-021** | Routines are private to one child. Parents see only their own child's entries.                                      |
| **BR-TCH-022** | Every entry records who created it and who last edited it. "Logged by" is the signed-in user and cannot be changed. |
| **BR-TCH-023** | A nap's end time must be after its start time.                                                                      |
| **BR-TCH-024** | A bottle entry needs the millilitres drunk.                                                                         |
| **BR-TCH-025** | The time since the last meal, bottle or nappy is calculated by the system.                                          |
| **BR-TCH-026** | A photo added to a routine also appears in the child's album in the Parents App.                                    |
| **BR-TCH-027** | Showering is not recorded.                                                                                          |
| **BR-TCH-028** | A note from home can be read but never edited or deleted by staff.                                                  |

## Class updates and gallery

| **ID**         | **Rule**                                                                                                                                                                                     |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-029** | A Class update belongs to one class. An Event update can include several of the teacher's own classes, with children tagged across them.                                                     |
| **BR-TCH-030** | A child without media consent cannot be tagged in any update or photo.                                                                                                                       |
| **BR-TCH-031** | Learning domains come from the brand's list. Teachers pick from it and cannot add to it; activity tags can be added by teachers.                                                             |
| **BR-TCH-032** | Updates contain photos and videos only. The video length limit is set per brand (default: 2 minutes).                                                                                        |
| **BR-TCH-033** | Review before posting is on or off per centre (default: off in Singapore, on in Malaysia). When on, parents see nothing until the Centre Director or a delegated Senior Teacher approves it. |
| **BR-TCH-034** | Albums are never created by hand except named albums. They follow the tags; the class album always exists; a child's album holds only photos that child is tagged in.                        |
| **BR-TCH-035** | A teacher can recall their own update. It disappears for all parents at once and the recall is kept in history.                                                                              |
| **BR-TCH-036** | Parents cannot comment on an update and never see another family's reactions.                                                                                                                |

## Progress reports and portfolios

| **ID**         | **Rule**                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-037** | Teachers rate objectives and write comments on mobile. A teacher never publishes a report; submitting to the Centre Director is the teacher's last step. |
| **BR-TCH-038** | A report can be started only for a child who has attended for at least 3 months on the entry start date (default: 3 months, setting).                    |
| **BR-TCH-039** | A skipped objective needs one of two reasons, "Not taught yet" or "Taught, not yet achieved", and a remark. The two reasons are kept separate.           |
| **BR-TCH-040** | Domain summaries have no character limit.                                                                                                                |
| **BR-TCH-041** | A report can be submitted only when every objective has a rating or a skip and every domain has a summary.                                               |
| **BR-TCH-042** | A submitted or published report is read only for the teacher. A returned report opens again for editing.                                                 |
| **BR-TCH-043** | In a class with several teachers, each teacher rates only the domains assigned to them.                                                                  |
| **BR-TCH-044** | Portfolios are view only in the Teacher App. They are created and edited on the SMS web.                                                                 |

## Messages and inquiries

| **ID**         | **Rule**                                                                                                                                                                                                                                       |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-045** | One message goes to one class. A teacher never sends to families of another class or of two classes at once.                                                                                                                                   |
| **BR-TCH-046** | Each child has one class thread per class, shared by the guardians, the class teachers and the Centre Director.                                                                                                                                |
| **BR-TCH-047** | When a child changes class, a new thread is created and the old one becomes read only. Threads are kept until the child leaves the school.                                                                                                     |
| **BR-TCH-048** | A teacher cannot start a chat with the Centre Director or another staff member.                                                                                                                                                                |
| **BR-TCH-049** | Whether a child's messages go to both parents or to one named contact is set at enrolment. The teacher can still untick a parent before sending.                                                                                               |
| **BR-TCH-050** | A group conversation of several families needs the "Group parents in one conversation" permission (default: off for Teacher) and a name.                                                                                                       |
| **BR-TCH-051** | In Malaysia centres, the School Admin is notified each time a teacher sends a message to a parent, with the content and recipients. The setting is per centre (default: on in Malaysia, off in Singapore). The teacher is told before sending. |
| **BR-TCH-052** | A teacher sees only inquiries assigned to them. Teachers cannot create or reassign inquiries by default.                                                                                                                                       |

## Announcements, surveys and calendar

| **ID**         | **Rule**                                                                                                                           |
|----------------|------------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-053** | Creating announcements is a permission (default: off for Teacher). With the permission, a teacher sends only to their own classes. |
| **BR-TCH-054** | Teachers read survey and consent responses for their own classes only. Approving or changing a consent stays with the centre.      |
| **BR-TCH-055** | The calendar is view only in the Teacher App.                                                                                      |

## Approvals

| **ID**         | **Rule**                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| **BR-TCH-056** | Rejecting a leave request or sending back a class update needs a reason, because the family or the teacher is told the outcome. |
| **BR-TCH-057** | A reviewer checks the whole photo, including the background, before approving an update.                                        |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                      | **Recipient**                                           | **Channel**                              | **When**                                                         |
|---------------------------------------|---------------------------------------------------------|------------------------------------------|------------------------------------------------------------------|
| **New message**                       | Teacher; parent                                         | Push (Teacher App); push (Parents App)   | When a message is sent in a thread                               |
| **Teacher message alert (Malaysia)**  | School Admin                                            | In-app                                   | When a teacher sends a message to a parent, if on for the centre |
| **Inquiry assigned**                  | Teacher                                                 | Push (Teacher App)                       | When an inquiry is assigned or passed to the teacher             |
| **Inquiry reply**                     | Parent                                                  | Push (Parents App)                       | When the teacher replies or changes the status                   |
| **Routine recorded**                  | Parent                                                  | Push (Parents App), as set by the parent | When an entry is saved for their child                           |
| **Class update posted**               | Parents of tagged class                                 | Push (Parents App)                       | When an update is posted or approved                             |
| **Class update waiting for review**   | Centre Director; delegated Senior Teacher               | In-app (web); push (Teacher App)         | When a teacher posts and review is on                            |
| **Class update sent back / approved** | Teacher who posted                                      | Push (Teacher App)                       | When the reviewer decides                                        |
| **Progress report submitted**         | Centre Director                                         | In-app (web)                             | When a teacher submits a report                                  |
| **Progress report returned**          | Teacher                                                 | Push (Teacher App)                       | When the Centre Director returns a report                        |
| **Report reminder**                   | Teachers with reports not submitted                     | Push (Teacher App); Home reminder        | When the Centre Director or HQ sends it                          |
| **Leave request**                     | Delegated Senior Teacher                                | Push (Teacher App)                       | When a parent submits a request                                  |
| **Leave decision**                    | Parent                                                  | Push (Parents App)                       | When the request is approved or rejected                         |
| **Void request**                      | Centre Admin, Centre Director, assigned Senior Teachers | In-app (web)                             | When a teacher requests a void                                   |
| **Void decision**                     | Teacher who requested                                   | Push (Teacher App)                       | When the request is decided                                      |
| **Internal announcement**             | Staff in the audience                                   | Push (Teacher App)                       | When published or at the scheduled time                          |
| **Allergy information changed**       | Class teachers                                          | Push (Teacher App)                       | When the parent changes allergy information                      |
| **No attendance this month**          | Class teachers                                          | Push (Teacher App)                       | On the day-18 run day (Singapore citizen children)               |

## 6.2 Documents

- No documents are produced in the Teacher App. Published progress reports and portfolios are PDFs produced on the SMS web; the Teacher App displays them.

# 7. Reports & exports

| **Report**                          | **Content**                                                                             | **Used by** |
|-------------------------------------|-----------------------------------------------------------------------------------------|-------------|
| **Routines missing today**          | Children of the class with nothing recorded, shown on Routines and in "Needs you today" | Teacher     |
| **Progress report status by class** | Children done out of total, reports returned, due date                                  | Teacher     |
| **Survey response status**          | Responded and not responded per child for the teacher's classes                         | Teacher     |
| **Allergy list by class**           | Children with allergies and conditions for the selected classes                         | Teacher     |

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
<td><strong>AC-TCH-001</strong></td>
<td>Class scope</td>
<td>Given Ms Priya teaches Nursery 2 and K1 Blue,<br />
when she opens the student list in "All my classes",<br />
then only children of Nursery 2 and K1 Blue are listed, grouped by class.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-002</strong></td>
<td>No attendance in the app</td>
<td>Given a teacher is signed in to the Teacher App,<br />
when she looks for check in or check out,<br />
then no such action exists; she can only view today's records and request a void.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-003</strong></td>
<td>Void request</td>
<td>Given Liam's check out at 4:05 pm was recorded by mistake,<br />
when the teacher requests a void with the reason "Wrong child",<br />
then the request reaches the Centre Admin, the Centre Director and assigned Senior Teachers on the SMS web, and the record stays until decided.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-004</strong></td>
<td>Void reason required</td>
<td>Given a void request is being created,<br />
when the teacher submits it without a reason,<br />
then the system does not allow it.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-005</strong></td>
<td>Routines for the class</td>
<td>Given Infant class A has 10 children checked in,<br />
when the teacher records lunch "All" for the class and changes Mia to "Some",<br />
then 9 children show All, Mia shows Some, each entry shows the teacher as "Logged by", and each parent sees only their own child.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-006</strong></td>
<td>Nap time check</td>
<td>Given a nap starts at 13:00,<br />
when the teacher enters an end time of 12:30,<br />
then the system does not save it and asks for an end time after the start.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-007</strong></td>
<td>Note from home</td>
<td>Given Chloe's mother wrote "She slept late last night" in the Parents App,<br />
when the teacher opens Chloe's day,<br />
then the note shows under "From the family" with the writer and time, and cannot be edited.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-008</strong></td>
<td>Media consent</td>
<td>Given Ezra has no media consent,<br />
when the teacher tags children in a moment,<br />
then Ezra is greyed out with the reason and cannot be tagged.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-009</strong></td>
<td>Review on</td>
<td>Given review is on for Busy Bees Mont Kiara,<br />
when a teacher posts a moment,<br />
then the update waits for the Centre Director or a delegated Senior Teacher and parents see nothing until it is approved.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-010</strong></td>
<td>Review off</td>
<td>Given review is off for Small Wonder Tampines,<br />
when a teacher posts a moment for Nursery 2,<br />
then parents of Nursery 2 see it at once and the photos are filed into the class, child, domain and activity albums.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-011</strong></td>
<td>Video limit</td>
<td>Given the brand video limit is 2 minutes,<br />
when the teacher adds a 3-minute video,<br />
then the system rejects it and states the limit.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-012</strong></td>
<td>Three-month rule</td>
<td>Given Leo started on 1 August and the entry start date is 1 October,<br />
when the teacher opens Leo's report,<br />
then the report cannot be started because Leo has attended for less than 3 months.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-013</strong></td>
<td>Skip needs a reason</td>
<td>Given a teacher skips an objective,<br />
when she saves without choosing "Not taught yet" or "Taught, not yet achieved",<br />
then the system does not save the skip.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-014</strong></td>
<td>Save and return</td>
<td>Given a teacher has rated 12 of 30 objectives for Aiden,<br />
when she leaves the screen and opens the report later,<br />
then the 12 ratings are still there and the report shows Draft.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-015</strong></td>
<td>No publishing</td>
<td>Given a teacher has finished a report,<br />
when she looks for a publish action,<br />
then only "Send to the Centre Director" exists.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-016</strong></td>
<td>Returned report</td>
<td>Given the Centre Director returns Hana's report with a comment on 10 October,<br />
when the teacher opens Progress reports,<br />
then Hana's report is listed first with the full comment, name, role and date, and is editable.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-017</strong></td>
<td>One message, one class</td>
<td>Given a teacher teaches Nursery 2 and K1 Blue,<br />
when she starts a new message,<br />
then she must choose one class first and cannot add children of the other class.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-018</strong></td>
<td>Malaysia message check</td>
<td>Given the message check is on for a Malaysia centre,<br />
when a teacher writes to a parent,<br />
then the notice that the School Admin is notified shows before sending, and the School Admin receives the content and recipients after sending.</td>
</tr>
<tr class="odd">
<td><strong>AC-TCH-019</strong></td>
<td>Old class thread</td>
<td>Given Gabriel moved from Nursery 2 to K1 Blue,<br />
when his Nursery 2 teacher opens the old thread,<br />
then she can read it but cannot write in it.</td>
</tr>
<tr class="even">
<td><strong>AC-TCH-020</strong></td>
<td>No approvals without a right</td>
<td>Given a Teacher holds no delegated right,<br />
when she opens Home or More,<br />
then there is no Approvals entry anywhere in the app.</td>
</tr>
</tbody>
</table>
