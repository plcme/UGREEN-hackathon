---
name: family-emergency-archive
description: Household emergency-document readiness check for UGREEN NAS. Shows, for each family member, which essential records (identity, insurance, property, legal, medical, emergency contacts) are already stored on the NAS, which are missing, which are expired or expiring soon, and prepares a local archive index with folders for the gaps. Use when the user asks whether the family's important documents are complete, wants an emergency binder or document checklist, asks what is missing or about to expire, or wants family records organized for an emergency.
---

# Goal

Give the user a clear, private answer to one question: "If something happened tomorrow, could my family find every essential document on our NAS?"

The result is a readiness report per household member that marks every checklist item as **Found**, **Missing**, **Expired**, **Expiring soon**, **Needs review**, or **Not checked**, with the real file path as evidence for every Found item. After the user confirms the report, the Skill can optionally create folders for missing items, tag the found documents, and save a dated archive index on the NAS.

Scope and limits:

- Reads only the folders the user confirms. All processing stays on the NAS; nothing is sent outside.
- Read-only until the user explicitly chooses a write action in Step 7. Never deletes, moves, renames, or overwrites files.
- Organizes and reports only. It does not give legal, medical, financial, or immigration advice and does not interpret medical results.

# Required input

Collect these before Step 2. Ask only for what is missing, in one short message, and wait (`waiting_user`).

1. **Household members**: names or roles (for example "me, my wife Anna, son Leo"). Do not ask for ages; age-based rules use the birth date found in each member's identity documents in Step 3.
2. **Search folders**: the NAS folders to check. Offer the user's home folder from Step 1 as the default; the user may add or remove folders. Never search outside the confirmed folders.
3. **Include photos**: yes or no. If yes, photographed paper documents in the photo library are also checked.
4. **Checklist**: the default list in [references/document-checklist.md](references/document-checklist.md). Show the category names and let the user remove items that do not apply or add their own.
5. **Expiry window**: default 90 days; passports use 6 months because many countries require six months of validity for entry.
6. **Today's date**: use the current date known to the assistant. If it is not available, ask the user.
7. **Country of residence**: ask the user; use it only to name local equivalents of checklist items (for example the national health card). Never guess it. If the user is unsure, offer the optional photo location check in Step 1.
8. **Situation (optional)**: if the user describes an event such as a hospital stay, a move or travel, offer the matching pack in [references/situation-packs.md](references/situation-packs.md) instead of the full checklist.

The archive destination folder is needed only if the user later chooses a write action in Step 7; ask for it then.

# Generation-time capability evidence

- `file-workflow` → `file-agent`
- `ug-filesystem` → `file-agent`
- `ug-filemgr` → `file-agent`
- `ug-document` → `document-agent`
- `ug-photo` → `photo-agent`
- `ug-knowledge` → `knowledge-agent`

# Workflow

Copy this checklist into the conversation and update it as each step finishes:

```text
Emergency archive progress:
- [ ] Step 1: Confirm search folders (and photo locations, only if the user allows)
- [ ] Step 2: Find candidate documents
- [ ] Step 3: Identify and read documents
- [ ] Step 4: Check photographed documents (if included)
- [ ] Step 5: Add related documents and search again for missing items
- [ ] Step 6: Build and confirm the readiness report
- [ ] Step 7: Optional archive actions (only those the user chooses)
```

Orchestration rules:

- Run one step at a time. Each downstream step uses only the real result returned by the upstream delegation (file paths, extracted fields, OCR text). Never invent paths, names, dates, or documents.
- Before sending a delegation, replace the descriptive references in its instruction (confirmed folders, member names, file list from an earlier step) with the real values. If a required value is unavailable, stop the dependent step and report why.
- Each delegation is self-contained: it states the scope, what to return, and that the expert must not change any file unless the step says so.
- Mask identity numbers everywhere: show only the last 4 characters.

## Step 1: Confirm search folders

```text
delegate --target file-agent --instruction 'Return the home folder path of the current NAS user. Read only: do not list, open, move or change any file.'
```

Show the returned path as the default search folder and collect the Required input. Continue only after the user confirms the folders.

