# BLUF Communication — Agent Skill

A portable Agent Skills package for putting the bottom line first in professional and technical communication. Optimized for engineering status reports, decision requests, incident updates, code review findings, handoffs, PR summaries, and short stakeholder messages.

## What it does

- Leads with an answer, outcome, recommendation, impact, blocker, or explicit request.
- Prioritizes evidence, consequences, important uncertainty, and next actions afterward.
- Preserves source accuracy and avoids manufactured status, owners, deadlines, metrics, and verification.
- Adapts the BLUF principle to the intended medium rather than enforcing a fixed form.

BLUF is an ordering convention, not a four-part form. For four-part escalation with Situation / Background / Assessment / Recommendation, use an SBAR skill; if both are requested, one opening BLUF can precede the SBAR sections.

## Install

The archive contains one top-level `bluf-communication/` directory. Extract that folder into the skills directory used by your agent.

Codex, repository-local: `.agents/skills/bluf-communication/SKILL.md`.

Codex, user-wide: `~/.agents/skills/bluf-communication/SKILL.md`.

Claude Code, repository-local: `.claude/skills/bluf-communication/SKILL.md`.

For PowerShell from a repository root (with the archive in the current directory):

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null; Expand-Archive -LiteralPath .\bluf-communication.zip -DestinationPath .\.agents\skills -Force
```

Then request, for example: “Use `$bluf-communication` to rewrite this engineering update. Preserve all caveats and test evidence.”

## Layout

- `SKILL.md` — discovery metadata and working instructions.
- `agents/openai.yaml` — optional Codex presentation metadata.
- `references/` — detailed usage guidance and before/after examples.
- `templates/` — five reusable communication skeletons.
- `.tools/regenerate_manifest.py` — reproducible file manifest generator and checker (Python standard library only).
- `manifest.json` — SHA-256 file inventory, excluding the manifest itself.

## Maintaining the package

From the skill root, regenerate hashes with `python .tools/regenerate_manifest.py` or verify with `python .tools/regenerate_manifest.py --check`. This validates package file integrity, **not** whether a given message communicates an accurate bottom line; such evaluation requires understanding the source and audience.

## Source and provenance

The skill is an original, technical-workflow adaptation of the Bottom Line Up Front communication principle. Background: [BLUF (communication), Wikipedia](https://en.wikipedia.org/wiki/BLUF_(communication)); see also the [Agent Skills specification](https://agentskills.io/specification). The package does not copy the encyclopedia article verbatim.
