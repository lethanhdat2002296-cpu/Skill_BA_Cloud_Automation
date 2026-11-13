
## BBA-1059 BBA input: Height and weight – growth chart, absent children, deleting, parent view, HQ report

### Description
Needed by: Fri 13 Nov, so design can start before Sprint 4 (23 Nov).
BBA owner: Alan → Centre Operations
How to reply: please answer in a comment, using the question numbers (for example "Q1: …").
Related: the measuring schedule for each brand (term or semester) is asked in BBA-529, so it is not repeated here.
Attached files: Parent App Requirements Provided to DotB (30 July 2026).pdf; Taidii - Center Staff Role permissions.xlsx.
Q1. Growth chart
What we know: In the Parent App review (16 Sep) you removed BMI and asked for an age-based growth chart, and offered to send the Singapore chart. The Taidii Parents App today plots growth "according to WHO standards".
Taidii Parents App today, Height & Weight screen
Questions:
• Should we use the WHO standards, as Taidii does, or a Singapore chart? If Singapore, please send the chart and its source.

• Which chart should Malaysia use?

Q2. Absent children and children on temporary withdrawal
What we know: In the Administration workshop (15 Sep) you described the entry screen as listing every child in the class for the teacher to fill in.
Question: Should the class entry screen also list children who are absent or on temporary withdrawal, so teachers can leave them blank and fill in later?
Q3. Deleting a measurement
What we know: The Centre Director does not need to approve measurements (Centre Leadership workshop, 17 Sep). In Taidii, "Update Height and Weight" is held by both CD/ACD/Admin and Teachers.
File "Taidii - Center Staff Role permissions.xlsx", sheet "Center Staff Role", row 14 (table redrawn from the Excel file; wording unchanged)
Question: May a measurement be deleted? If yes, which role may delete it?
Q4. When parents see measurements
What we know: Your Parent App requirements let parents view height, weight and growth history (item 19). A measurement is just a record, with no approval step (Administration workshop, 16 Sep).
File "Parent App Requirements Provided to DotB (30 July 2026).pdf", page 4, item 19
Question: Should parents see a new measurement as soon as the teacher saves it, or only at a set time, for example at the end of term like the portfolio?
Q5. Report for HQ
What we know: Many centres forget to enter measurements, so portfolios end up blank, and you asked for a checklist showing "what is done and what is not done" (Administration workshop, 15 Sep).
Questions:
• Does the HQ report only need completion status (by centre, class and term, and the percentage of children measured), or also growth statistics?

• Who will use the report?

### Comment 1
Q2. Yes, should include those children, possibly group them separately from the present students depending on the UX design.
Q3. A measurement can be deleted, can be a single permission for CRUD. Currently we assign to CD, Admin, and all Teachers.
Q4. Parents can see the measurements as soon as the entries are recorded.
Q5. Report only needs completion status. CD, Admin, Cluster Heads will be main users of the report for a start.

### Comment 2
Q1
• Singapore base on the Anthropometric study conducted by the Singapore National Healthcare Group Polyclinics.
• Sample chart reference available at https://littleetoile.com.sg/baby-weight-chart-singapore-13884/?srsltid=AYCX9vJaox5_lNWjZfVxbi4ej3JN8xhk8VSjOqcpxDMpcpPXTOy2RKr4.

• Malaysia chart reference - https://www.malaysia.gov.my/en/categories/health/babies-and-children/child-health-record-book

## BBA-1058 BBA input: Health changes in the system, 6-monthly review, printing the allergy list

### Description
Needed by: Fri 13 Nov, so design can start before Sprint 4 (23 Nov).
BBA owner: Alan → Centre Operations / Safeguarding
How to reply: please answer in a comment, using the question numbers (for example "Q1: …").
Attached files: Appendix 3Medical Care Assessment Review 2025.pdf; Appendix 1 Medical Care Assessment Checklist_.pdf.
Q1. Health changes in the system and the 6-monthly review
What we know:
• When a parent updates health information in the Parents App, the Centre Director and class teachers are notified (process review, 21 Sep).

