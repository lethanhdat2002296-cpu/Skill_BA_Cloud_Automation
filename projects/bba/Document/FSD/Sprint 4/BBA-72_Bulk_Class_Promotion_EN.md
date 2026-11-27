# Bulk Class Promotion

| Item | Value |
|---|---|
| Project | Busy Bees Asia SMS |
| Module | Children & Families — Classes |
| Feature | BBA-72 Bulk Class Promotion |
| Document code | FRD-3.1.5.01_Bulk_Class_Promotion |
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

**Readiness:** The user story, functional requirements, rules, checks, data and acceptance criteria are specified.

## 2. Purpose and background

The academic year runs from January to December. In November–December, each centre sets up next year's classes (creates the classes and assigns teachers). At the end of the year, the user moves all children in a class up to a class at the next level (for example N2 to K1) that has already been set up, in one action instead of moving each child one by one. The old class and its list of children are kept.

## 3. Scope and phase boundaries

| In scope | Out of scope |
|---|---|
| Moving a whole class up within the same centre (annual promotion): choose an existing class for the new academic year and the effective date; select all children and untick children who stay; confirm; result; history. | The effect of the promotion on fees, invoices, message threads and attendance lists (handled by the related modules). Creating classes (Classes). Infant to Playgroup at 18 months (Infant promotion) and moving to another class at the same level (Class change). K2 graduation (Joining & leaving › Graduation). Moving to another centre (Transfer). |

## 4. Actors, roles and access

| Actor | Scope | Rights / Responsibilities |
|---|---|---|
| Authorised User | Classes and children in the centres assigned to them. | Move a whole class up. |
| System | Current class, new class, selected children. | Move the children to the new class from the effective date, show the result, keep the history. |
| Unauthorised User | Outside the role or data scope granted. | Cannot see or use the feature. |

**General rule:** Viewing and actions follow Roles & permissions and the user's data scope. Permission to create classes belongs to Classes, not to this feature.

## 5. Feature overview and functional breakdown

| Module | Feature | Description | User Story |
|---|---|---|---|
| **Classes** | Move a whole class up to the next level | From the class details, select Move children up; choose the new class and effective date; select all children and untick children who stay; confirm; see the result. | BBA-72: US-001 |

## 6. Functional requirements by user story

### 6.1 BBA-72: US-001 - Move a whole class up to the next level

#### User Story

As a user, I want to move all children in a class up to a class at the next level for the new academic year in one action, so that I do not have to move each child one by one.

#### Functional Requirements

| FR ID | Functional requirement |
|---|---|
| FR-001 | An authorised user opens the promotion flow from the class details (BR-001, BR-002). |
| FR-002 | The user chooses the new class from the classes already set up and chooses the effective date (BR-003, BR-004, BR-005; VAL-001). |
| FR-003 | The system lists all children in the current class, all selected by default; the user unticks children who stay (BR-006; VAL-002). |
| FR-004 | The user confirms; the system moves the selected children to the new class (BR-007, BR-008, BR-009). |
| FR-005 | The system shows how many children were moved up (BR-010). |
| FR-006 | The system records the history for each child and for the class (DATA-001, DATA-002). |

#### Functional Flow - Main

1. The user opens the class and selects Edit › Move children up (FR-001).
2. The user chooses the new class, keeps or changes the effective date, and selects Continue (FR-002).
3. The system shows all children in the current class, all selected; the user unticks any children who stay, and selects Continue (FR-003).
4. The system shows "n children move into <new class> on <date>"; the user selects Done (FR-004).
5. The system moves the children, records the history and shows the result (FR-004, FR-005, FR-006).

#### Functional Flow - Alternative

1. The new class would go over its maximum size: a warning is shown, and the user can still continue (BR-008).
2. Some children could not be moved: the user repeats the action (FR-005; BR-010).
3. The class is at the highest level the centre offers: Move children up is not available, and the user is pointed to Graduation or Transfer (BR-002).
4. The user selects Back to go to the previous step, or Close to close without moving any children.

#### Functional Flow - Exception

1. No new class is available: the user cannot continue; a user with permission creates the class in Classes and then tries again (BR-004; VAL-001).
2. The current class has no children: there are no children to move (VAL-002).
3. An error occurs when moving one child: that child stays in the old class, and the other children are still moved (BR-010).

#### Business Rules

| BR ID | Rule |
|---|---|
| BR-001 | Children are moved up only within the same centre. Moving to another centre is a Transfer. |
| BR-002 | A class at the highest level the centre offers has no Move children up; if the centre does not offer the next level, the user is pointed to Transfer. |
| BR-003 | The new class is at the next level, in the new academic year, in the same centre. |
| BR-004 | The new class must be created in advance in Classes by a user with permission to create classes. The promotion flow does not create classes. |
| BR-005 | The effective date defaults to the start date of the new academic year. |
| BR-006 | All children in the class are selected by default. The user unticks exceptions (for example a child repeating the year); unticked children stay in the current class with no change. |
| BR-007 | Selected children join the new class, and the level on their enrolment changes to the new level from the class's effective date. |
| BR-008 | If the new class goes over its maximum size, the system only warns and does not block. |
| BR-009 | The old class and its list of children are kept. |
| BR-010 | Each child is moved separately: an error for one child does not stop the others. |

#### Validation Rules

| VAL ID | Condition | System response |
|---|---|---|
| VAL-001 | The centre has no class at the next level for the new academic year. | Shows "There is no class at this centre for <level> the next academic year yet, so there is nowhere for these children to move to."; the user cannot continue. |
| VAL-002 | The current class has no children. | Shows "No children are in this class." |

