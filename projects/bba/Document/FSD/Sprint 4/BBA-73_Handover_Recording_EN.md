# Handover Recording

| Item | Value |
|---|---|
| Project | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Feature | BBA-73 Handover recording |
| Document code | FRD-3.2.1.01_Handover_Recording |
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

This document describes how drop-off and pick-up information is managed in the SMS: viewing arrival time, departure time, the adult who dropped off, the adult who picked up, their relationship to the child, the child's temperature at drop-off and pick-up, and the handover photos; searching and filtering; seeing which children are still at the centre; exporting data; and letting authorised users add missing drop-off / pick-up information in the SMS, with a reason and approval.

Drop-off and pick-up information is recorded in the App when staff receive and hand over the child, and is then sent to the SMS. The App flows and screens are covered in the App specification.

## 3. Scope and phase boundaries

| In scope | Out of scope |
|---|---|
| View, search and filter drop-off / pick-up information in the SMS; view temperature at drop-off / pick-up and handover photos; see which children are still at the centre; export data; authorised users add missing drop-off / pick-up information, with a reason and approval; keep a change history. | Editing or deleting existing drop-off / pick-up information. App flows and screens for receiving and handing over children; App photo capture and data sync; creating, adding and approving authorised collectors (Children & Families, Parents App); recording and correcting Present / Absent attendance results (BBA-77); temperature-taking rules (BBA-74); late arrival (BBA-75); approval route set-up (BBA-53); notifications to parents. |

## 4. Actors, roles and access

| Actor | Scope | Rights / Responsibilities |
|---|---|---|
| Centre Director (CD) | Children in the centres assigned to them. | View data and photos; add missing drop-off / pick-up information. |
| Authorised SMS user | Data within their assigned scope. | View data, open photos, search, filter, export data; add drop-off / pick-up information as permitted. |
| Approver | Requests to add information at the step assigned to them in the approval route. | Approve or reject requests in My approvals. |
| System | Drop-off / pick-up information and related child records. | Provide data for display and export; work out which children are still at the centre; check permissions; send requests for approval; record history. |

## 5. Feature overview and functional breakdown

BBA-73 has two user stories in the SMS, described in section 6.

| Module | Feature | Description | User Story |
|---|---|---|---|
| **Attendance** | View and export drop-off / pick-up information | View drop-off / pick-up information, temperatures, handover photos and children still at the centre; search, filter, export data. | BBA-73: US-001 |
| **Attendance** | Add drop-off / pick-up information | Authorised users add missing drop-off / pick-up information in the SMS, with a reason; the information is recorded after approval. | BBA-73: US-002 |

## 6. Functional requirements by user story

### 6.1 BBA-73: US-001 - View and export drop-off / pick-up information

#### User Story

As an authorised SMS user, I want to view drop-off / pick-up information and handover photos, search, filter and export the data, so that I can see who dropped off and picked up each child, at what time, and which children are still at the centre.

#### Functional Requirements

| FR ID | Functional requirement |
|---|---|
| FR-001 | The system shows children's drop-off / pick-up information within the user's data scope. |
| FR-002 | The system lets users search by child name or child ID and filter by centre, class, date and attendance result. |
| FR-003 | The system lets authorised users export drop-off / pick-up data for a selected date range, with the columns in Appendix B. |
| FR-004 | The system shows the handover photos taken at drop-off and pick-up, and lets authorised users open each photo. |

#### Functional Flow - Main

1. The user opens Daily Operations › Attendance.
2. The system shows drop-off / pick-up information and handover photos within the user's scope.
3. The user searches by child name / ID or selects a centre, class and date; the user selects a photo to open it.
4. The user selects a date range and exports the data using the standard export function.

#### Functional Flow - Alternative

1. No matching data: the system shows an empty result, following the standard design.
2. A child has no arrival time, departure time, temperature or photo yet: the empty cell shows "—".

#### Functional Flow - Exception