• Your review form: after any change, a new Medical Care Assessment, Medical Overview and medicine form must be completed; the Centre Director or senior staff confirm with the parent every 6 months and both sign.

File "Appendix 3 Medical Care Assessment Review 2025", page 1
Questions:
• When a parent changes health information in the app, does it apply straight away, or only after the Centre Director completes the new assessment?

• Should the 6-monthly review be tracked in the system, with a reminder on the "Date of Next Review" and a sign-off?

Q2. Printing and exporting the allergy list
What we know: Your Medical Care Assessment Checklist asks parents to agree that their child's name and photo may be shown on the medical list.
File "Appendix 1 Medical Care Assessment Checklist", page 3
Questions:
• Which roles may print or export the allergy list?

• Should we record who printed or exported it, and when?

• For a child whose parent did not agree, what should the printed list show?

### Comment 1
Q1. Changes should apply only after CD or Admin completes the assessment. Yes, 6-monthly review should be tracked as part of the centre checklist, with auto reminder 1 month before to trigger the form to parents for reassessment.
Q2. CD, Admin, Teachers may print/export the allergy list. No need to reach who print/export. For children whose parents did not sign off, data will not appear in the child profile.

## BBA-529 BBA input: Height and weight records today

### Description
Requested in: email "Sprint 4 – SRS & prototype sign-off needed by Fri 6 Nov". Needed by Fri 6 Nov so design can start for Sprint 4 (23 Nov).
BBA owner: Alan → Centre Operations
What we already have from you
• Singapore measures height and weight every term, 4 terms a year 

• Reminder to centres in the middle of the last month of each quarter: mid-March, mid-June, mid-September, mid-December 

• Teachers enter height and weight for the whole class on one screen, instead of opening each child's record 

• Parents see height and weight in the app, and the same figures appear in the portfolio "About me" page 

What we still need
• Does any brand measure on a different schedule? The portfolio samples suggest Brighton measures by semester and Agape once per term. Please confirm the schedule for each brand, Singapore and Malaysia

• One sample export of the height and weight records from Taidii (one class is enough), so the new screen, the HQ report and the data migration match what you keep today

### Comment 1
Though Brighton measures by semester while the rest of the brands does the height and weight measurement term-wise. It would be sufficient to send the reminder in the middle of the last quarter for all brands. Sample export as attached.

## BBA-528 BBA input: Staff clock-in / clock-out flow

### Description
Requested in: email "Sprint 4 – SRS & prototype sign-off needed by Fri 6 Nov". Needed by Fri 6 Nov so design can start for Sprint 4 (23 Nov).
BBA owner: Alan → Centre Operations / HR
What we already have from you
• Staff clock-in and clock-out is in Phase 1 and needs a report (24 Sep)

• Today staff clock in on their own phone in Taidii, by location (GPS) or QR code, with monthly statistics: late, leave early, absent, on leave, overtime

• Temperature is recorded at clock-in (same fever threshold as children)

• All staff have a BBA Microsoft account (27 Oct, BBA-470)

What we still need
Please discuss with the departments concerned and confirm how staff will clock in and out in the new system:
• Where and how staff clock in and out (for example own phone, gate iPad, SMS web), and how to make sure no one can clock in or out for a colleague

• Who must clock in and out: all centre staff? HQ staff too?

• Are breaks recorded, or only start and end of the day?

• What happens when a staff member forgets to clock in or out, and who corrects it

• One sample of the staff attendance report you use from Taidii today

### Comment 1
• Staff clock in and out only on attendance app on gate iPad, with photo to be captured.
• Exception for CD app.

• Source user (attendance app or CD) to be captured.

• All centre staff to clock in/out. HQ staff and all visitors are also required to clock in/out as visitors, along with purpose to be captured.

• Breaks not required to be recorded.

• CD to monitor attendance and to correct if necessary.
• Possibly a notification to CD at configured time e.g. 1000 hr, on any staff absence?

• Sample of the staff attendance report as attached

## BBA-525 BBA input: GIRO "keep enough funds" reminder (Singapore)

