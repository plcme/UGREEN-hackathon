# Skill development notes

- Package source: `skill/paper-nag/` (only SKILL.md and references/*.md — no README inside the package; the kit checker rejects it).
- Static check (uliya-skill-kit 0.7.3, not committed):
  `node <kit>/scripts/check-skill.mjs skill/paper-nag`
  Last result (2026-11-04, under the old name family-emergency-archive): `static-pass`, 0 errors, 0 warnings. Re-run after the rename to paper-nag is pending.
- Build the submission ZIP from inside `skill/`: `zip -r ../deliverable/paper-nag.zip paper-nag` (about 20 KB, 4 files).
- Test cases: [test-cases.md](test-cases.md).
