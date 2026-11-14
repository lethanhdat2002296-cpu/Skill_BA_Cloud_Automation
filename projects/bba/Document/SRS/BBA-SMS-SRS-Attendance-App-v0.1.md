Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Attendance App**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-ATT-NNN and acceptance criteria AC-ATT-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Attendance App of the Busy Bees Asia School Management System (SMS), Phase 1. The Attendance App runs on a shared iPad at the centre gate. Staff use it to check children in and out, take temperatures and clock themselves in and out. It also shows how many visitors are on site; visitors sign themselves in on their own phone.

The Attendance App and Child attendance on the SMS web write to the same attendance record. Corrections, voids, approvals and reports are done on the SMS web and are described in the Daily Operations SRS.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-attendance-visitor.lovable.app. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Device set-up: the shared iPad signs in with the centre's account and remembers the level and class it serves.

- Children screen: every child in scope as a card, with search by name, bus service filter and the day's status.

- Child check in: time, photo, the adult who brought the child and a temperature reading, one child at a time or a whole bus at once.

- Child check out: time, photo and the person collecting, chosen from the approved Authorised pickup list.

- Temperature readings: any number per child per day, with Bluetooth thermometer support and a fever flag.

- Void requests: any staff member can request a void from the iPad; approval happens on the SMS web.

- Staff clock in and clock out with temperature.

- Offline working: every record is saved on the iPad first and synced when the connection returns, with a sync queue.

- Visitors: self sign-in and sign-out by QR code on the visitor's own phone, a count of visitors on site at the gate, and a staff fallback.

- Check-in and check-out notifications to parents in the Parents App.

## 1.2 Not in Phase 1

- Check in by QR code, RFID or face recognition for children.

- Check out at excursion sites.

- Late pickup records and late pickup fees.

- Emergency roll-call.

- Check in on the school bus (boarding the bus as attendance).

- Staff leave and rosters.

- A second attendance mark in the classroom, and attendance in the Teacher App.

- Approving voids or voiding directly on the iPad (done on the SMS web).

- Reports, charts and statistics on the iPad (done on the SMS web).

- Symptom checklists at check out carried over to the next day's check in.

- Visit appointments and NRIC capture for visitors.

# 2. Who uses it

| **Role**                        | **What they do in this module**                                                                                                                                                                                                                         |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Gate staff (centre account)** | Any Teacher or Centre Admin on duty at the gate. Uses the iPad signed in with the centre's account: checks children in and out, takes temperatures, requests voids, signs visitors in by hand. The staff member who presses the button is not recorded. |
| **Staff member**                | Clocks in and out on the iPad with a personal PIN and a temperature reading.                                                                                                                                                                            |
| **Centre Admin**                | Sets up the iPad with the centre account; reviews the sync queue; approves void requests and voids directly on the SMS web.                                                                                                                             |
| **Centre Director**             | Approves void requests and voids directly on the SMS web; receives fever alerts; assigns Senior Teachers who can approve voids.                                                                                                                         |
| **Senior Teacher (assigned)**   | Approves void requests and voids directly on the SMS web when the Centre Director assigns them.                                                                                                                                                         |
| **Visitor**                     | Signs in and out on their own phone by scanning the centre's QR code. Never uses the iPad.                                                                                                                                                              |
| **Parent (Parents App)**        | Receives a notification on every check in and check out of their child.                                                                                                                                                                                 |
| **HQ Admin**                    | Creates centre accounts for the iPads; sets the fever threshold, late cut-off, idle time and visitor data retention.                                                                                                                                    |

# 3. Process overview

## P1. Morning arrival at the gate

1\. The iPad opens on the Children screen of the centre, with the scope shown in the header.

2\. When a bus arrives, staff filter by the bus service, untick children not on the bus and check in the rest together.

3\. For a child brought by an adult, staff find the child by name and open Check in.

4\. Staff record the adult who brought the child, take a photo and record a temperature; the time defaults to now.

5\. A reading at or above the fever threshold (default 37.5°C) is flagged in red and the class teacher and Centre Director are notified.

6\. The record syncs to the SMS and the parent receives an in-app check-in notification.

## P2. Pickup at the gate

1\. Staff find the child and open Check out.

2\. Staff select the person collecting from the child's approved Authorised pickup list.

3\. Staff take a photo; the time defaults to now; the record is saved.