### Description
Requested in: email "Sprint 4 – SRS & prototype sign-off needed by Fri 6 Nov". Needed by Fri 6 Nov so design can start for Sprint 4 (23 Nov).
BBA owner: Alan → Finance SG
What we already have from you
• Singapore bills monthly: draft on the 24th, billed on the second-last day of the month, due on the 5th, reminders on the 15th and 25th

• Malaysia bills by term (one invoice for 3 months, about 80% of invoices), monthly for corporate and instalment cases; the monthly fee and discount are kept separately inside the term invoice. Malaysia has no GIRO and collects by payment gateway, card and bank transfer (MY Finance SMS requirement)

• GST (Singapore): 9% of (gross − discount), rate set per period, GST number per legal entity

• GIRO runs (Singapore): 1st run submitted around the 3rd (value ~5th), 2nd run around the 17th (value ~21st) and re-collects what failed

• Parents on GIRO get an app reminder to keep enough funds before each deduction (25 Sep)

What we still need
• How many days before each GIRO deduction should the "keep enough funds" reminder go out?

### Comment 1
• One reminder to go out on 1st of the month.

• If able to track those on GIRO with outstanding amounts, e.g. first deduction failed or adhoc invoices, second reminder to go out on 15th of the month.

## BBA-524 BBA input: Approval matrix – who approves and amount limits

### Description
Requested in: email "Sprint 4 – SRS & prototype sign-off needed by Fri 6 Nov". Needed by Fri 6 Nov so design can start for Sprint 4 (23 Nov).
BBA owner: Alan / YC → HQ Operations, Finance SG, Finance MY
CD = Centre Director · DM = District Manager · HOB = Head of Brand
What we already have from you and need your double check:
• Approval routes must be configurable down to brand level (for both SG and MY?)

• Monthly recurring invoices: no approval; drafts are checked and confirmed automatically on the 31st (for both SG and MY?)

• Discounts: promo codes are pre-approved; any other discount (for example staff discount) must be approved in the system when it is given to a child, with name and date. Each discount item is marked "pre-approved" or "requires approval". There is no discount approval matrix today; centres set their own (for both SG and MY?)

• Refund: Finance prepares it, the head of Finance approves it (for both SG and MY?)

• Credit note requests and notice-period waivers need an approval workflow that traces back to a name and a date (for both SG and MY?)

• Withdrawal with full notice: no approval. Short notice: DM (SG) / Ops Manager (MY) / CD (Odyssey) / HOB (Brighton) (for both SG and MY?)

• Withdrawal or transfer on any day other than the last day of the month goes to a second-level approval (for both SG and MY?)

• Transfer with short notice: DM of both centres (for both SG and MY?)

• Malaysia fee waivers and retention fee waivers: CD informs the Ops Manager, who asks Finance; Finance gives the final approval and keeps an approval matrix with limits (for both SG and MY?)

• Attendance void: anyone can request; Centre Admin, CD or a senior teacher named by the CD approves; when they void it themselves no approval is needed.

What we still need
• Discounts that require approval: who approves, and is there an amount above which a second approver is needed?

• Credit note requests, refunds and notice-period waivers: who approves, and above what amount is a second approver needed?

• Malaysia: please share the Finance approval matrix (approver and limit per level) 

• Withdrawal or transfer in the middle of the month: who is the second-level approver? 

• Temporary withdrawal: Please confirm the approver(s) for Singapore and Malaysia, per brand where different

• Short-notice withdrawal: Please confirm if this approval was to stay on email or to be configured in the system for Phase 1, and the approvers?

### Comment 1
DM will now be known as Cluster Heads (CH) for both SG and MY. 
Finance = anyone under Finance role group. 
Finance Super Admin = Finance Managers.
• Discounts that require approval: who approves, and is there an amount above which a second approver is needed? → Currently all discount items are pre-approved and entered into the list by Finance, except "BBS Discount" which is open amount and will route to Finance for approval. 

• Credit note requests, refunds and notice-period waivers: who approves, and above what amount is a second approver needed?
• CN → CH

• Refunds → Finance Super Admin

• Notice-period waivers → CH

• Malaysia: please share the Finance approval matrix (approver and limit per level) → Currently no limit set, but will be ideal to have that configurable.

• Withdrawal or transfer in the middle of the month: who is the second-level approver? → CH / HOB

