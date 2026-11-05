import json, html, sys, re
src, out_html = sys.argv[1], sys.argv[2]
a = json.load(open(src))
e = html.escape
qs = "".join(f'<section><h3><span class="n">{i}</span>{e(q)}</h3><p>{e(x)}</p>' + (FLOW if i == 4 else "") + '</section>' for i, (q, x) in enumerate(a, 1)) if False else None
FLOW = '''<div class="flow">
<div>1 Confirm members &amp; folders</div><div>2 Find files</div><div>3 Read &amp; OCR</div><div>4 Rules &amp; re-search</div><div>5 Confirm report</div><div>6 Approved actions</div></div>'''
parts = []
for i, (q, x) in enumerate(a, 1):
    parts.append(f'<section><h3><span class="n">{i}</span>{e(q)}</h3><p>{e(x)}</p>{FLOW if i == 4 else ""}</section>')
doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Family Emergency Archive - Project Proposal</title>
<style>
@page {{ size: A4; margin: 16mm 16mm 14mm; }}
body {{ font-family: "Helvetica Neue", Arial, sans-serif; font-size: 10pt; line-height: 1.42; color: #1d1d1f; }}
header {{ border-bottom: 2px solid #1a7f5a; padding-bottom: 8px; margin-bottom: 10px; }}
h1 {{ font-size: 20pt; margin: 0; color: #12583f; }}
.sub {{ color: #555; margin-top: 3px; }}
.meta {{ display: grid; grid-template-columns: auto 1fr; gap: 2px 12px; margin-top: 8px; font-size: 9.5pt; }}
.meta b {{ color: #333; }}
section {{ margin: 0 0 7px; break-inside: avoid; }}
h3 {{ font-size: 10.5pt; margin: 0 0 2px; color: #12583f; }}
.n {{ display: inline-block; min-width: 18px; padding: 0 3px; box-sizing: border-box; height: 18px; border-radius: 9px; background: #1a7f5a; color: #fff; text-align: center; font-size: 9pt; line-height: 18px; margin-right: 6px; }}
p {{ margin: 0; }}
.flow {{ display: flex; gap: 4px; margin-top: 5px; }}
.flow div {{ flex: 1; background: #e8f4ee; border: 1px solid #b7dcc8; border-radius: 4px; padding: 4px; font-size: 8pt; text-align: center; }}
.disc {{ margin-top: 10px; border-top: 1px solid #ccc; padding-top: 6px; font-size: 8.6pt; color: #333; break-inside: avoid; }}
.disc h2 {{ font-size: 10pt; margin: 0 0 3px; }}
table {{ border-collapse: collapse; width: 100%; margin: 3px 0 6px; }}
td, th {{ border: 1px solid #ccc; padding: 2px 5px; text-align: left; vertical-align: top; }}
th {{ background: #f2f2f2; }}
.todo {{ background: #fff3c4; }}
</style></head><body>
<header><h1>Family Emergency Archive</h1>
<div class="sub">Know which family documents are on your NAS, and which ones are missing, before you need them.</div>
<div class="meta"><b>Track</b><span>Automate Your Workflow</span>
<b>Skill package</b><span>family-emergency-archive.zip (SKILL.md + 5 reference files)</span>
<b>Team</b><span class="todo">TEAM MEMBER NAMES AND REPRESENTATIVE TO BE ADDED</span></div></header>
{"".join(parts)}
<div class="disc"><h2>Third-party components, external services and data flows</h2>
<table><tr><th>Component</th><th>Source</th><th>License</th><th>Use</th></tr>
<tr><td>Checklist section structure</td><td>Emergency Financial First Aid Kit, FEMA and Operation HOPE (ready.gov)</td><td>U.S. government public information</td><td>Inspiration for categories only; items rewritten and made country-neutral</td></tr>
<tr><td>uliya-skill-kit 0.7.3</td><td>UGREEN Hackathon Starter Kit</td><td>UGREEN SkillHub User Agreement</td><td>Format rules and static checker; not included in the package</td></tr></table>
External services: none. Data flow: all reading, extraction and OCR run through registered NAS experts on the user's NAS; nothing leaves the device. No open source libraries, scripts or binaries are included.
<h2 style="margin-top:6px">AI tools used</h2>
Claude Code (Anthropic): research, drafting Skill files and this proposal under the team's direction, running the static checker. Gemini (Google): brainstorming. Cursor agent (Grok): compiling official rules into notes.</div>
</body></html>'''
open(out_html, "w").write(doc)
