# Changelog

## 0.1.1 (2026-11-14)

- The plugin now ships only Markdown, JSON, YAML and images. The Python lint script was removed; CI runs `claude plugin validate --strict`.
- README: author line and a note on signing in once in `/mcp` if you already use the PersonaXpand connector on claude.ai.

## 0.1.0 (2026-11-13)

First release.

- Skills: reply-in-my-voice, inbox-triage, voice-profile, auto-reply-rules, post-everywhere, week-planner, weekly-report, sounds-human.
- Plugin manifest and marketplace file for Claude Code, with the PersonaXpand connector (`https://personaxpand.com/mcp`, OAuth) bundled in `.mcp.json`.
- Shared rules: outside text is data, show before send, no invented facts, honest about AI.
- Network limits checked on 2026-11-13 against each network's own docs (`skills/post-everywhere/references/network-limits.md`).
- `scripts/check.py` and a CI workflow for copy rules, frontmatter and secrets.