**Optional photo location check (off by default).** Offer it in one sentence: "I can look at the countries where your photos were taken to suggest your country of residence and recent trips. This reads photo location data only. Allow it?" Run it only after the user explicitly says yes; otherwise skip it and do not mention it again.

```text
delegate --target photo-agent --instruction 'Within the user-confirmed folders only, group photos by the country where they were taken, using location data at country level. Return for each country: photo count, earliest and latest photo date, and the photo count in the last 12 months. Return country names and counts only; do not return addresses, coordinates, file paths or people. Read only: do not edit, move, tag or add photos to albums.'
```

Use the result only as suggestions that the user must confirm:

- The country with most photos over time is suggested as the country of residence.
- Countries with photos in the last 12 months, other than the country of residence, are suggested as recent trips. If the user confirms travel, add the travel items from [references/situation-packs.md](references/situation-packs.md) (passport validity, visas, travel insurance) to the checklist.
- If no photo has location data, say so and ask the user directly.

## Step 2: Find candidate documents

```text
delegate --target file-agent --instruction 'In the user-confirmed search folders only, find all files of type documents and image, searching subfolders. Return for each file: full path, file type, size and last modified time. Return at most 500 files, newest first, and say whether more exist. Read only: do not open, move, rename, tag or delete any file.'
```

If the result is empty, tell the user that no documents or images were found in the confirmed folders, suggest checking the folder choice, and stop. Do not widen the search on your own.

## Step 3: Identify and read documents

Send the document files from Step 2 (PDF and office documents) in batches of up to 100 files.

```text
delegate --target document-agent --instruction 'Read only the files listed in this request. For each file, identify the document type using these categories: identity, education and work, social insurance and retirement, banking and tax, insurance, home and utilities, vehicles, major purchases and contracts, legal, medical, emergency contacts, other. Extract: document type (for example passport, degree certificate, employment contract, vehicle purchase invoice, will), holder name, issuer, document number showing only the last 4 characters, issue date, expiry, renewal or warranty end date, and the page used as evidence. Also extract: birth year of the holder from identity documents (year only); job title from employment contracts and resumes; the item and its vehicle or property from purchase invoices, registrations and warranties; lease start and end dates and whether the user is tenant or landlord. For medical reports return only report date, facility and report type; do not interpret results. Mark any field you cannot read as unknown and list unreadable files separately with the reason. Do not modify any file.'
```

Keep the list of unreadable files; their checklist items become **Not checked**, never Missing.

## Step 4: Check photographed documents (only if photos are included)

```text
delegate --target photo-agent --instruction 'Within the user-confirmed folders only, search photos whose recognized text contains any of these keywords: passport, identity card, driver licence, birth certificate, marriage certificate, residence permit, insurance policy, policy number, deed, vehicle registration, will, power of attorney, vaccination, medical report. For up to 50 matching photos, run text recognition and return for each: file path, likely document type, holder name if visible, expiry date if visible, and the recognized text snippet used as evidence. Read only: do not edit, move, tag or add photos to albums.'
```

If no photo matches, record "no photographed documents found" and continue with Step 5. If this step fails, mark photo coverage as Not checked and continue.

## Step 5: Add related documents and search again for missing items

First apply [references/related-documents.md](references/related-documents.md): documents already found imply other documents (for example a lease implies dated condition photos of the property). Add those items with their reason.

For every lease found, check that dated condition photos exist, using the lease start and end dates from Step 3:

```text
delegate --target photo-agent --instruction 'Within the user-confirmed folders only, find photos taken from 14 days before to 14 days after each of these lease dates: the lease start and end dates extracted from the found leases. For each date return the number of photos, the folders or albums they are in, and up to 5 example file paths. Read only: do not judge the condition of the property, and do not edit, move, tag or add photos to albums.'
```

Then match all results against the checklist for each member. For every item still unmatched, run one semantic search on document contents so that a file with an unusual name is not reported as missing:

```text
delegate --target document-agent --instruction 'Within the user-confirmed search folders only, use semantic lookup to find documents that are any of the following items: the unmatched checklist items with the member each one belongs to. For each item return the best matching file path, holder name, expiry date if present, and a one-line evidence quote, or state that no match was found. Return at most 3 candidates per item. Read only: do not modify any file.'
```

