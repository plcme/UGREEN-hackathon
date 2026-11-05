# Resources

## Hackathon Starter Kit (UGREEN Skill Developer Package)

URL: https://ai.ugreen.com/pages/hackathon-starter-kit

The Devpost overview page says: "It has the tools and technical docs you need. **You must use this package to build your Skill.**" The kit describes itself this way: "This guide is for participants in the UGREEN NAS Skill Hackathon. Use the official UGOS Skill Creation Tool with your preferred AI assistant to create skills that can be used on UGREEN NAS / Uliya."

### Starter Kit sections

1. **Read Before You Start.** "By participating in this event and using the creation tool to develop skills, you confirm that you have read and agree to":
   - [User Agreement](https://api.ugnas.com/api/system/v1/ua/agreement/page?agreementCode=skillhub-user-agreement&acceptLanguage=en-US)
   - [Privacy Policy](https://api.ugnas.com/api/system/v1/ua/agreement/page?agreementCode=skillhub-privacy-policy&acceptLanguage=en-US)
   - [Skill Content Safety and Publishing Guidelines](https://api.ugnas.com/api/system/v1/ua/agreement/page?agreementCode=skillhub-publish-audit-spec&acceptLanguage=en-US)
2. **Set Up Your Creation Environment.** "The tool currently supports WorkBuddy, Claude, and Codex. For the best development experience, we recommend using one of these assistants whenever possible. Other environments may not support all tool features." "The creation tool helps you generate skill files and check them against the relevant requirements."
3. **Install the UGOS Skill Creation Tool.** Download: [uliya-skill-kit-0.7.3-en.zip](https://cdn.shopify.com/s/files/1/0630/9416/1602/files/uliya-skill-kit-0.7.3-en.zip?v=1790578898). "Place the entire uliya-skill-kit folder in the skills directory used by your AI assistant." Then reload the assistant and ask, for example, "What can I do with this tool?" If the assistant answers using the tool, installation is complete.
4. **Think It Through Before Generating.** Define who the Skill is for, when it should be used, what result it should produce, and what requires user confirmation. Suggested prompt: "Do not generate any files yet. Help me check whether this idea is currently supported and suitable as a UGREEN NAS skill."
5. **Create a Skill.** Describe the Skill in one sentence, confirm a name (for example `download-dedup-archive`), then use "Generate the skill files according to the guidelines." and "Help me check this skill." Repeat the check until no required changes remain. Typical generated structure:
   ```
   your-skill-name/
   ├── SKILL.md         Required. Describe what it does, when to use it, how it works, and how to handle missing results or actions requiring confirmation.
   ├── README.md        Recommended. Explain in more conversational language who it is for and how to use it.
   └── references/      Optional. Supplementary documentation.
   ```
   Requirements listed in the kit:
   - Define the intended result clearly.
   - Only use capabilities actually supported on UGREEN NAS.
   - Each step must use the actual output of the previous step.
   - Ask for confirmation before deleting, moving, overwriting, or sending or sharing externally.
   - If no result is found, say so and stop.
   - No credentials, passwords, or keys.
   - "Do not include scripts, executable files, or undisclosed external downloads."
   - "Do not leave TODOs, 'TBD,' or placeholder content in the finished skill."
   - Work must be original.
6. **UGOS Skill Capability Scope.** "More capabilities will be added over time; the capabilities included in the creation-tool archive take precedence."

   | Area | What you can do | Example use case (official) |
   |---|---|---|
   | Files | Find, browse, organize, deduplicate, and tag | Deduplicate the Downloads directory, then archive files after confirmation |
   | Albums | Find photos by person, location, or time; create or organize albums | Create a travel album from photos of the beach and the children |
   | Documents | Read, answer questions, extract information, translate, and reconcile | Extract project information from contracts and invoices |
   | Knowledge | Look up official documentation, transcribe recordings, and save text | Transcribe a meeting recording into minutes and save it |
   | Video / Music | Search content, control playback, and find subtitles | Find a movie and check whether subtitles are available |
   | Surveillance | Query camera events and organize related details | Check whether there were any unusual events in the garage during a given period |

   Areas can be chained. "Every step must map to a real capability listed above."
7. **Testing Your Skill.** Check it with the creation tool, review it from a user's perspective, and test on a real device (finalists only). Common issues found during checks:
   - Name or description is incomplete or does not match the workflow
   - Unsupported capabilities
   - Missing confirmation before high-risk actions
   - Placeholders or sensitive info
   - Non-compliant file structure, size, or required document
8. **Required Compliance.** Read the Skill Content Safety and Publishing Guidelines in full. Key points:
   - The name and description must be accurate. Do not present the Skill as an official UGREEN skill.
   - No keys or tokens, and do not instruct users to run untrusted code.
   - No unauthorized access or hidden external transmission.
   - Confirm before high-risk actions.
   - Work must be original and properly licensed.

### Contents of the official tool archive (uliya-skill-kit 0.7.3, en)

This is the file listing of the official ZIP linked above, as downloaded on 2026-11-03 (37,575 bytes zipped; 35 entries):

```
uliya-skill-kit/
├── SKILL.md
├── assets/skill-template/SKILL.template.md
├── data/capability-catalog.json
├── docs/skill-development-standard.md          (the "Uliya Skill Development Standard")
├── schemas/capability-catalog.schema.json
├── schemas/check-result.schema.json
├── scripts/check-lib.mjs, scripts/check-skill.mjs   (the kit's own static checker; this is the tool, not part of a submission)
└── references/
    ├── capability-query.md, check-workflow.md, cli-capabilities.md, cli-usage-rules.md,
    ├── completion-and-errors.md, expert-orchestration.md, help.md, init-workflow.md,
    ├── runtime-authoring-lessons.md, safety-and-approval.md, skill-format.md
    └── examples/ contract-invoice-audit.md, duplicate-file-report.md, extract-conclusion-and-save.md,
                  find-pdf-and-read-metadata.md, meeting-notes-archive.md, organize-annual-photos.md,
                  query-monitor-events.md
```

Key official text from the archive:

- `docs/skill-development-standard.md`: "A Skill is a Markdown entry point describing a user-facing workflow. A capability domain groups related NAS operations. A CLI capability is a published operation family; an Action is one operation within it. A registered expert performs the real NAS work after delegation." "Use only capabilities present in the catalog. If a required step has no matching capability, state that it is unsupported; never infer support from a product name or UI label."
- `references/skill-format.md`: "`SKILL.md` begins with only `name` and `description` frontmatter. The body must state the goal, required input, capability evidence, expert orchestration, and completion/failure behavior. Optional resources are ordinary Markdown files under `references/` and must be linked directly from the root. [...] Do not add manifests, sidecars, scripts, binaries, credentials, or direct `cli.invoke` calls."
- `SKILL.md` (kit): "The parent Skill may use only `delegate --target <agent-id> --instruction '<task>'`. It must not directly execute `cli.invoke`, bypass approval, or claim NAS execution from local generation or static checks." Generated Skills must handle `completed`, `failed`, `cancelled`, `waiting_user`, and `waiting_approval`, and must record each CLI used as `- <cli> -> <agent>`.
- `assets/skill-template/SKILL.template.md` sections: Goal, Required input, Capability evidence, Expert orchestration, Completion and failure.

## Official links (from the Devpost Resources page)

| Resource | Link |
|---|---|
| UGREEN Skill Developer Package (required) | https://ai.ugreen.com/pages/hackathon-starter-kit |
| UGREEN AI NAS ("Learn what UGREEN AI NAS can do") | https://ai.us.ugreen.com/3xNZ5C |
| UGREEN UGOS | https://ai.ugreen.com/pages/operating-system |
| UGREEN Skills Hub | https://skills.ugreen.com/skill-hub/ |
| UGREEN NAS Community (teammates, help, Office Hours and AMA per the update post) | https://community.ugreen.com/nas/ |
| Technical support email | nas-support@ugreen.com |
| Support ticket (sign-in) | https://web.ugnas.com/account/login/#/login |

"UGREEN will respond to requests submitted through either channel. Product suggestions will be forwarded to the product team for review."

## Helpful skills (official list)

- Python or JavaScript/TypeScript
- Linux (Debian 12) and Docker
- LLM and AI agent tools, prompt and tool design, and REST APIs
- File, media, and document processing (OCR, metadata, and search)
- Vue or React

## NAS access for Finalists

"UGREEN will give each Finalist one assigned testing day of free remote access to a UGREEN AI NAS iDX6011 Pro (64GB), between November 22 and November 28. UGREEN will email each Finalist their login details, testing date, and setup steps. You do not need to buy a NAS or apply for access. Use the NAS only to install, test, and record your Skill for this Hackathon."

## Official updates

- 🎁 Join the UGREEN Community & Enter the Hackathon Giveaway: https://ugreenhackathon.devpost.com/updates/47352-join-the-ugreen-community-enter-the-hackathon-giveaway. Community benefits listed: official updates and resources, "Office Hours and AMA sessions for live Q&A", finding teammates, and community giveaways. Office Hours and AMA dates: Not stated on Devpost.

---
Sources: https://ai.ugreen.com/pages/hackathon-starter-kit , https://cdn.shopify.com/s/files/1/0630/9416/1602/files/uliya-skill-kit-0.7.3-en.zip?v=1790578898 , https://ugreenhackathon.devpost.com/resources , https://ugreenhackathon.devpost.com/ , https://ugreenhackathon.devpost.com/updates . Retrieved 2026-11-03.
