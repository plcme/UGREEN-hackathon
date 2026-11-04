# Brainstorm brief (paste this whole file into Gemini)

You are helping a 1–3 person team brainstorm ideas for a hackathon. Generate ideas only; do not write implementation files.

## The hackathon
UGREEN (a consumer electronics brand that makes chargers and home NAS devices) runs "UGREEN Hackathon 2026 on AI NAS: Bring Your Skills to UGOS". A NAS is a home/small-office storage server; users control it through a mobile app or web UI and a built-in AI chat assistant called **Uliya** (local LLM on the NAS). Target users are people who only use the app and never use SSH or code.

A **Skill** is a Markdown file (SKILL.md) that tells Uliya how to complete a workflow. It contains NO code and NO scripts. It can only delegate steps to registered expert agents, each backed by a fixed set of NAS operations. Every step must use the real output of the previous step. Any delete / move / overwrite / write / external sharing must ask the user for confirmation. If nothing is found, the Skill must say so and stop. No external APIs, no network calls, no credentials.

## Available capabilities (the ONLY things a Skill can do)
- **file-agent**: find/list/read files by type, size, date; checksums; dedupe scan; tags (read/add/remove); organize-by-type/date/size/resolution/duration plans; move, copy, rename, mkdir, delete, write a text file (writes need confirmation).
- **document-agent**: page count, metadata; Q&A over documents (extraction, comparison, summary, outline, locate content, time period, condition); structured extraction with schemas: invoice, contract, expense, receipt, medical-report, purchase_order, mixed_reconciliation; reconcile documents; translate; writing (outline, polish, rewrite, expand, compress, draft, minutes).
- **knowledge-agent**: look up official UGREEN docs; audio transcription (multiple speakers); collect evidence across files; save text as a note/file.
- **photo-agent**: list albums, person albums, object albums; search photos by person, pet, location, object, text inside the photo (OCR), time, folder, camera model, lens; read photo metadata; OCR an image; ask a local vision-language model any question about one image; create albums (manual, smart/conditional by location/person/camera/lens/focal length/aperture/ISO/OCR text, anniversary, baby album), timeline.
- **media-agent**: search movies/TV/music library, play/pause, find and download subtitles.
- **security-monitor-agent** (read-only): list cameras; event timeline filtered by Human / Face / Vehicle / Pet / Package, known vs stranger; resolve identity; get snapshot/clip evidence; list faces and license plates.
- NOT available: internet/APIs, calendar/reminders, email/messaging, scheduled jobs, smart-home control, databases.

## Ideas that are already taken (official examples — do not propose these as-is)
Download-folder dedupe and archive; yearly photo album by person/place; abnormal camera events query; find subtitles; music search; contract + invoice audit; meeting recording to minutes.

## Judging (4 criteria, equal weight)
1. User Value: clear real problem, clear workflow, meaningful result.
2. Innovation & Differentiation: new function/interaction/workflow vs common AI tools and existing apps (Google Photos, iCloud, Immich, Paperless-ngx, ChatGPT file upload). Separate prizes for the 2 most creative.
3. Technical Quality: sound orchestration, correct use of capabilities, permissions, error handling.
4. AI NAS Fit: makes meaningful use of local data, storage, compute and privacy — not something that could run anywhere.

## What we want
- Users: people with a specific job, role, or life situation (not generic "everyone"), who keep lots of private files on a NAS and would never upload them to the cloud. Think beyond the obvious; consider families, caregivers, small businesses, creators, hobbyists, landlords, students, etc.
- Each idea MUST chain at least 2 of the agents above.
- Strong preference for ideas where privacy is the reason the NAS wins.
- One optional inspiration (do not overfit): the team previously built "TrackBite", a family meal recommender that keeps a profile per family member (allergies, diet restrictions), reads health reports, and always asks a human to confirm risky decisions.

## Output format
Give **15 ideas**, as a table with columns:
`#` | name (lowercase-hyphenated) | one-sentence pitch | target user & the specific pain | step-by-step flow, naming the agent used in each step and where the user confirms | why NAS + privacy matters | what is new vs existing tools | self-score 1–5 for each of the 4 criteria | biggest risk.
Then list your top 3 with a short justification. Be concrete and avoid vague ideas.