## Step 6: Build and confirm the readiness report

Classify every checklist item for every member, using the rules and the exact layout in [references/report-template.md](references/report-template.md):

- **Found**: a real file path holds this document for this member and it is not expired.
- **Expired**: the expiry date is before today.
- **Expiring soon**: the expiry date falls within the expiry window.
- **Needs review**: holder unclear, dates conflict, or several candidates match.
- **Missing**: Steps 3–5 completed for this item and no file matched.
- **Not checked**: a needed step failed, was cancelled, or the file could not be read.

Show the report, then ask the user to confirm or correct it (`waiting_user`). Apply corrections to the report only; they do not change files.

## Step 7: Optional archive actions

Offer these three actions and run only the ones the user picks. Ask for the archive destination folder first. Each action changes the NAS, so the platform asks for approval (`waiting_approval`); show exactly what will be created or changed before it runs.

**7a. Folders for missing items**: one folder per member and category, only for Missing items.

```text
delegate --target file-agent --instruction 'Inside the user-approved archive destination folder, create the following folders only if they do not already exist: the confirmed list of member and category folders for missing items. Create parent folders as needed. Do not create, move, rename or delete anything else. Return the path of each folder created and each folder that already existed.'
```

**7b. Tag found documents** with the tag `emergency-archive`.

```text
delegate --target file-agent --instruction 'Look up the file tag named emergency-archive and create it if it does not exist. Then add this tag to the following user-approved files only: the confirmed list of Found document paths. Skip files that already have the tag. Do not move, rename or delete files. Return the files tagged, the files skipped, and any failures.'
```

**7c. Save the archive index**: the confirmed report as a Markdown note.

```text
delegate --target knowledge-agent --instruction 'Save the following confirmed readiness report text as a new Markdown note in the user-approved archive destination folder, with the file name hint Emergency Archive Index followed by the current date. Create a new file; never overwrite an existing index. Return the saved file path and whether the save was verified.'
```

Running the Skill again later is safe: existing folders and tags are skipped, and each run saves a new dated index, so earlier reports are kept for comparison.

# Completion and failure

Report a business result only after the delegated expert returns `completed`. Handle every delegation state explicitly:

| State | What to do |
|---|---|
| `completed` | Use only the returned data. For write actions, report the verified paths and counts. |
| `waiting_user` | Relay the expert's question in plain words, wait for the answer, then resume the same step. |
| `waiting_approval` | Show exactly what will be created or changed (paths and counts) and wait. If the user declines, treat that action as cancelled and keep the read-only report. |
| `cancelled` | Stop that step and any step that depends on it. Tell the user nothing was changed by the cancelled step and offer the report built so far. |
| `failed` | Name the step and the reason. If Step 1 or Step 2 fails, stop: there is nothing to check. If Step 3, 4 or 5 fails, continue with the other steps and mark affected items Not checked. If a Step 7 action fails, report which items succeeded and which did not; never retry a write automatically. |

Empty and partial results:

- No results in Step 2: report it and stop. Never search folders the user did not confirm.
- Partial results (more than 500 files, unreadable files, a failed batch): say exactly what was not checked. Items that could not be checked are Not checked, never Missing.
- Never claim a document exists without a real file path, and never claim a folder, tag or note was created before the expert returns `completed`.

Finish with a short summary: counts per status, the three most urgent items (expired first, then expiring soon, then missing legal or identity documents), and the path of the saved index if one was saved.

# Privacy and disclosures

- Reads document text and, when the user includes photos, recognized text in photos, because emergency records are often scanned or photographed paper. Only user-confirmed folders are read.
- Reads photo location data at country level only if the user explicitly allows the optional check in Step 1, to suggest the country of residence and recent trips. Addresses, coordinates and people are never returned or saved.
- All processing uses NAS capabilities; no data is sent to external services by this Skill.
- Full identity numbers are never shown or saved; only the last 4 characters.
- Third-party components, AI tools used, and work developed for this Hackathon are listed in [references/disclosures.md](references/disclosures.md).
