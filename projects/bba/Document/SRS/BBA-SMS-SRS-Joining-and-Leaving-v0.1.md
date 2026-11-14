Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Joining & Leaving**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-JNL-NNN and acceptance criteria AC-JNL-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Joining & Leaving module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes what the module must do so that centres can bring a child from booking fee to the first day, and manage every way a child leaves or returns, without Taidii.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/lifecycle. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Joining: new starters from the booking fee to the first day, Parents App account, registration form, documents, signatures, handbook, verification, start date changes, e-Form 1 prompt, welcome letter.

- Withdrawals: parent request in the Parents App, retention, locked last day, notice period check, family balance check, approvals, Form 3 record, refund hand-off.

- Temporary withdrawals: creation at the centre, approval, extension, effects on attendance and billing, return or exit at expiry, retention fee (Malaysia).

- Transfers between centres in the same country.

- Graduation: K2 year-end mass withdrawal.

- Re-enrolment of children who left.

- Lifecycle reports exported to Excel: starters, withdrawals, transfers, graduation, re-enrolment.

- What parents see in the Parents App: registration form, handbook, e-Form 1 prompt, start date change request, withdrawal request and result.

## 1.2 Not in Phase 1

- Enquiries, visits and the booking fee (handled in Enquiries before this module).

- Invoices, deposits and refunds themselves (handled in Fees & Payments; this module passes on the locked dates and outcomes).

- SingPass (MyInfo) login and data retrieval.

- Integration with ECDA. e-Form 1, Form 2 and Form 3 are submitted to ECDA manually in Phase 1.

- e-Form 3 with electronic signature (Form 3 stays on paper in Phase 1).

- Late start and deferment of the start date by policy.

- Programme / session and nationality changes.

- Annual promotion workflow (class moves are handled in Children & Families › Classes).

- Checking seat availability in the system for transfers and re-enrolment.

- Parent blacklist.

# 2. Who uses it

| **Role**                                                                       | **What they do in this module**                                                                                                                                                            |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **School Admin (Singapore) / Centre Director (Malaysia)**                      | Runs joining, verifies registrations, locks the last day, records Form 3, starts and receives transfers, creates temporary withdrawals, re-enrols children.                                |
| **Centre Director**                                                            | Holds the retention conversation; approves withdrawals with enough notice and temporary withdrawals as configured; approves short-notice withdrawals for Odyssey.                          |
| **District Manager (SG) / Operations Manager (MY) / Head of Brand (Brighton)** | Approves short-notice withdrawals, mid-month withdrawals and short-notice transfers as configured in Approval routes; Operations Manager approves temporary withdrawals in Malaysia.       |
| **HQ Finance**                                                                 | Receives the first invoice trigger, refund hand-offs, notice waiver requests and retention fee waivers in Fees & Payments; uses the transfer and withdrawal reports.                       |
| **HQ Admin**                                                                   | Has every permission in the module; configures notice periods, reminder timings, handbooks, welcome letters, withdrawal reasons and approval routes.                                       |
| **Class teacher**                                                              | Receives notices about new starters, returns and leavers; no actions in this module.                                                                                                       |
| **Parent (Parents App)**                                                       | Completes the registration form, signs, acknowledges the handbook, completes the e-Form 1 prompt, requests a start date change, submits a withdrawal request, confirms the refund account. |

# 3. Process overview

## P1. Joining a new starter

1\. The family pays the booking fee in Enquiries; the child appears in New starters.

2\. The system creates the Parents App account and sends the registration form, pre-filled from the enquiry.

3\. The parent completes Part A (details, documents, pick-up persons, allergies), signs both signature boxes and acknowledges the brand handbook; Part B (GIRO) can be skipped.

4\. The system triggers the first invoice in Fees & Payments; the admin verifies the registration and confirms level and start date.

5\. Before the start date the system prompts e-Form 1, sends the welcome letter and notifies the class teacher.

6\. On the first day the child is active in attendance; the admin submits e-Form 1 to ECDA manually.

## P2. Withdrawal

1\. The parent submits a withdrawal in the Parents App with a reason and a preferred last day; a short notice shows a deposit warning.

2\. The Centre Director and the admin are notified; the Centre Director records the retention attempt.

3\. If the family stays, the request is closed as Retained. Otherwise the admin locks the last day.

4\. The system checks the notice period and the family balance and routes the request for approval.

