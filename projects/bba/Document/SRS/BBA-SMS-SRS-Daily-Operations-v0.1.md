Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Daily Operations**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-OPS-NNN and acceptance criteria AC-OPS-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Daily Operations module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes what the module must do so that centres can run each day without Taidii: attendance, visitors, daily care records, leave, the centre calendar, the centre log and the safety overview.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/operations. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Child attendance: check in and check out, temperature readings, absence and leave, late arrival, void of wrong records, the day-18 no-attendance alert, the e-Form 1 trigger and attendance reports.

- Staff attendance: clock in and clock out with temperature, staff on site, attendance report.

- Visitors: self sign-in by QR code on the visitor's own phone, sign-out, visitor log.

- Daily routines: meals, bottles, naps, nappy and toilet records per child, shared with parents.

- Child leave requests from the Parents App, with approval by the centre.

- Calendar: centre events, centre closures, fire drills, birthdays and holidays, shown to parents.

- Centre log: one daily log per centre for incidents, accidents, deviations and menu changes, read by the Centre Director.

- Safety overview: allergies, consent gaps, today's touchpoints, centre log gaps and drills, for centres and the HQ Safeguarding team.

- Bus services: groups of children per bus for quick check in and check out.

- What parents see in the Parents App: check-in and check-out, daily routines, leave requests, calendar.

## 1.2 Not in Phase 1

- Full incident reporting, escalation and incident dashboards. Incidents that need reporting to the Safeguarding team or ECDA are still reported outside the system.

- Centre log on mobile devices (Phase 1 is on the SMS web only).

- Medication administration records.

- Infectious disease tracking, symptom checks and exclusion rules.

- CCTV.

- Facility and premises checklists.

- Emergency roll-call.

- Digital drill records (the Emergency Evacuation Record stays on paper).

- Staff leave, rosters, training, relief cover and device handover.

- Parent-teacher conference (PTC) slot booking.

- Check in by QR code, RFID or face recognition.

- Late pickup records and late pickup fees.

- A second attendance mark in the classroom.

- Check out at excursion sites.

- Bus schedules, routes and communication with bus operators.

- Automatic submission of e-Form 1 to ECDA (Phase 1 prepares the list; submission is manual).

- Separate attendance per programme for children in both a main class and an early intervention programme.

# 2. Who uses it

| **Role**                                  | **What they do in this module**                                                                                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Teacher**                               | Checks children in and out; records temperatures and daily routines; creates centre log entries; requests attendance voids; creates class events.                                                |
| **Senior Teacher**                        | Everything a Teacher can do; approves attendance voids and leave requests when the Centre Director assigns them.                                                                                 |
| **Centre Director**                       | Oversees the centre's day; approves attendance voids and leave requests; reads and acknowledges the centre log; manages the centre calendar, drills and bus services; receives the day-18 alert. |
| **Centre Admin / School Admin**           | Runs attendance at the front desk; approves attendance voids; manages visitors, calendar, bus services and exports; receives the day-18 alert.                                                   |
| **Safeguarding officer (HQ)**             | Views the centre log and the safety overview of every centre; exports them for review. Cannot change centre records.                                                                             |
| **District Manager / Operations Manager** | Views attendance, centre log and safety overview of the centres they cover.                                                                                                                      |
| **HQ Admin**                              | Has every permission in the module; configures settings, centre log categories and calendar event types.                                                                                         |
| **Parent (Parents App)**                  | Receives check-in and check-out notifications; views daily routines and the calendar; submits leave requests.                                                                                    |

# 3. Process overview

## P1. Morning arrival

1\. Staff open the Attendance app on the centre iPad at the gate, or Child attendance on the SMS web.

2\. When a bus arrives, staff select the bus service and check in its children together; other children are checked in one by one.

3\. For each child, staff record the adult who brought the child, a photo and a temperature reading.

4\. A reading at or above the fever threshold (default 37.5°C) is flagged to the class teacher and the Centre Director.

5\. A child checked in after the centre's late cut-off (default 9:15 am) is flagged as late, visible to staff only.

6\. The parent receives an in-app check-in notification.

## P2. Pickup

1\. Staff open the child's row and select the person collecting from the approved Authorised pickup list.

2\. Staff take a photo and record the time; the system saves the check out.

3\. The parent receives an in-app check-out notification.

