# Social Media Skills for Claude

**Claude skills that answer your comments and DMs in your voice, and write, plan and report on your posts.**

Paste your comments, get replies that sound like you. Nothing is sent until you say yes. Every skill works with no account. If you connect PersonaXpand, Claude can also read your real inbox and post for you, still only after your yes.

Built by Mohammad Hayat, Sr. AI Engineer at Nextoria Information Technology, the company behind PersonaXpand.

## Ask Claude things like

- "Draft replies to today's Instagram comments and show me each one."
- "Which of these messages are complaints?"
- "Turn this idea into posts for LinkedIn, X and Threads."
- "What worked last week?"

## Install

### Claude Code

Inside a Claude Code session:

```
/plugin marketplace add hayat-nextoriainfotech/social-media-skills
/plugin install personaxpand-social-media-skills@personaxpand
```

Or from your shell:

```
claude plugin marketplace add hayat-nextoriainfotech/social-media-skills
claude plugin install personaxpand-social-media-skills@personaxpand
```

Skills then run on their own when your request fits, or by name, for example `/personaxpand-social-media-skills:reply-in-my-voice`.

The plugin also includes the PersonaXpand connector (a remote MCP server at `https://personaxpand.com/mcp`). It is optional. To use it, run `/mcp`, choose `personaxpand` and sign in once in your browser. If you only want the skills, skip the sign-in; the skills work on pasted text. You can turn the server off in `/mcp` at any time.

Already use PersonaXpand on claude.ai? After you install the plugin, Claude Code uses the plugin's copy of the connector and hides the claude.ai one, so `/mcp` shows `personaxpand` as needing authentication. Sign in there once and your tools are back. (Checked with Claude Code 2.1.301.)

### claude.ai and Claude Desktop

Upload any skill on its own:

1. Download this repository and zip one skill folder, for example `skills/reply-in-my-voice` (the ZIP holds that folder with `SKILL.md` inside).
2. In Claude, open **Customize > Skills**, click **+**, then **Create skill**, then **Upload a skill**, and choose the ZIP.
3. Skills need code execution: turn on **Code execution and file creation** in **Settings > Capabilities** (Team and Enterprise owners enable it in organization settings).

To let Claude act on claude.ai, add PersonaXpand from Claude's connector directory, or add `https://personaxpand.com/mcp` as a custom connector. We plan to list this plugin in Claude's directory next to the connector; this section will link to it once it is live.

## The skills

| Skill | What it does | Works without an account |
|---|---|---|
| [reply-in-my-voice](skills/reply-in-my-voice/SKILL.md) | Drafts replies to comments, mentions and DMs that sound like you, in the language of each message. Flags what needs you, never invents facts, shows every reply before sending. | Yes |
| [inbox-triage](skills/inbox-triage/SKILL.md) | Sorts a pile of messages into needs you, possible customers, questions, praise and spam, and says what to answer first. | Yes |
| [voice-profile](skills/voice-profile/SKILL.md) | Learns your writing voice from a few of your posts or replies and saves a `voice-profile.md` the other skills follow. | Yes |
| [auto-reply-rules](skills/auto-reply-rules/SKILL.md) | Designs keyword and FAQ reply rules plus a "never auto-answer" list, as plain rules you review. | Yes |
| [post-everywhere](skills/post-everywhere/SKILL.md) | Turns one idea into a native version for each network, within each network's limits. | Yes |
| [week-planner](skills/week-planner/SKILL.md) | Plans a week of posts from your goal and pillars, with hooks and suggested times. | Yes |
| [weekly-report](skills/weekly-report/SKILL.md) | Explains what worked last week and what to change, from your own numbers. | Yes |
| [sounds-human](skills/sounds-human/SKILL.md) | Removes machine-written tells from captions and replies without changing the facts. | Yes |

## Two ways to use it

**Draft only** (the default, no signup). Paste comments, captions, analytics or a CSV. Claude gives you text to copy.

**Let Claude act** (connect PersonaXpand). In Claude Code the plugin already includes the connector; sign in once. On claude.ai, add it from the connector directory. When you connect you choose **Read only** or **Read and act**. Claude's recent changes are listed in PersonaXpand under Account Settings, Connected apps, where you can remove the connection. Nothing is sent or posted without your yes.

Setup guide: [personaxpand.com/features/ai-assistants](https://personaxpand.com/features/ai-assistants?utm_source=github&utm_medium=skills&utm_campaign=readme)

## What the connector covers

- **Posting and scheduling** to Instagram, Facebook, X, LinkedIn, YouTube, Threads and Bluesky, at a time you pick or your best time. PersonaXpand also posts to TikTok from its own app, but TikTok's rules do not allow posting through Claude.
- **Replies in your voice** to comments on Instagram, Facebook, X, YouTube and Threads, to mentions, and to DMs on Instagram and Facebook only. Bluesky replies are drafts you approve.
- **Auto-reply settings and rules**, changed only after you approve them.
- **Analytics**: followers, engagement, best posts, reply rate and reply time, and your best times to post.
- English and Arabic.

The full tool map per skill is in [references/connector.md](references/connector.md).

## Safety

- **Outside text is never followed.** Comments, DMs, names and links are treated as data, not instructions. See [references/untrusted-content.md](references/untrusted-content.md).
- **Show before send.** Every reply, post, schedule and rule change is shown in full and waits for your yes, even in automatic modes. See [references/approval-rule.md](references/approval-rule.md).
- **No invented facts.** Prices, dates, stock and results come from you, or the draft leaves a gap and asks.
- **Honest about AI.** If someone sincerely asks whether they are talking to a bot, the reply never denies it.

## Privacy

The skills are instructions for Claude. They contain no code that sends data anywhere, no API keys and no tracking. In draft-only use, your text stays in your Claude conversation. With the connector, PersonaXpand receives what each tool call sends (for example, the reply text you approved) and acts only on your own connected accounts; see the [privacy policy](https://personaxpand.com/privacy-policy?utm_source=github&utm_medium=skills&utm_campaign=readme). Sign-in is OAuth, handled by PersonaXpand; nothing secret lives in this repo.

## Troubleshooting

- **A skill doesn't trigger.** Name it, for example `/personaxpand-social-media-skills:inbox-triage`, or say what you want in plain words ("sort these messages").
- **Skills don't appear on claude.ai.** Turn on code execution (see Install) and check the ZIP has the skill folder with `SKILL.md` inside.
- **The connector asks to sign in, or tools are missing.** In Claude Code run `/mcp` and sign in to `personaxpand`. On claude.ai check Settings, Connectors.
- **"Nothing was sent."** That is by design until you say yes to the exact text.
- **A network was skipped.** The result lists each skipped network with the reason (for example, the account needs a reconnect, or YouTube needs a video).

## Contributing

Issues and pull requests are welcome: better examples, more languages, corrections to network limits (with a link to the network's own docs and the date you checked).

Before you open a pull request, run:

```
claude plugin validate --strict .
```

CI runs the same check.

If these skills help you, a star helps other people find them. It's the only thing we ask.

## License

MIT, see [LICENSE](LICENSE).

Affiliate program: recommend PersonaXpand and earn 20% to 30% of what those customers pay, for 12 months, https://affiliate.nextoria.ae