4\. The parent receives an in-app check-out notification with the name of the person collecting.

## P3. Temperature during the day

1\. Staff open a child and choose Add temperature reading.

2\. The Bluetooth thermometer fills in the value, or staff pick it (default 36.5) or enter it manually.

3\. Staff choose or type a label, for example Before nap.

4\. A raised reading is flagged and notified as in P1.

## P4. Working offline

1\. The network drops; the header says so in plain words.

2\. Staff keep checking in, checking out and taking temperatures; each record is saved on the iPad and shows Not synced.

3\. A record that is still Not synced can be corrected; every correction is kept.

4\. When the connection returns, records sync; any failure shows its reason and can be retried one by one.

5\. Parent notifications are sent when each record reaches the SMS.

## P5. Wrong attendance record

1\. Staff find a synced record that is wrong, for example the wrong child was checked in.

2\. Staff open the record, choose Request void, type their name and a reason.

3\. The request appears on the SMS web for the Centre Admin, the Centre Director and assigned Senior Teachers.

4\. An approver approves or rejects it on the SMS web; the iPad shows the outcome on the child's day.

## P6. Staff clock in and clock out

1\. On arrival, a staff member opens Staff on the iPad and selects their name.

2\. They enter their personal PIN and record a temperature.

3\. The clock-in time is recorded; at the end of the day they clock out the same way without a temperature.

## P7. Visitor

1\. The visitor scans the centre's QR code at the entrance on their own phone; a web page opens with no app and no login.

2\. The visitor enters a phone number; the page reads the data notice and checks for an open visit.

3\. With no open visit, the visitor enters name, purpose and temperature and is signed in.

4\. The Visitors screen on the iPad shows the number of visitors on site.

5\. On leaving, the visitor scans again, confirms "Is this you?" and is signed out.

6\. At closing time any open visit is closed and marked Did not scan out.

# 4. Modules, sub-modules, features and functions

## 1. Device