1. The user has no permission or asks for data outside their scope: the system does not provide that data.
2. The data cannot be loaded or exported: the system shows an error, following standard system behaviour.

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-001 | Viewing data, opening photos and exporting data follow the user's permissions and centre data scope. |
| BR-002 | A child is treated as still at the centre when they have an arrival time and no departure time. |
| BR-003 | The list shows: date, child name, class, centre, arrival time, drop-off adult, relationship, temperature at drop-off, departure time, pick-up adult, relationship, temperature at pick-up, drop-off photo, pick-up photo, and reason (for information added in the SMS). Empty cells show "—"; available photos can be opened. |
| BR-004 | The drop-off adult is a family member of the child: the user selects them from the child's family list. If the adult is not on the list, the user selects "Someone else" and enters their full name and relationship to the child (required). |
| BR-005 | The pick-up adult can only be selected from the child's authorised collector list; there is no option for a stranger or a one-off collector. |
| BR-006 | Arrival / departure time is the date and time staff saved the record in the App (or the time the user added in the SMS). It is shown in the user's time zone and is not tied to a session or fixed time of day. |
| BR-007 | Exports use the columns in Appendix B, for the selected date range and the user's data scope, following the standard export function. |
| BR-008 | A child on temporary withdrawal does not appear on the days within the withdrawal period. |

#### Validation Rules

| VAL ID | Condition | System response |
|---|---|---|
| VAL-001 | The user asks to view or export data outside their scope. | Data outside the scope is not provided. |
| VAL-002 | The export start date is after the end date. | Shows that the date range is not valid and does not export. |

#### UI Reference

| Screen / Version | Reference / Link |
|---|---|
| BBA-73: UI-US-001 - Drop-off / pick-up information in the SMS | |

#### UI Components / Field Specification

| Field / Control | Type | Default / State | Check | Behaviour |
|---|---|---|---|---|
| Search | Text box | Empty | BR-001 | Search by child name or child ID. |
| Centre | Dropdown | The user's centre | VAL-001 | Filter by assigned centre. |
| Class | Dropdown | All | — | Filter by class. |
| Date | Date picker | Today | BR-006 | Filter by date, in the user's time zone. |
| Child name, class, centre | Display | From the child record | BR-003 | Identify the child. |
| Arrival time / Departure time | Display | "—" when missing | BR-006 | Recorded date and time, in the user's time zone. |
| Drop-off adult / Pick-up adult | Display | "—" when missing | BR-004; BR-005 | Name of the drop-off / pick-up adult. |
| Relationship | Display | "—" when missing | BR-004 | Relationship to the child; Someone else. |
| Temperature at drop-off / Temperature at pick-up | Display | "—" when missing | BR-003 | Temperature taken when the child arrives / leaves (°C), as per BBA-74. |
| Drop-off photo / Pick-up photo | Photo / open | Saved photo | BR-001; FR-004 | Select to open the photo of the child with the drop-off / pick-up adult. |
| Reason | Display | "—" for data from the App | BR-003 | Reason the user entered when adding information in the SMS (US-002). |
| Still at the centre | Display | From SMS data | BR-002 | Shows that the child is still at the centre. |
| From date / To date | Date picker | From date = To date = today | VAL-002 | Export date range. |
| Export data | Action | Based on export conditions | BR-001; BR-007; VAL-002 | Export as per Appendix B and the standard rules. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-001 | Use the child record, centre, class, arrival / departure date and time, drop-off / pick-up adult, relationship, temperature at drop-off / pick-up, handover photos, reason and record source (App / SMS) for display and export. |
| DATA-002 | Viewing the list or opening a photo does not create a drop-off / pick-up record. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | The user has access to Attendance | the user opens the screen | the user's centre and today's date are selected by default; drop-off / pick-up information and photos within the user's scope are shown | FR-001; BR-001; BR-003; DATA-002 |
| AC-002 | There is data for several centres | the user searches by name and selects a centre, class and date | only matching data within the user's scope is shown | FR-002; BR-001; VAL-001 |
| AC-003 | Ethan arrived at 08:12 and has no departure time | the system loads the data | Ethan is shown as still at the centre | BR-002 |
| AC-004 | Ethan has no departure time, pick-up temperature or pick-up photo | the system shows the list | the empty cells show "—" | BR-003; DATA-001 |
| AC-005 | Noah was dropped off by his helper Siti (not on the family list) | the system shows the list | Noah: drop-off adult Siti, relationship "Helper (Someone else)" | BR-004 |
| AC-006 | Ethan has a drop-off photo and a pick-up photo; the user may view them | the user selects each photo | the correct photo opens | FR-004; BR-001 |
| AC-007 | The user may export and keeps the default From date / To date | the user exports the data | From date and To date are today; the file has the columns in Appendix B and data within the user's scope | FR-003; BR-007 |
| AC-008 | The export start date is after the end date | the user exports | the system shows that From date / To date is not valid and does not export | VAL-002 |
| AC-009 | Noah was dropped off at 13:30 | the system shows the list | arrival time 13:30 | BR-006 |
| AC-010 | Millie is on temporary withdrawal from 24/11 to 01/12/2026 | the user selects 25/11/2026 | there is no row for Millie | BR-008 |
| AC-011 | Ethan's temperature was 36.6 °C at drop-off and 36.8 °C at pick-up | the system shows the list | temperature at drop-off 36.6 °C, temperature at pick-up 36.8 °C | BR-003 |