5\. On approval the admin records Form 3; the system hands off the refund to Fees & Payments and notifies the parent.

6\. On the locked last day the withdrawal becomes Completed and the child leaves attendance and the Parents App class views.

## P3. Temporary withdrawal

1\. The parent asks at the centre with a medical or relocation reason and a supporting document.

2\. The admin creates the temporary withdrawal with start date and expected return date (up to 3 months).

3\. The request is approved as configured per country.

4\. During the period the child has no attendance, no invoices and no subsidy; the seat is kept.

5\. Before the return date the teacher and the centre are reminded; at expiry the admin chooses Return, Extend or Withdraw.

## P4. Transfer between centres

1\. The sending centre starts the transfer with the receiving centre and the proposed last day.

2\. The sending centre confirms the family balance is cleared.

3\. The receiving centre confirms a seat and accepts.

4\. The sending centre locks the last day, records Form 3 and releases the child.

5\. The receiving centre receives the child; a new enrolment record starts with new T&C signatures, a new e-Form 1 and a welcome letter.

## P5. K2 graduation

1\. The admin loads the K2 cohort with the last day 31 December.

2\. The admin unticks children who are not graduating (K3 or repeating K2, overage, early intervention).

3\. The admin confirms one mass withdrawal with reason Graduation.

4\. Parents are notified and asked to confirm the refund account; year-end refunds are created in Fees & Payments.

## P6. Re-enrolment

1\. The admin searches past children (withdrawn or graduated).

2\. The admin re-enrols the child with centre, level, programme and start date.

3\. The system creates a new enrolment record on the existing child profile and asks the parent to review the pre-filled details and sign the current T&C.

4\. Joining steps from e-Form 1 onwards run as for a new starter.

# 4. Modules, sub-modules, features and functions

## 1. Joining

