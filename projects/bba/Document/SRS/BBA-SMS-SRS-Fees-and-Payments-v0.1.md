Busy Bees Asia

School Management System (SMS) — Phase 1

**Software Requirements Specification**

**Fees & Payments**

# Document control

| **Version** | **Date**        | **Prepared by** | **Description**                         |
|-------------|-----------------|-----------------|-----------------------------------------|
| **0.1**     | 14 October 2026 | DOTB            | Baseline for review with Busy Bees Asia |

## Conventions

- Features are individual actions a user or the system performs; functions describe what each feature does.

- Business rules are numbered BR-FEE-NNN and acceptance criteria AC-FEE-NNN.

- Rules common to all modules (HQ Admin has every permission; every list offers search, filters, sortable columns, paging of 20 / 50 / 100 rows and export; records that have been used are never deleted) are described in the SMS General Requirements document.

- Screen names and on-screen wording follow the prototype.

# 1. Purpose & scope

This document is the baseline Software Requirements Specification (SRS) for the Fees & Payments module of the Busy Bees Asia School Management System (SMS), Phase 1. It describes what the module must do so that the Finance team and the centres can bill, collect, refund and close each month without Taidii.

It is a starting point for discussion. Each area will be reviewed in detail during sprint planning, and the DOTB Business Analyst will update this SRS with the agreed details.

Read it together with the prototype at https://bba-sms-crm.lovable.app/billing. Each feature in Section 4 links to the prototype screen.

## 1.1 In scope for Phase 1

- Fee set-up: fee items and prices, fee schemes, discounts and promo codes, corporate accounts, billing settings.

- Billing: first invoice on enrolment, monthly billing runs, invoices, ad hoc invoices, credit notes.

- Payments and receipts: GIRO accounts and collection runs, PayNow QR, manual payments, receipts, outstanding balances and reminders, transactions.

- Deposits and refunds: deposit ledger, refunds, K2 year-end refunds.

- Subsidy (GSII) reconciliation.

- Finance approvals.

- Finance reports and month-end close.

- What parents see in the Parents App: invoices, receipts, PayNow QR, refund account confirmation, payment notifications.

## 1.2 Not in Phase 1

- Paying several invoices with one PayNow QR.

- Automatic promotion engine (promotions are applied as discount items).

- Finance dashboards and charts (Phase 1 provides reports exported to Excel).

- Parent blacklist, warning letters and debt write-off.

- Debit notes.

- Reopening a closed month.

- Direct integration with the bank's e-GIRO portal (Phase 1 exchanges bank files).

- Malaysia e-invoicing (MyInvois). Malaysia-specific billing (term billing, DuitNow, SST) will be detailed during sprint planning.

# 2. Who uses it

| **Role**                                  | **What they do in this module**                                                                                                                                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HQ Finance**                            | Sets up fees, discounts and billing settings; reviews and pauses billing runs; runs GIRO collections; records payments and issues receipts; processes refunds; approves finance requests; runs reports; closes the month. |
| **HQ Admin**                              | Has every permission in the module; configures settings, approval routes and templates.                                                                                                                                   |
| **Centre Director**                       | Views invoices of the centre; requests corrections on draft invoices; requests discounts and credit notes; approves level-1 requests as configured.                                                                       |
| **Centre Admin / School Admin**           | Views invoices of the centre; creates ad hoc invoices; requests corrections on drafts; uploads GSII reports and resolves differences.                                                                                     |
| **District Manager / Operations Manager** | Approves requests routed to them (for example short-notice withdrawals).                                                                                                                                                  |
| **Parent (Parents App)**                  | Views and downloads invoices and receipts; pays by PayNow; confirms the refund account; receives payment notifications.                                                                                                   |

# 3. Process overview

## P1. First invoice on enrolment

1\. The family pays the booking fee in Enquiries (before this module).

2\. The parent submits the registration form; the enrolment is confirmed.

3\. The system creates one Draft invoice with the registration fee and the deposit, less the booking fee, and records whether the deposit is paid from CDA or non-CDA.

4\. Finance reviews and bills it; the parent sees it in the Parents App.

## P2. Monthly billing cycle

1\. On the draft day (default 24th) the system generates next month's invoices as Draft for every centre.

2\. Finance reviews the change report; centres request corrections on drafts; Finance can pause a centre's run.

3\. Overnight on the day before the last day of the month, all Drafts that are not paused become Billed and appear in the Parents App.

4\. Invoices are due on the 5th of the billed month.

5\. GIRO families are collected in the 1ST DD run (school fees) and the 2ND DD run (other invoices); other families pay by PayNow or manual payment.

6\. Families with unpaid invoices receive in-app reminders on the 15th and 25th.

## P3. GIRO collection

1\. Finance creates a 1ST DD or 2ND DD batch and reviews the preview (GIRO and CDA totals).

2\. Finance downloads the bank file per legal entity and sends it to the bank.

3\. Finance uploads the bank result file.

4\. Successful lines create receipts and mark invoices Paid; failed lines are marked Unsuccessful and the parent is notified with the reason.

## P4. PayNow and manual payments

1\. Each Billed invoice shows a PayNow QR in the Parents App.

