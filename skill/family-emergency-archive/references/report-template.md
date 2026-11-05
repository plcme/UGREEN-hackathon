# Readiness report template

Use this exact layout in Step 6 and for the saved index in Step 7c. Keep wording short. Show only the last 4 characters of any document number.

## Status rules

| Status | Rule |
|---|---|
| Found | A real file path holds this document for this member and it is not expired or expiring soon. |
| Expired | Expiry date is before today. |
| Expiring soon | Expiry date is within the expiry window (default 90 days; passports 6 months). |
| Needs review | Holder unclear, conflicting dates, or more than one candidate file. |
| Missing | Steps 3–5 finished for this item and nothing matched. |
| Not checked | A needed step failed or was cancelled, or the file was unreadable. |

Items added by a related-document rule show the reason in brackets.

Order inside each member: Expired, Expiring soon, Missing, Needs review, Not checked, Found.

## Layout

```markdown
# Family Emergency Archive — readiness report (YYYY-MM-DD)

Checked folders: [list]
Photos included: yes/no
Expiry window: 90 days (passports 6 months)

## Summary
| Member | Found | Expired | Expiring soon | Missing | Needs review | Not checked |
|---|---|---|---|---|---|---|
| [member] | n | n | n | n | n | n |

## Most urgent
1. [member] — [item] — Expired on YYYY-MM-DD — [file path]
2. ...

## [Member name]
| Item | Status | Expiry | Evidence |
|---|---|---|---|
| Passport | Expiring soon | YYYY-MM-DD | [file path], no. ••••1234 |
| Will | Missing | — | — |
| Health insurance policy | Found | YYYY-MM-DD | [file path] |
| Condition photos (because a lease was found) | Missing | — | No photos within 14 days of lease start YYYY-MM-DD |

## Household
| Item | Status | Expiry | Evidence |
|---|---|---|---|

## Not checked
- [file path] — [reason]

## Suggested next steps
- Renew or replace expired and expiring documents.
- Scan or photograph missing documents into the matching folder, then run the check again.

This report organizes documents stored on this NAS. It is not legal, medical or financial advice.
```

## Example

Input situation: two adults (Sam, Alex) and one child (Mia); Sam's passport scan expires in 4 months; no will for either adult; Alex's insurance policy is a phone photo.

Output excerpt:

```markdown
## Most urgent
1. Sam — Passport — Expiring soon (YYYY-MM-DD, within 6 months) — Documents/scans/passport_sam.pdf
2. Sam — Will — Missing
3. Alex — Will — Missing

## Alex
| Item | Status | Expiry | Evidence |
|---|---|---|---|
| Will | Missing | — | — |
| Health insurance policy | Found | YYYY-MM-DD | Photos/2026/IMG_2231.jpg (photo, recognized text) |
```