## P3. Attendance void

1\. A staff member finds a wrong attendance record and requests a void with a reason.

2\. A Centre Admin, the Centre Director or a Senior Teacher assigned by the Centre Director approves or rejects it.

3\. An approved void removes the record from attendance; the record stays in history with who, when and why.

4\. Centre Admins, Centre Directors and assigned Senior Teachers void directly, still with a reason.

## P4. Child leave

1\. The parent submits a Personal or Medical leave request in the Parents App, with dates and an optional attachment.

2\. The Centre Director, or a Senior Teacher with delegated approval, approves or rejects it.

3\. The parent is notified of the decision.

4\. On approved leave days the child shows On leave in Child attendance.

## P5. Day-18 no-attendance check

1\. On the run day (default the 18th), the system lists Singapore citizen children with no attendance day in the month so far.

2\. The Centre Director, Centre Admins and the class teachers are notified.

3\. Staff open the "No attendance this month" list and follow up with the families.

## P6. Centre log

1\. During the day, staff create entries of type Incident, Accident, Deviation or Menu, answering the prompts of the chosen category.

2\. If nothing happened, a staff member records "Nothing to report" for the day.

3\. The Centre Director reads each entry and marks it as read.

4\. Days with no entry are flagged on the centre log and in the safety overview.

5\. The HQ Safeguarding team reviews the centre log and the safety overview across centres.

## P7. Fire drill

1\. The Centre Director schedules a Fire drill event on the Calendar.

2\. The safety overview shows the last and next drill of each centre.

3\. A centre with no Fire drill in the last 3 months is flagged and the Centre Director is notified.

# 4. Modules, sub-modules, features and functions

## 1. Attendance

