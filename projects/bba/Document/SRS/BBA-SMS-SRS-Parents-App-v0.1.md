Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Parents App**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-PAR-NNN and acceptance criteria AC-PAR-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Parents App of the Busy Bees Asia School Management System (SMS), Phase 1. The Parents App is the mobile app that parents and guardians use to follow their child's day, talk to the centre, pay fees and complete joining and leaving steps. It replaces the Taidii parent app.

The Parents App is the parent side of the SMS modules Children & Families, Communication, Daily Operations, Learning, Fees & Payments and Joining & Leaving. The business rules in this document match those modules. Where a rule is about what staff do, it is described in the module concerned.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-parents.lovable.app. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Account and sign-in: one account per guardian, created after the booking fee is paid; switching between children.

- Home: announcements, today's arrival, latest class update, the most urgent fee reminder and pinned features.

- Attendance and the child's day: check-in and check-out records with handover photos and temperatures, daily routines, leave requests.

- Health and care: health information and allergies entered by the parent, attachments, vaccination record, growth and temperature history, authorised pickup persons, requested documents.

- Communication: announcements, messages with the class and the Centre Director, inquiries, surveys and consents.

- Learning: class updates, photo gallery, published progress reports and portfolios.

- Fees: invoices, receipts, credits, PayNow payment, refunds and the refund account.

- Joining and leaving: registration form, signatures, documents, handbook, e-Form 1 acknowledgement, start date change, withdrawal request.

- Centre calendar.

- Notifications and settings: notification centre, push settings per category, contact details.

## 1.2 Not in Phase 1

- SingPass (MyInfo) sign-in and data retrieval.

- Event and parent-teacher conference (PTC) slot booking.

- Medication requests and medication records.

- Activity log.

- Homework and learning progress beyond published progress reports and portfolios.

- Comments on class updates, photos and announcements (parents react with a heart only).

- Group chats between several families created by parents.

- Paying several invoices with one PayNow QR.

- Enrichment enrolment or withdrawal through the app.

- One-time (temporary) pickup persons.

- Resource library.

- Automatic translation of messages and content.

- App languages other than English.

- SMS notifications and email digests.

- Referral programme (submitting and tracking referrals).

- Temporary withdrawal requests by parents (temporary withdrawals are created by centre users).

# 2. Who uses it

| **Role**                        | **What they do in this module**                                                                                                                                 |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Parent / guardian**           | Uses the app for their own children only. Each guardian has an own account and receives their own notifications.                                                |
| **Primary contact**             | The guardian who completes the registration form for a new child and receives joining reminders.                                                                |
| **Billing contact**             | The guardian named on invoices; receives fee reminders and confirms the refund account. Any guardian with an account can view invoices and pay.                 |
| **Second guardian**             | Has an own account and sees the same children; signs the second signature box of the registration form.                                                         |
| **Centre Director**             | Approves leave, pickup persons and start date changes; replies in class and private threads; receives withdrawal requests (staff side, SMS web and staff apps). |
| **Centre Admin / School Admin** | Sends app invitations and document requests; reviews documents and registrations; answers fee and general inquiries (staff side).                               |
| **Teacher**                     | Records check-in, check-out, temperatures and routines; posts class updates; replies in class threads (staff side).                                             |
| **HQ Finance**                  | Bills invoices, issues receipts and processes refunds that parents see in the app (staff side).                                                                 |

# 3. Process overview

## P1. Account and registration

1\. The family pays the booking fee in Enquiries.

2\. The system creates an account for each guardian and emails the activation instructions.

3\. The primary contact completes Part A of the registration form (details, documents, pickup persons, allergies, diet, emergency contacts) and may complete or skip Part B (GIRO).

4\. Both guardians sign, the primary contact acknowledges the handbook and submits.

5\. The centre verifies the form or returns a step for correction; the parent is notified.

6\. Before the start date the parent acknowledges the e-Form 1 prompt and receives the first-day reminder.

## P2. A child's day

1\. Staff check the child in at the gate; the parent is notified with the time and the handover photo.

2\. Staff record temperatures and routines during the day.

3\. Staff check the child out to an approved pickup person; the parent is notified with the name of the person.

4\. The parent receives one "Daily routines updated" notification and views the day in Routines and Attendance.

## P3. Leave request

1\. The parent opens Leave request and chooses Personal or Medical leave.

2\. The parent enters the dates, a description and optional attachments, and reads the two notices.

3\. The parent submits; the request shows Pending.

4\. The Centre Director (or a delegated Senior Teacher) decides; the parent is notified and approved days show On leave.

## P4. Authorised pickup

1\. The parent adds a person with photo, full name, relationship, NRIC/FIN and phone number and accepts the terms.

2\. The request shows Pending until the Centre Director or School Admin decides.

3\. Approved persons appear on the pickup list used at check-out; the parent is notified of the decision.

4\. The parent can remove a person at any time; the removal applies at once and the centre is notified.

## P5. Paying a fee

1\. The parent receives a notification when an invoice is Billed and opens it in Fees.

2\. For an invoice not being collected by GIRO, the parent taps Pay, checks the summary and gets the PayNow QR.

3\. The parent pays from the banking app; the invoice becomes Paid and the receipt appears immediately.

4\. Unpaid families are reminded on the 15th and 25th; failed GIRO deductions are notified with the reason and can be paid by PayNow.

## P6. Refund

1\. A refund request is created by the centre or Finance (for example after a withdrawal) and approved by Finance.

2\. The billing contact is asked in the app to confirm the refund account (PayNow by mobile number, NRIC or UEN).