#### Dependencies

App (receiving / handing over children, drop-off / pick-up adults, photos); authorised collector list (Children & Families); Temporary withdrawal (Joining & leaving); temperature readings (BBA-74).

### 6.2 BBA-73: US-002 - Add drop-off / pick-up information in the SMS

#### User Story

As an authorised Centre Director, I want to add missing drop-off / pick-up information in the SMS, with a reason, so that I can fill in information the App did not record.

#### Functional Requirements

| FR ID | Functional requirement |
|---|---|
| FR-005 | The system lets authorised users add missing drop-off / pick-up information in the SMS, with a reason: arrival time, drop-off adult, temperature at drop-off, departure time, pick-up adult, temperature at pick-up, handover photos (BR-004, BR-005, BR-009, BR-010, BR-011). |
| FR-006 | Every addition must be approved; the information is recorded and shown after approval (BR-012, BR-013). |

#### Functional Flow - Main

1. The user opens Attendance and selects the child, centre and date to add information for, within their scope.
2. The system shows the existing information as read-only. The user enters the missing information and a reason (FR-005).
3. The user selects Save. The system checks permissions and data (VAL-003 to VAL-007), then sends the request for approval (FR-006).
4. The approver selects Approve in My approvals; the system records the information, shows it in US-001 and records the history (BR-012, BR-013).

#### Functional Flow - Alternative

1. The drop-off adult is not on the child's family list: the user selects Someone else and enters their full name and relationship to the child (BR-004).
2. The approver selects Reject: the information is not recorded (BR-012).
3. The user closes the screen or selects Cancel before saving: the system does not send the request.

#### Functional Flow - Exception

1. The user has no permission or the record is outside their scope: the system refuses (VAL-003).
2. The request cannot be saved: the system shows an error, following standard behaviour, and does not send the request.

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-009 | In the SMS, drop-off / pick-up information can only be added. |
| BR-010 | After the addition, the child's attendance information must have an arrival time, a departure time, a drop-off adult and a pick-up adult. |
| BR-011 | Every addition requires a reason. Reasons follow the list set in BBA-77. |
| BR-012 | Every addition must be approved through the approval route (BBA-53), in My approvals (BBA-52). The information is recorded only when approved; if rejected, it is not recorded. |
| BR-013 | Each addition is recorded in the history: added values, reason, added by, approver, approval result, time. |

#### Validation Rules

| VAL ID | Condition | System response |
|---|---|---|
| VAL-003 | The user has no permission to add, or the record is outside their scope. | Refuses; does not send the request. |
| VAL-004 | After the addition, the arrival time, departure time, drop-off adult or pick-up adult is still missing. | Shows an error at the field and does not send the request. |
| VAL-005 | No reason is entered. | Shows an error at the Reason field and does not send the request. |
| VAL-006 | Someone else is missing a full name or relationship. | Shows "Enter the name and relationship of the adult." and does not send the request. |
| VAL-007 | The pick-up adult is not on the authorised collector list. | Shows "Only a person authorised to collect this child may be named here." and does not send the request. |

#### UI Reference