#### UI Reference

| Screen / Version | Reference / Link |
|---|---|
| Move children up | |
| Classes — class details › Children, History | |

#### UI Components / Field Specification

| Field / Control | Type | Required | Default / State | Check | Behaviour |
|---|---|---|---|---|---|
| Move children up | Item in Edit | As permitted | Hidden for classes at the highest level | — | FR-001; BR-002. |
| Destination class — next year | Dropdown | Yes | — | VAL-001. | Classes as per BR-003, with current size / maximum size (FR-002). |
| Effective date | Date picker | Yes | As per BR-005 | — | FR-002. |
| Children list | List with tick boxes | — | All selected | VAL-002. | Each row: child name, "Moves up" when selected, "Stays in <current class>" when unticked (FR-003; BR-006). |
| Class size warning | Message | — | When over the maximum size | — | "<new class> would hold <n> of <maximum>" (BR-008). |
| Confirmation summary | Display | — | — | — | "n children move into <new class> on <date>". |
| Done | Button | — | — | — | Confirms the promotion (FR-004). |
| Back / Continue / Close | Button | — | — | VAL-001; VAL-002. | Go to the next / previous step, or close. |
| Result | Table | — | After confirmation | — | Shows the number of children moved successfully (FR-005). |
| Old class › Children | List | — | — | — | Still shows the children who moved up (BR-009). |
| Class › History | List | — | — | — | Promotion line: old class → new class, number of children, effective date, done by, time (FR-006). |

#### Data and Audit

| ID | Requirement |
|---|---|
| DATA-001 | For each child moved, save the old class and level, new class and level, effective date, done by and time of confirmation. |
| DATA-002 | For each promotion, save the current class, new class, effective date, number of children moved, errors (with reason), children who stayed, done by and time. |

#### Acceptance Criteria

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Class N2 · Sunbeams in 2026; the centre has created class K1 · Honeybees for 2027 | the user selects Edit › Move children up | the destination list has K1 · Honeybees 2027 in the same centre; the effective date defaults to the start of the 2027 academic year | FR-001; FR-002; BR-001; BR-003; BR-005 |
| AC-002 | The centre has not created a K1 class for 2027 | the user selects Move children up on the N2 class | the VAL-001 message is shown; there is no button to create a class; the user cannot continue | FR-002; BR-004; VAL-001 |
| AC-003 | Class K2 · Blossom | the user opens Edit | there is no Move children up; the user is pointed to Graduation | BR-002 |
| AC-004 | The centre only offers up to N2 | the user opens Edit on the N2 class | there is no Move children up; the user is pointed to Transfer | BR-002 |
| AC-005 | A teacher without promotion permission | the teacher opens Edit on the class | there is no Move children up | FR-001 |
| AC-006 | Class Sunbeams has 16 children | the user goes to the children step | all 16 children are selected, each showing "Moves up" | FR-003; BR-006 |
| AC-007 | 16 children are selected, effective date 04/01/2027 | the user selects Done | the 16 children are in class K1 · Honeybees, at level K1, from 04/01/2027; the result shows 16 children moved | FR-004; FR-005; BR-007 |
| AC-008 | 2 children are repeating N2 | the user unticks the 2 children and confirms | the 2 children show "Stays in N2 · Sunbeams" and stay in Sunbeams; 14 children move up to K1 · Honeybees | FR-003; FR-004; BR-006; BR-007 |
| AC-009 | Class Honeybees has a maximum of 20 and already has 8 children; 14 children are selected | the user goes to the next step | "K1 · Honeybees would hold 22 of 20" is shown with a warning; Continue is still enabled | BR-008 |
| AC-010 | The current class has no children | the user opens Move children up | "No children are in this class." is shown | VAL-002 |
| AC-011 | The promotion has been confirmed | the user opens class Sunbeams › Children after the effective date | the children who moved up are still listed; children who stayed are unchanged | FR-004; BR-009 |
| AC-012 | Class Sunbeams has had children | the user looks for an action to delete the class | there is no delete action; the class history is kept | BR-009 |
| AC-013 | 3 children are selected and moving Chloe fails | the user views the result | 2 children are moved; Chloe shows an error with a reason and stays in Sunbeams | FR-005; BR-010 |
| AC-014 | The promotion has been confirmed | the user opens the History of class Sunbeams | there is a promotion line: old class, new class, number of children, effective date, done by | FR-006; DATA-002 |

#### Dependencies

Classes (classes for the new academic year, class size); levels offered by the centre (Organisation); the child's enrolment; Joining & leaving (Graduation, Transfer).

## 7. Appendix

### Appendix A. Glossary

| Term | Meaning in this FRD |
|---|---|
| Level | Age-based year group: Infant, Playgroup, N1, N2, K1, K2; each centre offers only some levels. |
| Annual promotion | At the end of the academic year, a whole class moves up to the next level within the same centre. |
| Infant promotion | An infant moves up to Playgroup by age (18 months), at any time of the year, one child at a time. |
| Class change | Moving to another class at the same level. |
| Current class / new class | The child's class now / the class for the new academic year, already set up, that the child moves into. |
| Effective date | The date the promotion takes effect. |
| Repeating the year | The child stays at the same level for another year. |
| Graduation | K2 children leave the school in December (Joining & leaving). |
| Transfer | The child moves to another centre (Joining & leaving). |

### Appendix B. Catalogues

| Catalogue | Description | Depends on |
|---|---|---|
| Promotion result | Moved, Error, Stayed. | Children selected and the processing result. |
