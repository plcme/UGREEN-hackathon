# Proposal (Round 1 PDF)

- `answers.json`: the 10 answers (source of truth). 470 words in total; limit is 500.
- `proposal-draft.pdf`: rendered draft (A4, 2 pages, under 100 KB; limit is 1 MB).
- Rebuild: `python3 tools/build.py answers.json proposal.html && node tools/render.js $PWD/proposal.html $PWD/proposal-draft.pdf` (needs Playwright with Chromium).

Before submitting: add team member names and the Representative, rewrite answers in the team's own words (the organizers' FAQ recommends writing PDF answers yourselves), and keep the AI tools disclosure accurate.
