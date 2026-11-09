Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Communication**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-COM-NNN and acceptance criteria AC-COM-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Communication module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes how centres and HQ communicate with the parents of enrolled children, and how HQ and centres send internal announcements to staff, without Taidii.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/communication. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Announcements to parents and internal announcements to staff, with scheduling, acknowledgement and read tracking.

- Messages: class threads for each child, private threads between the Centre Director and a family, bulk send to families, group conversations by permission.

- Inquiries: parent requests by category (for example fees, birthday), routing, replies, status and reassignment.

- Surveys and consents: one module with two tabs; paid survey questions linked to invoices; consent records with withdrawal.

- Notifications: push and in-app notifications per guardian, notification centre, settings per category.

- What parents see in the Parents App: announcements, messages, inquiries, surveys, consents and notifications.

- What staff see in the Teacher App: messages, inquiries assigned to them, internal announcements and notifications.

## 1.2 Not in Phase 1

- New leads and enquiries from prospective families (handled in Enquiries).

- A combined inbox for WhatsApp, phone and email.

- Events with dates, capacity and sign-up (announcements and surveys are used instead).

- Parent-teacher conference (PTC) slot booking.

- Resource library.

- Chat between staff members (for example Centre Director and teacher).

- SMS notifications and email digests.

- Exporting message content.

- Voice notes in messages.

# 2. Who uses it

| **Role**                                    | **What they do in this module**                                                                                                                                                                      |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HQ Admin**                                | Has every permission in the module; configures permissions, inquiry categories and routing, announcement categories and notification settings; sends system-wide announcements to parents and staff. |
| **HQ staff (for example Customer Service)** | Reads and replies to inquiries and threads of every centre as permitted; sends announcements within their permitted scope.                                                                           |
| **Centre Director**                         | Creates announcements and surveys for the centre; reads every thread of the centre; holds private threads with families; handles inquiries; groups parents in one conversation.                      |
| **Centre Admin / School Admin**             | Handles fee and general inquiries; adds inquiries received another way; creates surveys and consents as permitted; in Malaysia, is notified when a teacher messages a parent.                        |
| **Teacher**                                 | Replies in the class threads of their classes; handles birthday inquiries of their class; tracks survey responses of their class; reads internal announcements.                                      |
| **All staff**                               | Receive internal announcements for their organisation, centre or role; see parent announcements of their centre and classes as read-only.                                                            |
| **Parent / guardian (Parents App)**         | Reads announcements; messages the class and the Centre Director; raises inquiries; answers surveys and signs or withdraws consents; manages notification settings.                                   |

# 3. Process overview

## P1. Announcement to parents

1\. A user with the "Create announcement" permission writes the announcement, picks a category and attaches files.

2\. The user selects Parents and the audience within their own scope: whole system, centre, level or class.

3\. The user publishes now or schedules a date and time; drafts can be saved.

4\. Parents receive a push and in-app notification; staff in that scope see it read-only.

5\. The sender tracks read and acknowledged counts and sends reminders to those who have not read or acknowledged.

## P2. Internal announcement to staff

1\. A user with the "Create announcement" permission selects Staff as the recipient type.

2\. The user selects the audience: whole organisation, centre or role.

3\. The user publishes now or schedules it.

4\. Staff receive it in the SMS web and the Teacher App; the sender tracks who has read it.

## P3. Class thread

1\. When a child is placed in a class, the system creates one class thread for that child and their guardians.

2\. The class teachers and the Centre Director reply in the same thread; a teacher who joins the class later sees the full history.

3\. Parents and staff receive a push notification for each new message.

4\. When the child changes class, the system creates a new thread; the old thread becomes read-only.

5\. Threads are kept until the child leaves the school.

## P4. Inquiry

1\. A parent raises an inquiry in the Parents App with a category, the child, a subject, the details and attachments; or a staff member adds one received another way.

2\. The system assigns it by category: Fees to the Centre Admin / School Admin, Birthday to the class teachers, other categories to the Centre Director and Centre Admin.

3\. The assignee replies and moves it from Open to In progress to Closed.

4\. Users with the "Reassign inquiries" permission can pass it to another person; every change is logged.

5\. The parent is notified of each reply and status change.

## P5. Survey with a paid question

1\. A user creates a survey (for example a field trip) with questions, attachments, an audience and a deadline; a question option can carry a fee item and an amount.

