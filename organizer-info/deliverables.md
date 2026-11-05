# Deliverables

All submission materials must be in English (Official Rules §4, Language Requirements).

## Round 1 (open to all). Due November 15, 2026, 11:45 pm PT (Mon 16 Nov 2026, 18:45 Sydney)

"You do not need a NAS for Round 1. You also do not need a code repo link or a demo video. Submit these items on the Hackathon Website by Sunday, November 15, 2026 at 11:45 pm PT" (overview page).

### 1. Project Proposal (PDF)

- **Format:** a separate PDF file, **no larger than 1 MB** (overview page; the Rules do not state a PDF size limit).
- **Word limit:** "The ten substantive responses must not exceed 500 English words in total. Team consent declarations, member names, electronic signatures, and third-party license information are excluded from this word limit."
- **Third-party disclosure:** "Any third-party components must be identified, including their sources and applicable licenses." (overview). The Rules add: "The Proposal must identify third-party components, their sources and applicable licenses, and any external services and data flows." (§4, Third Party Integrations)

#### The 10 questions, verbatim

Two official versions are published with slightly different wording. The Rules prevail if they conflict (§11).

**Official Rules version** (https://ugreenhackathon.devpost.com/rules, §4 "Round 1 Submission Requirements"):

1. One sentence: What does the Skill do?
2. Who is the target user and problem?
3. What is your proposed solution?
4. What is the Core User Flow?
5. What substantive difference does your idea offer compared with existing tools or conventional AI solutions?
6. Which UGREEN AI NAS capabilities will be used, and at which step in the workflow?
7. What was your technical approach? Describe the planned Skill workflow, supported NAS CLI capabilities, expert agent orchestration, required inputs, permissions, AI model choices, and data handling, as applicable;
8. What is the current development status? Identify what was implemented already, not yet implemented, or is pending NAS validation if selected to be a Finalist.
9. What is your final validation plan? Name two core test cases and one edge case to validate if selected as a Finalist.
10. Are there any known limitations of your Project? Describe current known limitations, technical risks, and any external dependencies.

**Overview page version** (https://ugreenhackathon.devpost.com/, "What to Submit: Round 1"):

1. What does your Skill do? (one sentence)
2. Who is your target user, and what is their problem?
3. What is your solution?
4. What is the main user flow?
5. How is your idea different from existing tools or common AI solutions?
6. Which UGREEN AI NAS features does your Skill use, and at which step?
7. What is your technical approach? (Describe the planned Skill workflow, supported NAS CLI capabilities, expert agent orchestration, required inputs, permissions, AI model choices, and data handling, as applicable)
8. What have you built so far? What is not built yet? What still needs testing on a NAS?
9. How will you test your Skill if you become a Finalist? Name two core test cases and one edge case.
10. What are the known limits, risks, or outside dependencies of your Skill?

Followed by: "Any third-party components must be identified, including their sources and applicable licenses."

### 2. Pre-test Skill Package (ZIP). The Rules call it the "ZIP Initial Skill Package".

The package must follow "the official Uliya Skill Development Standard".

**Structure**

- `SKILL.md` (**Required**): "The required entry point containing the Skill name, description, user goal, required inputs, supported CLI capabilities, expert orchestration workflow, and completion and failure handling." (Rules)
  - Frontmatter: `name`: "A lowercase, hyphenated name containing 2–64 characters." `description`: "A description of no more than 1,024 characters."
- `references/` (**Optional**): "Additional Markdown files under the references/ directory, each directly linked from SKILL.md."
- The Starter Kit also shows `README.md` as "Recommended" in the generated folder (see resources.md).

**Size and file limits**

- Rules: "The ZIP file must not exceed 10 MB for contest submission."
- Overview: "The ZIP file and uncompressed package must each be no larger than 10 MB, with a maximum of 1 MB per file and 100 files."

**Prohibited content**

- "Separate manifests, scripts, executables, binaries, and other unsupported files are prohibited. Use placeholders for configuration examples; do not include real credentials, personal data, or API keys." (overview)
- "Executable scripts must not be included in the Skill package." (Rules)
- "The package must not contain real credentials, personal data, unauthorized third-party materials, malicious code, or functionality that enables undisclosed high-risk external access. Password protection that prevents review is prohibited." (Rules)

**Required disclosures** (overview): "In SKILL.md or its linked references, disclose third-party components and open source libraries, their sources and licenses, the principal functionality developed for this Hackathon, and AI tools used and their principal uses." The FAQ adds: "You must list every AI tool you used, and how you used it, in your disclosures."

**What is NOT required in Round 1**

- "The Initial Skill Package does not need to be fully installable or operational on UGREEN AI NAS at this stage. Local test results are optional."
- "Entrants are not required to submit demo videos, runtime screenshots, test reports, public repositories, Git histories, AI conversation logs, model weights, or training datasets during Round 1."
- "Round 1 does not require a separate code repository link, or a demo link/video."

**Originality:** "You may build on an idea conceived before the Hackathon, but your submitted Skill and its core workflow must be newly developed during the Hackathon. Do not reuse previously developed Skills or submission materials."

**Also required:** "Complete and enter all of the required fields on the 'Enter a Submission' page of the Hackathon Website" (Rules §4). The specific form fields are Not stated.

## Round 2 (Finalists only). Due November 30, 2026, 11:45 pm PT (Tue 1 Dec 2026, 18:45 Sydney)

"UGREEN will invite up to 30 Finalists to Round 2 by email on November 21. Each Finalist gets a private submission link and one assigned day of remote access to a UGREEN AI NAS, between November 22 and November 28. For teams, UGREEN sends the login details to the team Representative only." Submit through the private link.

### 1. Final Skill Package (ZIP)

- "Submit the final version of the same Skill entered in Round 1 as one ZIP file. Follow the same Uliya Skill Development Standard, file structure, technical limits, and disclosure requirements specified for Round 1. The Skill must operate on your assigned UGREEN AI NAS." (overview)
- "The Skill must pass the required validation checks and successfully operate in the provided UGREEN AI NAS test environment." (Rules)
- "The Final Skill Package must install and run consistently in the assigned UGREEN AI NAS environment. It must function as shown in the video and described in the documentation." (Rules, Functionality)

### 2. Demo video

- "Provide a link to a public YouTube video of no more than 3 minutes, using English narration or complete English subtitles. Record the Skill operating on your assigned UGREEN AI NAS during your assigned testing day, and show its core workflow, key capabilities, and actual results." (overview)
- Rules: "should be less than three (3) minutes. Judges are not required to watch beyond three minutes". It "must include footage that shows the Project running in the UGREEN AI NAS test environment and narration explaining the Skill's core workflow, key capabilities, and actual results". It "must be uploaded to and made publicly visible on YouTube". It "must not include third party trademarks, or copyrighted music or other material unless the Entrant has permission".

"Do not delete your Round 1 materials."

---
Sources: https://ugreenhackathon.devpost.com/ , https://ugreenhackathon.devpost.com/rules , https://ugreenhackathon.devpost.com/resources , https://ai.ugreen.com/pages/hackathon-starter-kit . Retrieved 2026-11-03.