3\. Money paid from CDA goes back to CDA; no account is asked for that part.

4\. The parent is notified when the refund succeeds or fails; after a failure the parent updates the account.

## P7. Withdrawal

1\. The parent opens the child profile and taps Withdraw at the bottom.

2\. The parent chooses a reason and a preferred last day; the notice period of the centre and level is shown.

3\. If the preferred last day gives less notice than required, the app warns that the deposit may be forfeited.

4\. The parent submits; the button turns grey and the centre is alerted.

5\. The centre talks with the family; the parent is notified of the outcome and the locked last day.

# 4. Modules, sub-modules, features and functions

## 1. Account & sign-in

### 1.1 Sign in

*Prototype:* [<u>https://bba-parents.lovable.app/signin</u>](https://bba-parents.lovable.app/signin)

| **Feature**                         | **Function**                                                                                |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| **Activate account**                | From the activation email sent after the booking fee is paid; the guardian sets a password. |
| **Sign in with email and password** | Default sign-in method.                                                                     |
| **Sign in with Google**             | Linked to the guardian's email address.                                                     |
| **Sign in with Microsoft**          | Linked to the guardian's email address.                                                     |
| **Reset password**                  | Reset link sent to the guardian's email address.                                            |
| **Change sign-in method**           | From Profile; the account and its children stay the same.                                   |
| **Sign out**                        | From Profile.                                                                               |

### 1.2 My children

*Prototype:* [<u>https://bba-parents.lovable.app/children</u>](https://bba-parents.lovable.app/children)

| **Feature**              | **Function**                                                                            |
|--------------------------|-----------------------------------------------------------------------------------------|
| **View linked children** | Every child linked to the guardian, across brands, centres and countries.               |
| **Switch child**         | Every screen then shows the selected child only.                                        |
| **View child profile**   | Photo, name, brand, centre, class and country.                                          |
| **View classes**         | Main class and enrichment classes with their teachers; other children are never listed. |

## 2. Home

### 2.1 Home

*Prototype:* [<u>https://bba-parents.lovable.app/</u>](https://bba-parents.lovable.app/)

| **Feature**                  | **Function**                                                                     |
|------------------------------|----------------------------------------------------------------------------------|
| **View latest announcement** | Shown at the top, above today's records and fees.                                |
| **View today's arrival**     | Time, the adult who dropped the child off, temperature and handover photo.       |
| **View latest class update** | Today's or the most recent update only.                                          |
| **View fee reminder**        | At most one reminder, the most urgent: GIRO failed, then overdue, then upcoming. |
| **Open notifications**       | From the bell, which shows the unread count.                                     |
| **Open pinned feature**      | Each tile opens the feature directly.                                            |

### 2.2 All features

*Prototype:* [<u>https://bba-parents.lovable.app/features</u>](https://bba-parents.lovable.app/features)

| **Feature**           | **Function**                                                         |
|-----------------------|----------------------------------------------------------------------|
| **View all features** | Grouped as My child's day, Learning, Health & care, School & family. |
| **Pin feature**       | Adds the feature to Home; maximum 8.                                 |
| **Unpin feature**     | Removes the feature from Home; minimum 4.                            |
| **Reset to default**  | Restores the default 8 features.                                     |

## 3. Attendance & day

### 3.1 Attendance

*Prototype:* [<u>https://bba-parents.lovable.app/attendance</u>](https://bba-parents.lovable.app/attendance)

| **Feature**                   | **Function**                                                               |
|-------------------------------|----------------------------------------------------------------------------|
| **View daily record**         | Check-in and check-out times for each day.                                 |
| **View dropped off by**       | The adult who handed the child over.                                       |
| **View picked up by**         | The adult who collected the child.                                         |
| **View handover photo**       | Photo taken at check-in and at check-out.                                  |
| **View temperature readings** | Every reading of the day with its time and label.                          |
| **View monthly summary**      | Days present and days absent in the month.                                 |
| **View absent day**           | The reason shown for the day: on leave, closure, public holiday or absent. |
| **Pick a date**               | Jump to any date since the child started.                                  |

### 3.2 Routines

*Prototype:* [<u>https://bba-parents.lovable.app/routines</u>](https://bba-parents.lovable.app/routines)

| **Feature**                | **Function**                                                              |
|----------------------------|---------------------------------------------------------------------------|
| **View routines by day**   | Meals, snacks, bottles, naps, nappy and toilet records recorded by staff. |
| **Pick a date**            | Date picker to jump to an earlier day.                                    |
| **Filter by routine type** | Meals, snacks, naps, nappy and toilet.                                    |
| **Add note from home**     | A note for the day (sleep, appetite, mood) that staff read in their apps. |
| **View empty day reason**  | Closure, public holiday, absent, or nothing recorded yet.                 |

### 3.3 Leave requests

*Prototype:* [<u>https://bba-parents.lovable.app/requests/leave</u>](https://bba-parents.lovable.app/requests/leave)

| **Feature**                | **Function**                                                                                                             |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **View request list**      | Leave and pickup requests with status Pending, Approved or Rejected.                                                     |
| **Filter by request type** | Leave, pickup.                                                                                                           |
| **Create leave request**   | Child, leave type, from date, to date, description.                                                                      |
| **Select leave type**      | Personal or Medical.                                                                                                     |
| **Attach file**            | JPEG, PNG or PDF, for example a medical certificate.                                                                     |
| **Show leave notices**     | A Singapore child needs at least one attendance day each month to keep the subsidy; fees are not reduced for leave days. |
| **Edit pending request**   | Allowed until the centre decides.                                                                                        |
| **View request detail**    | Dates, type, attachments, status, who decided and when.                                                                  |

## 4. Health & care

### 4.1 Health

*Prototype:* [<u>https://bba-parents.lovable.app/health</u>](https://bba-parents.lovable.app/health)

| **Feature**                           | **Function**                                                                         |
|---------------------------------------|--------------------------------------------------------------------------------------|
| **View health overview**              | Critical allergy and medical notes at the top, then growth and today's temperatures. |
| **Enter required health information** | Allergies, skin conditions, respiratory conditions and the child's medical history.  |
| **Enter optional health information** | Diet and daily habits (eating, naps, daily habits).                                  |
| **Set allergy severity**              | Mild, Moderate or Severe.                                                            |
| **Edit health information**           | The parent edits what the parent entered; the centre is notified.                    |
| **Write family note**                 | Free text for the child's teachers.                                                  |
| **Upload health attachment**          | Medical letters or reports.                                                          |
| **Upload vaccination record**         | Vaccination record file.                                                             |
| **View height and weight**            | Latest values and a growth chart.                                                    |
| **View measurement history**          | Date measured, height, weight.                                                       |
| **View temperature history**          | Daily readings; readings of 37.5°C or more are marked as raised.                     |
| **View change history**               | Who changed each item and when.                                                      |

### 4.2 Authorised pickup

*Prototype:* [<u>https://bba-parents.lovable.app/requests/new</u>](https://bba-parents.lovable.app/requests/new)

| **Feature**                                | **Function**                                            |
|--------------------------------------------|---------------------------------------------------------|
| **View pickup list**                       | Approved and pending persons with their status.         |
| **Add pickup person**                      | Photo, full name, relationship, NRIC/FIN, phone number. |
| **Accept terms**                           | Tick box; no signature.                                 |
| **Add again a removed or rejected person** | Past persons are offered for a new request.             |
| **Submit request**                         | Status Pending until the centre decides.                |
| **Remove pickup person**                   | No approval; applies at once; the centre is notified.   |
| **View decision**                          | Approved, or Rejected with the reason.                  |

### 4.3 Documents

*Prototype:* [<u>https://bba-parents.lovable.app/profile</u>](https://bba-parents.lovable.app/profile)

| **Feature**                          | **Function**                                                            |
|--------------------------------------|-------------------------------------------------------------------------|
| **View requested documents**         | Document type and status Missing, Pending review, Accepted or Rejected. |
| **Upload document**                  | For a document requested by the centre.                                 |
| **Upload again a rejected document** | The rejection reason is shown.                                          |

## 5. Communication

### 5.1 Announcements

*Prototype:* [<u>https://bba-parents.lovable.app/announcements</u>](https://bba-parents.lovable.app/announcements)

| **Feature**                  | **Function**                                                           |
|------------------------------|------------------------------------------------------------------------|
| **View announcement list**   | Newest first, with source (HQ or Centre), category, audience and date. |
| **Search**                   | Title and text.                                                        |
| **Filter by category**       | For example Event, Payment, Health & safety, Closure, General.         |
| **View attachments**         | Images and files.                                                      |
| **Acknowledge announcement** | "Acknowledge" button when the sender requires it.                      |
| **React with a heart**       | No comment box.                                                        |
| **Open linked survey**       | When the announcement links to a survey or consent.                    |

### 5.2 Messages

*Prototype:* [<u>https://bba-parents.lovable.app/messages</u>](https://bba-parents.lovable.app/messages)

| **Feature**                     | **Function**                                                                     |
|---------------------------------|----------------------------------------------------------------------------------|
| **View thread list**            | Class threads per child and private threads with the Centre Director.            |
| **Search**                      | Child, class and message text.                                                   |
| **Open class thread**           | Shared by all class teachers and the Centre Director; shows who is in it.        |
| **Open private thread**         | Between the family and the Centre Director; teachers do not see it.              |
| **Send text**                   |                                                                                  |
| **Send photo**                  | Up to 25 MB per file.                                                            |
| **Send video**                  | Up to 3 minutes.                                                                 |
| **Send document**               | Up to 25 MB per file.                                                            |
| **Quote class update or photo** | From a class update or the gallery; the item is shown at the top of the message. |
| **View read receipt**           | "Seen" with time.                                                                |
| **Recall own message**          | Within 15 minutes; the thread shows "Message removed".                           |
| **View old class thread**       | Read-only after the child changes class.                                         |

### 5.3 Inquiries

*Prototype:* [<u>https://bba-parents.lovable.app/messages</u>](https://bba-parents.lovable.app/messages)

| **Feature**           | **Function**                                                           |
|-----------------------|------------------------------------------------------------------------|
| **View inquiry list** | Subject, category, child, status, date.                                |
| **Filter by status**  | Open, In progress, Closed.                                             |
| **Create inquiry**    | Category, child, subject, details.                                     |
| **Select category**   | From the list set by HQ Admin; the parent does not choose who answers. |
| **Attach file**       | JPEG, PNG or PDF.                                                      |
| **View reply**        | Answer, who answered and when.                                         |
| **Reopen inquiry**    | Within 7 days of closing; after that the parent raises a new inquiry.  |

### 5.4 Surveys & consents

*Prototype:* [<u>https://bba-parents.lovable.app/forms</u>](https://bba-parents.lovable.app/forms)

| **Feature**                    | **Function**                                                 |
|--------------------------------|--------------------------------------------------------------|
| **View survey list**           | Survey tab (default): title, deadline, status.               |
| **View consent list**          | Consent tab: title, status, expiry where it applies.         |
| **View attachment**            | Memo or file attached to the form.                           |
| **Answer survey**              | Once per child.                                              |
| **Change answer**              | Until the deadline.                                          |
| **View fee before submitting** | When an option carries a fee, the amount and what it covers. |
| **Respond to consent**         | Agree or Disagree, once per child.                           |
| **Sign consent**               | When the consent requires a signature.                       |
| **Withdraw consent**           | Only when the consent allows it.                             |
| **View submitted forms**       | Answers, signature and date.                                 |

## 6. Learning

### 6.1 Class updates

*Prototype:* [<u>https://bba-parents.lovable.app/weekly</u>](https://bba-parents.lovable.app/weekly)

| **Feature**            | **Function**                                                       |
|------------------------|--------------------------------------------------------------------|
| **View class updates** | Text, photos and videos posted for the child's class or the child. |
| **React with a heart** | No comment box.                                                    |
| **Reply privately**    | Opens the class thread with the update quoted.                     |

### 6.2 Photo gallery

*Prototype:* [<u>https://bba-parents.lovable.app/gallery</u>](https://bba-parents.lovable.app/gallery)

| **Feature**                     | **Function**                               |
|---------------------------------|--------------------------------------------|
| **View my child's album**       | Photos the child is tagged in.             |
| **View class album**            | Photos tagged with the child's class.      |
| **View learning domain albums** | Created automatically from tags.           |
| **Filter by class**             | Classes the child has been in.             |
| **Filter by school year**       |                                            |
| **React with a heart**          | No comment box.                            |
| **Download photo**              | One photo to the phone.                    |
| **Download album**              | All photos of an album by a download link. |
| **Share download link**         | The link expires after 7 days.             |

### 6.3 Progress reports & portfolios

*Prototype:* [<u>https://bba-parents.lovable.app/portfolio</u>](https://bba-parents.lovable.app/portfolio)

| **Feature**                        | **Function**                                |
|------------------------------------|---------------------------------------------|
| **View report and portfolio list** | Published items only, with period and date. |
| **Filter by school year**          |                                             |
| **Filter by term**                 |                                             |
| **Open PDF**                       | Read-only, in the app.                      |
| **Download PDF**                   |                                             |

## 7. Fees

### 7.1 Invoices

*Prototype:* [<u>https://bba-parents.lovable.app/fees</u>](https://bba-parents.lovable.app/fees)

| **Feature**                  | **Function**                                                                                              |
|------------------------------|-----------------------------------------------------------------------------------------------------------|
| **View outstanding balance** | Total of unpaid Billed invoices of the child.                                                             |
| **View invoice list**        | Number, description, amount, due date, status, payment method.                                            |
| **Filter by status**         | All, Unpaid, Overdue, Paid.                                                                               |
| **Sort**                     | Newest first or oldest first.                                                                             |
| **View invoice detail**      | Lines, subsidy, credit applied, amount to pay, payments.                                                  |
| **View GIRO state**          | For example "GIRO deduction scheduled · 5 Oct" or "GIRO deduction failed · 3 Sep" with the bank's reason. |
| **Download invoice**         | PDF.                                                                                                      |

### 7.2 PayNow

*Prototype:* [<u>https://bba-parents.lovable.app/fees/INV-2609</u>](https://bba-parents.lovable.app/fees/INV-2609)

| **Feature**                            | **Function**                                                  |
|----------------------------------------|---------------------------------------------------------------|
| **View payment summary**               | Invoice and amount before the QR is shown.                    |
| **Show PayNow QR**                     | For one invoice; generated after the parent taps Pay.         |
| **Confirm payment**                    | Automatic when the payment arrives; the receipt is shown.     |
| **Hide PayNow during GIRO collection** | "Being collected by GIRO" until the bank result is uploaded.  |
| **Pay failed GIRO deduction**          | PayNow is offered for an invoice whose GIRO deduction failed. |

### 7.3 Receipts

*Prototype:* [<u>https://bba-parents.lovable.app/fees/receipt</u>](https://bba-parents.lovable.app/fees/receipt)

| **Feature**           | **Function**                  |
|-----------------------|-------------------------------|
| **View receipt list** | Number, amount, method, date. |
| **View receipt**      | Invoices paid, method, date.  |
| **Download receipt**  | PDF.                          |

### 7.4 Credits

*Prototype:* [<u>https://bba-parents.lovable.app/fees</u>](https://bba-parents.lovable.app/fees)

| **Feature**               | **Function**                                             |
|---------------------------|----------------------------------------------------------|
| **View credit remaining** | Total unused credit, with the CDA part shown separately. |
| **View credit applied**   | Which invoice each credit was used on, and when.         |

### 7.5 Refunds

*Prototype:* [<u>https://bba-parents.lovable.app/fees/refund/RF-2612</u>](https://bba-parents.lovable.app/fees/refund/RF-2612)

| **Feature**                | **Function**                                                           |
|----------------------------|------------------------------------------------------------------------|
| **View refund list**       | Number, amount, status.                                                |
| **View refund detail**     | Lines for credit and deposit, offsets, destination, status.            |
| **Confirm refund account** | PayNow by mobile number, NRIC or UEN, with a responsibility statement. |
| **Update refund account**  | After a failed refund.                                                 |
| **Mask account details**   | Only the last digits are shown.                                        |

## 8. Joining & leaving

### 8.1 Registration

*Prototype:* [<u>https://bba-parents.lovable.app/</u>](https://bba-parents.lovable.app/)

| **Feature**                    | **Function**                                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------------------------|
| **Open registration form**     | From the notification or Home; pre-filled from the enquiry.                                                |
| **Complete Part A**            | Mandatory, step by step: personal details, documents, pickup persons, allergies, diet, emergency contacts. |
| **Upload birth certificate**   | Skipped for an unborn child; reminded before the start date.                                               |
| **Upload immunisation record** | Skipped for an unborn child; reminded before the start date.                                               |
| **Complete Part B (GIRO)**     | Bank (DBS, OCBC, UOB) and method (paper form or e-GIRO).                                                   |
| **Skip Part B**                | GIRO can be set up later.                                                                                  |
| **Save and continue later**    | Completed steps are kept.                                                                                  |
| **Sign registration**          | Two signature boxes, both required; a sole guardian signs both.                                            |
| **Acknowledge handbook**       | The brand's handbook opens as a read-only PDF; tick to confirm receipt.                                    |
| **Submit registration**        | Sends the form to the centre.                                                                              |
| **Correct returned step**      | The step and the reason are shown.                                                                         |

### 8.2 Before the first day

*Prototype:* [<u>https://bba-parents.lovable.app/</u>](https://bba-parents.lovable.app/)

| **Feature**                        | **Function**                                                             |
|------------------------------------|--------------------------------------------------------------------------|
| **Acknowledge e-Form 1**           | Pre-filled from the registration; at least 7 days before the start date. |
| **Request start date change**      | New date and reason; applies after the centre approves.                  |
| **Sign T&C on transfer**           | The receiving centre's T&C.                                              |
| **Review details on re-enrolment** | Pre-filled details and documents; sign the current T&C.                  |

### 8.3 Withdrawal

*Prototype:* [<u>https://bba-parents.lovable.app/requests/withdrawal</u>](https://bba-parents.lovable.app/requests/withdrawal)

| **Feature**                 | **Function**                                                                               |
|-----------------------------|--------------------------------------------------------------------------------------------|
| **Open withdrawal**         | From the bottom of the child profile only.                                                 |
| **Select reason**           | From the list set by HQ Admin.                                                             |
| **Pick preferred last day** | Any date can be chosen.                                                                    |
| **View notice period**      | Notice period of the child's centre and level, and the earliest last day with full notice. |
| **Show deposit warning**    | When the preferred last day gives less than the required notice.                           |
| **Add comment**             | Optional.                                                                                  |
| **Submit withdrawal**       | The centre is alerted; the button turns grey and shows "Withdrawal request submitted".     |

## 9. Calendar

### 9.1 Calendar

*Prototype:* [<u>https://bba-parents.lovable.app/calendar</u>](https://bba-parents.lovable.app/calendar)

| **Feature**              | **Function**                                              |
|--------------------------|-----------------------------------------------------------|
| **View month**           | Events, closures and public holidays shared with parents. |
| **Pick a date**          |                                                           |
| **Filter by event type** |                                                           |
| **View event detail**    | Date, time, description, attachments.                     |
| **View closure reason**  |                                                           |

## 10. Settings & notifications

### 10.1 Notifications

*Prototype:* [<u>https://bba-parents.lovable.app/notifications</u>](https://bba-parents.lovable.app/notifications)

| **Feature**                  | **Function**                                                            |
|------------------------------|-------------------------------------------------------------------------|
| **View notification centre** | "Needs you" items first, then activity by day.                          |
| **Search**                   | Title and text.                                                         |
| **Filter by period**         | 7 days, 30 days, 3 months, All.                                         |
| **Filter by category**       | Routines, Fees, Messages, Announcements, Surveys & Consents, Approvals. |
| **Open record**              | Each notification opens the exact record it is about.                   |
| **Mark all read**            |                                                                         |
| **View unread badge**        | On the bell only.                                                       |

### 10.2 Profile & settings

*Prototype:* [<u>https://bba-parents.lovable.app/profile</u>](https://bba-parents.lovable.app/profile)

| **Feature**                  | **Function**                                                                   |
|------------------------------|--------------------------------------------------------------------------------|
| **View parent profile**      | Name, relationship, phone, email, children.                                    |
| **Edit own contact details** | Phone number, email and address; the change is recorded in the family history. |
| **View family contacts**     | Guardians of the child and the billing contact.                                |
| **Turn category on**         | Push notifications for the category.                                           |
| **Turn category off**        | Stops push only; items still appear under the bell.                            |
| **Open withdrawal**          | Last item of the child profile.                                                |

# 5. Business rules

## Accounts and access

| **ID**         | **Rule**                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-001** | Each guardian has an own account. Accounts are created after the family pays the booking fee and activated from an email.     |
| **BR-PAR-002** | One account shows every child linked to that guardian, across brands, centres and countries.                                  |
| **BR-PAR-003** | A guardian sees only their own children. No screen shows another child's name, photo or record.                               |
| **BR-PAR-004** | Switching child changes every screen; no screen keeps the previous child's data.                                              |
| **BR-PAR-005** | Guardians who are not parents get no account by default. An account is created only on request and with the parent's consent. |
| **BR-PAR-006** | A parent can change own contact details but never the child's enrolment, class or centre.                                     |
| **BR-PAR-007** | A child on temporary withdrawal is hidden from attendance and class views in the app until the child returns.                 |
| **BR-PAR-008** | The app is in English. The registration form shows Chinese text next to the English.                                          |

## Home

| **ID**         | **Rule**                                                                                                                            |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-009** | The Home screen shows between 4 and 8 pinned features (default: 8). The app explains why when a change would go below 4 or above 8. |
| **BR-PAR-010** | Home shows at most one fee reminder. A failed GIRO deduction comes first, then an overdue invoice, then an upcoming invoice.        |
| **BR-PAR-011** | An overdue reminder is shown to every family. An upcoming reminder is shown only to families who do not pay by GIRO.                |

## Attendance and routines

| **ID**         | **Rule**                                                                                                                               |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-012** | Only staff check a child in and out. Parents cannot check in or check out.                                                             |
| **BR-PAR-013** | The app shows the adult who dropped off and the adult who picked up, never the staff member who recorded it.                           |
| **BR-PAR-014** | A day can hold any number of temperature readings, each with the label staff entered. A reading of 37.5°C or more is marked as raised. |
| **BR-PAR-015** | The late flag is never shown to parents.                                                                                               |
| **BR-PAR-016** | Routines are read-only for parents. The parent can add one note from home per day.                                                     |
| **BR-PAR-017** | Parents receive one "Daily routines updated" notification per day, when the child is checked out.                                      |

## Leave

| **ID**         | **Rule**                                                                                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-018** | Leave type is Personal or Medical. Attachments are optional.                                                                                                             |
| **BR-PAR-019** | Before submitting, the parent sees two notices: a Singapore child needs at least one attendance day each month to keep the subsidy; fees are not reduced for leave days. |
| **BR-PAR-020** | A leave request can be edited until it is decided. Approved leave days show On leave in Attendance.                                                                      |

## Health

| **ID**         | **Rule**                                                                                                              |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-021** | The parent is the source of health information. Health information has a Required part and an Optional part.          |
| **BR-PAR-022** | Staff never change what the parent entered. Staff notes are kept separately and shown separately.                     |
| **BR-PAR-023** | Every change records who changed it and when, and the parent can see it.                                              |
| **BR-PAR-024** | When the parent changes allergy information, the Centre Director, School Admin and the child's teachers are notified. |
| **BR-PAR-025** | Parents upload the vaccination record even when SingPass shows vaccinations as complete.                              |

## Authorised pickup and documents

| **ID**         | **Rule**                                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-026** | There is no limit on the number of authorised pickup persons. Authorisation has no dates; it lasts until removed. |
| **BR-PAR-027** | Each new person needs approval by the Centre Director or the School Admin. Rejecting requires a reason.           |
| **BR-PAR-028** | Removing a person needs no approval, applies at once, and notifies the centre.                                    |
| **BR-PAR-029** | Parents upload documents the centre requests. A new upload replaces the current file; earlier versions are kept.  |

## Communication

| **ID**         | **Rule**                                                                                                                                                                              |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-030** | Announcements are one-way. Parents can acknowledge when required and react with a heart; they cannot comment.                                                                         |
| **BR-PAR-031** | A centre-wide announcement reaches a guardian once, whatever number of children they have. A class or level announcement is sent per child.                                           |
| **BR-PAR-032** | Each child has one class thread per class, shared by all class teachers and the Centre Director. When the child changes class, a new thread starts and the old one becomes read-only. |
| **BR-PAR-033** | Private threads are between one family and the Centre Director. Teachers do not see them.                                                                                             |
| **BR-PAR-034** | Parents choose an inquiry category but not who answers. A closed inquiry can be reopened within 7 days (setting).                                                                     |
| **BR-PAR-035** | A survey is answered once per child and can be changed until the deadline. A survey option with a fee creates an invoice line in Fees when the survey closes.                         |
| **BR-PAR-036** | A consent marked "Can be withdrawn" can be withdrawn at any time; the original response and the withdrawal are both kept.                                                             |
| **BR-PAR-037** | A parent never sees a survey or consent that does not apply to the child's country.                                                                                                   |

## Learning

| **ID**         | **Rule**                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-038** | Parents see only class updates and photos tagged with their own child or class.                                      |
| **BR-PAR-039** | Parents react with a heart on class updates and photos. They cannot comment. A private reply opens the class thread. |
| **BR-PAR-040** | Progress reports and portfolios are shown only after they are published, as read-only PDF.                           |

## Fees

| **ID**         | **Rule**                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-041** | Amounts shown match the finance record exactly, in the currency of the child's country.                                                          |
| **BR-PAR-042** | An invoice being collected by GIRO has no Pay button. A failed GIRO deduction can be paid by PayNow.                                             |
| **BR-PAR-043** | Each invoice is paid with its own PayNow QR. The QR is shown only after the parent taps Pay.                                                     |
| **BR-PAR-044** | A PayNow payment is confirmed automatically and the receipt appears immediately.                                                                 |
| **BR-PAR-045** | When credit has been applied, the invoice shows the amount before credit, the credit applied and the amount to pay.                              |
| **BR-PAR-046** | Fee reminders are sent on the 15th and the 25th to families with an unpaid Billed invoice.                                                       |
| **BR-PAR-047** | Only the parent sets or changes the refund account. It is asked for only when a refund is approved. Money paid from CDA is refunded to CDA only. |

## Joining and leaving

| **ID**         | **Rule**                                                                                                                             |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **BR-PAR-048** | Part A of the registration form is mandatory and completed step by step. Part B (GIRO) can be skipped.                               |
| **BR-PAR-049** | Both signature boxes are required. A sole guardian signs both.                                                                       |
| **BR-PAR-050** | The e-Form 1 prompt is sent before the start date (default: 2 weeks) and must be acknowledged at least 7 days before the start date. |
| **BR-PAR-051** | A start date change applies only after the centre approves it.                                                                       |
| **BR-PAR-052** | The app never blocks a preferred last day. When notice is short, the parent is warned that the deposit may be forfeited.             |
| **BR-PAR-053** | After submitting, the parent does not see the withdrawal status; the parent receives the outcome by notification.                    |

## Notifications

| **ID**         | **Rule**                                                                                                     |
|----------------|--------------------------------------------------------------------------------------------------------------|
| **BR-PAR-054** | Notifications are sent to each guardian separately, not once per family. Each says which children it covers. |
| **BR-PAR-055** | Categories are Routines, Fees, Messages, Announcements, Surveys & Consents and Approvals.                    |
| **BR-PAR-056** | Turning a category off stops push notifications only; items stay in the notification centre.                 |
| **BR-PAR-057** | The unread badge is shown on the bell only and matches the notification centre.                              |
| **BR-PAR-058** | An item that needs action stays in "Needs you" until the task is done.                                       |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                           | **Recipient**                               | **Channel**          | **When**                                                                            |
|--------------------------------------------|---------------------------------------------|----------------------|-------------------------------------------------------------------------------------|
| **Account activation**                     | Each guardian                               | Email                | When the booking fee is paid                                                        |
| **Registration form**                      | Primary contact                             | Push + in-app; email | When the account is created; resend on request                                      |
| **Registration reminder**                  | Primary contact                             | Push + in-app        | Day 2, or days 3 and 5, while the form is incomplete                                |
| **Registration returned**                  | Primary contact                             | Push + in-app        | When the centre returns a step for correction                                       |
| **e-Form 1 prompt**                        | Guardians                                   | Push + in-app        | Before the start date (default 2 weeks); reminder 7 days before if not acknowledged |
| **Start date change decision**             | Requesting guardian                         | Push + in-app        | When the centre approves or rejects                                                 |
| **First-day reminder**                     | Guardians                                   | Push + in-app        | 7 days before the start date                                                        |
| **Child checked in**                       | Guardians                                   | Push + in-app        | On check-in, with time and photo                                                    |
| **Child checked out**                      | Guardians                                   | Push + in-app        | On check-out, with the name of the person picking up                                |
| **Daily routines updated**                 | Guardians                                   | Push + in-app        | Once a day, when the child is checked out                                           |
| **Leave decision**                         | Requesting guardian                         | Push + in-app        | When the request is approved or rejected                                            |
| **Pickup request result**                  | Requesting guardian                         | Push + in-app        | When the request is approved or rejected                                            |
| **Document request**                       | Guardians                                   | Push + in-app        | When the centre requests a document                                                 |
| **Document rejected**                      | Guardians                                   | Push + in-app        | When a document is rejected, with the reason                                        |
| **Vaccination reminder**                   | Guardians                                   | Push + in-app        | Before a vaccination is due (default 14 days)                                       |
| **New announcement**                       | Guardians in the audience                   | Push + in-app        | When published                                                                      |
| **Announcement reminder**                  | Guardians who have not read or acknowledged | Push + in-app        | When the sender sends a reminder                                                    |
| **New message**                            | Guardians in the thread                     | Push + in-app        | When staff send a message                                                           |
| **Inquiry reply**                          | Guardian who raised it                      | Push + in-app        | When staff reply or change the status                                               |
| **New survey or consent**                  | Guardians in the audience                   | Push + in-app        | When published                                                                      |
| **Survey or consent reminder**             | Guardians who have not responded            | Push + in-app        | When sent by staff; automatically 1 day before the deadline                         |
| **New class update**                       | Guardians of the tagged class or child      | Push + in-app        | When posted                                                                         |
| **Progress report or portfolio published** | Guardians                                   | Push + in-app        | When published or on the release date                                               |
| **New invoice**                            | Guardians                                   | Push + in-app        | When an invoice is Billed                                                           |
| **Payment reminder**                       | Guardians with an unpaid invoice            | Push + in-app        | On the 15th and the 25th                                                            |
| **Keep funds for GIRO**                    | Guardians on GIRO                           | Push + in-app        | Before each deduction day                                                           |
| **GIRO failed**                            | Guardians                                   | Push + in-app        | When the bank result shows a failure, with the reason                               |
| **Receipt**                                | Guardians                                   | Push + in-app        | When a payment is recorded                                                          |
| **Confirm refund account**                 | Billing contact                             | Push + in-app        | When a refund is approved, or after a failed refund                                 |
| **Refund result**                          | Billing contact                             | Push + in-app        | When the refund succeeds or fails                                                   |
| **Withdrawal result**                      | Guardians                                   | Push + in-app        | When retained, approved with the locked last day, or cancelled                      |
| **Graduation**                             | Guardians                                   | Push + in-app        | When the graduation is confirmed                                                    |
| **New or changed event**                   | Guardians in the audience                   | Push + in-app        | When an event or closure is published, changed or cancelled                         |

## 6.2 Documents

- Invoice and receipt: PDF from the brand's template, downloadable in the app.

- Progress report and portfolio: PDF, read-only, downloadable in the app.

- Registration form with both signatures and the handbook acknowledgement: PDF kept on the child record.

- Brand handbook: read-only PDF shown during registration.

# 7. Reports & exports

| **Report**                                | **Content**                                                                        | **Used by**                             |
|-------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------|
| **Parents App accounts**                  | Guardians per centre with account status (invited, active, not invited)            | Centre Director, School Admin, HQ Admin |
| **Announcement read and acknowledgement** | Sent, read and acknowledged per announcement, with who has not                     | Centre Director, HQ Admin               |
| **Survey and consent responses**          | Answers, signatures and withdrawals per form                                       | Centre Director, Teacher, HQ Admin      |
| **Registration progress**                 | New starters with their current registration step and days since the form was sent | School Admin, HQ Enrolment              |

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
<tr class="odd">
<th><strong>AC-PAR-001</strong></th>
<th>One account, several children</th>
<th>Given Sarah Tan has Emma at Small Wonder Tampines (Singapore) and Sophia at Brighton Montessori Mont Kiara (Malaysia),<br />
when Sarah signs in once,<br />
then she sees both children with brand, centre, class and country, and switching to Sophia changes every screen to Sophia's data.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-002</strong></th>
<th>Own children only</th>
<th>Given Emma is tagged in a class photo with two other children,<br />
when Sarah opens the photo in the gallery,<br />
then no other child's name is shown on the photo or anywhere in the app.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-003</strong></th>
<th>Pinned features</th>
<th>Given Sarah has 4 features pinned on Home,<br />
when she tries to unpin one more,<br />
then the app refuses and explains that at least 4 features must stay pinned.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-004</strong></th>
<th>Fee reminder for GIRO family</th>
<th>Given Emma's family pays by GIRO and has an October invoice due on 5 October that is not yet deducted,<br />
when Sarah opens Home on 1 October,<br />
then no fee reminder is shown.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-005</strong></th>
<th>Check-out notification</th>
<th>Given Grandma Lim is an approved pickup person for Emma,<br />
when staff check Emma out to Grandma Lim at 17:30,<br />
then each guardian receives a notification naming Grandma Lim and the time, and Attendance shows "Picked up by Grandma Lim" with the handover photo.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-006</strong></th>
<th>Temperature readings</th>
<th>Given staff recorded six readings for Emma on 8 September, one at 37.8°C,<br />
when Sarah opens 8 September in Attendance,<br />
then all six readings are shown in time order with their labels, and the 37.8°C reading is marked as raised.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-007</strong></th>
<th>Leave request</th>
<th>Given Sarah creates a Medical leave for Emma from 22 to 23 September with a medical certificate,<br />
when she submits,<br />
then the request shows Pending with the attachment, the two notices were shown before submitting, and Sarah is notified when the Centre Director decides.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-008</strong></th>
<th>Health edit by parent</th>
<th>Given Sarah entered "Allergic to shellfish" for Emma and a teacher added a staff note,<br />
when Sarah changes the allergy to "Allergic to shellfish and peanuts",<br />
then the staff note is unchanged, the history shows Sarah and the time, and the Centre Director, School Admin and Emma's teachers are notified.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-009</strong></th>
<th>Pickup person added and removed</th>
<th>Given Sarah adds Uncle David with photo, name, relationship, NRIC/FIN and phone,<br />
when the School Admin approves, and a week later Sarah removes him,<br />
then he shows Pending then Approved; after removal he leaves the pickup list at once without approval and the centre is notified.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-010</strong></th>
<th>Announcement once per guardian</th>
<th>Given Sarah has three children at the same centre and the centre announces a closure on 27 October,<br />
when the announcement is published,<br />
then Sarah receives one notification that says it covers all her children, and David Tan receives his own.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-011</strong></th>
<th>Acknowledgement</th>
<th>Given an announcement requires acknowledgement,<br />
when Sarah taps "Acknowledge",<br />
then the announcement shows as acknowledged for Sarah and there is no comment box.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-012</strong></th>
<th>Private thread</th>
<th>Given the Centre Director starts a private thread with Emma's family,<br />
when Emma's teacher opens Messages,<br />
then the teacher does not see that thread.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-013</strong></th>
<th>Inquiry reopen</th>
<th>Given Sarah's inquiry about a receipt was closed on 1 October,<br />
when she tries to reopen it on 10 October,<br />
then the app does not allow it and offers to raise a new inquiry.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-014</strong></th>
<th>PayNow blocked during GIRO</th>
<th>Given Emma's October invoice is in a 1ST DD batch without a bank result,<br />
when Sarah opens the invoice,<br />
then there is no Pay button and the invoice shows "Being collected by GIRO".</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-015</strong></th>
<th>PayNow payment</th>
<th>Given Emma's excursion invoice of S$38.00 is Billed and not on GIRO,<br />
when Sarah taps Pay, sees the summary, and pays S$38.00 by the PayNow QR,<br />
then the invoice becomes Paid and the receipt appears immediately.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-016</strong></th>
<th>CDA refund</th>
<th>Given a deposit refund of S$1,200 is approved, of which S$800 was paid from CDA,<br />
when Sarah opens the refund,<br />
then the S$800 shows CDA as its destination and she is asked to confirm a PayNow account for the S$400 only.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-017</strong></th>
<th>Registration</th>
<th>Given Sarah completes Part A for her new child and skips Part B,<br />
when she tries to submit before David signs the second box,<br />
then the form cannot be submitted until both signature boxes are signed and the handbook is acknowledged.</th>
</tr>
<tr class="header">
<th><strong>AC-PAR-018</strong></th>
<th>Short-notice withdrawal</th>
<th>Given Emma's centre requires one month's notice and Sarah submits on 14 October,<br />
when she picks 31 October as the preferred last day,<br />
then the app accepts the date, warns that the deposit may be forfeited, and after submitting the button turns grey with no status shown.</th>
</tr>
<tr class="odd">
<th><strong>AC-PAR-019</strong></th>
<th>Push off</th>
<th>Given Sarah turns off the Fees category,<br />
when a payment reminder is sent on 15 October,<br />
then Sarah gets no push on her phone but the reminder appears under the bell and in "Needs you".</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