• Temporary withdrawal: Please confirm the approver(s) for Singapore and Malaysia, per brand where different → CH / HOB

• Short-notice withdrawal: Please confirm if this approval was to stay on email or to be configured in the system for Phase 1, and the approvers? → Preferably be configured in system for phase 1. CH / HOB

## BBA-512 BBA input: Handling rules for NRIC / FIN / MyKad numbers

### Description
Requested in: email "Sprint 4 – SRS, prototype and inputs needed by Fri 6 Nov" (listed as still open).
BBA owner: Alan
What we already have from you
• Parents and guardians are identified by NRIC / FIN / MyKad / passport number; children by birth certificate or passport number (BBA-471, BBA-473, 27 Oct)

• The same parent across centres or brands is merged into one account (BBA-471, 27 Oct)

• Citizenship drives the billing structure and the admin keeps it up to date on the child record (25 Sep)

• Taidii today has a separate permission "View Full IC of Child and Parent", and teachers can currently see the full IC (Taidii role permissions you sent)

• Bank account numbers on the profile must be masked (9 Sep)

• Registration forms by brand (Singapore and Malaysia); ECDA Withdrawal Form 3

What we still need
• Parents and guardians: do you need to keep the full NRIC / FIN / MyKad number, or are the last 3 digits and letter enough (for example ••••567D)? Under the PDPC NRIC guidelines, the full number should only be collected when the law requires it

• Children: for which purposes do you need the full number (for example ECDA subsidy claims)?

• Who may view a full ID number (for example Centre Director, centre admin, HQ Finance)?

• How long should ID numbers be kept after a child withdraws or graduates?

• An NRIC number does not show whether the person is a Singapore citizen or a PR. Where is citizenship or residency recorded today?

• Which documents must print the full ID number (for example ECDA forms, invoices, receipts)?

### Comment 1
Pls find the reply above.

### Comment 2
• Parents and guardians: do you need to keep the full NRIC / FIN / MyKad number, or are the last 3 digits and letter enough (for example ••••567D)? Under the PDPA NRIC guidelines, the full number should only be collected when the law requires it. Yes, need to collect the full number. However, based on PDPA guidelines shld mask and display the last 4 characters. 

• Children: for which purposes do you need the full number (for example ECDA subsidy claims)?Registration form, ECDA Forms(1,2 & 3)

• Who may view a full ID number (for example Centre Director, centre admin, HQ Finance)? Teacher, Admin, CD and also Finance staffs

• How long should ID numbers be kept after a child withdraws or graduates? 5 years

• An NRIC number does not show whether the person is a Singapore citizen or a PR. Where is citizenship or residency recorded today? Currently captured in the Enquiry record and admin will be updating correctly for the subsidy calculations

• Which documents must print the full ID number (for example ECDA forms, invoices, receipts)? Registration form, ECDA Forms(1,2 & 3). All Finance documents - Eg.Invoice, Receipts are to be masked.

## BBA-494 BBA input: Apps – working offline, photos and videos

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA". Ideally by Mon 2 Nov, before the Sprint 3 grooming.
BBA owner: Alan / YC
What we already have from you
• The Attendance app works offline and syncs automatically (Phase 1 scope)

• Class updates are mostly photos, with some video and no audio; Taidii limits video to about 1–2 minutes, and the limit should be configurable (8 Sep)

• BBA asked how long media stays in fast storage before moving to cheaper long-term storage (18 Sep)

What we still need
• Apart from attendance at the gate, which centre tasks must still work without internet (for example routines in the Teacher App)?

• Default maximum video length for class updates (we will make it configurable)

### Comment 1


### Comment 2
• Routines are good to have to work without internet, other tasks to work with internet.

• Set 2min as the default max video length for a start.

## BBA-493 BBA input: Personal data (PDPA) – log retention and contact

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA". Ideally by Mon 2 Nov, before the Sprint 3 grooming.
BBA owner: YC
What we already have from you
• Financial records must be kept for 5 years and be retrievable for audit (9 Sep)

• BBA is preparing an overview of PDPA and data policy for Singapore and Malaysia with the UK team (18 Sep)

