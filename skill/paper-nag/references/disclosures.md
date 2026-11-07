# Disclosures

## What this Skill does with data

- Reads files and, if the user agrees, recognized text in photos, only inside folders the user confirms.
- Reads photo location data, at country level only, if the user explicitly allows the optional location check; used only to suggest the country of residence and recent trips for the user to confirm.
- Writes only after the user chooses an action and approves it: creates folders for missing items, adds the tag `emergency-archive` to found documents, and saves a new Markdown index note. It never deletes, moves, renames or overwrites files.
- Uses only NAS capabilities delegated to the registered experts `file-agent`, `document-agent`, `photo-agent` and `knowledge-agent`. The Skill itself makes no network requests and sends no data to external services.
- Shows and saves only the last 4 characters of identity and policy numbers.

## Third-party components and sources

| Component | Source | License | Use |
|---|---|---|---|
| Checklist structure (four sections: identification, financial and legal, medical, contacts) | Emergency Financial First Aid Kit, FEMA and Operation HOPE, ready.gov | U.S. government public information | Inspiration for the category structure only; items were rewritten and made country-neutral |
| uliya-skill-kit 0.7.3 | UGREEN Hackathon Starter Kit | UGREEN SkillHub User Agreement | Skill format rules and static checker; not included in this package |

No open source libraries, scripts, binaries or external datasets are included.

## Developed for this Hackathon

All files in this package (the workflow, checklist, status rules, report template and disclosures) were written during the UGREEN Hackathon 2026.

## AI tools used

| Tool | Principal use |
|---|---|
| Claude Code (Anthropic) | Research on the capability catalog and Skill best practices; drafting the Skill files and the proposal answers under the entrant's direction; running the kit's static checker |
| Gemini (Google) | Idea brainstorming |
| Cursor agent (Grok) | Compiling the official hackathon rules and dates into notes |

The project idea, target user, checklist scope and product decisions were made by the entrant, Tianyi Tong (Coda).
