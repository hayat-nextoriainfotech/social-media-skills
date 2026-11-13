# Network limits and habits

**Checked on 2026-11-13** against each network's own documentation (links below). Networks change these. Re-check before each release, and if a user reports a different limit, trust the network's current help page over this file.

## Hard limits

| Network | Post text | Other limits | Source (checked on 2026-11-13) |
|---|---|---|---|
| Instagram | 2,200 characters per caption | 20 @mentions per caption. Hashtags: Instagram's Help Center says up to 5 per post; the publishing API reference still says 30. Use 5 or fewer. | [Instagram API: IG User Media](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media), [Instagram Help: Use hashtags](https://help.instagram.com/351460621611097) (this page loads its text with script; we read "You can use up to 5 tags on a post" in a rendered browser on 2026-11-13) |
| X | 280 characters | Every link counts as 23 characters. Emoji and Chinese, Japanese and Korean characters count as 2. | [X docs: Counting characters](https://docs.x.com/fundamentals/counting-characters) |
| LinkedIn | 3,000 characters | | [LinkedIn Help: Post and share updates](https://www.linkedin.com/help/linkedin/answer/a528176) |
| Threads | 500 characters | One topic tag per post, 1 to 50 characters, no periods or ampersands. At most 5 links per post. Emoji count by their byte length through the API. | [Threads API: Posts](https://developers.facebook.com/docs/threads/posts) |
| Bluesky | 300 characters (grapheme clusters) | Also at most 3,000 bytes (UTF-8). Link text in the post counts like any other text (no fixed link length as on X). | [Bluesky post lexicon](https://github.com/bluesky-social/bsky/blob/main/lexicons/app/bsky/feed/post.json) |
| YouTube | Title up to 100 characters; description up to 5,000 characters | Needs a video. | [YouTube Help: Add video titles and descriptions](https://support.google.com/youtube/answer/57404) |
| TikTok | Caption up to 2,200 (UTF-16 units) | Through the PersonaXpand connector Claude cannot post to TikTok; the user posts from the app. | [TikTok Content Posting API](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post) |
| Facebook | Long posts are allowed | We could not confirm a current official character limit on 2026-11-13, so none is stated here. Keep the point in the first lines. | |

## Habits that work (guidance, not rules)

These are writing habits, not platform facts, so they carry no numbers.

- **Instagram**: the first line is the hook, the rest sits behind "more". Links in captions are not clickable; use "link in bio" or a DM. A question at the end invites comments.
- **Facebook**: clickable links work in the post. Short posts with one clear point and a photo read best on phones.
- **X**: one idea per post. Cut every word that isn't needed. A thread only when there are several real points.
- **LinkedIn**: the first two lines decide whether people click "see more". First person, one lesson or story, short paragraphs. Hashtags sparingly, at the end.
- **Threads**: conversational, like talking to followers. One topic tag, chosen on purpose.
- **Bluesky**: plain and direct; the audience dislikes marketing speak. Alt text on images.
- **YouTube**: the title says what the viewer gets; the first lines of the description repeat it with the key link.
- **TikTok**: the caption supports the video; keep it short and searchable.

## Counting tips

- Count the final text, after hashtags and links are added.
- Line breaks and spaces count.
- Through the connector, PersonaXpand checks each version against the network's rules before it goes out and lists anything it skipped.
