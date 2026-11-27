# Temperature Readings

| Item | Value |
|---|---|
| Project | Busy Bees Asia SMS |
| Module | Daily Operations — Temperature |
| Feature | BBA-74 Temperature readings (≥3/day) |
| Document code | FRD-3.2.1.02_Temperature_Readings |
| Sprint | 4 |
| Version | 0.1 |
| Status | DRAFT FOR CONFIRMATION |
| Date | 10/11/2026 |
| Prepared by | Business Analysis |
| Reviewed by | HaiNguyen |
| Approved by | HaiNguyen |

## 1. Document control

| Version | Date | Author | Summary of changes | Approved |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Initial version | HaiNguyen |

**Readiness:** The user stories, functional requirements, rules, checks, data and acceptance criteria are specified.

## 2. Purpose and background

This document describes how all of a child's temperature readings are managed in the SMS, on the Temperature tab: searching, filtering, adding, editing, deleting and viewing the history. Each child has their temperature taken at least 3 times a day (on arrival, after nap, before pick-up), plus extra readings when something seems unusual.

Readings are recorded in the App (entered by hand or from a thermometer) and then sent to the SMS. The App flows and screens are covered in the App specification.

## 3. Scope and phase boundaries

| In scope | Out of scope |
|---|---|
| The Temperature tab holds every reading for each child; filter by brand, centre, class and date; search by child name; add a reading from an attendance row or from the Temperature tab; edit, delete and view history as permitted; the number of required readings each day. | App flows and screens for taking temperatures; thermometer connection and App data sync; parents viewing readings (Parents App); °F unit; the child's health record (Health); drop-off / pick-up information (BBA-73). |

## 4. Actors, roles and access

| Actor | Scope | Rights / Responsibilities |
|---|---|---|
| Authorised SMS user | Data within their assigned scope. | View, search, filter, add, edit and delete readings, and view the history, as permitted. |
| System | Temperature readings and related child records. | Provide data for display; check permissions and data; count required readings; record history. |

## 5. Feature overview and functional breakdown

BBA-74 has two user stories in the SMS, described in section 6.

| Module | Feature | Description | User Story |
|---|---|---|---|
| **Temperature** | View temperature readings | The Temperature tab shows every reading; search, filter; number of required readings. | BBA-74: US-001 |
| **Temperature** | Add, edit and delete readings | Add from an attendance row or the Temperature tab; edit, delete and view the history. | BBA-74: US-002 |

## 6. Functional requirements by user story

### 6.1 BBA-74: US-001 - View temperature readings

#### User Story

As an authorised SMS user, I want to see every temperature reading for each child, and search and filter them, so that I can follow children's temperatures through the day.

#### Functional Requirements

| FR ID | Functional requirement |
|---|---|
| FR-001 | The system has a Temperature tab that shows every temperature reading for children within the user's scope, one row per reading. |
| FR-002 | The system lets users filter by brand, centre, class and date, and search by child name. |
| FR-003 | The system shows how many of the child's required readings for the day have been taken. |

#### Functional Flow - Main

1. The user opens Daily Operations › Temperature tab.
2. The user selects a brand, centre, class and date, or searches by child name. The system shows the readings that match all selected conditions.

#### Functional Flow - Alternative

1. A child has several readings in a day: each reading is one row, including readings in the same Round.

#### Functional Flow - Exception

1. No matching readings: the system shows an empty list, following the standard design.
2. The user has no permission or the data cannot be loaded: standard system behaviour applies.

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-001 | The Temperature tab holds every reading for each child in every Round. Each row is one reading; the list does not show only the latest reading. Viewing the list does not create a reading. |
| BR-002 | Each row shows: child name, class, brand, centre, Round, Temperature (°C, 1 decimal place), Time, Measurement method, and the reason for an extra reading (when Extra). Readings of 37.5 °C or higher are shown in red. |
| BR-003 | Rounds are: On arrival, Before nap, After nap, Before pickup, Extra. The required Rounds each day are On arrival, After nap and Before pickup; "x of 3" counts how many required Rounds have a reading that day. |
| BR-004 | Brand, centre, class, date and name search apply together. The date filter uses the time the reading was taken. A child on temporary withdrawal does not appear on the days within the withdrawal period. |

#### Validation Rules

| VAL ID | Condition | System response |
|---|---|---|
| VAL-001 | The user asks to view data outside their scope. | Data outside the scope is not provided. |

#### UI Reference