2\. The user publishes it and can publish a linked announcement that opens the survey.

3\. Parents answer in the Parents App and can change their answer until the deadline; the sender tracks responses and sends reminders.

4\. When the survey closes, each answer with a fee creates an ad hoc invoice line for the child in Fees & Payments.

5\. Results are viewed and exported on the web.

## P6. Consent

1\. A user creates a consent form with the statement, attachments, Agree / Disagree, signature setting, audience and deadline.

2\. Parents agree or disagree and sign in the Parents App.

3\. Staff track who has responded and send reminders.

4\. If the form allows it, a parent can withdraw consent later; the original response and the withdrawal are both kept.

# 4. Modules, sub-modules, features and functions

## 1. Announcements

### 1.1 Announcements

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication</u>](https://bba-sms-crm.lovable.app/communication)

| **Feature**                     | **Function**                                                                                                 |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| **View announcement list**      | Title, recipient type (Parents / Staff), audience, category, posted by, date, status, read count.            |
| **Search**                      | Partial, case-insensitive match on title and content.                                                        |
| **Filter**                      | Recipient type, scope (HQ / centre / level / class), category, status (Draft / Scheduled / Sent / Recalled). |
| **Sort**                        | Default newest first.                                                                                        |
| **Paging**                      | 20 / 50 / 100 rows; "1-20 of N".                                                                             |
| **Create announcement**         | Title, content, category, attachments. Only users with the "Create announcement" permission.                 |
| **Select recipient type**       | Parents or Staff (internal announcement).                                                                    |
| **Select parent audience**      | Whole system (HQ only), centre, level or class, limited to the creator's scope.                              |
| **Select staff audience**       | Whole organisation (HQ only), centre or role, limited to the creator's scope.                                |
| **Attach files**                | Images and documents.                                                                                        |
| **Require acknowledgement**     | Recipients tap "Acknowledge"; optional for each announcement.                                                |
| **Link to a survey or consent** | Adds a button that opens the selected survey or consent form.                                                |
| **Save draft**                  | Keeps the announcement as Draft.                                                                             |
| **Schedule send**               | Date and time; status Scheduled until sent.                                                                  |
| **Publish**                     | Sends now.                                                                                                   |
| **Send push notification**      | Automatically on publish to every recipient.                                                                 |
| **View as staff (read-only)**   | Staff of the centre or class see parent announcements of their scope without editing.                        |
| **Track read and acknowledged** | Sent, read and acknowledged counts; list of who has not read or acknowledged.                                |
| **Send reminder**               | To recipients who have not read or not acknowledged, sent by the user.                                       |
| **Edit announcement**           | After publishing; an "Edited" label is shown; option "Notify recipients again" (default: off).               |
| **Recall announcement**         | Removes it from the Parents App and staff views; the record is kept with status Recalled.                    |
| **View history**                | Created, edited, published, recalled, reminders sent: who and when.                                          |
| **Export**                      | Announcement list with read and acknowledged counts to Excel.                                                |

## 2. Messages

### 2.1 Messages

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication/messages</u>](https://bba-sms-crm.lovable.app/communication/messages)

| **Feature**                           | **Function**                                                                                                                 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Create class thread automatically** | One thread per child per class, for the child's guardians, the class teachers and the Centre Director.                       |
| **Create new thread on class change** | The previous class thread becomes read-only.                                                                                 |
| **Create private thread**             | Between the Centre Director and one family.                                                                                  |
| **Group parents in one conversation** | Several families in one conversation; only users with this permission.                                                       |
| **Bulk send to families**             | One message to several families; each family receives it in its own thread.                                                  |
| **View inbox**                        | Threads grouped by class and child, last message, unread count.                                                              |
| **Search**                            | Message text, child name, parent name.                                                                                       |
| **Filter**                            | Class, thread type (Class / Private / Group), Read / Unread, Unanswered.                                                     |
| **Sort**                              | Default latest message first.                                                                                                |
| **Load more**                         | Older messages load on scroll.                                                                                               |
| **Send message**                      | Text.                                                                                                                        |
| **Send attachment**                   | Images, videos and documents (default limits: 25 MB per file, 3 minutes per video).                                          |
| **Show read receipt**                 | "Seen" with time.                                                                                                            |
| **Recall message**                    | The sender recalls their own message within 15 minutes (default); the thread shows "Message removed" and the record is kept. |
| **Send push notification**            | Automatically for each new message; opens the thread.                                                                        |
| **Notify School Admin (Malaysia)**    | The School Admin is notified when a teacher sends a message to a parent; on or off per centre.                               |
| **Monitor centre threads**            | The Centre Director reads and replies in every thread of the centre; HQ users read and reply in every centre as permitted.   |
| **View archived threads**             | Read-only threads of previous classes, kept until the child leaves the school.                                               |

## 3. Inquiries

### 3.1 Inquiries

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication/inquiries</u>](https://bba-sms-crm.lovable.app/communication/inquiries)

| **Feature**                                  | **Function**                                                                                                                                                           |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Create inquiry (parent)**                  | In the Parents App: category, child, subject, details, attachments.                                                                                                    |
| **Fill birthday form**                       | Category Birthday opens a fixed form: preferred date, cake, gifts, other comments.                                                                                     |
| **Add an inquiry a family sent another way** | Staff record an inquiry received by phone, email or in person: family, child, category, channel, details.                                                              |
| **Route inquiry automatically**              | By category, as configured by HQ Admin (default: Fees to Centre Admin / School Admin; Birthday to the class teachers; others to the Centre Director and Centre Admin). |
| **View inquiry list**                        | Subject, child, category, status, assignee, centre, waiting time.                                                                                                      |
| **Search**                                   | Subject, child name, parent name.                                                                                                                                      |
| **Filter**                                   | Category, status (Open / In progress / Closed), assignee, centre.                                                                                                      |
| **Sort**                                     | Default longest waiting first.                                                                                                                                         |
| **Paging**                                   | 20 / 50 / 100 rows; "1-20 of N".                                                                                                                                       |
| **View inquiry detail**                      | Details, attachments, replies, assignee, history.                                                                                                                      |
| **Reply**                                    | Text and attachments; the parent is notified.                                                                                                                          |
| **Change status**                            | Open, In progress, Closed.                                                                                                                                             |
| **Reassign**                                 | Only users with the "Reassign inquiries" permission; reason optional; logged.                                                                                          |
| **Bulk reassign**                            | Several inquiries to one assignee.                                                                                                                                     |
| **Reopen inquiry (parent)**                  | Within 7 days of closing (default); after that the parent raises a new inquiry.                                                                                        |
| **Notify parent**                            | On each reply and status change.                                                                                                                                       |
| **View history**                             | Every reply, status change and reassignment: who and when.                                                                                                             |
| **Export**                                   | Filtered inquiry list to Excel.                                                                                                                                        |

## 4. Surveys & consents

### 4.1 Surveys

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication/surveys</u>](https://bba-sms-crm.lovable.app/communication/surveys)

| **Feature**                               | **Function**                                                                                              |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **View survey list**                      | Survey tab (default): title, audience, deadline, status, response rate.                                   |
| **Search**                                | Title.                                                                                                    |
| **Filter**                                | Status (Draft / Open / Closed), centre, class.                                                            |
| **Sort**                                  | Default nearest deadline first.                                                                           |
| **Paging**                                | 20 / 50 / 100 rows; "1-20 of N".                                                                          |
| **Create survey**                         | Title, description, attachments, questions.                                                               |
| **Add question**                          | Single choice, multiple choice, yes / no, short text, date; required or optional.                         |
| **Add fee to an option**                  | Fee item and amount on a choice option (for example "Joining the field trip: \$25").                      |
| **Select audience**                       | Centre, level or class, limited to the creator's scope.                                                   |
| **Set deadline**                          | Date and time.                                                                                            |
| **Save draft**                            | Keeps the survey as Draft.                                                                                |
| **Publish**                               | Sends to the audience; status Open.                                                                       |
| **Send push notification**                | Automatically on publish.                                                                                 |
| **Answer survey (parent)**                | In the Parents App, once per child; can be changed until the deadline.                                    |
| **Track responses**                       | Responded and not responded, per class.                                                                   |
| **Send reminder**                         | To parents who have not responded, sent by the user.                                                      |
| **Send automatic reminder**               | To parents who have not responded, 1 day before the deadline (default: on).                               |
| **Edit survey**                           | Only while no one has responded.                                                                          |
| **Close early**                           | Before the deadline; answers received are kept.                                                           |
| **Close automatically**                   | At the deadline.                                                                                          |
| **Create invoice lines for paid answers** | When the survey closes, one ad hoc invoice line per child for each answer with a fee, in Fees & Payments. |
| **View results**                          | Totals per question and answers per child.                                                                |
| **Export results**                        | Excel; web only.                                                                                          |

### 4.2 Consents

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication/surveys</u>](https://bba-sms-crm.lovable.app/communication/surveys)

| **Feature**                     | **Function**                                                                 |
|---------------------------------|------------------------------------------------------------------------------|
| **View consent list**           | Consent tab: title, audience, deadline, status, response rate.               |
| **Search**                      | Title.                                                                       |
| **Filter**                      | Status (Draft / Open / Closed), centre, class.                               |
| **Sort**                        | Default nearest deadline first.                                              |
| **Paging**                      | 20 / 50 / 100 rows; "1-20 of N".                                             |
| **Create consent form**         | Title, statement, attachments, Agree / Disagree.                             |
| **Set signature requirement**   | Signature on screen required or not (default: required).                     |
| **Set withdrawal rule**         | "Can be withdrawn" or "Final once given" (default: can be withdrawn).        |
| **Select audience**             | Centre, level or class, limited to the creator's scope.                      |
| **Set deadline**                | Date and time.                                                               |
| **Publish**                     | Sends to the audience; status Open.                                          |
| **Send push notification**      | Automatically on publish.                                                    |
| **Respond to consent (parent)** | Agree or Disagree and sign, once per child.                                  |
| **Withdraw consent (parent)**   | Only when the form allows it; the response and the withdrawal are both kept. |
| **Track responses**             | Agreed, disagreed, withdrawn, not responded.                                 |
| **Send reminder**               | To parents who have not responded, sent by the user.                         |
| **Edit consent form**           | Only while no one has responded.                                             |
| **Close early**                 | Before the deadline; responses received are kept.                            |
| **View consent record**         | Per child: response, signature, date, withdrawal.                            |
| **Export results**              | Excel; web only.                                                             |

## 5. Notifications

### 5.1 Notification centre

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication/notifications</u>](https://bba-sms-crm.lovable.app/communication/notifications)

| **Feature**                          | **Function**                                                                   |
|--------------------------------------|--------------------------------------------------------------------------------|
| **Send push notification**           | For every event in this module, to each guardian separately.                   |
| **View notification centre (app)**   | List of notifications per guardian account; each opens the record it is about. |
| **Show badge**                       | Unread count on the bell only.                                                 |
| **Filter**                           | Category, Read / Unread.                                                       |
| **Mark as read**                     | One notification.                                                              |
| **Mark all as read**                 | Every notification of the guardian.                                            |
| **View sent notification log (web)** | Recipient, category, record, sent at, read at.                                 |
| **Search**                           | Recipient name.                                                                |
| **Export**                           | Notification log to Excel.                                                     |

### 5.2 Notification settings

*Prototype:* [<u>https://bba-sms-crm.lovable.app/communication/notifications</u>](https://bba-sms-crm.lovable.app/communication/notifications)

| **Feature**                                    | **Function**                                                                  |
|------------------------------------------------|-------------------------------------------------------------------------------|
| **Turn category on or off (parent)**           | Routines, Fees, Messages, Announcements, Surveys & Consents, Approvals.       |
| **Set default categories**                     | HQ Admin sets the categories that are on for new guardians (default: all on). |
| **Turn Malaysia School Admin alert on or off** | Per centre (default: on for Malaysia centres, off for Singapore centres).     |

# 5. Business rules

## Scope and permissions

| **ID**         | **Rule**                                                                                                                                                                                     |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-COM-001** | The module covers communication with the parents of enrolled children and internal announcements to staff. Prospective families are handled in Enquiries.                                    |
| **BR-COM-002** | Who can create announcements, surveys and consents is a permission in Roles & permissions, configured by HQ Admin. By default it is on for HQ Admin and Centre Director and off for Teacher. |
| **BR-COM-003** | A creator can only send to audiences within their own scope (for example a Centre Director sends only to their centre).                                                                      |
| **BR-COM-004** | "Group parents in one conversation" is a separate permission. By default it is on for Centre Director, Centre Admin and HQ Admin.                                                            |
| **BR-COM-005** | "Reassign inquiries" is a separate permission. By default it is on for Centre Director, Centre Admin and HQ Admin.                                                                           |

## Announcements

| **ID**         | **Rule**                                                                                                                                  |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-COM-006** | Announcements are one-way. Parents cannot reply to an announcement; they use Messages or Inquiries.                                       |
| **BR-COM-007** | An announcement is sent either to Parents or to Staff, never both in one announcement.                                                    |
| **BR-COM-008** | A staff audience is selected by organisation, centre or role.                                                                             |
| **BR-COM-009** | Staff in the scope of a parent announcement (centre or class) see it as read-only.                                                        |
| **BR-COM-010** | A centre-wide announcement reaches a parent once, whatever number of children they have. A class or level announcement is sent per child. |
| **BR-COM-011** | Each announcement shows its scope (for example whole centre or class name) and its category.                                              |
| **BR-COM-012** | Announcement categories are a list managed by HQ Admin.                                                                                   |
| **BR-COM-013** | A scheduled announcement can be edited or cancelled until it is sent.                                                                     |
| **BR-COM-014** | Editing a sent announcement shows an "Edited" label. Recipients are notified again only if the editor ticks "Notify recipients again".    |
| **BR-COM-015** | A recalled announcement disappears from the Parents App and staff views; the record and its read counts are kept.                         |
| **BR-COM-016** | Reminders go only to recipients who have not read, or have not acknowledged when acknowledgement is required.                             |

## Messages

| **ID**         | **Rule**                                                                                                                                                       |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-COM-017** | Each child has one class thread per class. All class teachers and the Centre Director reply in the same thread.                                                |
| **BR-COM-018** | A teacher who joins a class sees the full history of that class's threads.                                                                                     |
| **BR-COM-019** | When a child changes class, a new thread is created and the old thread becomes read-only.                                                                      |
| **BR-COM-020** | Threads are kept until the child leaves the school, then become read-only for staff and are removed from the Parents App.                                      |
| **BR-COM-021** | Private threads are between the Centre Director and one family. There is no chat between staff members.                                                        |
| **BR-COM-022** | Bulk send creates or uses one thread per family. Families never see each other in a bulk send.                                                                 |
| **BR-COM-023** | Families are grouped in one conversation only by a user with the "Group parents in one conversation" permission. Every member sees who is in the conversation. |
| **BR-COM-024** | Each thread shows who is in it.                                                                                                                                |
| **BR-COM-025** | Opening a thread marks its messages as read on every device.                                                                                                   |
| **BR-COM-026** | A sender can recall their own message within 15 minutes (setting). The thread shows "Message removed" and the original is kept for audit.                      |
| **BR-COM-027** | Attachments are limited to 25 MB per file and 3 minutes per video (settings).                                                                                  |
| **BR-COM-028** | In Malaysia centres, the School Admin is notified each time a teacher sends a message to a parent. This is a setting per centre.                               |
| **BR-COM-029** | A thread counts as Unanswered when the last message is from a parent and no staff reply has been sent for 2 days (setting).                                    |

## Inquiries

| **ID**         | **Rule**                                                                                                                                                                                                                |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-COM-030** | Parents raise inquiries in the Parents App. Staff add inquiries received another way with the "Add an inquiry a family sent another way" form, recording the channel.                                                   |
| **BR-COM-031** | Every inquiry has a category, a child, a subject and an assignee.                                                                                                                                                       |
| **BR-COM-032** | Inquiry categories and their default assignees are configured by HQ Admin. Defaults: Fees to Centre Admin / School Admin; Birthday to the class teachers; all other categories to the Centre Director and Centre Admin. |
| **BR-COM-033** | Parents do not choose the assignee.                                                                                                                                                                                     |
| **BR-COM-034** | Inquiry statuses are Open, In progress and Closed.                                                                                                                                                                      |
| **BR-COM-035** | A parent can reopen a closed inquiry within 7 days (setting); after that they raise a new inquiry.                                                                                                                      |
| **BR-COM-036** | Inquiries are never deleted.                                                                                                                                                                                            |
| **BR-COM-037** | Every reply, status change and reassignment is recorded with who and when.                                                                                                                                              |

## Surveys and consents

| **ID**         | **Rule**                                                                                                                                                            |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-COM-038** | Surveys and consents are one module with two tabs: Survey (default) and Consent.                                                                                    |
| **BR-COM-039** | A survey or consent can be edited only while no one has responded.                                                                                                  |
| **BR-COM-040** | A parent answers once per child and can change the answer until the deadline.                                                                                       |
| **BR-COM-041** | A survey closes at its deadline or when closed early. Answers received are kept.                                                                                    |
| **BR-COM-042** | A survey option can carry a fee item and an amount. When the survey closes, each answer with a fee creates an ad hoc invoice line for the child in Fees & Payments. |
| **BR-COM-043** | A consent response records Agree or Disagree, the signature when required, the guardian and the date.                                                               |
| **BR-COM-044** | A consent marked "Can be withdrawn" can be withdrawn by the parent at any time. The original response and the withdrawal are both kept.                             |
| **BR-COM-045** | Results are exported on the web only.                                                                                                                               |

## Notifications

| **ID**         | **Rule**                                                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-COM-046** | Notifications are sent to each guardian separately, not once per family.                                                                   |
| **BR-COM-047** | Each notification says which children it covers and opens the exact record it is about.                                                    |
| **BR-COM-048** | Notification categories are Routines, Fees, Messages, Announcements, Surveys & Consents and Approvals.                                     |
| **BR-COM-049** | A parent can turn each category on or off. Turning a category off stops push notifications; items stay visible in the notification centre. |
| **BR-COM-050** | The unread badge is shown on the bell only, and matches the count in the notification centre.                                              |
| **BR-COM-051** | Phase 1 sends push and in-app notifications only. No SMS and no email digest.                                                              |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                     | **Recipient**                                | **Channel**                       | **When**                                                           |
|--------------------------------------|----------------------------------------------|-----------------------------------|--------------------------------------------------------------------|
| **New announcement**                 | Parents in the audience                      | Push + in-app                     | When published or at the scheduled time                            |
| **Internal announcement**            | Staff in the audience                        | In-app (web) + push (Teacher App) | When published or at the scheduled time                            |
| **Announcement edited**              | Recipients                                   | Push + in-app                     | When edited and "Notify recipients again" is ticked                |
| **Announcement reminder**            | Recipients who have not read or acknowledged | Push + in-app                     | When the sender sends a reminder                                   |
| **New message**                      | Guardians and staff in the thread            | Push + in-app                     | When a message is sent                                             |
| **Teacher message alert (Malaysia)** | School Admin                                 | In-app                            | When a teacher sends a message to a parent, if on for the centre   |
| **New inquiry**                      | Assignee                                     | In-app (web) + push (Teacher App) | When an inquiry is raised or added                                 |
| **Inquiry reassigned**               | New assignee                                 | In-app (web) + push (Teacher App) | When an inquiry is reassigned                                      |
| **Inquiry reply**                    | Parent                                       | Push + in-app                     | When staff reply                                                   |
| **Inquiry status change**            | Parent                                       | Push + in-app                     | When the status changes                                            |
| **New survey or consent**            | Parents in the audience                      | Push + in-app                     | When published                                                     |
| **Survey or consent reminder**       | Parents who have not responded               | Push + in-app                     | When sent by the user, and automatically 1 day before the deadline |
| **Consent withdrawn**                | Creator of the consent form, Centre Director | In-app (web)                      | When a parent withdraws consent                                    |

## 6.2 Documents

- Announcement, survey and consent attachments (images, PDF) uploaded by staff.

- Consent record per child with response, signature and date, viewable and exportable on the web.

# 7. Reports & exports

| **Report**                                | **Content**                                                                | **Used by**                             |
|-------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------|
| **Announcement read and acknowledgement** | Sent, read and acknowledged per announcement, with the list of who has not | HQ Admin, Centre Director               |
| **Inquiry list**                          | Inquiries by category, status, assignee and waiting time                   | HQ Admin, Centre Director, Centre Admin |
| **Survey results**                        | Answers per question and per child, including paid answers                 | Creator, Centre Director, HQ Admin      |
| **Consent results**                       | Agreed, disagreed, withdrawn and not responded per child                   | Creator, Centre Director, HQ Admin      |
| **Notification log**                      | Notifications sent and read per recipient                                  | HQ Admin                                |

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
<td><strong>AC-COM-001</strong></td>
<td>Create permission</td>
<td>Given a Teacher has the "Create announcement" permission turned off,<br />
when the Teacher opens Announcements,<br />
then the Teacher sees announcements of their classes read-only and there is no create button.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-002</strong></td>
<td>Creator scope</td>
<td>Given the Centre Director of centre A creates an announcement,<br />
when they choose the parent audience,<br />
then only centre A and its levels and classes can be selected.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-003</strong></td>
<td>Internal announcement</td>
<td>Given HQ Admin publishes a Staff announcement to the role Teacher at centre A,<br />
when it is sent,<br />
then every teacher of centre A sees it in the SMS web and the Teacher app, and no parent receives it.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-004</strong></td>
<td>Staff view of parent announcement</td>
<td>Given a parent announcement was sent to class K1 Sunflower,<br />
when a teacher of K1 Sunflower opens Announcements,<br />
then the teacher sees the announcement read-only.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-005</strong></td>
<td>One announcement per parent</td>
<td>Given a parent has two children at centre A,<br />
when a centre-wide announcement is published,<br />
then the parent receives it once.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-006</strong></td>
<td>Scheduled announcement</td>
<td>Given an announcement is scheduled for 20 October 2026 at 08:00,<br />
when that time passes,<br />
then the status changes from Scheduled to Sent and parents receive a push notification.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-007</strong></td>
<td>Acknowledgement reminder</td>
<td>Given an announcement requires acknowledgement and 12 of 40 parents have not acknowledged,<br />
when the sender sends a reminder,<br />
then only those 12 parents receive it.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-008</strong></td>
<td>Recall</td>
<td>Given a sent announcement,<br />
when the sender recalls it,<br />
then it disappears from the Parents App and remains in the web list with status Recalled.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-009</strong></td>
<td>Class change thread</td>
<td>Given Emma moves from K1 Sunflower to K2 Rainbow on 1 November 2026,<br />
when the move is saved,<br />
then a new K2 Rainbow thread is created for Emma's guardians and the K1 Sunflower thread becomes read-only.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-010</strong></td>
<td>New teacher sees history</td>
<td>Given a teacher joins K2 Rainbow,<br />
when they open a child's class thread,<br />
then they see every earlier message in that thread.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-011</strong></td>
<td>No staff chat</td>
<td>Given a Centre Director opens Messages,<br />
when they look for a way to start a thread with a teacher,<br />
then no such option exists.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-012</strong></td>
<td>Bulk send</td>
<td>Given the Centre Director sends one message to 15 families,<br />
when it is sent,<br />
then each family receives it in its own thread and no family sees another.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-013</strong></td>
<td>Malaysia admin alert</td>
<td>Given the alert is on for a Malaysia centre,<br />
when a teacher sends a message to a parent,<br />
then the School Admin receives an in-app notification.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-014</strong></td>
<td>Fee inquiry routing</td>
<td>Given a parent raises an inquiry with category Fees,<br />
when it is submitted,<br />
then it is assigned to the Centre Admin / School Admin of the child's centre with status Open.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-015</strong></td>
<td>Inquiry added by staff</td>
<td>Given a parent asks a question by phone,<br />
when the Centre Admin uses "Add an inquiry a family sent another way" with channel Phone,<br />
then the inquiry appears in the list with status Open and the parent sees it in the Parents App.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-016</strong></td>
<td>Reassign permission</td>
<td>Given a Teacher does not have the "Reassign inquiries" permission,<br />
when they open an assigned inquiry,<br />
then the reassign action is not available.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-017</strong></td>
<td>Paid survey answer</td>
<td>Given a field trip survey has the option "Joining: $25" and closes on 25 October 2026,<br />
when it closes with 18 children answering "Joining",<br />
then 18 ad hoc invoice lines of $25 are created in Fees &amp; Payments, one per child.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-018</strong></td>
<td>Survey edit lock</td>
<td>Given a survey has received one response,<br />
when the creator tries to edit a question,<br />
then the system blocks the edit.</td>
</tr>
<tr class="odd">
<td><strong>AC-COM-019</strong></td>
<td>Consent withdrawal</td>
<td>Given a parent agreed to a consent marked "Can be withdrawn" on 5 October 2026,<br />
when the parent withdraws it on 12 October 2026,<br />
then the consent shows Withdrawn and both the agreement and the withdrawal remain on record.</td>
</tr>
<tr class="even">
<td><strong>AC-COM-020</strong></td>
<td>Category turned off</td>
<td>Given a parent has turned off Announcements,<br />
when a new announcement is published,<br />
then the parent receives no push notification and the announcement still appears in the notification centre.</td>
</tr>
</tbody>
</table>
