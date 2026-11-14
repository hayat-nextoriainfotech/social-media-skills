# Security

This repository holds instructions (skills) and manifests only. It contains no code that runs on your machine apart from `.github/scripts/check.py`, a lint script used by CI (not part of the plugin), and no keys or tokens. The bundled connector signs in with OAuth on the PersonaXpand side.

## Reporting a problem

Please use GitHub's **Report a vulnerability** button (Security tab) on this repository for anything sensitive, such as a prompt that makes a skill send a reply without approval, follow instructions from an inbox message, or reveal data it shouldn't. For everything else, open an issue.

Include the skill name, the exact prompt or message text, what happened and what you expected.

## Design rules we hold ourselves to

- Text from other people (comments, DMs, names, links) is data, never instructions.
- Nothing is posted, scheduled or sent without the user's yes to the exact text.
- No secrets in the repository; CI scans every change.