| Screen / Version | Reference / Link |
|---|---|
| BBA-74: UI-US-001 - Temperature tab in the SMS | |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Check | Behaviour |
|---|---|---|---|---|---|
| Temperature | Tab | Yes | In Daily Operations | FR-001; BR-001 | Shows every reading within the user's scope. |
| Brand / Centre / Class | Dropdown filters | No | Within the user's scope | BR-004; VAL-001 | Applied together. |
| Date | Date filter | No | Today | BR-004 | Filter by the date of the reading. |
| Search | Text box | No | Empty | FR-002 | Search by child name. |
| Temperature readings | List | When available | One row per reading | BR-001; BR-002 | Columns as per BR-002; Edit, Delete, View audit actions (US-002). |
| x of 3 | Display | — | By child and date | FR-003; BR-003 | Number of required Rounds with a reading. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-001 | Save each reading as a separate record: child, Round, Temperature, Time, Measurement method, reason for an extra reading (when Extra), record source (App / SMS), and brand / centre / class for filtering within the user's scope. Readings on the same day or in the same Round are not merged into one latest result. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | There are readings for children in several brands, centres and dates | the user filters by brand, centre and date and searches by name | only readings that match all conditions within the user's scope are shown | FR-002; BR-004; VAL-001 |
| AC-002 | Ethan has 4 readings on 24/11/2026, 2 of them in the Extra Round | the user views the list | all 4 rows are shown, not only the latest | FR-001; BR-001; DATA-001 |
| AC-003 | Noah has a reading of 37.9 °C | the user views the list | 37.9 is shown in red | BR-002 |
| AC-004 | Ethan has On arrival and After nap readings on 24/11/2026 | the user views Ethan's readings for that day | "2 of 3" is shown | FR-003; BR-003 |
| AC-005 | Millie is on temporary withdrawal from 24/11 to 01/12/2026 | the user selects 25/11/2026 | there are no readings for Millie | BR-004 |

#### Dependencies

App (taking and recording readings); Temporary withdrawal (Joining & leaving).

### 6.2 BBA-74: US-002 - Add, edit and delete readings

#### User Story

As an authorised SMS user, I want to add, edit and delete temperature readings and view their history, so that I can keep children's temperature data accurate.

#### Functional Requirements

| FR ID | Functional requirement |
|---|---|
| FR-004 | The system lets users add a reading from an attendance row or from the Temperature tab. From an attendance row, the child is already selected; from the Temperature tab, the user selects the child. |
| FR-005 | The add form has Child, Round, Temperature, Time, Measurement method, and the reason for an extra reading when Round = Extra. Time defaults to the time of creation. |
| FR-006 | Authorised users can edit or delete a reading; no reason or approval is needed. |
| FR-007 | The system records the history of adding, editing and deleting readings, and lets users view it. Deleted readings still appear in the history. |

#### Functional Flow - Main

1. The user selects Add temperature, selects the child, and enters Round, Temperature, Time and Measurement method.
2. The user selects Save. The system checks the data, saves one record for the reading and records the history.
3. The user selects Edit or Delete on a reading. The system saves the change or deletes the reading, updates the list and records the history.
4. The user selects View audit to see the history of additions, edits and deletions.

#### Functional Flow - Alternative

1. Adding from an attendance row: the user selects Add temperature on the child's row; the form opens with the child already selected, and the other fields as per FR-005.
2. The user closes the form or selects Cancel before saving: changes are not saved.

#### Functional Flow - Exception

1. Required data is missing or not valid: an error shows at the field and nothing is saved (VAL-002 to VAL-006).
2. The user has no permission, or saving / deleting fails: standard behaviour applies; a failed action is not shown as completed.

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-005 | When adding from an attendance row, the child is already selected. When adding from the Temperature tab, the user selects a child within their scope. |
| BR-006 | Temperature accepts 36.0–40.0 °C, in steps of 0.1. Measurement method is Manual or Device. Time defaults to the time of creation and is shown in the user's time zone. |
| BR-007 | When Round = Extra, the reason for the extra reading is required, for example "Child felt warm". |
| BR-008 | A reading can only be added for a child who is present that day (has an arrival time); Time cannot be before the arrival time or after the current time. |
| BR-009 | Readings can be edited and deleted regardless of date, Round or Measurement method, without a reason or approval, as permitted by the user's role. Readings recorded in the App can also be edited. |
| BR-010 | The history records: action, reading / child, old / new value (where relevant), user, time. Deleting a reading does not delete its history. |

#### Validation Rules