### 1.1 New starters

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle/joining</u>](https://bba-sms-crm.lovable.app/lifecycle/joining)

| **Feature**                       | **Function**                                                                                                                          |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **View new starter list**         | Children who paid the booking fee: child, parent, centre, level, start date, current registration step, days since the form was sent. |
| **Search**                        | Child name, parent name, phone.                                                                                                       |
| **Filter**                        | Centre, start month, missing step.                                                                                                    |
| **Sort**                          | Default by start date, earliest first.                                                                                                |
| **Paging**                        | 20 / 50 / 100 rows.                                                                                                                   |
| **Create Parents App account**    | Automatically after the booking fee is paid; the parent receives activation instructions by email.                                    |
| **Send registration form**        | Multi-step form in the Parents App, pre-filled from the enquiry.                                                                      |
| **Resend registration form**      | For a parent who has not started.                                                                                                     |
| **Track registration steps**      | Shows each step as Not started, In progress or Done.                                                                                  |
| **Send registration reminders**   | Automatic reminders while the form is incomplete; the child is flagged for admin follow-up after 7 days.                              |
| **View child registration**       | All submitted data, documents, signatures and handbook acknowledgement.                                                               |
| **Verify registration**           | Admin checks the data and documents and confirms level, programme, class and start date.                                              |
| **Return registration to parent** | Reason required; the parent is notified which step to correct.                                                                        |
| **Trigger first invoice**         | On submission of Part A: registration fee and deposit, less the booking fee, created in Fees & Payments.                              |
| **Approve start date change**     | From a parent request; the new date updates all joining timings.                                                                      |
| **Reject start date change**      | Reason required; the parent is notified.                                                                                              |
| **View email log**                | Every system email sent for the child: type, recipient, date, delivery status.                                                        |
| **Export Starter report**         | Filtered list to Excel, including nationality.                                                                                        |

### 1.2 Registration in the Parents App

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle/joining</u>](https://bba-sms-crm.lovable.app/lifecycle/joining)

| **Feature**                   | **Function**                                                                                                                     |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Complete Part A**           | Mandatory and in order: confirm personal details, upload documents, add pick-up persons, allergies, diet and emergency contacts. |
| **Upload documents**          | Birth certificate and immunisation record; skipped for an unborn child.                                                          |
| **Remind missing documents**  | For an unborn child, the parent is reminded to upload documents before the start date.                                           |
| **Complete Part B (GIRO)**    | Optional; choose bank (DBS, OCBC, UOB) and method (paper form or e-GIRO); the GIRO account is created in Fees & Payments.        |
| **Sign registration**         | Two signature boxes, both required; a sole guardian signs both.                                                                  |
| **Acknowledge handbook**      | The brand's handbook opens as a read-only PDF; the parent must tick to confirm receipt before continuing.                        |
| **Submit registration**       | Sends the form to the centre.                                                                                                    |
| **Request start date change** | New date and reason; goes to the centre.                                                                                         |

### 1.3 Before the first day

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle/joining</u>](https://bba-sms-crm.lovable.app/lifecycle/joining)

| **Feature**                         | **Function**                                                                                                                            |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Send e-Form 1 prompt**            | To the parent before the start date (default: 2 weeks), pre-filled from the registration.                                               |
| **Track e-Form 1 acknowledgement**  | The parent acknowledges at least 7 days before the start date; the time stamp is stored.                                                |
| **Remind e-Form 1**                 | If not acknowledged 7 days before the start date; the admin is also notified.                                                           |
| **Mark e-Form 1 submitted to ECDA** | Admin records the manual submission date.                                                                                               |
| **Send welcome letter**             | Brand template, to the parent (default: 2 weeks before the start date in Singapore, 1 week in Malaysia); can be switched off per brand. |
| **Send first-day reminder**         | To the parent 7 days before the start date.                                                                                             |
| **Notify class teacher**            | Child name, class and start date (default: 2 weeks before the start date).                                                              |

## 2. Leaving

### 2.1 Withdrawals

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle</u>](https://bba-sms-crm.lovable.app/lifecycle)

| **Feature**                          | **Function**                                                                                                                            |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **View withdrawal list**             | Tabs In flight and Completed: child, centre, level, requested last day, locked last day, reason, notice given, notice required, status. |
| **Search**                           | Child name, parent name.                                                                                                                |
| **Filter**                           | Centre, status, reason, last-day month, short notice yes / no.                                                                          |
| **Sort**                             | Default by locked last day, earliest first.                                                                                             |
| **Paging**                           | 20 / 50 / 100 rows.                                                                                                                     |
| **Submit withdrawal (parent)**       | In the Parents App: reason from the list and preferred last day; any date is allowed.                                                   |
| **Show deposit warning**             | When the preferred last day gives less than the required notice, the parent sees that the deposit may be forfeited before submitting.   |
| **Notify Centre Director and admin** | On submission.                                                                                                                          |
| **Record retention attempt**         | Centre Director records date, outcome and notes (default: within 3 working days).                                                       |
| **Close as retained**                | The request ends; the parent is notified; the child stays active.                                                                       |
| **Lock last day**                    | Admin only; may differ from the parent's date; all later calculations use the locked date.                                              |
| **Check notice period**              | Compares notice given with the notice required for the month of the last day.                                                           |
| **Check family balance**             | Shows outstanding amounts of the whole family, including siblings.                                                                      |
| **Route for approval**               | By notice and last day, using Approval routes.                                                                                          |
| **Approve withdrawal**               | Records who and when.                                                                                                                   |
| **Reject withdrawal**                | Reason required; the request returns to the admin.                                                                                      |
| **Request notice waiver**            | Creates a waiver request in Fees & Payments › Approvals.                                                                                |
| **Record Form 3**                    | Form number, date and scanned file.                                                                                                     |
| **Hand off refund**                  | Creates the deposit refund request in Fees & Payments with the locked last day and the notice outcome.                                  |
| **Notify parent of result**          | Locked last day, outcome and next steps.                                                                                                |
| **Complete withdrawal**              | Automatically on the locked last day.                                                                                                   |
| **Cancel withdrawal**                | Before completion; reason required; the parent is notified.                                                                             |
| **View history**                     | Every status change, who, when, comments.                                                                                               |
| **Export Withdrawal report**         | Filtered list to Excel, including nationality.                                                                                          |

### 2.2 Temporary withdrawals

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle</u>](https://bba-sms-crm.lovable.app/lifecycle)

| **Feature**                         | **Function**                                                                                                              |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **View temporary withdrawal list**  | Child, centre, reason, start date, return date, extensions, status.                                                       |
| **Search**                          | Child name.                                                                                                               |
| **Filter**                          | Centre, status, return month.                                                                                             |
| **Sort**                            | Default by return date, earliest first.                                                                                   |
| **Create temporary withdrawal**     | Centre users only: reason (medical or relocation), supporting document, start date, expected return date.                 |
| **Approve temporary withdrawal**    | As configured per country.                                                                                                |
| **Reject temporary withdrawal**     | Reason required; the child stays active.                                                                                  |
| **Apply effects**                   | During the period: no attendance, no invoices, no subsidy; hidden from attendance and Parents App class views; seat kept. |
| **Remind before return**            | To the class teacher and the centre (default: 2 weeks before the return date).                                            |
| **Extend temporary withdrawal**     | New supporting document and new return date; goes for approval and can be rejected.                                       |
| **Resolve at expiry**               | Admin chooses Return, Extend or Withdraw; the system never converts it to a withdrawal by itself.                         |
| **Charge retention fee (Malaysia)** | Created in Fees & Payments; non-refundable.                                                                               |
| **Request retention fee waiver**    | Goes to Finance Malaysia in Fees & Payments › Approvals.                                                                  |
| **View history**                    |                                                                                                                           |
| **Export**                          | Filtered list to Excel.                                                                                                   |

### 2.3 Transfers

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle</u>](https://bba-sms-crm.lovable.app/lifecycle)

| **Feature**                       | **Function**                                                                                                              |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **View transfer list**            | Child, from centre, to centre, last day at sending centre, first day at receiving centre, status.                         |
| **Search**                        | Child name.                                                                                                               |
| **Filter**                        | Sending centre, receiving centre, status, month.                                                                          |
| **Sort**                          | Default by transfer date.                                                                                                 |
| **Start transfer**                | Sending centre only, within the same country: receiving centre, proposed last day and first day.                          |
| **Confirm balance cleared**       | Sending centre confirms the whole family has no outstanding amount.                                                       |
| **Accept transfer**               | Receiving centre confirms a seat is available.                                                                            |
| **Decline transfer**              | Reason required; the child stays at the sending centre.                                                                   |
| **Approve short-notice transfer** | District Manager of both centres.                                                                                         |
| **Release child**                 | Sending centre locks the last day and records Form 3.                                                                     |
| **Receive child**                 | Receiving centre creates the new enrolment record and sets the class.                                                     |
| **Re-sign T&C**                   | The parent signs the receiving centre's T&C in the Parents App.                                                           |
| **Send new e-Form 1 prompt**      | For the new enrolment record.                                                                                             |
| **Hand off deposit and GIRO**     | Passes the transfer to Fees & Payments: GIRO kept for the same legal entity; re-application for a different legal entity. |
| **View history**                  |                                                                                                                           |
| **Export Transfer report**        | Child name, NRIC, from, to, date, deposit, credit, outstanding.                                                           |

### 2.4 Graduation

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle/graduation</u>](https://bba-sms-crm.lovable.app/lifecycle/graduation)

| **Feature**                  | **Function**                                                                        |
|------------------------------|-------------------------------------------------------------------------------------|
| **Load K2 cohort**           | K2 children of the selected centres with last day 31 December of the selected year. |
| **Untick exceptions**        | K3 or repeating K2, overage, early intervention; reason required for each.          |
| **Confirm mass withdrawal**  | One action for all ticked children; reason Graduation; no parent request needed.    |
| **Flag unprocessed K2**      | K2 children who are neither graduated nor marked as exceptions.                     |
| **Notify parents**           | Graduation message and request to confirm the refund account.                       |
| **Create year-end refunds**  | Passes the graduating children to Fees & Payments.                                  |
| **Export Graduation report** | Separate from the Withdrawal report.                                                |

## 3. Returning

### 3.1 Re-enrolment

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle/rejoin</u>](https://bba-sms-crm.lovable.app/lifecycle/rejoin)

| **Feature**                      | **Function**                                                                                           |
|----------------------------------|--------------------------------------------------------------------------------------------------------|
| **Search past children**         | Withdrawn and graduated children by name, parent, NRIC.                                                |
| **Filter**                       | Centre, leaving year, leaving reason.                                                                  |
| **View past enrolments**         | Every enrolment record of the child with dates and centres.                                            |
| **Re-enrol**                     | Centre, level, programme and start date; creates a new enrolment record on the existing child profile. |
| **Ask parent to review details** | The parent reviews pre-filled details and documents and signs the current T&C in the Parents App.      |
| **Export Re-enrolment report**   | Filtered list to Excel.                                                                                |

# 5. Business rules

## Joining

| **ID**         | **Rule**                                                                                                                                                                                                      |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-001** | A child enters this module when the booking fee is paid. Before that the family is handled in Enquiries.                                                                                                      |
| **BR-JNL-002** | The Parents App account is created automatically after the booking fee is paid.                                                                                                                               |
| **BR-JNL-003** | Part A of the registration form is mandatory and completed step by step. Part B (GIRO) can be skipped.                                                                                                        |
| **BR-JNL-004** | Every registration form has two signature boxes and both are required. A sole guardian signs both boxes.                                                                                                      |
| **BR-JNL-005** | The parent must acknowledge the brand's handbook before submitting. HQ Admin sets one handbook per brand.                                                                                                     |
| **BR-JNL-006** | Birth certificate and immunisation record are required, except for an unborn child, whose parent is reminded before the start date.                                                                           |
| **BR-JNL-007** | The first invoice (registration fee and deposit, less the booking fee) is created when Part A is submitted, whether or not GIRO is set up.                                                                    |
| **BR-JNL-008** | Registration reminders: if the start date is 7 days away or less, one reminder on day 2; if it is more than 7 days away, reminders on day 3 and day 5. After 7 days the child is flagged for admin follow-up. |
| **BR-JNL-009** | A start date change requested by the parent applies only after the centre approves it.                                                                                                                        |
| **BR-JNL-010** | The e-Form 1 prompt is sent before the start date (default: 2 weeks). The parent must acknowledge it at least 7 days before the start date. The acknowledgement time is stored.                               |
| **BR-JNL-011** | In Phase 1 the admin submits e-Form 1 to ECDA manually and records the submission date.                                                                                                                       |
| **BR-JNL-012** | The welcome letter is sent per brand template (default: 2 weeks before the start date in Singapore, 1 week in Malaysia). A brand can switch it off (default: off for Odyssey).                                |
| **BR-JNL-013** | All joining timings are settings per brand, with centre override.                                                                                                                                             |

## Withdrawals

| **ID**         | **Rule**                                                                                                                                                                                                                |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-014** | Withdrawals are started by the parent in the Parents App. The app never blocks a date.                                                                                                                                  |
| **BR-JNL-015** | Withdrawal reasons are picked from a shared list maintained in Settings.                                                                                                                                                |
| **BR-JNL-016** | The Centre Director must record a retention attempt before the last day can be locked.                                                                                                                                  |
| **BR-JNL-017** | Only the admin can lock the last day. Every calculation uses the locked last day, not the requested date.                                                                                                               |
| **BR-JNL-018** | Fees are always charged for the full month of the last day.                                                                                                                                                             |
| **BR-JNL-019** | The required notice depends only on the month in which the last day falls. It is set per brand and can be overridden per centre (default: 2 months when the last day is in November or December, otherwise 1 month).    |
| **BR-JNL-020** | Notice given is counted from the date the parent submits the request to the locked last day.                                                                                                                            |
| **BR-JNL-021** | A withdrawal with enough notice is approved by the Centre Director.                                                                                                                                                     |
| **BR-JNL-022** | A withdrawal with short notice is approved as set in Approval routes (default: District Manager in Singapore, Operations Manager in Malaysia, Centre Director for Odyssey, Head of Brand for Brighton).                 |
| **BR-JNL-023** | A last day that is not the calendar month-end needs a second-level approval (default: the short-notice approver of the brand), even if notice is enough. The calendar month-end counts even when it falls on a weekend. |
| **BR-JNL-024** | Short notice means the deposit is forfeited and the parent pays the outstanding fees. A notice waiver is requested in Fees & Payments › Approvals.                                                                      |
| **BR-JNL-025** | Before approval the system shows the outstanding balance of the whole family, including siblings.                                                                                                                       |
| **BR-JNL-026** | Form 3 is completed on paper in Phase 1. The admin records the form number and attaches the scanned file.                                                                                                               |
| **BR-JNL-027** | An approved withdrawal creates the deposit refund request in Fees & Payments automatically.                                                                                                                             |
| **BR-JNL-028** | A withdrawal can be cancelled before completion with a reason.                                                                                                                                                          |
| **BR-JNL-029** | Withdrawal statuses are Submitted, Retention, Pending approval, Approved, Completed, Retained, Rejected and Cancelled.                                                                                                  |

## Temporary withdrawals

| **ID**         | **Rule**                                                                                                                                                |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-030** | Only centre users create temporary withdrawals. Parents cannot request them in the app.                                                                 |
| **BR-JNL-031** | A temporary withdrawal needs a medical or relocation reason and a supporting document. There is no notice period.                                       |
| **BR-JNL-032** | Each period lasts up to 3 months. Longer absences need an extension with a new supporting document and a new approval.                                  |
| **BR-JNL-033** | Approval in Malaysia is Centre Director then Operations Manager. Approval in Singapore is set in Approval routes (default: Centre Director).            |
| **BR-JNL-034** | During the period the child has no attendance, no invoices and no subsidy, and is hidden from attendance and Parents App class views. The seat is kept. |
| **BR-JNL-035** | At expiry the admin chooses Return, Extend or Withdraw. The system never turns a temporary withdrawal into a withdrawal by itself.                      |
| **BR-JNL-036** | Malaysia centres charge a non-refundable retention fee, set per brand. A waiver needs Finance Malaysia approval.                                        |
| **BR-JNL-037** | Temporary withdrawal can be switched off per brand (default: off for Odyssey and Agape).                                                                |

## Transfers

| **ID**         | **Rule**                                                                                                                                                       |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-038** | Only centres start transfers, and only within the same country.                                                                                                |
| **BR-JNL-039** | The sending centre must confirm the whole family's balance is cleared before release.                                                                          |
| **BR-JNL-040** | The receiving centre checks seat availability outside the system in Phase 1 and accepts or declines.                                                           |
| **BR-JNL-041** | The receiving centre can receive the child only after the sending centre releases them.                                                                        |
| **BR-JNL-042** | The sending centre records Form 3 for every transfer. Mid-month and short-notice rules of withdrawals apply to the last day at the sending centre.             |
| **BR-JNL-043** | A short-notice transfer is approved by the District Managers of both centres.                                                                                  |
| **BR-JNL-044** | A transfer keeps one child profile and creates a new enrolment record at the receiving centre. Attendance belongs to the enrolment record.                     |
| **BR-JNL-045** | The new enrolment record needs new T&C signatures, a new e-Form 1 and a welcome letter.                                                                        |
| **BR-JNL-046** | A mid-month transfer needs at least one attendance day at each centre.                                                                                         |
| **BR-JNL-047** | In internal reports a transfer is counted neither as a withdrawal nor as a new starter.                                                                        |
| **BR-JNL-048** | GIRO stays when both centres belong to the same legal entity. A different legal entity needs a new GIRO application and a deposit transfer in Fees & Payments. |

## Graduation

| **ID**         | **Rule**                                                                                                                              |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-049** | The graduating cohort is K2 children with the last day 31 December.                                                                   |
| **BR-JNL-050** | Children going to K3 or repeating K2, overage children and early intervention children are unticked with a reason.                    |
| **BR-JNL-051** | Graduation is recorded as a withdrawal with reason Graduation. Parents do not need to submit a request.                               |
| **BR-JNL-052** | In the Parents App the record shows as a withdrawal with reason Graduation; the notification tells parents their child is graduating. |
| **BR-JNL-053** | Graduation is reported separately from other withdrawals.                                                                             |
| **BR-JNL-054** | K2 children not processed by the cohort cut-off are flagged to the admin.                                                             |

## Re-enrolment

| **ID**         | **Rule**                                                                                                                                 |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-055** | A returning child keeps the existing child profile. Re-enrolment creates a new enrolment record and never repeats the full registration. |
| **BR-JNL-056** | The parent reviews pre-filled details and signs the T&C that apply at re-enrolment.                                                      |
| **BR-JNL-057** | A re-enrolment needs a new e-Form 1. Attendance and the first attendance date belong to the new enrolment record.                        |

## General

| **ID**         | **Rule**                                                                                                                    |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| **BR-JNL-058** | Each enrolment record keeps the centre, level, start date, last day and leaving reason. Past records are never overwritten. |
| **BR-JNL-059** | Approval routes, notice periods, reminder timings, handbooks and welcome letter templates are configured by HQ Admin.       |
| **BR-JNL-060** | Teachers receive notices only and have no actions in this module.                                                           |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**                  | **Recipient**          | **Channel**   | **When**                                                       |
|-----------------------------------|------------------------|---------------|----------------------------------------------------------------|
| **Account activation**            | Parent                 | Email         | When the booking fee is paid                                   |
| **Registration form**             | Parent                 | In-app; email | When the account is created; resend on request                 |
| **Registration reminder**         | Parent                 | In-app        | Day 2, or days 3 and 5, while the form is incomplete           |
| **Registration follow-up**        | Admin                  | In-app (web)  | 7 days after the form was sent if incomplete                   |
| **Registration submitted**        | Admin                  | In-app (web)  | When the parent submits                                        |
| **Registration returned**         | Parent                 | In-app        | When the admin returns a step for correction                   |
| **Missing documents**             | Parent                 | In-app        | Before the start date for an unborn child                      |
| **Start date change decision**    | Parent                 | In-app        | When the centre approves or rejects                            |
| **e-Form 1 prompt**               | Parent                 | In-app        | Before the start date (default 2 weeks)                        |
| **e-Form 1 reminder**             | Parent; admin          | In-app        | 7 days before the start date if not acknowledged               |
| **Welcome letter**                | Parent                 | Email; in-app | Per brand timing before the start date                         |
| **First-day reminder**            | Parent                 | In-app        | 7 days before the start date                                   |
| **New starter**                   | Class teacher          | In-app        | Before the start date (default 2 weeks)                        |
| **Withdrawal submitted**          | Centre Director; admin | In-app (web)  | When the parent submits                                        |
| **Withdrawal approval request**   | Approver               | In-app (web)  | When the request is routed                                     |
| **Withdrawal decision**           | Admin                  | In-app (web)  | When approved or rejected                                      |
| **Withdrawal result**             | Parent                 | In-app        | When retained, approved with the locked last day, or cancelled |
| **Child leaving**                 | Class teacher          | In-app        | When a withdrawal or transfer is approved                      |
| **Temporary withdrawal decision** | Admin                  | In-app (web)  | When approved or rejected                                      |
| **Return reminder**               | Class teacher; admin   | In-app        | Before the return date (default 2 weeks)                       |
| **Temporary withdrawal expiry**   | Admin                  | In-app (web)  | On the return date if not resolved                             |
| **Transfer request**              | Receiving centre admin | In-app (web)  | When a transfer is started                                     |
| **Transfer released**             | Receiving centre admin | In-app (web)  | When the sending centre releases the child                     |
| **Transfer T&C and e-Form 1**     | Parent                 | In-app        | When the receiving centre receives the child                   |
| **Graduation**                    | Parent                 | In-app        | When the mass withdrawal is confirmed                          |
| **Unprocessed K2**                | Admin                  | In-app (web)  | When K2 children remain unprocessed                            |
| **Re-enrolment details**          | Parent                 | In-app        | When the child is re-enrolled                                  |

## 6.2 Documents

- Registration form with two signatures and handbook acknowledgement, stored as PDF on the child profile.

- Brand handbook (PDF, read-only in the Parents App) and welcome letter (brand template).

- Form 3 scanned file and supporting documents for temporary withdrawals, stored on the enrolment record.

# 7. Reports & exports

| **Report**                    | **Content**                                                                      | **Used by**                           |
|-------------------------------|----------------------------------------------------------------------------------|---------------------------------------|
| **Starter report**            | New starters by centre and start month with registration step and nationality    | Centre admin, HQ Admin                |
| **Withdrawal report**         | Withdrawals with reason, notice given, notice required, last day and nationality | Centre Director, HQ Admin, HQ Finance |
| **Temporary withdrawal list** | Children on temporary withdrawal with dates and extensions                       | Centre admin, HQ Admin                |
| **Transfer report**           | Child, NRIC, from, to, date, deposit, credit, outstanding                        | HQ Finance                            |
| **Graduation report**         | Graduating K2 children and exceptions per centre                                 | Centre Director, HQ Admin, HQ Finance |
| **Re-enrolment report**       | Children re-enrolled with previous and new enrolment dates                       | Centre admin, HQ Admin                |
| **Email log**                 | System emails sent per child with status                                         | Centre admin                          |

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
<td><strong>AC-JNL-001</strong></td>
<td>Account on booking fee</td>
<td>Given a family pays the booking fee for Mia Tan at centre A,<br />
when the payment is recorded in Enquiries,<br />
then Mia appears in New starters at step "Registration form sent" and the parent receives the account activation email.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-002</strong></td>
<td>Part A order</td>
<td>Given a parent has not uploaded the birth certificate,<br />
when the parent tries to open the pick-up persons step,<br />
then the app does not allow it until the documents step is done.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-003</strong></td>
<td>Unborn child</td>
<td>Given a child is registered with an expected birth date,<br />
when the parent reaches the documents step,<br />
then the step can be skipped and a document reminder is scheduled before the start date.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-004</strong></td>
<td>Two signatures</td>
<td>Given a sole guardian completes the registration form,<br />
when they sign only the first box,<br />
then the form cannot be submitted until the second box is also signed.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-005</strong></td>
<td>Registration reminders</td>
<td>Given a form was sent on 1 November for a start date of 5 January,<br />
when the form is still incomplete,<br />
then the parent is reminded on 3 and 5 November and the child is flagged to the admin on 8 November.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-006</strong></td>
<td>First invoice</td>
<td>Given a parent submits Part A and skips GIRO,<br />
when the registration is submitted,<br />
then a Draft first invoice with the registration fee and deposit less the booking fee is created in Fees &amp; Payments.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-007</strong></td>
<td>e-Form 1 prompt</td>
<td>Given a child starts on 2 February and the brand uses the default timing,<br />
when it is 19 January,<br />
then the parent receives the e-Form 1 prompt and must acknowledge it by 26 January.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-008</strong></td>
<td>No date block</td>
<td>Given today is 10 December,<br />
when a parent submits a withdrawal with last day 15 December,<br />
then the request is accepted and the parent sees the deposit warning before submitting.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-009</strong></td>
<td>Retention first</td>
<td>Given a withdrawal is in Retention,<br />
when the admin tries to lock the last day,<br />
then the system blocks it until the Centre Director records the retention attempt.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-010</strong></td>
<td>Retained</td>
<td>Given the Centre Director records that the family will stay,<br />
when the outcome is saved,<br />
then the request closes as Retained, the parent is notified and the child stays active.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-011</strong></td>
<td>Year-end notice</td>
<td>Given a centre uses the brand default and the locked last day is 31 December,<br />
when the request was submitted on 15 November,<br />
then the system shows 2 months required, 1.5 months given, and routes the request to the short-notice approver.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-012</strong></td>
<td>Short notice approver</td>
<td>Given a short-notice withdrawal at a Malaysia centre,<br />
when the request is routed,<br />
then it goes to the Operations Manager and not to the District Manager.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-013</strong></td>
<td>Mid-month last day</td>
<td>Given a withdrawal with enough notice and locked last day 15 March,<br />
when the Centre Director approves it,<br />
then the request goes to the second-level approver before it becomes Approved.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-014</strong></td>
<td>Month-end on weekend</td>
<td>Given a withdrawal with enough notice and locked last day Saturday 31 October,<br />
when the Centre Director approves it,<br />
then no second-level approval is needed.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-015</strong></td>
<td>Refund hand-off</td>
<td>Given a withdrawal is approved,<br />
when Form 3 is recorded,<br />
then a deposit refund request with the locked last day and notice outcome is created in Fees &amp; Payments.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-016</strong></td>
<td>Temporary withdrawal effects</td>
<td>Given an approved temporary withdrawal from 1 March to 31 May,<br />
when the April billing run and attendance lists are created,<br />
then the child has no April invoice and does not appear in attendance.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-017</strong></td>
<td>No automatic withdrawal</td>
<td>Given a temporary withdrawal reaches its return date unresolved,<br />
when the date passes,<br />
then the child stays on temporary withdrawal and the admin is asked to choose Return, Extend or Withdraw.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-018</strong></td>
<td>Transfer release</td>
<td>Given the receiving centre has accepted a transfer,<br />
when the receiving admin tries to receive the child before release,<br />
then the system blocks it until the sending centre releases the child.</td>
</tr>
<tr class="odd">
<td><strong>AC-JNL-019</strong></td>
<td>Graduation exceptions</td>
<td>Given the K2 cohort of centre A has 20 children and 2 are marked as repeating K2,<br />
when the admin confirms the mass withdrawal,<br />
then 18 children are withdrawn with reason Graduation and 18 year-end refund requests are passed to Fees &amp; Payments.</td>
</tr>
<tr class="even">
<td><strong>AC-JNL-020</strong></td>
<td>Re-enrolment record</td>
<td>Given Ethan Lim withdrew in June 2026,<br />
when the admin re-enrols him for January 2027,<br />
then a new enrolment record is added to his existing profile and no new child profile is created.</td>
</tr>
</tbody>
</table>
