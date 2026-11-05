# Skill development notes

- Package source: `skill/family-emergency-archive/` (only SKILL.md and references/*.md — no README inside the package; the kit checker rejects it).
- Static check (uliya-skill-kit 0.7.3, not committed):
  `node <kit>/scripts/check-skill.mjs skill/family-emergency-archive`
  Last result (2026-11-04): `static-pass`, 0 errors, 0 warnings.
- Build the submission ZIP from inside `skill/`: `zip -r ../deliverable/family-emergency-archive.zip family-emergency-archive` (about 20 KB, 4 files).
- Test cases: [test-cases.md](test-cases.md).
