# Devpost project details (draft, paste field by field)

## Project name
Paper Nag

## Elevator pitch
The family paperwork assistant that nags you before an emergency does: it finds what's missing, right on your NAS.

## About the project (Markdown)

## Inspiration
Every family has one person who keeps the paperwork, and that person usually finds out a document is missing at the worst moment: at the hospital desk, during an insurance claim, or the night before a flight. Existing tools only work on what you hand them. We wanted something that asks first.

## What it does
Paper Nag checks each family member's essential documents on the UGREEN AI NAS and reports what is found, missing, expired or expiring. It reasons across documents: a car insurance policy means the purchase invoice should be kept too, new furniture means a receipt and warranty, and a claim usually needs several papers at once. Then it nags you to fill the gaps and, with your approval, prepares folders, tags files and saves a dated index.

## How we built it
Paper Nag is a Uliya Skill. It orchestrates four NAS experts in order: Files for search and gap folders, Documents for text extraction and semantic lookup, Albums for OCR on photographed papers, and File tags plus Knowledge for tagging and the index. It stays read-only until you pick an action, every write needs platform approval, and only local NAS AI is used, so sensitive data never leaves home.

## Challenges we ran into
Keeping the Skill honest: an unreadable file must show as "Not checked", never "Missing", and handwritten or blurry dates go to the user instead of being guessed. Writing related-document rules that stay country-neutral was also harder than expected.

## Accomplishments that we're proud of
The cross-document rules, and a package that passes the uliya-skill-kit 0.7.3 static check with zero errors and warnings.

## What we learned
The most useful question for family records is not "where is it?" but "what am I missing?"

## What's next for Paper Nag
Testing extraction and OCR on a real UGREEN AI NAS, country-specific checklists for markets where UGREEN sells, and scheduled re-checks together with UGREEN.

## Built with
uliya-skill-kit, UGREEN AI NAS, UGOS, Markdown

## Try it out links
(leave empty for Round 1)