### 1.1 Device set-up

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/settings</u>](https://bba-attendance-visitor.lovable.app/settings)

| **Feature**                     | **Function**                                                                                                                                                                |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sign in with centre account** | A Centre Admin signs the iPad in once with the centre's account created by HQ Admin. No personal login for gate staff.                                                      |
| **Choose level**                | A level of the centre, or All levels.                                                                                                                                       |
| **Choose class**                | A class of the chosen level, or All classes. A gate iPad normally serves the whole centre.                                                                                  |
| **Remember scope**              | The scope stays on the iPad after the app closes or restarts.                                                                                                               |
| **Show scope in header**        | Centre, level and class in plain words on every screen, for example "Busy Bees @ Tampines · All levels · All classes".                                                      |
| **Change scope**                | Reopens the picker with the current choice selected.                                                                                                                        |
| **Set screen orientation**      | Landscape or portrait (default: landscape).                                                                                                                                 |
| **Show fever threshold**        | Read-only; the value comes from the SMS setting for the country (default 37.5°C).                                                                                           |
| **Lock idle screen**            | After a period with no touch (default: 2 minutes), the app shows a cover screen with the centre name only and no child names or photos. One tap returns to the last screen. |
| **Show network status**         | Network on or No network, with a plain message when offline.                                                                                                                |
| **Sign out the device**         | Centre Admin only; blocked while records are Not synced.                                                                                                                    |

## 2. Child attendance

### 2.1 Children

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/</u>](https://bba-attendance-visitor.lovable.app/)

| **Feature**                             | **Function**                                                                                                    |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **View children**                       | Cards with photo or initials, name and the day's status: Not here yet, Signed in, Signed out, On leave, Absent. |
| **Show temperature status**             | Whether a reading has been taken today, and a red flag when a reading is raised.                                |
| **Show late flag**                      | A late marker when check in was after the centre's late cut-off (default 9:15 am).                              |
| **Search**                              | Child name, matched as it is typed.                                                                             |
| **Filter by bus service**               | Shows only the children assigned to the chosen bus service.                                                     |
| **Choose date**                         | Look back at a previous day; new records are always saved against today.                                        |
| **Hide temporarily withdrawn children** | Children on temporary withdrawal or suspension are not shown.                                                   |
| **Show empty state**                    | An empty list names the scope and the date, for example "No children in K1 · Sunflower on 23/09/2026".          |
| **View child's day**                    | Arrival, going home, all temperature readings and void requests for the date.                                   |

### 2.2 Check in

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/</u>](https://bba-attendance-visitor.lovable.app/)

| **Feature**                            | **Function**                                                                                                            |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Check in**                           | One check in per child per day.                                                                                         |
| **Set time**                           | Defaults to now; staff can correct it.                                                                                  |
| **Record adult who brought the child** | Chosen from the child's parents and Authorised pickup list, or Someone else with a typed name and relationship.         |
| **Take photo**                         | Full-screen camera with shutter, switch camera, retake and save. Required.                                              |
| **Record temperature**                 | Picker defaults to 36.5°C with a range of 36°C to 40°C, or "Enter manually". Required at check in.                      |
| **Read Bluetooth thermometer**         | A paired thermometer fills in the reading automatically.                                                                |
| **Flag fever**                         | A reading at or above the threshold is shown in red and notified.                                                       |
| **Flag late arrival**                  | Automatically when check in is after the late cut-off; visible to staff only.                                           |
| **Block second check in**              | A child already checked in shows "Already checked in at 08:10" instead of the button.                                   |
| **Bulk check in by bus**               | Select a bus service; all its children not yet checked in are ticked; staff untick children not on the bus and confirm. |
| **Notify parent**                      | In-app check-in notification once the record reaches the SMS.                                                           |

### 2.3 Check out

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/</u>](https://bba-attendance-visitor.lovable.app/)

| **Feature**                         | **Function**                                                                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| **Check out**                       | One check out per child per day.                                                             |
| **Set time**                        | Defaults to now; staff can correct it.                                                       |
| **Select person collecting**        | Only from the child's approved Authorised pickup list.                                       |
| **Take photo**                      | Full-screen camera. Required.                                                                |
| **Block check out before check in** | A child not checked in cannot be checked out; the screen explains and offers Check in first. |
| **Check out bus children**          | Each child is checked out individually with a photo, from the bus service filter.            |
| **Notify parent**                   | In-app check-out notification with the name of the person collecting.                        |

### 2.4 Temperature readings

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/</u>](https://bba-attendance-visitor.lovable.app/)

| **Feature**                    | **Function**                                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------------------------|
| **Add temperature reading**    | A separate action at any time of day; no limit on the number of readings.                             |
| **Choose label**               | Suggestions On arrival, Mid-morning, Before nap, After nap, Going home, or free text.                 |
| **Read Bluetooth thermometer** | A paired thermometer fills in the reading automatically.                                              |
| **Enter manually**             | Picker default 36.5°C, range 36°C to 40°C, or typed value.                                            |
| **Flag fever**                 | A reading at or above the threshold is shown in red on the card and in the child's day, and notified. |
| **View readings**              | All readings of the day in time order with time, value and label.                                     |

### 2.5 Void requests

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/</u>](https://bba-attendance-visitor.lovable.app/)

| **Feature**             | **Function**                                                                                |
|-------------------------|---------------------------------------------------------------------------------------------|
| **Request void**        | On a synced check in or check out: the requester's name and a reason are required.          |
| **View request status** | Pending, Approved or Rejected, on the child's day.                                          |
| **Show voided record**  | A voided record is shown struck through with the reason; it no longer counts as attendance. |

## 3. Staff attendance

### 3.1 Staff clock in

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/</u>](https://bba-attendance-visitor.lovable.app/)

| **Feature**                  | **Function**                                                               |
|------------------------------|----------------------------------------------------------------------------|
| **Select staff name**        | From the staff list of the centre.                                         |
| **Enter personal PIN**       | A 4-digit PIN set by the staff member in the SMS (default: required).      |
| **Clock in**                 | Time defaults to now.                                                      |
| **Record staff temperature** | Same picker as for children; required at clock in.                         |
| **Clock out**                | Same steps without temperature.                                            |
| **Block double clock in**    | A staff member already clocked in sees Clock out instead.                  |
| **View staff on site**       | Names and clock-in times of staff clocked in today; no temperatures shown. |

## 4. Sync

### 4.1 Sync queue

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/queue</u>](https://bba-attendance-visitor.lovable.app/queue)

| **Feature**              | **Function**                                                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Save on device first** | Every check in, check out, temperature, staff clock record and void request is saved on the iPad before it is sent.     |
| **View queue**           | Code, activity, child or staff name, date and time, status: Synced, Not synced, Sync error.                             |
| **Filter by activity**   | Check in, Check out, Temperature reading, Staff clock, Void request.                                                    |
| **Filter by status**     | Synced, Not synced, Sync error.                                                                                         |
| **Filter by date**       | One day.                                                                                                                |
| **Sync all**             | A button with the number waiting, for example "Sync (12)". Syncing also runs automatically when the connection returns. |
| **Retry one record**     | On a row with Sync error.                                                                                               |
| **Show error reason**    | Each failed row says what went wrong in plain words.                                                                    |
| **Fix a mistake**        | A record that is Not synced can be corrected; every correction is listed on the record.                                 |
| **Lock synced records**  | A synced record cannot be changed on the iPad; changes go through a void request.                                       |
| **Show waiting count**   | The number of records waiting is shown on the Sync queue menu item.                                                     |

## 5. Visitors

### 5.1 Visitors on site

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/visitors</u>](https://bba-attendance-visitor.lovable.app/visitors)

| **Feature**                      | **Function**                                                                                                                             |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **View visitors on site count**  | The number of visitors signed in and not signed out, shown first.                                                                        |
| **View visitors on site**        | Name, arrival time, purpose, phone number.                                                                                               |
| **View finished visits**         | Today's visits with arrival and departure times.                                                                                         |
| **Sign out visitor**             | Staff sign out a visitor who forgot; the departure time is recorded.                                                                     |
| **Sign in visitor by hand**      | For a visitor whose phone cannot open the page: phone number, name, purpose, temperature. Recorded as signed in by staff. Works offline. |
| **Close visits at closing time** | Automatically at the centre's closing time, or by Close the day; open visits are marked Did not scan out.                                |

### 5.2 Visitor self sign-in

*Prototype:* [<u>https://bba-attendance-visitor.lovable.app/visit</u>](https://bba-attendance-visitor.lovable.app/visit)

| **Feature**                      | **Function**                                                                                                                                                           |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Open by QR code**              | The QR code at the entrance opens the visitor page for that centre in the phone's browser. No app, no account.                                                         |
| **Show data notice**             | States that the phone number is used for the visitor record and contact tracing and is kept for the retention period (default: 90 days), before the number is entered. |
| **Enter phone number**           | Normalised to the centre's country code before matching, so "9123 4567" and "+65 9123 4567" are the same visitor.                                                      |
| **Find open visit**              | An open visit for the number leads to sign out; no open visit leads to sign in.                                                                                        |
| **Sign in**                      | Full name, purpose of visit, temperature; the sign-in time is recorded.                                                                                                |
| **Pre-fill from this phone**     | Name and purpose are pre-filled only if this phone filled in the form before. A number alone never reveals another person's details.                                   |
| **Show sign-in confirmation**    | "You checked in at 09:14. Scan this code again when you leave."                                                                                                        |
| **Confirm identity at sign out** | Shows the name and arrival time found for the number with "Is this you?" before closing the visit.                                                                     |
| **Sign out**                     | The sign-out time is recorded.                                                                                                                                         |
| **Sign in again**                | A visitor who signed out can sign in again the same day; each visit is its own record.                                                                                 |

# 5. Business rules

## Attendance

| **ID**         | **Rule**                                                                                                                                                                                                               |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ATT-001** | In Singapore and Malaysia, attendance is taken once per child per day: one check in and one check out, at the gate on the Attendance app or on Child attendance on the SMS web. Both write the same attendance record. |
| **BR-ATT-002** | There is no second attendance mark in the classroom. The Teacher App does not take attendance.                                                                                                                         |
| **BR-ATT-003** | A child checked in on the SMS web shows as checked in on the iPad after sync, and the other way round.                                                                                                                 |
| **BR-ATT-004** | Check in records the adult who brought the child. The staff member who pressed the button is never recorded or shown.                                                                                                  |
| **BR-ATT-005** | Check out is allowed only to a person on the child's approved Authorised pickup list. A new person must be added by the parent in the Parents App and approved by the centre first.                                    |
| **BR-ATT-006** | Every check in and check out has a photo and a time. The time defaults to now.                                                                                                                                         |
| **BR-ATT-007** | A child cannot be checked out before being checked in.                                                                                                                                                                 |
| **BR-ATT-008** | Bus children can be checked in as a group; each child is checked out individually with a photo.                                                                                                                        |
| **BR-ATT-009** | Late arrival is flagged automatically after the centre's late cut-off (default 9:15 am). The late flag is visible to staff only and never shown to parents.                                                            |
| **BR-ATT-010** | Children on temporary withdrawal or suspension are not shown in the Attendance app.                                                                                                                                    |
| **BR-ATT-011** | Approved leave days show On leave on the child's card.                                                                                                                                                                 |

## Temperature

| **ID**         | **Rule**                                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ATT-012** | A temperature is required at check in and at staff clock in.                                                                                                                  |
| **BR-ATT-013** | A child can have any number of temperature readings in a day; each has a time, a value and a label.                                                                           |
| **BR-ATT-014** | The picker defaults to 36.5°C with a range of 36°C to 40°C; staff can enter a value manually. A paired Bluetooth thermometer fills in the value.                              |
| **BR-ATT-015** | A reading at or above the fever threshold is shown in red and notified to the class teacher and the Centre Director. The threshold is a setting per country (default 37.5°C). |
| **BR-ATT-016** | Red is used only for things that need a person: a raised temperature, a sync error, a visit that did not scan out. Not here yet is a normal state and is never red.           |

## Corrections and voids

| **ID**         | **Rule**                                                                                                                                                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ATT-017** | A record that is Not synced can be corrected on the iPad. Every correction is kept with the old value, the new value and the time.                                           |
| **BR-ATT-018** | A synced record cannot be changed or deleted on the iPad.                                                                                                                    |
| **BR-ATT-019** | Any staff member can request a void of a synced record from the iPad, with their name and a reason.                                                                          |
| **BR-ATT-020** | Void requests are approved or rejected on the SMS web by a Centre Admin, the Centre Director or a Senior Teacher assigned by the Centre Director.                            |
| **BR-ATT-021** | These three roles can void directly without approval on the SMS web, still with a reason. Direct voids are not possible on the iPad because it uses a shared centre account. |
| **BR-ATT-022** | A voided record no longer counts as attendance and stays in history with who requested, who approved, when and why.                                                          |

## Device and access

| **ID**         | **Rule**                                                                                               |
|----------------|--------------------------------------------------------------------------------------------------------|
| **BR-ATT-023** | The iPad signs in with the centre's account. There is no personal login for gate staff.                |
| **BR-ATT-024** | The centre account sees only its own centre. Level and class are a device choice and survive restarts. |
| **BR-ATT-025** | The scope is always visible in the header.                                                             |
| **BR-ATT-026** | After the idle time (default 2 minutes) the screen shows a cover with no child names or photos.        |
| **BR-ATT-027** | Visitors never use the iPad; child names and photos are never shown on any visitor screen.             |
| **BR-ATT-028** | The Attendance app has no reports, charts or statistics; these are on the SMS web.                     |
| **BR-ATT-029** | The device cannot be signed out while records are Not synced.                                          |

## Offline and sync

| **ID**         | **Rule**                                                                                                                                                                       |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ATT-030** | Every record is saved on the iPad before it is sent. Check in, check out, temperatures, staff clock records, void requests and by-hand visitor sign-ins work without internet. |
| **BR-ATT-031** | Each record has one of three states: Synced, Not synced, Sync error.                                                                                                           |
| **BR-ATT-032** | Records sync automatically when the connection returns; staff can also sync by hand.                                                                                           |
| **BR-ATT-033** | A sync error states its reason in plain words and can be retried for that record alone.                                                                                        |
| **BR-ATT-034** | If the same child is checked in on the iPad and on the SMS web for the same day, the earlier check in is kept and the later one is shown as a sync error for review.           |
| **BR-ATT-035** | The visitor self sign-in page needs an internet connection on the visitor's phone.                                                                                             |

## Staff attendance

| **ID**         | **Rule**                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------|
| **BR-ATT-036** | Staff clock in and clock out only on the centre iPad or on the SMS web, not on personal devices. |
| **BR-ATT-037** | A staff member identifies themselves by name and a personal PIN.                                 |
| **BR-ATT-038** | A temperature is recorded at clock in; the same fever threshold applies.                         |

## Visitors

| **ID**         | **Rule**                                                                                                                                                                                        |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ATT-039** | Visitors sign in and out on their own phone by scanning the centre's QR code. No app installation and no account.                                                                               |
| **BR-ATT-040** | A visitor provides full name, purpose of visit, phone number and temperature.                                                                                                                   |
| **BR-ATT-041** | Phone numbers are normalised to the centre's country code before they are stored or matched.                                                                                                    |
| **BR-ATT-042** | Sign in or sign out is decided by whether the number has an open visit, not by whether the visitor came earlier that day.                                                                       |
| **BR-ATT-043** | Sign out shows the visit found and asks "Is this you?" before closing it.                                                                                                                       |
| **BR-ATT-044** | Pre-filling uses only what the same phone entered before. A phone number alone never reveals another visitor's name or purpose.                                                                 |
| **BR-ATT-045** | The visitor page states what the phone number is used for and how long it is kept. The retention period is a setting (default 90 days); after it, phone numbers are removed from visit records. |
| **BR-ATT-046** | The iPad shows the number of visitors on site at all times on the Visitors screen. It equals the number of open visits.                                                                         |
| **BR-ATT-047** | Open visits are closed at the centre's closing time and marked Did not scan out, never shown as a normal departure.                                                                             |
| **BR-ATT-048** | A visit is never deleted.                                                                                                                                                                       |

## Parent notifications

| **ID**         | **Rule**                                                                                                                             |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **BR-ATT-049** | Parents receive an in-app notification on every check in and check out of their child.                                               |
| **BR-ATT-050** | Notifications for records taken offline are sent when the record reaches the SMS, with the actual time of the check in or check out. |
| **BR-ATT-051** | Notifications never mention the late flag or the staff member at the gate.                                                           |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**              | **Recipient**                                           | **Channel**          | **When**                                                                               |
|-------------------------------|---------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------|
| **Child checked in**          | Parent                                                  | In-app (Parents App) | When a check in reaches the SMS                                                        |
| **Child checked out**         | Parent                                                  | In-app (Parents App) | When a check out reaches the SMS, with the name of the person collecting               |
| **Fever reading**             | Class teacher, Centre Director                          | In-app (web and app) | When a child's reading is at or above the fever threshold                              |
| **Staff fever reading**       | Centre Director                                         | In-app (web and app) | When a staff reading at clock in is at or above the fever threshold                    |
| **Void request**              | Centre Admin, Centre Director, assigned Senior Teachers | In-app (web and app) | When a void is requested from the iPad                                                 |
| **Sync errors waiting**       | Centre Admin                                            | In-app (web)         | When records on a centre iPad have stayed in Sync error for more than 1 hour (default) |
| **Visitors did not scan out** | Centre Admin                                            | In-app (web)         | At closing time, when open visits were closed automatically                            |

## 6.2 Documents

- Visitor QR code poster per centre, printable for the entrance.

- Visitor data notice text shown on the visitor page.

# 7. Reports & exports

| **Report**                        | **Content**                                                                                                                                     | **Used by**                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| **Daily student attendance list** | Check-in and check-out times, adults and status per child, from the Attendance app and the SMS web; produced in Child attendance on the SMS web | Centre Admin, Centre Director |
| **Temperature list**              | All child readings with time, value and label; produced on the SMS web                                                                          | Centre Admin, Centre Director |
| **Staff attendance**              | Clock-in and clock-out times and temperatures; produced on the SMS web                                                                          | Centre Director, HQ Admin     |
| **Visitor log**                   | Visits with times, purpose, phone number and temperature, including Did not scan out; produced on the SMS web                                   | Centre Admin, Centre Director |
| **Void log**                      | Void requests from the iPad and the SMS web with requester, approver and reason                                                                 | Centre Director, HQ Admin     |

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
<td><strong>AC-ATT-001</strong></td>
<td>Check in</td>
<td>Given Mia is not yet checked in at 8:10 am,<br />
when a staff member checks her in with her father as the adult, a photo and 36.5°C,<br />
then Mia shows Signed in at 8:10 am with her father recorded, and her parent receives an in-app notification.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-002</strong></td>
<td>No staff name recorded</td>
<td>Given Ms Lim checks Mia in on the centre iPad,<br />
when anyone opens Mia's check in on the iPad or the SMS web,<br />
then the record shows her father as the adult and does not show Ms Lim.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-003</strong></td>
<td>Second check in blocked</td>
<td>Given Mia was checked in at 8:10 am,<br />
when a staff member opens Mia again,<br />
then the screen shows "Already checked in at 08:10" and offers no second check in.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-004</strong></td>
<td>Authorised pickup only</td>
<td>Given Mia's approved Authorised pickup list has her mother and grandmother,<br />
when a staff member opens Check out,<br />
then only these two people can be selected as the person collecting.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-005</strong></td>
<td>Check out before check in</td>
<td>Given Noah was not checked in today,<br />
when a staff member tries to check him out,<br />
then the app explains he is not checked in and offers Check in first.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-006</strong></td>
<td>Bulk check in by bus</td>
<td>Given bus service Bus A has 8 children and Ethan did not take the bus today,<br />
when the staff member filters by Bus A, unticks Ethan and confirms,<br />
then 7 children are checked in and Ethan stays Not here yet.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-007</strong></td>
<td>Bluetooth thermometer</td>
<td>Given a Bluetooth thermometer is paired with the iPad,<br />
when a staff member takes Mia's temperature during check in,<br />
then the reading fills in automatically and can still be changed by hand.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-008</strong></td>
<td>Unlimited readings with fever</td>
<td>Given Mia has readings of 36.6°C On arrival and 36.8°C Mid-morning,<br />
when a third reading of 37.8°C is added with the label Before nap,<br />
then all three readings are shown in time order and the third is red and notified to the class teacher and the Centre Director.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-009</strong></td>
<td>Late flag hidden from parents</td>
<td>Given centre A's late cut-off is 9:15 am,<br />
when Noah is checked in at 9:20 am,<br />
then Noah's card shows the late marker and his parent's notification does not mention late.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-010</strong></td>
<td>Offline check in</td>
<td>Given the iPad has no internet connection,<br />
when staff check in 5 children,<br />
then the 5 records show Not synced, sync when the connection returns, and the parents are notified then with the actual check-in times.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-011</strong></td>
<td>Correct before sync</td>
<td>Given a check-in temperature was entered as 3.6 and is Not synced,<br />
when a staff member uses Fix a mistake and changes it to 36.6,<br />
then the record shows 36.6 with the correction listed.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-012</strong></td>
<td>Synced record locked</td>
<td>Given Liam's check in is Synced,<br />
when a staff member opens it on the iPad,<br />
then there is no edit or delete action, only Request void.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-013</strong></td>
<td>Void request from the iPad</td>
<td>Given Liam was checked in by mistake and the record is Synced,<br />
when Ms Lim requests a void with her name and the reason "Wrong child",<br />
then the request reaches the Centre Admin, the Centre Director and the assigned Senior Teachers on the SMS web, and Liam stays checked in until it is approved.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-014</strong></td>
<td>Temporarily withdrawn child hidden</td>
<td>Given Zoe is on temporary withdrawal,<br />
when a staff member searches for Zoe on the iPad,<br />
then Zoe is not found.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-015</strong></td>
<td>Same record on web and iPad</td>
<td>Given Mia was checked in on the SMS web at 8:05 am,<br />
when the iPad syncs,<br />
then Mia shows Signed in at 8:05 am on the iPad.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-016</strong></td>
<td>Staff clock in</td>
<td>Given Ms Tan arrives at 7:20 am,<br />
when she selects her name, enters her PIN and records 36.7°C,<br />
then she is clocked in at 7:20 am and appears in staff on site.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-017</strong></td>
<td>Visitor sign-in</td>
<td>Given a visitor scans centre A's QR code on his own phone and has no open visit,<br />
when he enters his phone number, name, purpose and 36.6°C,<br />
then he is signed in and the iPad shows 1 visitor on site.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-018</strong></td>
<td>Visitor sign out confirmation</td>
<td>Given the visitor with number 9123 4567 has an open visit from 9:14 am,<br />
when he scans again and types "+65 9123 4567",<br />
then the page shows his name and arrival time with "Is this you?" and signs him out after he confirms.</td>
</tr>
<tr class="odd">
<td><strong>AC-ATT-019</strong></td>
<td>No details revealed by number</td>
<td>Given a phone that has never used the visitor page,<br />
when someone enters the number of a visitor who signed in last week and has no open visit,<br />
then the sign-in form is empty and shows no name or purpose.</td>
</tr>
<tr class="even">
<td><strong>AC-ATT-020</strong></td>
<td>Did not scan out</td>
<td>Given centre A closes at 7:00 pm and a visitor is still signed in,<br />
when closing time passes,<br />
then the visit is closed, marked Did not scan out, and the visitors on site count shows 0.</td>
</tr>
</tbody>
</table>
