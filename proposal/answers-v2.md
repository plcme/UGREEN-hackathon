# Proposal answers v2 (co-written draft)

## 1. What does your Skill do? (one sentence)
Family Emergency Archive is a nudging assistant, not a filing tool: it works out which family documents should be on your NAS, chases you to store the missing ones, without data leaving home.

## 2. Who is your target user, and what is their problem?
Every household has one person who keeps the paperwork, often the same parent who set up the NAS. In an emergency, a hospital stay, an insurance claim, a lost passport, is when they find a document is missing, expired, or buried in a phone photo.

## 3. What is your solution?
The Skill reads what you have already stored and works out what it implies. A car insurance policy means the purchase invoice should be kept too; new furniture means a receipt and warranty. It reports each item as found, missing, expired or expiring, with file paths, and offers to prepare folders for the gaps.

## 4. What is the main user flow?
Tell the Skill who is in the family and where files live. It searches documents and photos, reads text in scanned papers, and applies related-document rules. You review a plain report of what is missing or expiring. If you agree, it creates gap folders, tags files and saves a dated index.

## 5. How is your idea different from existing tools or common AI solutions?
Most tools are passive: they only handle what you give them. Cloud vaults such as Trustworthy add expiry reminders, but your records live on their servers. This Skill asks the opposite question, what is missing, and reasons across documents: a claim usually needs several papers, so it checks the whole set before you need it, all on the family's own NAS.

## 6. Which UGREEN AI NAS features does your Skill use, and at which step?
Files (ug-filesystem, file-workflow): home folder, document search, gap folders. Documents (ug-document): extraction and semantic lookup inside contents. Albums (ug-photo): text search in photos, OCR, date search for condition photos. File tags (ug-filemgr): tagging. Knowledge (ug-knowledge): saving the index.

## 7. What is your technical approach?
The Skill calls four NAS experts in order, using only real results from each step. It stays read-only until the user picks an action, and every write needs platform approval. Reruns never duplicate folders or overwrite an index. Unreadable files are marked Not checked, never Missing. Only local NAS AI is used; identity numbers are masked and photo locations need explicit consent.

## 8. What have you built so far? What is not built yet? What still needs testing on a NAS?
Built: the full Skill package, which passes the uliya-skill-kit 0.7.3 static check with no errors or warnings. Still to test on a NAS: extraction and OCR quality on real scans, semantic search recall, and the approval flow.

## 9. How will you test your Skill if you become a Finalist?
Core 1: a first check of a made-up three-person family should find an expired ID, a passport within six months of expiry, missing wills, an oddly named policy found by content, and missing lease condition photos. Core 2: create folders, tag files and save the index, then rerun; existing items are skipped and a new index is saved. Edge: an empty folder ends cleanly.

## 10. What are the known limits, risks, or outside dependencies of your Skill?
Handwritten, blurry or partly covered dates go to the user to confirm, never guessed. Document requirements differ by country, so the checklist is editable. One run checks up to 500 files. A Skill only runs when called, so reminders depend on the user rerunning it; scheduled checks are a natural next step with UGREEN.