| VAL ID | Condition | System response |
|---|---|---|
| VAL-002 | Child, Round or Measurement method is not selected; Temperature or Time is missing. | Shows the required field and does not save. |
| VAL-003 | Temperature is not a number, is outside 36.0–40.0 °C, or is not in steps of 0.1. | Shows "Check the temperature: it must be between 36.0 and 40.0 °C, in steps of 0.1." and does not save. |
| VAL-004 | Round = Extra and the reason for the extra reading is empty. | Shows "Enter why this extra reading was taken." and does not save. |
| VAL-005 | Time is before the arrival time or after the current time. | Shows "Check the time: it cannot be before arrival or after the current time." and does not save. |
| VAL-006 | The child is not present that day (no arrival time) or is on temporary withdrawal. | Shows that the child is not on the active list for that day and does not save. |

#### UI Reference

| Screen / Version | Reference / Link |
|---|---|
| BBA-74: UI-US-002 - Add / edit reading form in the SMS | |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Check | Behaviour |
|---|---|---|---|---|---|
| Add temperature | Action | As permitted | On an attendance row or the Temperature tab | FR-004; BR-005 | Opens the add form; the child is already selected when opened from an attendance row. |
| Child | Dropdown | Yes | Pre-selected from the attendance row; selected on the Temperature tab | VAL-002; VAL-006 | Identifies the child for the reading. |
| Round | Dropdown | Yes | As selected | VAL-002; BR-003 | On arrival / Before nap / After nap / Before pickup / Extra. |
| Temperature | Number box | Yes | Entered or measured value | VAL-002; VAL-003 | Records the temperature (°C). |
| Time | Date and time | Yes | Time of creation | VAL-002; VAL-005 | Records or changes the time of the reading. |
| Measurement method | Dropdown | Yes | From the data or as selected | VAL-002; BR-006 | Manual / Device. |
| Reason for extra reading | Text box | When Round = Extra | Hidden | VAL-004 | BR-007. |
| Save / Cancel | Action | — | In the add / edit form | VAL-002 to VAL-006 | Saves valid data and records the history; Cancel closes without saving. |
| Edit / Delete | Action | As permitted | On each reading | FR-006; BR-009 | Edit the fields or delete the reading; records the history. |
| View audit | Action | As permitted | On the Temperature tab and each reading | FR-007; BR-010 | View the history of additions, edits and deletions, including deleted readings. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-002 | Record the history of additions, edits and deletions as per BR-010; allow the history to be viewed on each reading and on the Temperature tab, including deleted readings. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-006 | The user is viewing Ethan's attendance row (present) | the user selects Add temperature | the form opens with Ethan already selected and Time defaulting to the time of creation | FR-004; FR-005; BR-005 |
| AC-007 | The user is on the Temperature tab | the user selects Add, selects a child and saves valid data | a reading is created with Round, Temperature, Time and Measurement method; the history is recorded | FR-004; FR-005; DATA-001; DATA-002 |
| AC-008 | There is a reading from a previous day; the user has permission | the user edits or deletes the reading | the action is allowed with no reason or approval; the history is recorded | FR-006; BR-009; DATA-002 |
| AC-009 | A reading has been added, edited and deleted | the user opens View audit | the history shows the action, old / new value (where relevant), user and time, including the deleted reading | FR-007; BR-010 |
| AC-010 | Round or Temperature is missing | the user selects Save | the required field is shown and nothing is saved | VAL-002 |
| AC-011 | The user enters a temperature of 41.0 | the user selects Save | the system shows "Check the temperature: it must be between 36.0 and 40.0 °C, in steps of 0.1." and does not save | BR-006; VAL-003 |
| AC-012 | Round = Extra and the reason for the extra reading is empty | the user selects Save | the system shows "Enter why this extra reading was taken." and does not save | BR-007; VAL-004 |
| AC-013 | Ethan arrived at 08:12 | the user enters Time 07:50 and saves | the system shows "Check the time: it cannot be before arrival or after the current time." and does not save | BR-008; VAL-005 |
| AC-014 | Ava was absent on 25/11/2026 | the user adds a reading for Ava on that day | the system shows that the child is not on the active list for that day and does not save | BR-008; VAL-006 |
| AC-015 | The user is adding or editing a reading | the user selects Cancel | the form closes and changes are not saved | FR-004; FR-006 |

#### Dependencies

US-001; the child's arrival time (BBA-73).

## 7. Appendix

### Appendix A. Glossary

| Term | Meaning in this FRD |
|---|---|
| Reading | One temperature check for a child; each reading is a separate record. |
| Round | When the reading is taken: On arrival, Before nap, After nap, Before pickup, Extra. |
| Required Round | On arrival, After nap, Before pickup; each child needs all 3 of these Rounds every day. |
| Measurement method | Manual or Device; not the same as the record source (App / SMS). |
| Record source | The App, or the SMS account that recorded the data. |