2\. When the payment arrives, the system creates the receipt immediately.

3\. Payments that do not match an invoice go to Unmatched payments for Finance to match.

4\. Bank transfer, AXS and cheque payments are recorded by Finance, who issues the receipt.

## P5. Deposit refund

1\. A withdrawal (or a Deposits page action, or the K2 year-end run) creates a refund request.

2\. Finance chooses to offset unpaid invoices first or refund in full.

3\. The parent confirms the refund account in the Parents App; CDA money goes back to CDA.

4\. The request is approved in Finance approvals.

5\. Finance generates the PayNow refund file, then uploads the bank result: successful refunds post to the deposit ledger; failed refunds are voided and the parent is asked to update the account.

## P6. GSII reconciliation

1\. Each centre uploads GSII-A and GSII-B (and optionally GSII-D) for the month.

2\. The system compares GSII with child profiles and with billed invoices and lists differences.

3\. The centre accepts or keeps each profile difference with a reason; invoice differences create a credit note or ad hoc invoice request for approval.

4\. GSII-D flags children withdrawn on ECDA but still active in the system.

## P7. Month-end close

1\. Finance checks the month-end checklist and runs the month-end reports.

2\. Finance closes the month; the month is locked permanently.

3\. Any later correction is made by credit note in an open month.

# 4. Modules, sub-modules, features and functions

## 1. Overview

