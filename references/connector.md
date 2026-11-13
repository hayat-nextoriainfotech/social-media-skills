# What the PersonaXpand connector adds

Every skill works on its own: paste text in, copy the result out. If the PersonaXpand connector is connected, Claude can also read your real inbox, posts and numbers, and act on them after your yes.

- In Claude Code, this plugin already includes the connector (`.mcp.json` points to `https://personaxpand.com/mcp`). Run `/mcp`, pick `personaxpand`, and sign in once in the browser. Sign-in is OAuth; there are no keys in this repo.
- On claude.ai, add PersonaXpand from the connector directory, or add `https://personaxpand.com/mcp` as a custom connector.
- When you connect, you choose **Read only** or **Read and act**. Claude's recent changes are listed in PersonaXpand under Account Settings, Connected apps, where you can remove the connection at any time.

Setup help: https://personaxpand.com/features/ai-assistants?utm_source=github&utm_medium=skills&utm_campaign=connector

## Coverage (checked against the connector on 2026-11-13)

- **Posting and scheduling** through the connector: Instagram, Facebook, X, LinkedIn, YouTube (with a video), Threads and Bluesky. TikTok's rules require posting from the PersonaXpand app itself, so Claude cannot post to TikTok through the connector.
- **Replies in your voice**: comments on Instagram, Facebook, X, YouTube and Threads; mentions; direct messages on Instagram and Facebook only. Bluesky replies are drafts you approve. LinkedIn is for posting only here.
- **Analytics**: followers, engagement, best posts, reply rate and reply time, and best times to post.
- **Languages**: English and Arabic.

## Tool map (real tool names)

| Skill | Reads with | Acts with (only after your yes) |
|---|---|---|
| reply-in-my-voice | `get_voice`, `list_inbox`, `get_conversation`, `list_reply_drafts`, `list_connected_accounts` | `send_reply`, `schedule_reply`, `approve_reply_draft`, `reject_reply_draft`, `mark_handled` |
| inbox-triage | `list_inbox`, `get_conversation` | `mark_handled` |
| voice-profile | `get_voice`, `list_posts`, `get_post` | none |
| auto-reply-rules | `get_auto_reply_settings`, `list_reply_drafts`, `list_connected_accounts` | `create_auto_reply_rule`, `update_auto_reply_rule`, `delete_auto_reply_rule`, `set_auto_reply`, `set_account_auto_reply` |
| post-everywhere | `get_voice`, `list_connected_accounts`, `get_best_times`, `list_media`, `get_post` | `create_post`, `update_post`, `schedule_post`, `publish_post_now`, `import_media_from_link`, `create_upload_link`, `get_upload_result` |
| week-planner | `get_profile`, `get_voice`, `get_best_times`, `list_posts` | `create_post`, `schedule_post` |
| weekly-report | `get_analytics_summary`, `list_posts`, `get_post` | `refresh_analytics` (pulls fresh numbers, sends nothing) |
| sounds-human | none | none |

`get_plan_usage` answers "how many replies or posts do I have left". Never guess a limit.