What we still need
• The PDPA / data policy overview mentioned on 18 Sep, when ready

• The system keeps a log of who viewed or changed personal data. How long should this log be kept?

• Who at BBA handles personal data requests from parents?

### Comment 1
• No timeline yet on the data policy readiness.

• Will the log retention period be easily configured on front/back end? Any major concerns to keep up to 3 years from students' exit date?

• Parents may contact DPO@busybeesasia.com

## BBA-492 BBA input: Additional document templates

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA". Ideally by Mon 2 Nov, before the Sprint 3 grooming.
BBA owner: Alan → Admin / Finance
Chinese versions are not used today, and notices are written case by case (BBA-475). No need to send them.
What we already have from you
• Invoice, receipt and credit note templates (six brands)

• Finance email templates: invoice issued, Learning Horizon ad-hoc invoice, payment receipt, overdue reminders (SG and MY), payment reminder (Finance Email templates.xlsx, 2 Nov)

• Three new-enrolment emails

• K2 year-end withdrawal notice (Small Wonder) and the guide to update bank details for refunds

• Progress checklists (Agape, Learning Vision, Odyssey, Small Wonder, The Schoolhouse) and portfolio samples (six brands)

• 2027 BBS Common Terms for Enrolment (draft)

• An issued invoice is fixed at that point in time, including the master data (company name, address, fees, tax); reopening it shows that version (18 Sep)

What we still need
• If you use them today: refund voucher, welcome letter, transfer letter, consent request letter, progress report cover page

### Comment 1
• refund voucher: currently not in use by either finance/centre teams

• welcome letter: a standard template has been set up in taidii
• 

• transfer letter: not in use, but it would be good to have system notifications across centres to notify them of student transfers

• consent request letter: not in use, as parents have already given their consent through registration form declaration

• progress report cover page: there isn't a separate cover page for progress reports for each brand, as progress report is the checklist items, we can export the checklist in excel format

## BBA-491 BBA input: Notification rules (quiet hours, email fallback)

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA". Ideally by Mon 2 Nov, before the Sprint 3 grooming.
BBA owner: Alan / YC
What we already have from you
• Notifications are organised per parent, not per child: a parent with three children does not get the same notice three times 

• Six notification categories (routines, fees, messages, announcements, surveys and consents, approvals); parents can turn each category on or off 

• No email summary and no SMS; WhatsApp if ever needed 

• Malaysia: the centre admin is notified whenever a teacher messages a parent; Singapore does not need this 

• Parents on GIRO do not get payment reminders 

What we still need
• Quiet hours (no push notifications) for Singapore and Malaysia, if any

• If an important notification (for example an approval result or an invoice) is still unread after some time, should it also go by email? If yes, after how long?

### Comment 1
• Will the Quiet hours be configurable? At brand/centre level?
• Current operating hours configured as Monday to Friday, 0700 to 1900.

• Parents' message outside the operating hours will receive Auto Reply message, template attached.

• Can an in-app prompt be triggered instead? To show the prompt every time the app is opened until acknowledged/actioned.

## BBA-490 BBA input: Reminder rules to confirm

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA". Ideally by Mon 2 Nov, before the Sprint 3 grooming.
BBA owner: Alan → Finance / Admin
What we already have from you
• Invoice reminders: on the 15th and 25th at 8 pm, at most twice a cycle, in-app and email; parents on GIRO do not get payment reminders; reminder templates in Finance Email templates.xlsx

• Height and weight reminder: middle of March, June, September and December

• Every discount and subsidy should have an expiry date so admin knows what is coming up 

• A centre checklist (monthly / onboarding / quarterly) covering height and weight, portfolio and progress report was suggested by YC and Alan 

• Medicine and medical care forms

What we still need
• Which documents expire and need a reminder (for example passport, work pass, immunisation records), how early, and to whom?

• What should the centre checklist contain, and how often (monthly, quarterly, onboarding)?

### Comment 1
• Some other key documents with expiry and need reminder (should be configurable):
• Immunisation record - trigger reminder to parents, cc CD and Admin, up to 1 month before.

• Subsidy - trigger to CD and Admin, up to 2 months before.