### 1.1 Overview

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing</u>](https://bba-sms-crm.lovable.app/billing)

| **Feature**               | **Function**                                                                                                                                                            |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View "Waiting on you"** | Tasks for the user's role: drafts to review, correction requests, approvals, GIRO results not uploaded, GSII not uploaded, failed refunds. Each opens the right screen. |
| **View month summary**    | Invoices issued, amount collected and outstanding for the selected month.                                                                                               |
| **Filter**                | Centre, month.                                                                                                                                                          |

## 2. Fee set-up

### 2.1 Fee items & prices

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/fee-items</u>](https://bba-sms-crm.lovable.app/billing/fee-items)

| **Feature**            | **Function**                                                                          |
|------------------------|---------------------------------------------------------------------------------------|
| **View fee item list** | Code, name, GL account, tax treatment, CDA-deductible, status.                        |
| **Search**             | Partial, case-insensitive match on code and name.                                     |
| **Filter**             | Kind, status (Active / Stopped).                                                      |
| **Sort**               | Default by code.                                                                      |
| **Paging**             | 20 / 50 / 100 rows.                                                                   |
| **Create fee item**    | Code, name, GL account, tax treatment, CDA-deductible flag.                           |
| **Edit fee item**      | Name, GL account, tax treatment, CDA-deductible flag.                                 |
| **Stop using**         | "Stop using from \[date\]"; a stopped item cannot be used for new prices or invoices. |
| **Create price**       | Price by brand, level, programme (half day / full day) and citizenship.               |
| **Change price**       | Adds a new price with an effective date; past prices are never edited.                |
| **View price history** | All prices of an item over time.                                                      |
| **Export**             | Price book to Excel.                                                                  |

### 2.2 Fee schemes

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/fee-schemes</u>](https://bba-sms-crm.lovable.app/billing/fee-schemes)

| **Feature**              | **Function**                                                    |
|--------------------------|-----------------------------------------------------------------|
| **View scheme list**     | Name, brand, centres, level, version.                           |
| **Search**               | Name.                                                           |
| **Filter**               | brand, centre, level.                                           |
| **Create scheme**        | Fee items, deposit amount, last-month rule (half / full month). |
| **Edit scheme**          | Creates a new version with an effective date.                   |
| **Deactivate scheme**    | Instead of delete when in use.                                  |
| **View version history** |                                                                 |

### 2.3 Discounts & promo codes

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/discounts</u>](https://bba-sms-crm.lovable.app/billing/discounts)

| **Feature**                       | **Function**                                                                          |
|-----------------------------------|---------------------------------------------------------------------------------------|
| **View discount list**            | Name, amount or %, start and end date, approval type, children using it.              |
| **Search**                        | Name, campaign code.                                                                  |
| **Filter**                        | active / expired, approval type.                                                      |
| **Sort**                          | Sortable columns.                                                                     |
| **Create discount**               | Amount or %, start date, end date, approval type.                                     |
| **Set approval type**             | "Pre-approved (campaign / promo code)" or "Needs approval".                           |
| **Pick promo code**               | From the list of active campaign codes; no free text.                                 |
| **Auto-attach campaign discount** | A child created from an enquiry with a campaign code gets the discount automatically. |
| **Attach discount to a child**    | "Needs approval" discounts go to Finance approvals.                                   |
| **End discount**                  | End now; never deleted once used.                                                     |
| **Remove expired discounts**      | Automatically, and listed in the billing run change report.                           |
| **Export**                        | Children on a discount.                                                               |

### 2.4 Corporate accounts

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/corporate</u>](https://bba-sms-crm.lovable.app/billing/corporate)

| **Feature**                      | **Function**                                      |
|----------------------------------|---------------------------------------------------|
| **View corporate account list**  | Company, billing email, address, children billed. |
| **Search**                       |                                                   |
| **Sort**                         | Sortable columns.                                 |
| **Export**                       | Excel / CSV of the filtered list.                 |
| **Create corporate account**     | Company name, billing email, billing address.     |
| **Edit corporate account**       | Company name, billing email, billing address.     |
| **Deactivate corporate account** | Instead of delete.                                |
| **Set "Bill to" on a child**     | Parent or company.                                |

### 2.5 Billing settings

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/settings</u>](https://bba-sms-crm.lovable.app/billing/settings)

| **Feature**               | **Function**                                                                                          |
|---------------------------|-------------------------------------------------------------------------------------------------------|
| **View settings**         | Everyone can view; HQ Admin and Finance can edit.                                                     |
| **Edit billing dates**    | Draft day, Draft-to-Billed day, due day, reminder days.                                               |
| **Edit GIRO days**        | 1ST DD and 2ND DD days.                                                                               |
| **Edit document numbers** | Formats for invoice, receipt, credit note, refund.                                                    |
| **Preview schedule**      | Example: "October 2026 fees: draft 24 Sep · billed 29 Sep · due 5 Oct · reminders 15 Oct and 25 Oct". |
| **View history**          | Setting, old value, new value, who, when.                                                             |

## 3. Billing

### 3.1 Billing runs

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/runs</u>](https://bba-sms-crm.lovable.app/billing/runs)

| **Feature**                       | **Function**                                                                                                                                                                   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **View run list**                 | Month, centres, number of invoices, status (Draft / Paused / Billed).                                                                                                          |
| **Generate drafts automatically** | On the draft day, for every centre.                                                                                                                                            |
| **Calculate invoices**            | Tuition from the price book, active discounts, subsidy lines (Basic / Additional), pro-rated last month for leaving children; withdrawn children left out, new children added. |
| **Run now**                       | For one, several or all centres.                                                                                                                                               |
| **Pause billing**                 | Finance and HQ Admin, per centre; a red banner shows while paused; paused drafts are not billed.                                                                               |
| **Resume billing**                | Paused drafts are billed at the next conversion.                                                                                                                               |
| **Convert Draft to Billed**       | Automatically overnight on the Draft-to-Billed day.                                                                                                                            |
| **View change report**            | New, withdrawn, programme changes, subsidy changes, expired discounts removed, children with no invoice (with reason); each row links to the child or invoice.                 |
| **Export change report**          | Excel.                                                                                                                                                                         |

### 3.2 Invoices

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/invoices</u>](https://bba-sms-crm.lovable.app/billing/invoices)

| **Feature**                      | **Function**                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------|
| **View invoice list**            | Number, child, centre, month, amount, balance, status, bill to.                                          |
| **Search**                       | Invoice number, child, parent.                                                                           |
| **Filter**                       | Centre, month, status, bill to.                                                                          |
| **Sort**                         | Default newest first.                                                                                    |
| **Paging**                       | 20 / 50 / 100 rows.                                                                                      |
| **View invoice detail**          | Lines, subsidy, payments, credit notes, delivery.                                                        |
| **Edit draft invoice**           | Finance edits lines while Draft.                                                                         |
| **Request a correction**         | Centre users on a Draft; appears in Finance's "Waiting on you".                                          |
| **Mark correction done**         | Finance closes it; the requester is notified.                                                            |
| **Void invoice**                 | Reason required; not in a closed month.                                                                  |
| **Download PDF**                 | From the brand's invoice template.                                                                       |
| **Print**                        | From the brand's invoice template.                                                                       |
| **Send invoice email**           | Automatically when Billed for company-billed invoices and enrichment (Learning Horizon) ad hoc invoices. |
| **Resend invoice email**         | For company-billed invoices.                                                                             |
| **Show in Parents App**          | All other invoices are visible in the Parents App only.                                                  |
| **Notify parent of new invoice** | In-app notification when an invoice is Billed.                                                           |
| **View history**                 | Created, edited, correction requested / done, billed, emailed, paid, voided.                             |
| **Export**                       | Filtered list.                                                                                           |

### 3.3 Ad hoc invoices

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/invoices</u>](https://bba-sms-crm.lovable.app/billing/invoices)

| **Feature**                     | **Function**                                                                   |
|---------------------------------|--------------------------------------------------------------------------------|
| **Create single invoice**       | Centre users for one child.                                                    |
| **Create for a class or level** | Centre, class or level, fee item, amount, preview, then one invoice per child. |
| **Import from file**            | Download template, upload, row-by-row errors, confirm.                         |

### 3.4 Credit notes

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/credits</u>](https://bba-sms-crm.lovable.app/billing/credits)

| **Feature**               | **Function**                                     |
|---------------------------|--------------------------------------------------|
| **View credit note list** | Number, invoice, child, scope, amount, status.   |
| **Search**                | Credit note no., invoice no., child.             |
| **Filter**                | status, month, centre.                           |
| **Sort**                  | Sortable columns.                                |
| **Create credit note**    | From an invoice; scope Half month or Full month. |
| **Submit for approval**   | Every credit note goes to Finance approvals.     |
| **Apply credit note**     | Automatically when approved.                     |
| **Download PDF**          |                                                  |
| **View history**          |                                                  |
| **Export**                |                                                  |

## 4. Payments & receipts

### 4.1 GIRO accounts

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/giro</u>](https://bba-sms-crm.lovable.app/billing/giro)

| **Feature**                 | **Function**                                                                                                                    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **View GIRO account list**  | Child, parent, account type, bank, last 4 digits, DDA reference, status.                                                        |
| **Search**                  | Child, parent, last 4 digits.                                                                                                   |
| **Filter**                  | type (GIRO / CDA), status.                                                                                                      |
| **Create GIRO account**     | Pays by GIRO yes / no, account type GIRO or CDA, bank, account number, DDA reference, application method (paper form / e-GIRO). |
| **Update status**           | Pending with bank / Active / Rejected (with reason).                                                                            |
| **Edit GIRO account**       | Bank, account, DDA reference, status.                                                                                           |
| **Deactivate GIRO account** | Never deleted once used.                                                                                                        |
| **Mask account number**     | Only the last 4 digits outside the detail.                                                                                      |
| **View history**            |                                                                                                                                 |
| **Export**                  |                                                                                                                                 |

### 4.2 GIRO collection runs

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/batches</u>](https://bba-sms-crm.lovable.app/billing/batches)

| **Feature**                       | **Function**                                                                         |
|-----------------------------------|--------------------------------------------------------------------------------------|
| **View batch list**               | Run type, deduction date, lines, GIRO total, CDA total, status.                      |
| **Create batch**                  | 1ST DD (school fee invoices) or 2ND DD (other Billed invoices).                      |
| **Preview batch**                 | Child, invoice, amount, GIRO or CDA; untick lines.                                   |
| **Download bank file**            | Text file per legal entity in the bank's format.                                     |
| **Upload bank result**            | Successful lines: receipt and Paid; failed lines: Unsuccessful with the bank reason. |
| **Block duplicate result upload** |                                                                                      |
| **Hide PayNow during 1ST DD**     | "Being collected by GIRO" until the result is uploaded.                              |
| **Notify GIRO failure**           | Parent notified with the reason.                                                     |
| **Send "keep funds" reminder**    | Before each deduction day.                                                           |
| **Export batch result**           |                                                                                      |

### 4.3 PayNow

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/payments</u>](https://bba-sms-crm.lovable.app/billing/payments)

| **Feature**                   | **Function**                                                                   |
|-------------------------------|--------------------------------------------------------------------------------|
| **Generate PayNow QR**        | For each Billed invoice, from the legal entity UEN, invoice number and amount. |
| **Show QR in Parents App**    |                                                                                |
| **Create receipt on payment** | Immediately when the payment arrives.                                          |

### 4.4 Unmatched payments

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/unmatched</u>](https://bba-sms-crm.lovable.app/billing/unmatched)

| **Feature**                 | **Function**                                                      |
|-----------------------------|-------------------------------------------------------------------|
| **View unmatched payments** | Payments that do not match an invoice.                            |
| **Match payment**           | Finance searches candidate invoices and matches; receipt created. |
| **View matched history**    | Who matched, when.                                                |

### 4.5 Manual payments

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/payments</u>](https://bba-sms-crm.lovable.app/billing/payments)

| **Feature**          | **Function**                                                                  |
|----------------------|-------------------------------------------------------------------------------|
| **Record a payment** | Invoice, amount, date, method (bank transfer, AXS, cheque), proof attachment. |
| **Issue receipt**    | Finance and HQ Admin only.                                                    |
| **Void payment**     | Reason required; not in a closed month.                                       |

### 4.6 Receipts

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/payments</u>](https://bba-sms-crm.lovable.app/billing/payments)

| **Feature**             | **Function**                              |
|-------------------------|-------------------------------------------|
| **View receipt list**   | Number, child, method, amount, date.      |
| **Search**              | Receipt no., child, parent.               |
| **Filter**              | method, month, centre.                    |
| **Sort**                | Sortable columns.                         |
| **View receipt detail** | Invoices paid, issued by, date.           |
| **Download PDF**        |                                           |
| **Print**               |                                           |
| **Show in Parents App** |                                           |
| **Send receipt email**  | To companies for company-billed invoices. |
| **Void receipt**        | Reason required; not in a closed month.   |
| **Export**              |                                           |

### 4.7 Outstanding & reminders

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/receivables</u>](https://bba-sms-crm.lovable.app/billing/receivables)

| **Feature**                  | **Function**                                            |
|------------------------------|---------------------------------------------------------|
| **View outstanding list**    | Families with unpaid Billed invoices after the due day. |
| **Search**                   | Child, parent.                                          |
| **Filter**                   | centre, amount, days overdue.                           |
| **Sort**                     | default amount, highest first.                          |
| **Send automatic reminders** | In-app on the reminder days.                            |
| **Send reminder now**        | For one or several selected families.                   |
| **View reminder log**        | Who was reminded, when.                                 |
| **Export**                   |                                                         |

### 4.8 Transactions

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/transactions</u>](https://bba-sms-crm.lovable.app/billing/transactions)

| **Feature**           | **Function**                          |
|-----------------------|---------------------------------------|
| **View transactions** | All money movements.                  |
| **Search**            | Reference, payer, amount.             |
| **Filter**            | centre, status, method.               |
| **Sort**              | by created, transaction or void date. |
| **Export**            |                                       |

## 5. Deposits & refunds

### 5.1 Deposit ledger

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/deposits</u>](https://bba-sms-crm.lovable.app/billing/deposits)

| **Feature**             | **Function**                                               |
|-------------------------|------------------------------------------------------------|
| **View deposit ledger** | Per child: amount, source (CDA / non-CDA), date, movement. |
| **Search**              | Child.                                                     |
| **Filter**              | centre, source.                                            |
| **Record deposit**      | From the first invoice.                                    |
| **Offset deposit**      | Against unpaid invoices.                                   |
| **Transfer deposit**    | When a child transfers centre.                             |
| **View history**        |                                                            |
| **Export**              | Deposit balances.                                          |

### 5.2 Refunds

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/refunds</u>](https://bba-sms-crm.lovable.app/billing/refunds)

| **Feature**                         | **Function**                                                                     |
|-------------------------------------|----------------------------------------------------------------------------------|
| **View refund list**                | Number, child, amount, source, destination, status.                              |
| **Search**                          | Refund no., child.                                                               |
| **Filter**                          | status, source, centre.                                                          |
| **Sort**                            | default oldest pending first.                                                    |
| **Create refund request**           | Automatically from a withdrawal; manually from the Deposits page.                |
| **Choose offset or full refund**    | Default: offset unpaid invoices first.                                           |
| **Ask parent to confirm account**   | In-app notification.                                                             |
| **Confirm refund account (parent)** | PayNow by mobile number, NRIC or UEN.                                            |
| **Submit for approval**             |                                                                                  |
| **Generate PayNow refund file**     | Per legal entity; refunds move to Processing.                                    |
| **Upload bank result**              | Successful or Unsuccessful.                                                      |
| **Void failed refund**              | Automatically; parent notified; new request when the parent updates the account. |
| **Notify refund result**            | Parent notified when successful or failed.                                       |
| **View history**                    | Every status change, who, when.                                                  |
| **Export**                          |                                                                                  |

### 5.3 K2 year-end refunds

*Prototype:* [<u>https://bba-sms-crm.lovable.app/lifecycle/graduation</u>](https://bba-sms-crm.lovable.app/lifecycle/graduation)

| **Feature**                       | **Function**                                    |
|-----------------------------------|-------------------------------------------------|
| **Select graduating K2 children** | K3 (repeating K2) children unticked by default. |
| **Create year-end refunds**       | One action for the whole list.                  |

## 6. Subsidy (GSII)

### 6.1 GSII reconciliation

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/subsidy-reconciliation</u>](https://bba-sms-crm.lovable.app/billing/subsidy-reconciliation)

| **Feature**                 | **Function**                                                            |
|-----------------------------|-------------------------------------------------------------------------|
| **View upload list**        | Centre, month, file type, uploaded by, uploaded on, status.             |
| **Download sample files**   | GSII-A, GSII-B, GSII-D.                                                 |
| **Upload GSII**             | GSII-A and GSII-B per centre per month; GSII-D optional.                |
| **Validate month**          | Reads the month from the file and blocks a mismatch.                    |
| **Remind centres**          | Centres with no upload by the reminder day.                             |
| **Check profiles vs GSII**  | Lists differences; "Accept GSII value" or "Keep profile" with a reason. |
| **Check invoices vs GSII**  | Lists differences; creates a credit note or ad hoc invoice request.     |
| **Check withdrawn on ECDA** | GSII-D children still active in the system.                             |
| **Search**                  | Child.                                                                  |
| **Filter**                  | centre, month, difference type.                                         |
| **View history**            | Decisions, who, when, reason.                                           |
| **Export**                  | Each check.                                                             |

## 7. Approvals

### 7.1 Finance approvals

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/approvals</u>](https://bba-sms-crm.lovable.app/billing/approvals)

| **Feature**             | **Function**                                                     |
|-------------------------|------------------------------------------------------------------|
| **View approval inbox** | Type, child / centre, amount, requested by, date, level, status. |
| **Search**              | Child, request no.                                               |
| **Filter**              | type, status, centre.                                            |
| **Sort**                | default oldest pending first.                                    |
| **View request detail** | Amount, reason, attachments, source record, history.             |
| **Approve**             | Records who and when.                                            |
| **Reject**              | Reason required.                                                 |
| **Notify requester**    | In-app.                                                          |
| **Two-level approval**  | Second approver above an amount threshold.                       |
| **Export**              |                                                                  |

## 8. Reports & month-end

### 8.1 Reports

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/reports</u>](https://bba-sms-crm.lovable.app/billing/reports)

| **Feature**                                 | **Function**                                             |
|---------------------------------------------|----------------------------------------------------------|
| **Select period and centre / legal entity** |                                                          |
| **View deposit balance**                    | With CDA / non-CDA split.                                |
| **View trade debtors**                      | Balance per child at month end, ageing buckets.          |
| **View transactions**                       | By created date, transaction date, void date.            |
| **View payment mode**                       | Collections per method.                                  |
| **View advance payments**                   | Money received before the invoice month / unused credit. |
| **View credit notes**                       | Issued in the month.                                     |
| **View operational lists**                  | GIRO results, refunds by status, GSII results.           |
| **Export to Excel**                         | Every report.                                            |

### 8.2 Month-end close

*Prototype:* [<u>https://bba-sms-crm.lovable.app/billing/close</u>](https://bba-sms-crm.lovable.app/billing/close)

| **Feature**                  | **Function**                                                                         |
|------------------------------|--------------------------------------------------------------------------------------|
| **View month-end checklist** | Drafts not billed, GIRO results not uploaded, unmatched payments, GSII not uploaded. |
| **Close month**              | Locks the month permanently.                                                         |
| **Enforce lock**             | No edit, void, payment, receipt or credit note dated in a closed month.              |
| **View close log**           | Month, closed by, closed on.                                                         |

# 5. Business rules

## Billing calendar

| **ID**         | **Rule**                                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-001** | Next month's invoices are generated as Draft on the 24th of each month.                                                                                                       |
| **BR-FEE-002** | Drafts become Billed automatically overnight on the day before the last day of the month (for example 29 September for October fees), unless the run is paused.               |
| **BR-FEE-003** | Invoices are due on the 5th of the billed month.                                                                                                                              |
| **BR-FEE-004** | Families with an unpaid Billed invoice receive an in-app reminder on the 15th and the 25th; families who have paid are not reminded; at most 2 automatic reminders per cycle. |
| **BR-FEE-005** | All billing days are settings, not fixed values, and can be changed by HQ Admin or Finance.                                                                                   |

## Invoices

| **ID**         | **Rule**                                                                                                                                                                       |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-006** | Invoice statuses are Draft, Billed, Partially paid, Paid, Overdue and Void. Partially paid and Overdue are calculated from payments and the due day and are never set by hand. |
| **BR-FEE-007** | There is no approval of individual invoices; Finance controls billing by reviewing the change report, editing drafts and pausing runs.                                         |
| **BR-FEE-008** | Only Finance can change fees and prices. Centre users can request corrections on Draft invoices.                                                                               |
| **BR-FEE-009** | An issued invoice keeps the legal entity name, address and registration numbers that applied when it was issued; later changes do not alter it.                                |
| **BR-FEE-010** | Invoices billed to a company and enrichment (Learning Horizon) ad hoc invoices are emailed; all other invoices are delivered in the Parents App only.                          |
| **BR-FEE-011** | Enrichment fees are billed on a separate invoice from tuition.                                                                                                                 |
| **BR-FEE-012** | Document numbers are unique across all centres and run per centre.                                                                                                             |

## Pricing and discounts

| **ID**         | **Rule**                                                                                                                                                   |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-013** | Tuition is priced by brand, level, programme (half day / full day) and citizenship.                                                                        |
| **BR-FEE-014** | The registration fee comes from one place only, the price book.                                                                                            |
| **BR-FEE-015** | A price change is a new price with an effective date; past prices are never edited.                                                                        |
| **BR-FEE-016** | Discounts are either pre-approved (campaign or promo code) or need approval. Discounts that need approval go through the Centre Director and then Finance. |
| **BR-FEE-017** | A promo code is picked from the list of active campaign codes. A campaign code captured on the enquiry is attached to the child automatically.             |
| **BR-FEE-018** | Expired discounts are removed from the next run automatically.                                                                                             |
| **BR-FEE-019** | Waiving the registration fee requires Finance approval.                                                                                                    |

## First invoice and deposits

| **ID**         | **Rule**                                                                                                                                       |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-020** | The first invoice is created when the registration is submitted, with the registration fee and the deposit, less the booking fee already paid. |
| **BR-FEE-021** | Families who do not pay by GIRO pay one additional month of deposit. The number of deposit months is set per brand and centre.                 |
| **BR-FEE-022** | The source of every deposit (CDA or non-CDA) is recorded.                                                                                      |
| **BR-FEE-023** | Deposits are offset against unpaid invoices first unless Finance chooses a full refund.                                                        |
| **BR-FEE-024** | K2 deposits can be offset against up to 2 months of tuition and enrichment fees.                                                               |

## Credit notes

| **ID**         | **Rule**                                                                                                                                                               |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-025** | A credit note covers half a month or a full month.                                                                                                                     |
| **BR-FEE-026** | An invoice can have at most one credit note.                                                                                                                           |
| **BR-FEE-027** | Every credit note is approved in Finance approvals before it is issued.                                                                                                |
| **BR-FEE-028** | An approved credit note is applied to its invoice first; any remainder is applied to the child's oldest open invoice. It is never also deducted from the next invoice. |

## GIRO and PayNow

| **ID**         | **Rule**                                                                                                                                |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-029** | GIRO is collected in two runs: 1ST DD for school fee invoices and 2ND DD for all other Billed invoices.                                 |
| **BR-FEE-030** | A family can have one GIRO (bank) account and one CDA account. CDA is used only for CDA-deductible fee items.                           |
| **BR-FEE-031** | Bank files are produced per legal entity. Each legal entity has one bank account and one PayNow UEN.                                    |
| **BR-FEE-032** | A bank result file can be uploaded only once per batch.                                                                                 |
| **BR-FEE-033** | Successful GIRO lines create receipts automatically. Failed lines keep the invoice unpaid and notify the parent with the bank's reason. |
| **BR-FEE-034** | While an invoice is in a 1ST DD batch without a result, PayNow is not offered for it.                                                   |
| **BR-FEE-035** | Parents on GIRO are reminded to keep enough funds before each deduction day.                                                            |
| **BR-FEE-036** | Every Billed invoice has its own PayNow QR. A PayNow payment creates the receipt immediately.                                           |
| **BR-FEE-037** | Manual payment methods for Singapore centres are bank transfer, AXS and cheque. Only Finance and HQ Admin issue receipts.               |
| **BR-FEE-038** | Singapore centres never show Malaysia payment methods or currency.                                                                      |

## Refunds

| **ID**         | **Rule**                                                                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-039** | All refunds go through one refund list, whatever started them.                                                                                    |
| **BR-FEE-040** | Refund statuses are Pending approval, Approved, Rejected, Processing, Successful, Unsuccessful and Void.                                          |
| **BR-FEE-041** | Refunds are approved only in Finance approvals.                                                                                                   |
| **BR-FEE-042** | Money paid from CDA is refunded to CDA only.                                                                                                      |
| **BR-FEE-043** | Only the parent can set or change the refund account (PayNow by mobile number, NRIC or UEN). Finance can view it and ask the parent to update it. |
| **BR-FEE-044** | A failed refund is voided automatically and the parent is asked to update the account; a new request is created when they do.                     |
| **BR-FEE-045** | K2 children graduating in December are refunded in one year-end action; children repeating K2 are excluded.                                       |

## Subsidy (GSII)

| **ID**         | **Rule**                                                                                                                                              |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-046** | Each centre uploads GSII-A and GSII-B every month. A file for a different month is rejected.                                                          |
| **BR-FEE-047** | Centres that have not uploaded by the 10th of the following month are reminded.                                                                       |
| **BR-FEE-048** | Differences between GSII and the child profile are never applied automatically; the centre accepts the GSII value or keeps the profile with a reason. |
| **BR-FEE-049** | Differences between GSII and billed invoices are corrected by a credit note or an ad hoc invoice, approved in Finance approvals.                      |

## Approvals and month-end

| **ID**         | **Rule**                                                                                                                                                      |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BR-FEE-050** | All finance approvals are handled in one inbox. Rejecting requires a reason.                                                                                  |
| **BR-FEE-051** | Approval routes (who approves each request type, up to 2 levels and amount thresholds) are configured by HQ Admin in Administration.                          |
| **BR-FEE-052** | A closed month is locked permanently. Nothing dated in a closed month can be created, edited or voided; corrections are made by credit note in an open month. |
| **BR-FEE-053** | Records that have been used are never deleted; they are stopped, voided or deactivated.                                                                       |

# 6. Notifications & documents

## 6.1 Notifications

| **Notification**           | **Recipient**                               | **Channel**              | **When**                                                  |
|----------------------------|---------------------------------------------|--------------------------|-----------------------------------------------------------|
| **New invoice**            | Parent                                      | In-app                   | When an invoice is Billed                                 |
| **Invoice email**          | Company / parent (enrichment ad hoc)        | Email                    | When Billed; resend on request                            |
| **Correction request**     | Finance                                     | In-app (web)             | When a centre user requests a correction                  |
| **Correction done**        | Requester                                   | In-app (web)             | When Finance marks it done                                |
| **Payment reminder**       | Parent with unpaid invoice                  | In-app                   | On the reminder days (15th, 25th); or sent now by Finance |
| **Keep funds for GIRO**    | Parent on GIRO                              | In-app                   | Before each deduction day                                 |
| **GIRO failed**            | Parent                                      | In-app                   | When the bank result shows a failure                      |
| **Receipt**                | Parent; company for company-billed invoices | In-app; email to company | When a payment is recorded                                |
| **Confirm refund account** | Parent                                      | In-app                   | When Finance asks                                         |
| **Refund result**          | Parent                                      | In-app                   | When the refund succeeds or fails                         |
| **GSII not uploaded**      | Centre Admin                                | In-app (web)             | From the reminder day                                     |
| **Approval decision**      | Requester                                   | In-app (web)             | When a request is approved or rejected                    |

## 6.2 Documents

- Invoice (monthly, registration, enrichment, ad hoc), receipt, credit note: PDF from the brand's template, showing the issuing legal entity.

- GIRO bank file and PayNow refund file per legal entity; bank result files uploaded back.

# 7. Reports & exports

| **Report**                      | **Content**                                             | **Used by**                 |
|---------------------------------|---------------------------------------------------------|-----------------------------|
| **Deposit balance**             | Deposits held per child at month end, CDA / non-CDA     | HQ Finance                  |
| **Trade debtors**               | Balance owed per child at month end with ageing         | HQ Finance                  |
| **Transactions**                | By created date, transaction date and void date         | HQ Finance                  |
| **Payment mode**                | Collections per payment method for the month            | HQ Finance                  |
| **Advance payments**            | Money received before the invoice month / unused credit | HQ Finance                  |
| **Credit notes**                | Credit notes issued in the month                        | HQ Finance                  |
| **GIRO results**                | Success and failure counts and amounts per batch        | HQ Finance                  |
| **Refunds by status**           | Refunds and their status                                | HQ Finance                  |
| **GSII reconciliation results** | Differences found and decisions per centre              | HQ Finance, Centre Admin    |
| **Billing run change report**   | New, withdrawn, changed children per run                | HQ Finance                  |
| **Outstanding list**            | Families owing after the due day                        | HQ Finance, Centre Director |

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
<td><strong>AC-FEE-001</strong></td>
<td>Monthly drafts</td>
<td>Given it is the 24th of September,<br />
when the billing run starts,<br />
then October invoices are created as Draft for every centre, with tuition, active discounts and subsidy lines.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-002</strong></td>
<td>Draft to Billed</td>
<td>Given October drafts exist and the run of centre A is paused,<br />
when the night of 29 September passes,<br />
then all drafts except centre A's become Billed and appear in the Parents App; centre A's stay Draft until resumed.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-003</strong></td>
<td>Correction request</td>
<td>Given a Draft invoice of centre A,<br />
when the Centre Admin requests a correction,<br />
then Finance sees the request in "Waiting on you" and the requester is notified when Finance marks it done.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-004</strong></td>
<td>Due and overdue</td>
<td>Given a Billed October invoice is unpaid on 6 October,<br />
when the invoice list is opened,<br />
then the invoice shows Overdue.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-005</strong></td>
<td>Payment reminder</td>
<td>Given family A has an unpaid Billed invoice and family B has paid,<br />
when it is the 15th,<br />
then only family A receives the in-app reminder.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-006</strong></td>
<td>First invoice</td>
<td>Given a family paid a booking fee and does not use GIRO,<br />
when the registration is submitted,<br />
then one Draft invoice is created with the registration fee and the deposit including one additional month, less the booking fee.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-007</strong></td>
<td>One credit note per invoice</td>
<td>Given an invoice already has a credit note,<br />
when Finance tries to create another one,<br />
then the system blocks it and names the existing credit note.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-008</strong></td>
<td>Credit note application</td>
<td>Given an approved credit note is larger than its invoice balance,<br />
when it is applied,<br />
then it clears the invoice and the remainder is applied to the child's oldest open invoice.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-009</strong></td>
<td>GIRO success and failure</td>
<td>Given a 1ST DD batch with two invoices,<br />
when Finance uploads a result with one success and one failure,<br />
then the first invoice is Paid with a receipt; the second stays unpaid, is marked Unsuccessful and the parent is notified with the reason.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-010</strong></td>
<td>Duplicate result file</td>
<td>Given a result file was uploaded for a batch,<br />
when the same file is uploaded again,<br />
then the system rejects it.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-011</strong></td>
<td>PayNow during GIRO</td>
<td>Given an invoice is in a 1ST DD batch without a result,<br />
when the parent opens it in the Parents App,<br />
then PayNow is not offered and the invoice shows "Being collected by GIRO".</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-012</strong></td>
<td>PayNow receipt</td>
<td>Given a Billed invoice,<br />
when the parent pays the exact amount by its PayNow QR,<br />
then the invoice becomes Paid and a receipt is created immediately.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-013</strong></td>
<td>CDA refund</td>
<td>Given a deposit was paid from CDA,<br />
when a refund is created,<br />
then the destination is CDA and cannot be changed.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-014</strong></td>
<td>Refund approval</td>
<td>Given a refund is Pending approval,<br />
when Finance opens the Refunds list,<br />
then there is no approve button; the refund can only be decided in Finance approvals.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-015</strong></td>
<td>Failed refund</td>
<td>Given a refund is in Processing,<br />
when the bank result shows a failure,<br />
then the refund becomes Unsuccessful then Void, the parent is asked to update the account, and a new request is created after the update.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-016</strong></td>
<td>K2 year-end</td>
<td>Given the K2 cohort includes one child marked as repeating K2,<br />
when Finance creates year-end refunds,<br />
then a refund request is created for every graduating child except that child.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-017</strong></td>
<td>GSII month check</td>
<td>Given Finance selects September,<br />
when a GSII file for August is uploaded,<br />
then the upload is rejected with the file month and the selected month.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-018</strong></td>
<td>GSII profile difference</td>
<td>Given the GSII amount differs from the child profile,<br />
when reconciliation runs,<br />
then the difference is listed and the profile changes only when a user accepts the GSII value.</td>
</tr>
<tr class="odd">
<td><strong>AC-FEE-019</strong></td>
<td>Reject reason</td>
<td>Given a request in Finance approvals,<br />
when the approver rejects it without a reason,<br />
then the system does not allow it.</td>
</tr>
<tr class="even">
<td><strong>AC-FEE-020</strong></td>
<td>Closed month</td>
<td>Given September is closed,<br />
when a user tries to void a September invoice,<br />
then the system blocks it and asks for a credit note in an open month.</td>
</tr>
</tbody>
</table>
