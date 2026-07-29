---
name: inbox-round
description: Run a full inbox prioritization + drafting round for Mattie — pull Gmail, diff against the last round, tier-cut by delegation (Own/Manage/Monitor/Mattie-only), produce the command-accounting brief, and stage reply drafts into Gmail Drafts. Use when Mattie says "inbox round," "new round of email prioritization," "triage my inbox," or on the morning/evening cadence.
---

# Inbox round

One round = pull → diff → tier-cut → brief → stage drafts → report. The product is the brief plus staged drafts, and the brief must earn its read: deltas and decisions only, every line actionable in one gesture, length scales with content — a no-news round is one line.

Design authority: `newt/docs/operations/inbox-system-notes.md` (doctrine + verbatims), `newt/docs/operations/inbox-operating-agreement.md` (tier table, escalation triggers), `newt/docs/operations/inbox-system-options.md` (the spine). Read the notes doc's "Decisions made" and doctrine sections before the first round in a fresh session.

## The loop

**1. Pull (read-only).** Google-workspace MCP, user mattie@newtheory.ai. Two queries:
- `is:unread is:important in:inbox` — her working set
- The human-slice query (in the bankruptcy manifest / notes doc): `in:inbox is:unread -from:luma-mail.com -from:luma.com -from:notify.railway.app -from:news.railway.app -from:calendly.com -from:substack.com -from:mail.beehiiv.com -from:google.com -from:tally.so -category:promotions -category:updates`
Gmail's Important flag is one input, never the gate (measured 63% precision / 62% recall). Machine envelopes hide obligations: check Slides/Calendly/Luma/standup notifications for named assignments.

**2. Diff against the last round.** Prior snapshots live in the session scratchpad (`inbox-important.json`, `round*-brief.md`) or are regenerated fresh. New / resolved / aged. Harvest responses: staged drafts that got sent, replies received (quote the key line), tours booked.

**3. Tier-cut.** Tier is the organizing axis; priority is a column.
- **Own** — agent/Morrigan handles end-to-end within the operating agreement (Tally tours via `inbound-reply` stock template; machine-mail parsing; scheduled chases). Batches gate on Mattie's explicit go for external sends.
- **Manage** — agent drafts, Mattie fires. List each with what the draft should do.
- **Monitor** — ledger + escalation triggers only. Money, contracts, waiting-ons, outbound bounces.
- **Mattie-only** — signatures, credentials, boss threads, confidential decisions, anything pushback-register.

**4. Brief** (scratchpad `roundN-brief.md`, relayed in chat). Rules:
- Lead with what changed. Tier-grouped. Every line carries its Gmail link (`https://mail.google.com/mail/u/0/#all/<threadId>`). Asks and commitments quoted verbatim.
- Close with the **command accounting**: *Yours (≤5) / Mine (named, so handling is visible) / Nixed (counted, logged, exceptions named by name).* A top-5 without counterweights is a shame amplifier; the nix decision is the product. "The good opportunities will come back."
- Legibility contract: every disposition visible, nothing deleted, commitments extracted to the ledger BEFORE any state clears, receipts one click deep.

**5. Stage drafts (Manage lane).** Writer reads the FULL thread first, then the register skill: `draft-mattie` (casual), `executive-email` (exec), `outreach` (cold), `event-copy` (event copy — card-first gate), `network-mode` (batch follow-ups). Event threads run the event-card check (o-logvy `events/cards/`) before drafting. Boilerplate pulls verbatim from `newt/docs/devrel/blurbs.md`. Stage via Gmail API `drafts.create` with the compose token (`~/.config/gcp/scav-gmail-compose-token.json`, needs `uv run --with google-api-python-client --with google-auth`): reply-threaded (threadId + In-Reply-To/References), 2 variants where register could differ (recommended one staged, alternate held), pushback-register drafts ALWAYS stage for Mattie regardless of sender tier. Attachment-dependent drafts open with a `[attach X]` first line.

**6. Report + close the loop.**
- Chat report = the brief's headline + command accounting + staged-draft list with links. No placid restating.
- Tally submissions couple atomically: invite + Notion row + stage-count delta ("Qualified: N (+x)") — `inbound-reply` skill, stock template only, exceptions surfaced never customized.
- After Mattie sends an edited draft, run `absorb` (deltas ledger, two-instance promotion).
- Pipeline/ledger notes land in `newt/docs/operations/inbox-system-notes.md` if they change standing state.

## Hard rules

- **Nothing sends on agent authority.** Compose token stages only. Superhuman MCP send/trash tools are never called. Morrigan batch sends fire only on Mattie's explicit go relayed from the main thread.
- **Read-only until the modify decision.** Mark-read/archive runs via Superhuman `update_thread` for small named sets; bulk sweeps wait on `gmail.modify` scope and the staged bankruptcy manifest gates (Luma→Notion parse first, co-host carve-out, finance terms).
- **Stock over custom** in every delegated send; customization only as a surfaced exception.
- **Cards are context slots; search is fallback.** Facts from cards/blurbs, color from search.
- Preserve en-dashes. No "not X, but Y." Complete sentences over staccato.

## Cadence

Morning round before 8 AM, optional EOD sweep. Skip-days are fine. If Mattie skips the brief twice, the brief is wrong — redesign it, don't re-send it.