| Screen / Version | Reference / Link |
|---|---|
| BBA-73: UI-US-002 - Add drop-off / pick-up information in the SMS | |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Check | Behaviour |
|---|---|---|---|---|---|
| Child / Centre / Date | Display / select | Yes | From the selected record | VAL-003 | Identify the record to add to. |
| Existing information | Display | — | Read-only | BR-009 | Cannot be edited or deleted. |
| Arrival time | Date and time | When missing | Empty when missing | VAL-004 | Entered in the user's time zone (BR-006). |
| Drop-off adult | Dropdown | When missing | Empty when missing | VAL-004; VAL-006 | Person on the family list, or Someone else (BR-004). |
| Full name, Relationship (Someone else) | Text box | When Someone else is selected | Empty | VAL-006 | Details of a drop-off adult not on the list. |
| Temperature at drop-off | Number (°C) | No | Empty when missing | — | As per BBA-74. |
| Departure time | Date and time | When missing | Empty when missing | VAL-004 | Entered in the user's time zone. |
| Pick-up adult | Dropdown | When missing | Empty when missing | VAL-004; VAL-007 | Authorised collector (BR-005). |
| Temperature at pick-up | Number (°C) | No | Empty when missing | — | As per BBA-74. |
| Drop-off photo / Pick-up photo | Photo | No | Empty when missing | BR-001 | Upload the matching photo. |
| Reason | Dropdown / text box | Yes | Empty | VAL-005 | Reason for adding the information, as per BBA-77 (BR-011). |
| Save | Action | As permitted | — | VAL-003 to VAL-007 | Sends the request for approval (BR-012). |
| Cancel | Action | — | While the screen is open | Standard behaviour | Closes the screen without sending the request. |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-003 | Save the request to add information, with the reason and approval result; approved information is saved to the drop-off / pick-up data, including temperatures and handover photos. History is recorded as per BR-013. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-012 | The App has no drop-off / pick-up information for Ethan on 25/11/2026 | the user enters arrival 08:12, drop-off adult Serena Lim, departure 17:22, pick-up adult Daniel Lim and a reason, then selects Save | the request is sent for approval | FR-005; FR-006; BR-010; BR-011; BR-012 |
| AC-013 | Ethan's request is waiting for approval | the approver selects Approve | the list shows the new information and the reason; the history shows the added values, reason, added by, approver and time | FR-006; BR-012; BR-013; DATA-003 |
| AC-014 | Ethan's request is waiting for approval | the approver selects Reject | the information is not recorded; the history shows the Reject result | BR-012; BR-013 |
| AC-015 | The App has recorded Mia's arrival time and drop-off adult | the user opens the add screen | the arrival time and drop-off adult are read-only and cannot be edited | BR-009 |
| AC-016 | The user has no permission to add | the user selects Save | the system refuses | VAL-003 |
| AC-017 | The user enters a departure time but no pick-up adult | the user selects Save | an error shows at the field and the request is not sent | BR-010; VAL-004 |
| AC-018 | The App recorded Mia's arrival at 08:00, dropped off by her mother; there is no pick-up information | the user enters only departure 17:00, pick-up adult her father and a reason, then selects Save | the request is sent for approval; the drop-off part stays unchanged | BR-009; BR-010 |
| AC-019 | The user enters all information but leaves the reason empty | the user selects Save | an error shows at the Reason field and the request is not sent | BR-011; VAL-005 |
| AC-020 | The user selects Someone else and leaves the relationship empty | the user selects Save | the system shows "Enter the name and relationship of the adult." and does not send the request | BR-004; VAL-006 |
| AC-021 | Ethan's authorised collector list has Serena Lim and Daniel Lim | the user opens the Pick-up adult list | only Serena Lim and Daniel Lim are shown | BR-005; VAL-007 |
| AC-022 | The user is entering information | the user selects Cancel before saving | the screen closes and the request is not sent | FR-005 |

#### Dependencies

US-001; authorised collector list (Children & Families); reasons (BBA-77); approval route (BBA-53); My approvals (BBA-52); temperature readings (BBA-74).

## 7. Appendix

### Appendix A. Glossary

| Term | Meaning in this FRD |
|---|---|
| Drop-off | The child is brought to the centre, with an arrival time and a drop-off adult. |
| Pick-up | The child is collected from the centre, with a departure time and a pick-up adult. |
| Authorised collector | A person on the child's authorised collector list (already held on the child record). |
| Someone else | A drop-off adult who is not on the child's family list; the user enters their full name and relationship to the child. |
| Still at the centre | The child has an arrival time and no departure time. |
| Record source | The App, or the SMS account that added the data. |

### Appendix B. Drop-off / pick-up export columns

The export file has the following columns, for the selected date range and the user's centre scope. The export action, file format and data protection follow the standard export function.

| No. | Column | Meaning / Data |
|---|---|---|
| 1 | Date | Date of the record. |
| 2 | Child ID | Child ID. |
| 3 | Child | Child's full name. |
| 4 | Class | Child's class. |
| 5 | Centre | Child's centre. |
| 6 | Arrival | Arrival time. |
| 7 | Departure | Departure time. |
| 8 | In building | Yes when the child is still at the centre (BR-002); otherwise No. |
