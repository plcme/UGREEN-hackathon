# Test cases for family-emergency-archive

Not part of the Skill package. Used for PDF question 9 and for the Finalist NAS testing day. All test data must be synthetic (fake names, fake numbers, generated scans).

## Synthetic test data set

Folder `EmergencyTest/` on the NAS:

| File | Content | Purpose |
|---|---|---|
| `scans/passport_sam.pdf` | Passport for "Sam Rivera", no. ending 4821, expires today + 4 months | Expiring soon (6-month passport rule) |
| `scans/id_alex.pdf` | ID card for "Alex Rivera", expires today − 10 days | Expired |
| `docs/home_insurance_2026.pdf` | Home insurance policy, renewal today + 200 days | Found (household) |
| `docs/scan_0042.pdf` | Life insurance policy for Sam, file name gives no hint | Found only by Step 5 semantic search |
| `docs/broken.pdf` | Corrupted PDF | Not checked, never Missing |
| `docs/lease_2026.pdf` | Tenancy agreement, start date 2026-03-01, no photos near that date | Related rule adds "Condition photos" → Missing |
| Photo `IMG_2231.jpg` | Phone photo of Alex's health insurance card | Found via photo OCR (Step 4) |
| `medical/checkup_mia_2025.pdf` | Child check-up report | Medical item Found, no interpretation |
| (none) | No will for either adult | Missing |

Household: Sam (adult), Alex (adult), Mia (child, 8).

## Core case 1: first full check

- **Input**: "Are our family's important documents complete? It's me (Sam), Alex and our daughter Mia." Folders: `EmergencyTest/`. Photos: yes.
- **Expected**:
  - Asks only for the missing inputs, then confirms folders before searching.
  - Report lists Alex ID card Expired, Sam passport Expiring soon, both wills Missing, home insurance Found, life insurance Found with `scan_0042.pdf` as evidence, Alex health insurance Found from the photo, `broken.pdf` under Not checked.
  - "Condition photos (because a lease was found)" appears as Missing.
  - Only last 4 digits of numbers are shown (••••4821).
  - No file is changed before Step 7.

## Core case 2: archive actions and a repeat run

- **Input**: after case 1, the user chooses 7a, 7b and 7c with destination `EmergencyTest/Archive`.
- **Expected**:
  - Each action shows what will change and waits for approval (`waiting_approval`).
  - Folders created only for Missing items (for example `Archive/Sam/Legal`, `Archive/Alex/Legal`); found files tagged `emergency-archive`; a new dated index note saved and verified.
  - **Repeat run** the same day: existing folders and tags are reported as skipped, a second index is saved without overwriting the first, and the report is unchanged.

## Edge case: nothing to find, then a failure

- **Input A**: confirmed folder contains no documents or images.
- **Expected A**: reports that nothing was found in the confirmed folder, suggests checking the folder choice, stops, and does not search other folders.
- **Input B**: photo step fails (photo service unavailable) and the user declines approval for 7a.
- **Expected B**: photo-based items are marked Not checked (not Missing); the report is still delivered; 7a is treated as cancelled and the user is told nothing was changed.