• Giro application - trigger reminder to parents, cc CD and Admin, up to 2 months before.

• Allergy - no expiry, but to trigger review and confirmation to parents, cc CD and Admin, every 6 months.

• Centre checklist should contain mainly operational tasks.
• Separate checklist for BAU operations and onboarding.

• BAU operations - item frequency varies, e.g. check school fees receivables and student attendance on monthly basis, progress report completion every term.

• Onboarding checklist to contain items like collection of medical history documents, set up of Giro accounts.

## BBA-489 BBA input: 2027 term dates for each brand

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA", and again in the Sprint 4 email. Needed by Fri 6 Nov.
BBA owner: Alan → Curriculum
What we already have from you
• The school year runs from 1 January to 31 December, with 4 terms; term dates change every year 

• Each brand has its own term calendar, set by HQ; centres cannot change it. Example: The Schoolhouse Term 1 2 Jan – 15 Mar, Agape 2 Jan – 10 Mar 

• Some brands start the curriculum term one week after the school term 

• Screenshot of the current term set-up, Academic Year 2026: Term 1 01/01–22/03, Term 2 23/03–28/06, Term 3 29/06–13/09, Term 4 14/09–31/12 

• Height and weight reminder: middle of March, June, September and December 

• Event calendar import template (format only)

What we still need
• The 2027 start and end date of Term 1 to 4 for each brand (Singapore and Malaysia), and the curriculum term dates where they differ from the school term

### Comment 1
• Use attached file for the initial set up

## BBA-488 BBA input: Consent types and wording

### Description
Requested in: email "BBA Phase 1 – Sprint 3: business information needed from BBA", and again in the Sprint 4 email.
BBA owner: Alan → Admin / Safeguarding
What we already have from you
• Consent is collected once at enrolment: privacy policy, medical authorisation, and media / marketing consent 

• Media consent is a separate paper form today; it is sometimes asked again for a marketing event 

• Children without media consent must not be photographed or posted 

• In the app, a consent is a tick box, usually given once 

• 2025 Outdoor Learning Consent Form; registration form declarations (The Schoolhouse, Small Wonder); Learning Vision registration form; Parent App requirements 

What we still need
• The list of consent types for each brand, with the current wording (for example photography, outings, road crossing, medical, PDPA, and any others you use)

• When the wording of a consent changes, should parents be asked to agree again?

### Comment 1
• Consent Types as attached.

• Possible to have a retrigger consent collection upon update submission? Not all updates need to collect the consent again.

## BBA-487 BBA input: Confirm fields to track in change history

### Description
Requested in: email "BBA Phase 1 – For your review: reference lists (Sprint 2) and change history fields (Sprint 3)" (26 Oct). Ideally by Mon 2 Nov.
BBA owner: YC/Alan
Attachment: BBA-Change-History-Proposed-Fields-v0.1.xlsx
What it is
The fields where the system keeps every change: old value, new value, who, when and why. Our proposal covers 38 fields, for example child details, fees, attendance, approvals, users and settings. Approvals, status changes and records created or deleted are always logged.
What we need from you
• For each field, choose Keep, Remove or Not sure in column G

• Add any field we missed at the bottom of the list

• Tell us if any other field should be masked for the External Auditor (column H)

BBA can add or remove tracked fields later from the admin screen, so this does not need to be complete now.

### Comment 1
Updated the Google Sheets.

## BBA-486 BBA input: Confirm reference lists (dropdown values)

### Description
Requested in: email "BBA Phase 1 – For your review: reference lists (Sprint 2) and change history fields (Sprint 3)" (26 Oct). Ideally by Mon 2 Nov.
BBA owner: Alan / YC
Attachment: BBA-Reference-Lists-Draft-v0.1.xlsx
What it is
The lists people pick from in the new system (18 lists): country, brands, levels, sessions, citizenship, nationality, race, gender, relationship to the child, mother tongue, means-test band, ECDA class type, child status, reasons for leaving, payment methods, GIRO banks, calendar event types. We built them from your current Taidii data and forms, and cleaned up duplicate spellings.
What we need from you
• For each list, choose Confirm or Change in column G; if Change, write the correct values in column H

