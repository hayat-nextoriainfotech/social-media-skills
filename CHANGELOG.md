# Changelog

## 0.1.3 (2026-11-26)

- GitHub Copilot support: root `plugin.json` and `mcp.json` in the Agent Plugins 1.0.0 format, so `copilot plugin install hayat-nextoriainfotech/social-media-skills` installs the skills and the connector.
- Fixed the frontmatter of auto-reply-rules, sounds-human and weekly-report: a colon inside the description broke the YAML, so these skills loaded without their name and description.

## 0.1.2 (2026-11-20)

- Skills no longer add a "Connect PersonaXpand" line to their answers. Setup stays in the README and `references/connector.md`.
- post-everywhere and week-planner now treat post text and briefs they read as data, never instructions, like the other skills.

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