### 1.1 Child attendance

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations</u>](https://bba-sms-crm.lovable.app/operations)

| **Feature**                             | **Function**                                                                                                                                                             |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View class attendance**               | By class and date: status (Present, Absent, On leave, Signed in, Signed out), check-in and check-out times, latest temperature, late flag.                               |
| **Search**                              | Partial match on child name.                                                                                                                                             |
| **Filter**                              | Centre, class, stream (Main / Early intervention / Enrichment), bus service, status.                                                                                     |
| **Sort**                                | By child name or check-in time.                                                                                                                                          |
| **Paging**                              | 20 / 50 / 100 rows.                                                                                                                                                      |
| **Check in**                            | On the Attendance app (centre iPad) at the gate or on the SMS web. Time (default: now), photo and the adult who brought the child.                                       |
| **Check out**                           | On the Attendance app (centre iPad) at the gate or on the SMS web. Time, photo and the person collecting, chosen from the approved Authorised pickup list.               |
| **Bulk check in by bus**                | Select a bus service; all its children are checked in together. Children not on the bus that day are unticked first.                                                     |
| **Check out from a bus list**           | Open the bus list and check out each child with a photo.                                                                                                                 |
| **Record temperature**                  | Any number of readings per day. Default 36.5, range 36 to 40, or "Enter manually".                                                                                       |
| **Read Bluetooth thermometer**          | A paired thermometer fills in the reading automatically.                                                                                                                 |
| **Flag fever**                          | A reading at or above the fever threshold (default 37.5°C) is highlighted and notified.                                                                                  |
| **Mark absent**                         | By hand for a child who did not come.                                                                                                                                    |
| **Mark on leave**                       | Automatically from an approved leave request.                                                                                                                            |
| **Flag late arrival**                   | Automatically when check in is after the centre's late cut-off (default 9:15 am).                                                                                        |
| **Hide late flag from parents**         | The late flag is visible to staff only.                                                                                                                                  |
| **Work offline**                        | Check in, check out and temperatures are saved on the device and synced when the connection returns.                                                                     |
| **Hide temporarily withdrawn children** | They do not appear on the attendance screen.                                                                                                                             |
| **Request void**                        | Any staff member; reason required.                                                                                                                                       |
| **Approve void**                        | Centre Admin, Centre Director or a Senior Teacher assigned by the Centre Director.                                                                                       |
| **Reject void**                         | Reason required.                                                                                                                                                         |
| **Void directly**                       | Centre Admin, Centre Director and assigned Senior Teachers; reason required, no approval.                                                                                |
| **Send day-18 alert**                   | On the run day (default the 18th), Singapore citizen children with no attendance day in the month are notified to the Centre Director, Centre Admins and class teachers. |
| **View "No attendance this month"**     | List of these children; each row opens the child.                                                                                                                        |
| **Add to e-Form 1 list**                | The first real attendance of an enrolment adds the child to the 12:00 e-Form 1 batch list for ECDA.                                                                      |
| **Notify parents**                      | In-app notification on check in and check out.                                                                                                                           |
| **View history**                        | Every change and void: who, when, reason.                                                                                                                                |
| **Export attendance report**            | Any date range; by class, level, brand or centre. Large reports run in the background.                                                                                   |
| **Export temperature list**             | Readings by date range and class.                                                                                                                                        |

### 1.2 Staff attendance

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/staff-attendance</u>](https://bba-sms-crm.lovable.app/operations/staff-attendance)

| **Feature**                  | **Function**                                                          |
|------------------------------|-----------------------------------------------------------------------|
| **Clock in**                 | On the Attendance app or the SMS web.                                 |
| **Clock out**                | On the Attendance app or the SMS web.                                 |
| **Record staff temperature** | At clock in.                                                          |
| **View staff on site**       | By centre and date: name, clock-in time, clock-out time, temperature. |
| **Search**                   | Staff name.                                                           |
| **Filter**                   | Centre, date.                                                         |
| **Export**                   | Staff attendance report by date range.                                |

### 1.3 Visitors

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/visitors</u>](https://bba-sms-crm.lovable.app/operations/visitors)

| **Feature**               | **Function**                                                                                                                                          |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Show centre QR code**   | One QR code per centre, printable for the entrance.                                                                                                   |
| **Sign in visitor**       | The visitor scans the QR code on their own phone, in the browser with no app: name, purpose, phone number, temperature; the sign-in time is recorded. |
| **Sign out visitor**      | By the visitor from the same page, or by staff; the sign-out time is recorded.                                                                        |
| **View visitors on site** | Number and list of visitors signed in and not signed out.                                                                                             |
| **View visitor log**      | All visitors by date.                                                                                                                                 |
| **Search**                | Visitor name.                                                                                                                                         |
| **Filter**                | Centre, date.                                                                                                                                         |
| **Export**                | Visitor log for contact tracing.                                                                                                                      |

## 2. Daily care

### 2.1 Daily routines

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/routines</u>](https://bba-sms-crm.lovable.app/operations/routines)

| **Feature**                     | **Function**                                                                         |
|---------------------------------|--------------------------------------------------------------------------------------|
| **View routines by class**      | By date: each child's meals, naps and nappy records, and the missing required items. |
| **View notes from home**        | Notes the parent added for the day.                                                  |
| **Search**                      | Child name.                                                                          |
| **Filter**                      | Class, missing item.                                                                 |
| **Sort**                        | By child name or last entry time.                                                    |
| **Record for the whole class**  | One entry for all children, then adjust each child.                                  |
| **Record meal**                 | All / Most / Some / None.                                                            |
| **Record bottle**               | Millilitres prepared and millilitres drunk.                                          |
| **Record nap**                  | Start time, end time, quality; the duration is calculated.                           |
| **Record nappy / toilet**       | Diaper, Potty or Accident; Wet, BM or Dry.                                           |
| **Edit entry**                  | Change the time or details; who edited is recorded.                                  |
| **Configure required routines** | By level (default: Infant and Playgroup).                                            |
| **Show in Parents App**         | Parents see their own child's routines by day.                                       |
| **View history**                | Who recorded and who edited each entry.                                              |
| **Export**                      | Routines by date range and class.                                                    |

### 2.2 Child leave requests

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/leave</u>](https://bba-sms-crm.lovable.app/operations/leave)

| **Feature**               | **Function**                                                                                                                                                                                     |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Submit leave (parent)** | In the Parents App: Personal or Medical, dates, optional attachment. Two notices are shown: a Singapore child needs at least one attendance day each month; fees are not reduced for leave days. |
| **View leave list**       | Child, class, type, dates, status (Pending / Approved / Rejected).                                                                                                                               |
| **Search**                | Child name.                                                                                                                                                                                      |
| **Filter**                | Status, class, type.                                                                                                                                                                             |
| **Sort**                  | By start date (default: newest first).                                                                                                                                                           |
| **View leave detail**     | Dates, type, reason, attachment, decision history.                                                                                                                                               |
| **Approve leave**         | Centre Director, or a Senior Teacher with delegated approval.                                                                                                                                    |
| **Reject leave**          | Reason required.                                                                                                                                                                                 |
| **Delegate approval**     | The Centre Director assigns Senior Teachers who can approve.                                                                                                                                     |
| **Notify parent**         | In-app notification of the decision.                                                                                                                                                             |
| **Mark on leave**         | Approved leave days show On leave in Child attendance.                                                                                                                                           |
| **Export**                | Leave requests by date range.                                                                                                                                                                    |

## 3. Calendar

### 3.1 Calendar

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/calendar</u>](https://bba-sms-crm.lovable.app/operations/calendar)

| **Feature**                     | **Function**                                                                                                                          |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **View calendar**               | Day, week, month or list view.                                                                                                        |
| **Filter**                      | Event type, audience (centre, class, staff only), centre.                                                                             |
| **Create event**                | Type (Event, Centre closure, Fire drill, PTC, Learning journey, Other), title, date and time, centre, classes, audience, description. |
| **Edit event**                  | Any field until the event date.                                                                                                       |
| **Cancel event**                | Reason required; parents who could see it are notified.                                                                               |
| **Auto-create birthdays**       | From each child's date of birth, for the child's class.                                                                               |
| **Auto-create public holidays** | From the holiday list set by HQ Admin per country.                                                                                    |
| **Auto-create school visits**   | From visits booked in Enquiries.                                                                                                      |
| **Download import template**    | Excel template.                                                                                                                       |
| **Import events**               | Upload, row-by-row errors, confirm.                                                                                                   |
| **Show to parents**             | Events with a parent audience appear in the Parents App.                                                                              |
| **Show allergy warning**        | Birthday and food events show the allergies of the children in the class.                                                             |
| **Export**                      | Events in the filtered period.                                                                                                        |

### 3.2 Drills

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/calendar</u>](https://bba-sms-crm.lovable.app/operations/calendar)

| **Feature**                        | **Function**                                                                                     |
|------------------------------------|--------------------------------------------------------------------------------------------------|
| **Schedule fire drill**            | A Calendar event of type Fire drill for the centre.                                              |
| **Suggest next drill**             | After a drill date passes, the next date is suggested (default: 3 months later).                 |
| **Edit drill**                     | Date and time.                                                                                   |
| **Cancel drill**                   | Reason required.                                                                                 |
| **List drills in Safety overview** | Last and next Fire drill per centre.                                                             |
| **Flag overdue drill**             | A centre with no Fire drill in the last 3 months is flagged and the Centre Director is notified. |

## 4. Safety

### 4.1 Centre log

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/centre-log</u>](https://bba-sms-crm.lovable.app/operations/centre-log)

| **Feature**                    | **Function**                                                                                                                            |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **View log**                   | By centre and date: type, category, time, author, read status.                                                                          |
| **Search**                     | Entry text.                                                                                                                             |
| **Filter**                     | Centre, type, category, date, author, read status.                                                                                      |
| **Sort**                       | By date and time (default: newest first).                                                                                               |
| **Paging**                     | 20 / 50 / 100 rows.                                                                                                                     |
| **Create entry**               | Type (Incident, Accident, Deviation, Menu), category, date and time, children involved (optional), description, attachments (optional). |
| **Answer category prompts**    | Each category shows its prompt questions to fill in.                                                                                    |
| **Create entry from Home**     | A shortcut on the Home screen and on Child attendance.                                                                                  |
| **Record "Nothing to report"** | One entry that closes the day when nothing happened.                                                                                    |
| **Flag missing day**           | A day with no entry is flagged on the log and in the Safety overview.                                                                   |
| **Edit entry**                 | The author, the Centre Admin or the Centre Director; every edit is kept in history.                                                     |
| **Mark as read**               | The Centre Director reads and acknowledges each entry. There is no approval.                                                            |
| **Configure categories**       | HQ Admin sets the categories and prompt questions per type.                                                                             |
| **View history**               | Created, edited, read: who, when.                                                                                                       |
| **Export**                     | Centre log report by date range and centre.                                                                                             |

### 4.2 Safety overview

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/safety</u>](https://bba-sms-crm.lovable.app/operations/safety)

| **Feature**                      | **Function**                                                                    |
|----------------------------------|---------------------------------------------------------------------------------|
| **View allergy overview**        | Shortcut to Children & families › Health & allergies, by class and centre.      |
| **View consent gaps**            | Children without media consent or PDPA consent.                                 |
| **View high temperatures today** | Readings at or above the fever threshold.                                       |
| **View visitors on site**        | By centre.                                                                      |
| **View centre log gaps**         | Days with no centre log entry, and entries not yet read by the Centre Director. |
| **View drills**                  | Last and next Fire drill per centre; overdue centres highlighted.               |
| **Filter**                       | Centre, date.                                                                   |
| **Export**                       | Each list.                                                                      |

## 5. Bus services

### 5.1 Bus services

*Prototype:* [<u>https://bba-sms-crm.lovable.app/operations/bus</u>](https://bba-sms-crm.lovable.app/operations/bus)

| **Feature**                         | **Function**                                                                 |
|-------------------------------------|------------------------------------------------------------------------------|
| **View bus service list**           | Name, centre, driver and bus assistant contacts, number of children, status. |
| **Search**                          | Bus service name.                                                            |
| **Filter**                          | Centre, status (Active / Inactive).                                          |
| **Create bus service**              | Name, centre, driver name and phone, bus assistant name and phone.           |
| **Edit bus service**                | Name and contacts.                                                           |
| **Deactivate bus service**          | Instead of delete; it is no longer offered in attendance.                    |
| **Assign child to a bus service**   | On the child's profile or from the bus service.                              |
| **Remove child from a bus service** | From the child's profile or the bus service.                                 |
| **View children on a bus service**  | List with class and today's attendance status.                               |
| **Export**                          | Bus services with their children.                                            |

# 5. Business rules

## Check in and check out

| **ID**         | **Rule**                                                                                                                                                                                                                                              |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-001** | In Singapore and Malaysia, attendance is taken once per child per day: at the centre gate on the Attendance app (centre iPad), or on the SMS web. That single check in is the attendance record. There is no second attendance mark in the classroom. |
| **BR-OPS-002** | The SMS web can take attendance and is also used to correct, void and report it. Teachers do not take attendance in the Teacher App.                                                                                                                  |
| **BR-OPS-003** | Check in records the adult who brought the child, not the staff member who pressed the button.                                                                                                                                                        |
| **BR-OPS-004** | Check out is allowed only to a person on the child's approved Authorised pickup list. A new person must be added by the parent in the Parents App and approved by the centre first.                                                                   |
| **BR-OPS-005** | Every check in and check out has a photo.                                                                                                                                                                                                             |
| **BR-OPS-006** | Bus children can be checked in as a group; each child is checked out individually with a photo.                                                                                                                                                       |
| **BR-OPS-007** | Check in, check out and temperatures work without internet on the Attendance app and sync when the connection returns.                                                                                                                                |
| **BR-OPS-008** | Temporarily withdrawn children are hidden from the attendance screen.                                                                                                                                                                                 |
| **BR-OPS-009** | Parents receive an in-app notification on every check in and check out.                                                                                                                                                                               |

## Temperature

| **ID**         | **Rule**                                                                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-010** | A child can have any number of temperature readings in a day (for example arrival, nap time and departure).                                                 |
| **BR-OPS-011** | The temperature picker defaults to 36.5°C with a range of 36°C to 40°C; staff can enter a value manually.                                                   |
| **BR-OPS-012** | A reading at or above the fever threshold is flagged to the class teacher and the Centre Director. The threshold is a setting per country (default 37.5°C). |
| **BR-OPS-013** | Staff temperature is recorded at clock in.                                                                                                                  |

## Absence, late arrival and leave

| **ID**         | **Rule**                                                                                                                                       |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-014** | Late arrival is flagged automatically when check in is after the centre's late cut-off. The cut-off is a setting per centre (default 9:15 am). |
| **BR-OPS-015** | The late flag is visible to staff only and never shown to parents.                                                                             |
| **BR-OPS-016** | Approved leave days show On leave automatically; other absences are marked by hand.                                                            |
| **BR-OPS-017** | Leave requests are approved by the Centre Director, or by a Senior Teacher the Centre Director has delegated.                                  |
| **BR-OPS-018** | Rejecting a leave request requires a reason.                                                                                                   |
| **BR-OPS-019** | Leave does not reduce fees, and the parent sees this notice when submitting a request.                                                         |

## Attendance void

| **ID**         | **Rule**                                                                                                                   |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-020** | A wrong attendance record is voided, not checked out. A voided record no longer counts as attendance and stays in history. |
| **BR-OPS-021** | Any staff member can request a void, with a reason.                                                                        |
| **BR-OPS-022** | Centre Admins, the Centre Director and Senior Teachers assigned by the Centre Director approve or reject void requests.    |
| **BR-OPS-023** | These three roles can void directly without approval, still with a reason.                                                 |
| **BR-OPS-024** | Every void keeps an audit trail: who requested, who approved, when and why.                                                |

## Subsidy and ECDA

| **ID**         | **Rule**                                                                                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-025** | The day-18 alert covers Singapore citizen children only. It runs on the run day (default the 18th) and lists children with no attendance day in the month so far. |
| **BR-OPS-026** | The day-18 alert goes to the Centre Director, Centre Admins and the child's class teachers.                                                                       |
| **BR-OPS-027** | The first real attendance of an enrolment adds the child to the e-Form 1 list for the 12:00 batch. Submission to ECDA is manual in Phase 1.                       |

## Daily routines

| **ID**         | **Rule**                                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-028** | Routines can be recorded once for the whole class and then adjusted per child.                                           |
| **BR-OPS-029** | Required routines are set per level (default: Infant and Playgroup). Missing required items are shown on the class view. |
| **BR-OPS-030** | Every entry records who created it and who edited it.                                                                    |
| **BR-OPS-031** | Parents see only their own child's routines.                                                                             |

## Visitors

| **ID**         | **Rule**                                                                                                        |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| **BR-OPS-032** | Visitors sign in on their own phone by scanning the centre's QR code; no shared tablet and no app installation. |
| **BR-OPS-033** | The visitor sign-in page shows no child names or photos.                                                        |
| **BR-OPS-034** | Visitors still on site appear in Visitors and in the Safety overview until signed out.                          |

## Calendar and drills

| **ID**         | **Rule**                                                                                                                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-035** | Teachers create Event, Learning journey and Other events for their own classes. The Centre Director and Centre Admins create every event type for their centre. HQ Admin manages public holidays. |
| **BR-OPS-036** | Only the Centre Director, Centre Admins and HQ Admin can create a Centre closure.                                                                                                                 |
| **BR-OPS-037** | Birthdays, public holidays and school visits are created automatically.                                                                                                                           |
| **BR-OPS-038** | Birthday and food events show the allergies of the children in the class.                                                                                                                         |
| **BR-OPS-039** | Fire drills are Calendar events of type Fire drill. The drill interval is a setting (default every 3 months); a centre past the interval is flagged.                                              |
| **BR-OPS-040** | Drill records (evacuation time, headcount, evaluation) are kept outside the system in Phase 1.                                                                                                    |

## Centre log

| **ID**         | **Rule**                                                                                                                              |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-041** | Each centre has one centre log shared by teachers, admin and the Centre Director.                                                     |
| **BR-OPS-042** | Every entry has one of four types: Incident, Accident, Deviation or Menu.                                                             |
| **BR-OPS-043** | Each category has its own prompt questions, set by HQ Admin.                                                                          |
| **BR-OPS-044** | Each centre must have at least one entry per day; "Nothing to report" counts as an entry.                                             |
| **BR-OPS-045** | The Centre Director marks entries as read. Entries are not approved or rejected.                                                      |
| **BR-OPS-046** | Entries are never deleted; edits are kept in history and shown on the entry.                                                          |
| **BR-OPS-047** | Incidents that need reporting to the Safeguarding team or ECDA are reported outside the system; the centre log keeps the record only. |
| **BR-OPS-048** | The centre log is available on the SMS web only.                                                                                      |

## Access

| **ID**         | **Rule**                                                                                                               |
|----------------|------------------------------------------------------------------------------------------------------------------------|
| **BR-OPS-049** | The Safeguarding officer sees the centre log and the Safety overview of every centre and cannot change centre records. |
| **BR-OPS-050** | District Managers and Operations Managers see the centres they cover.                                                  |
| **BR-OPS-051** | Bus services are deactivated, not deleted, once children have been assigned.                                           |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**             | **Recipient**                                           | **Channel**          | **When**                                                           |
|------------------------------|---------------------------------------------------------|----------------------|--------------------------------------------------------------------|
| **Child checked in**         | Parent                                                  | In-app               | On check in                                                        |
| **Child checked out**        | Parent                                                  | In-app               | On check out, with the name of the person collecting               |
| **Fever reading**            | Class teacher, Centre Director                          | In-app (web and app) | When a reading is at or above the fever threshold                  |
| **Void request**             | Centre Admin, Centre Director, assigned Senior Teachers | In-app (web and app) | When a void is requested                                           |
| **Void decision**            | Requester                                               | In-app (web and app) | When a void request is approved or rejected                        |
| **No attendance this month** | Centre Director, Centre Admins, class teachers          | In-app (web and app) | On the day-18 run day                                              |
| **New leave request**        | Centre Director, delegated Senior Teachers              | In-app (web and app) | When a parent submits a request                                    |
| **Leave decision**           | Parent                                                  | In-app               | When the request is approved or rejected                           |
| **Daily routines updated**   | Parent                                                  | In-app               | Once a day, when the child is checked out                          |
| **New or changed event**     | Parents in the audience                                 | In-app               | When an event or centre closure is published, changed or cancelled |
| **New centre log entry**     | Centre Director                                         | In-app (web)         | When an Incident or Accident entry is created                      |
| **Missing centre log day**   | Centre Director, Centre Admins                          | In-app (web)         | The morning after a day with no entry                              |
| **Drill overdue**            | Centre Director                                         | In-app (web)         | When no Fire drill has taken place within the drill interval       |

## 6.2 Documents

- Visitor QR code per centre, printable for the entrance.

- Import template for calendar events (Excel).

# 7. Reports & exports

| **Report**                        | **Content**                                                                                                | **Used by**                             |
|-----------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| **Daily student attendance list** | Attendance per child per day with times and status; replaces the Taidii export                             | Centre Admin, Centre Director           |
| **Attendance report**             | Any date range, by class, level, brand or centre; runs in the background when large                        | Centre Admin, Centre Director, HQ Admin |
| **Temperature list**              | All readings by date range and class                                                                       | Centre Admin, Centre Director           |
| **No attendance this month**      | Singapore citizen children with no attendance day in the month                                             | Centre Director, Centre Admin           |
| **Void log**                      | Voided attendance records with requester, approver and reason                                              | Centre Director, HQ Admin               |
| **Staff attendance**              | Clock-in and clock-out times and temperatures by date range                                                | Centre Director, HQ Admin               |
| **Visitor log**                   | Visitors by date with times and temperature, for contact tracing                                           | Centre Admin, Centre Director           |
| **Daily routines**                | Meals, bottles, naps and nappy records by date range and class; replaces the Taidii Infant Activity export | Centre Director, Teacher                |
| **Leave requests**                | Requests and decisions by date range                                                                       | Centre Director, Centre Admin           |
| **Centre log report**             | Entries by date range and centre; replaces the Taidii Centre Log Report                                    | Centre Director, Safeguarding officer   |
| **Calendar**                      | Events in the selected period                                                                              | Centre Admin, Centre Director           |
| **Safety overview**               | Consent gaps, centre log gaps and drills per centre                                                        | Safeguarding officer, HQ Admin          |
| **Bus services**                  | Bus services with contacts and children                                                                    | Centre Admin                            |

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
<td><strong>AC-OPS-001</strong></td>
<td>Check in</td>
<td>Given child Mia is not yet checked in at 8:10 am,<br />
when a staff member checks her in with her father as the adult and a photo,<br />
then Mia shows Signed in at 8:10 am with her father recorded, and the parent receives an in-app notification.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-002</strong></td>
<td>Authorised pickup only</td>
<td>Given Mia's approved Authorised pickup list has her mother and grandmother,<br />
when a staff member checks her out,<br />
then only these two people can be selected as the person collecting.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-003</strong></td>
<td>Bulk check in by bus</td>
<td>Given bus service Bus A has 8 children and Ethan did not take the bus today,<br />
when the staff member selects Bus A, unticks Ethan and confirms,<br />
then 7 children are checked in and Ethan stays not checked in.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-004</strong></td>
<td>Multiple temperatures</td>
<td>Given Mia has a 36.6°C reading at arrival,<br />
when a second reading of 37.8°C is recorded at nap time,<br />
then both readings are kept and the second is flagged to the class teacher and the Centre Director as a fever.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-005</strong></td>
<td>Late arrival</td>
<td>Given centre A's late cut-off is 9:15 am,<br />
when Noah is checked in at 9:20 am,<br />
then Noah is flagged late for staff and the parent's notification does not mention late.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-006</strong></td>
<td>Offline check in</td>
<td>Given the Attendance app has no internet connection,<br />
when staff check in 5 children,<br />
then the check ins are saved on the device and appear in the SMS when the connection returns.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-007</strong></td>
<td>Void request</td>
<td>Given a teacher checked in Liam by mistake,<br />
when she requests a void with the reason "Wrong child",<br />
then the request reaches the Centre Admin, the Centre Director and the assigned Senior Teachers, and the record stays until approved.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-008</strong></td>
<td>Void by approver</td>
<td>Given a Centre Admin finds a wrong check in,<br />
when she voids it with a reason,<br />
then the record is voided immediately with no approval and the history shows who, when and why.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-009</strong></td>
<td>Void reason required</td>
<td>Given a void request is being created,<br />
when the user submits it without a reason,<br />
then the system does not allow it.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-010</strong></td>
<td>Day-18 alert</td>
<td>Given on 18 October, Singapore citizen Ava and a foreign child Ben have no attendance day in October,<br />
when the day-18 run starts,<br />
then only Ava is listed in "No attendance this month" and the Centre Director, Centre Admins and her class teachers are notified.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-011</strong></td>
<td>Temporarily withdrawn child</td>
<td>Given Zoe is on temporary withdrawal,<br />
when a staff member opens her class attendance,<br />
then Zoe is not shown.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-012</strong></td>
<td>Approved leave</td>
<td>Given Mia's parent submits Medical leave for 20 to 21 October and the Centre Director approves it,<br />
when staff open attendance on 20 October,<br />
then Mia shows On leave and her parent has been notified of the approval.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-013</strong></td>
<td>Delegated leave approval</td>
<td>Given the Centre Director has delegated leave approval to Senior Teacher Sarah,<br />
when a leave request is submitted,<br />
then Sarah can approve or reject it.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-014</strong></td>
<td>Routines for the class</td>
<td>Given Infant class A has 10 children,<br />
when the teacher records lunch "All" for the whole class and changes one child to "Some",<br />
then 9 children show All, one shows Some, and each parent sees only their own child's record.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-015</strong></td>
<td>Visitor sign-in</td>
<td>Given a visitor scans centre A's QR code on his phone,<br />
when he enters name, purpose, phone number and temperature,<br />
then he appears in Visitors on site and in the Safety overview until signed out.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-016</strong></td>
<td>Centre log missing day</td>
<td>Given centre A has no centre log entry on 13 October,<br />
when the morning of 14 October comes,<br />
then 13 October is flagged on the centre log and in the Safety overview, and the Centre Director is notified.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-017</strong></td>
<td>Nothing to report</td>
<td>Given nothing happened at centre A on 14 October,<br />
when a teacher records "Nothing to report",<br />
then 14 October is not flagged as missing.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-018</strong></td>
<td>Centre log read</td>
<td>Given an Accident entry is created at centre A,<br />
when the Centre Director opens it and marks it as read,<br />
then the entry shows read by the Centre Director with the date and time, and has no approve or reject action.</td>
</tr>
<tr class="odd">
<td><strong>AC-OPS-019</strong></td>
<td>Safeguarding view</td>
<td>Given a Safeguarding officer is signed in,<br />
when she opens the centre log of any centre,<br />
then she can view and export entries but cannot create or edit them.</td>
</tr>
<tr class="even">
<td><strong>AC-OPS-020</strong></td>
<td>Overdue drill</td>
<td>Given centre A's last Fire drill was on 1 June and no drill is scheduled,<br />
when it is 2 September,<br />
then centre A is flagged in the Safety overview and the Centre Director is notified.</td>
</tr>
</tbody>
</table>