• Answer the short question in column F where there is one

Please upload the completed file to the shared Teams folder and put the link in a comment here.

### Comment 1
Updated the Google Sheets.

## BBA-475 BBA input: Document templates (letters, notices, emails; EN / ZH)

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan
What we already have from you
• Invoice, receipt and credit note templates (six brands)

• Three new-enrolment emails

• K2 year-end withdrawal notice (Small Wonder) and the guide to update bank details for refunds

• Registration form declarations (The Schoolhouse, Small Wonder)

What we still need
• Chinese versions of the templates where you use them

• Letters or notices centres send today that we have not received, for example withdrawal confirmation and fee change notice

• Registration form declarations for the other brands

### Comment 1
Thanks Alan. Since there are no standard notice templates today, we will set up a few placeholder templates in the system (e.g. withdrawal confirmation, fee change notice) so the flows can be built and tested. Before go-live, your team can log in to the system to edit these placeholders or create your own templates.
cc:

### Comment 2
• Currently we do not use any Chinese versions of the letters/notices.

• No standard template for notices at the moment; they are ad hoc generated.

• Common registration form declaration at 2027 BBS Common Terms for Enrolment.pdf - pending finalized version & confirmation if fine to use same for MY.

## BBA-474 BBA input: Brand identity and email domains

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan → Marketing; YC
What we already have from you
• Printed invoice, receipt and credit note templates for six brands (logos visible, but no logo files)

What we still need
• Marketing, for each brand in Singapore and Malaysia: logo files (SVG or high-resolution PNG, light and dark versions), brand colours (hex codes), app icon, and the sender name parents should see in emails

• YC: the sending email domain for each brand, and who can add the DNS records we will provide

### Comment 1
please access to folder Marketing to get access to Brand logo files and brand colors. https://kupl.sharepoint.com/:f:/s/Asia-Project-Project-CRMSMS/IgDGWTZDy6LtQp4jntLCjEoLAQxpaBVIMI5S2Dx8ilXgrBw?e=oO56tR

### Comment 2
Added SWM files. Added DNS records. Pending app icon

### Comment 3
Pending app icon, and Small Wonder Malaysia's files

### Comment 4
• Brand logo files and brand colors available at Marketing

• Email sender name will be "{centre name + acroynm} Team", e.g. Learning Vision Techpoint (TPT) Team

## BBA-473 BBA input: ID types for children and parents

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan
What we already have from you
• Registration forms by brand (Singapore and Malaysia)

• ECDA Withdrawal Form 3

What we still need
• Which ID types you record for children and for parents / guardians in each country, for example birth certificate number, NRIC / FIN, MyKid, MyKad, passport

### Comment 1
thank you.
cc:

### Comment 2
• Children - Birth certificate / Passport number

• Parents / Guardians - NRIC / FIN / MyKad / Passport number

## BBA-472 BBA input: Languages and formats

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan
What we already have from you
• —

What we still need
• Languages for the Parents App and for the staff screens. Our plan is English and Chinese. Is Malay needed for Malaysia in Phase 1?

• Date format: we propose DD/MM/YYYY

• Currency: SGD for Singapore, MYR for Malaysia

### Comment 1
thank you.
cc:

### Comment 2
• Malay not needed in phase 1.

• DD/MM/YYYY is good.

• Yes, SGD and MYR.

## BBA-471 BBA input: One account per parent – matching rules

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan / YC
What we already have from you
• Taidii registration form export (26 Aug)

• Registration forms by brand

What we still need
• Which detail identifies the same parent: mobile number, email address, or NRIC / passport number?

• Who gets app access: mother, father, legal guardian, other contacts?

• Parents who have several Taidii accounts today: may we merge them into one account at migration?

### Comment 1
thank you.
cc:

### Comment 2
• Use NRIC / FIN / MyKad / Passport number as the identifier.

• Both parents / legal guardians get app access. Pick up contacts by default do not get access unless specifically requested by parents for certain arrangement.

• Yes, merge them into one account.

## BBA-470 BBA input: Staff sign-in with Microsoft (Entra)

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: YC
What we already have from you
• —

What we still need
• Microsoft Entra app registration for each environment (Development, UAT, Staging, Production), plus tenant details. We will send the redirect addresses for each environment

• Do all staff who will use the system have a BBA Microsoft account, including part-time and relief teachers? If not, how should they sign in?

• Should a staff member's role come from their Microsoft (Entra) group, or be assigned in the new system?

### Comment 1
Evidence – Microsoft Entra ID SSO
Screenshot evidence of Microsoft SSO integration. Pending BBA confirmation: app registrations for all four environments, sign-in options staff, and role assignment via Entra groups or within the system.

### Comment 2
Details in Teams Channel folder, General → 06 Migration → Restricted Files → DotB UAT – Microsoft Entra SSO Configuration.pdf.
  please check if all in order.

### Comment 3
Redirect URI / Callback URL: https://uat.bba.dotb.cloud/api/auth/microsoft/callback
Authentication method: OpenID Connect (OIDC)
 Authorization: OAuth 2.0

### Comment 4
• Yes, all staff have BBA Microsoft account. However, we should allow dual login options, i.e. username+password, due to common/shared terminals.

• Staff role ideally should be from MS group, but pending BBA to sort out the roles. Should also allow manual change in assignments.

### Comment 5
Could you share the authentication protocol (e.g. SAML 2.0 or OAuth 2.0) to be used and the redirect address please?

## BBA-469 BBA input: Legal entities and bank accounts

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan → Finance
What we already have from you
• Bank Account list (12 Singapore legal entities)

• Cost Centre Mapping

• Account Mapping (SG) and MY Account Mapping

What we still need
• Per legal entity: company name, registration number (UEN for Singapore, SSM for Malaysia), GST or SST registration number, registered address, text printed at the bottom of invoices, and the brands and centres it bills for

• Per bank account: GIRO originator ID; PayNow UEN (Singapore) or DuitNow details (Malaysia)

• Malaysian legal entities and bank accounts

• Please confirm the 12 Singapore entities are still current

Please do not send bank account numbers by email or in a comment here. A restricted folder on the project SharePoint would be best.

### Comment 1
received. Thanks
cc:

### Comment 2
• Details uploaded in Teams channel folder. General → 06 Migration → Restricted Files → Entity Master Data and Bank Account.xlsx

• Brand/centres to entity mapping is available at Centre List for Setup.xlsx

• 12 Singapore entities + Learning Horizon SG are current.

## BBA-468 BBA input: Brands and districts

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan
What we already have from you
• Invoice, receipt and credit note templates for six Singapore brands

What we still need
• Full list of brands in Singapore and Malaysia

• List of districts / regions, and the District Manager for each

### Comment 1
received. Thanks.
cc:

### Comment 2
As per BBA-467, listing in Centre List for Setup.xlsx

## BBA-467 BBA input: Organisation structure – list of centres for Phase 1

### Description
Requested in: email "BBA Phase 1 – Sprint 2: business information needed from BBA" (22 Oct). Ideally by Fri 30 Oct.
BBA owner: Alan → HQ Operations
What we already have from you
• Monthly POP Reconciliation – Jul'26 (cost centre master list, 197 cost centres)

• Cost Centre Mapping (93 Singapore centres)

• Class Programme Capacity master list (26 Aug)

What we still need
• One row per centre going live on the new system: country, brand, district, centre name (as parents see it), centre code and cost centre code, POP / Non-POP, licence type and number, licensed capacity, address

• Go-live wave per centre: 1 May, 1 Jun or 1 Jul 2027, or not in Phase 1

• Malaysian centres added to the brand and legal entity mapping

Please upload the file to the shared Teams folder and put the link in a comment here.

### Comment 1
thank you.
cc:

### Comment 2
• SG & MY list of centres in Centre List for Setup.xlsx

• Indication of centres in which Go-live wave TBC.

## BBA-410 BBA organization tree mapping

### Description
Description: Map BBA Group/Country/Brand/District/Centre/Class to the existing Teams hierarchy using a documented configuration, without a second hierarchy engine.
Expected: BBA organization units and their memberships can be configured using existing Teams.
