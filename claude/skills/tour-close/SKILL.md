---
name: tour-close
description: Close out a Mission Robotics tour — gather what was actually said, draft the post-tour followup, move the Notion prospect card, seed the Nexudus person record, and stage the team-review card. Use when Mattie says "close out the [name] tour", "tour followup for [name]", or "finish the [name] tour". Covers the whole post-tour motion: transcript provenance, pipeline stage move, prospect card for NT review, Nexudus coworker seeding, and the commitments ledger.
---

# Tour close — Mission Robotics post-tour motion

One tour produces five artifacts: a followup email, a Notion stage move, a tour card in the prospect's page body, a Nexudus person record, and a commitments ledger. This skill runs all five in order. The front door is [[inbound-reply]]; the template library and stage ladder are [[pipeline]]. This skill is the closeout.

**Same-day rule.** The followup goes out the day they walk the floor. If the tour was yesterday or older, say so in the handoff and send anyway — don't silently backdate.

## Step 1 — Gather what was said

Three sources, in this order:

1. **Pocket recording.** `mcp__pocket__search_pocket_conversations` / `query_pocket_meetings` by the person's name and the tour date, then `get_pocket_conversation` for the transcript. `search_pocket_actionitems` for the generated commitments.
2. **Calendar event** — `mcp__google-workspace__get_events` for the tour slot: who attended, who gave the tour, the real start time.
3. **Email thread** — the pre-tour thread (Superhuman or Gmail search by their address) for what they asked for before arriving and what we promised.

**Pocket is color, not canon.** This is a hard rule, not a caution:

- Its diarization mislabels speakers. Two people in a room become one voice, or a line lands on the wrong person entirely.
- Its generated summaries overstate. Documented case, 2026-08-03: asked how many desks he needed, the prospect's verbatim answer was **"One."** Pocket's summary said he was **"moving his 4-engineer team in."** Both statements were in the same recording; only one was said out loud.
- **Names in Pocket action items may come from calendar metadata, not audio** — an action item attributed to someone is not evidence they spoke.

So: **tag every extracted claim** `[transcript-verbatim]` or `[pocket-generated]` as you pull it. Only `[transcript-verbatim]` claims enter the Notion card, the email, or Nexudus. `[pocket-generated]` material fills gaps only when explicitly marked as inference in the card ("Pocket summary suggests X — unconfirmed"). When the two disagree, the verbatim wins and the disagreement itself is worth a line.

If there's no recording, say so and build the card from the email thread plus whatever Mattie recalls. A thin card with honest gaps beats a full one built on generated text.

## Step 2 — Route by tour outcome

The tour's outcome picks the template. Templates live in
[`operation-logvy/outreach/pipeline-followups.md`](../../../new-theory/operation-logvy/outreach/pipeline-followups.md) — **read the template there and compose from its blocks. Never duplicate template copy into this file**; pricing and the reusable blocks are single-source there and drift the moment they're copied.

| Tour outcome | Template | Notes |
|---|---|---|
| Tenant prospect, Mattie sends | **#2** Toured → intake form | Personalized callback slot is Mattie's move. Subject: "Good having you at Mission Robotics — the numbers". CC morrigan@. |
| Tenant prospect, Morrigan sends | **#2b** Morrigan variant | **Drop the callback slot** — general template is Morrigan's default. Sends via the AgentMail API (`morrigan@missionrobotics.ai` is not a verified Superhuman send-as alias), CC mattie@. |
| Community / peer, not a space fit | **#6** Toured → community keep-warm | Do NOT pitch space. Notion Category = Community, keep out of the tenant forecast. |
| Too early / pre-idea, still finding the wedge | **#8** Curated list | Add to the Luma `curated` contact tag per the distribution runbook. Distinct from #5 — #5 is a defined idea with wrong timing, #8 is no defined idea yet. |
| Not a fit — unfunded, wrong timing, wrong stage | **#5** Graceful keep-warm | Set a concrete revisit trigger **and a date**. This is a "later," not a "no." |

If the tour outcome is genuinely ambiguous, say which two templates are in play and what fact would decide it — don't pick by feel.

## Step 3 — Draft the followup

Compose from the template's blocks (Pricing / Events / Intake-CTA). Voice is MR: direct, operator-to-operator, anti-corporate — `operation-logvy/soul.md` and `fodder.md` if a draft drifts.

**Every specific claim in the draft traces to a `[transcript-verbatim]` source.** If the callback slot needs a detail you only have from a Pocket summary, leave the slot generic rather than assert something they didn't say. A wrong callback in the first line is worse than no callback.

**Staging rule: the draft is presented to Mattie for review, and nothing sends without her explicit go.** Mattie-sent drafts stage into Gmail Drafts via the compose-scope token. Morrigan sends go out via AgentMail only on an explicit main-thread go — surface the exact payload first.

## Step 4 — Notion: stage move + tour card

**Always via a subagent** — payloads are verbose. Follow the upsert recipe in
[`hatchery/projects/notion-prospects/RECIPE.md`](../../../new-theory/hatchery/projects/notion-prospects/RECIPE.md); the schema of record is
[`SCHEMA.md`](../../../new-theory/hatchery/projects/notion-prospects/SCHEMA.md) in the same directory. Data source: `collection://e1f5e2ed-5bba-46e4-97f2-14bea315e8cd`. The live DB title reads **💲 Mission Robotics CRM** (renamed from "Operation Logvy Prospects"; the IDs are unchanged).

Properties to set:

- **Stage** (status) → `Toured` (or the terminal stage if the tour routed to #5/#6/#8 — but set Tour date regardless; a tour counts no matter where they land)
- **Tour date** (date) → the date it happened
- **Tour guide** (select) → who gave it. **`Mattie` is the only option currently defined** (verified live 2026-08-03). If someone else gave the tour, surface it to Mattie so she adds the option — never create one.
- **Review status** (select) → `Pending` when the card is written and the team hasn't looked yet. Options: `Pending`, `In review`, `Cleared`, `Declined`. This is what stages the card for team review; leave the rest of the ladder to whoever reviews.
- **Next Followup** (date) → the cadence field, the one date the pipeline sorts by
- **Next action** (text) → the concrete next step
- **Last touch** (date) → today
- **Tier interest**, **Team size**, **Timeline**, **$/mo (MRR)** → verbatim-sourced only; leave blank rather than guess
- **Email** → backfill if it's missing; it's the match key for the Morrigan reconcile loop

Two gaps in that field set bite specifically on tour closes (logged in SCHEMA.md 2026-08-03):

- **`Tier interest` has no `Robot bay` option** and is single-value. Someone who wants a bay plus a desk goes to `Multi-tier`, which loses the specific combination — put the actual combination in the tour card's **Interest** line. If bay-interest leads keep recurring, surface the gap to Mattie; don't add the option.
- **`Timeline` has only relative buckets** (Next 30 days / Next 90 days / 6+ months / …). A named month or quarter ("early-mid Oct") has no slot — pick the closest bucket and put the exact target in the tour card.

Only existing fields and existing select options. `Probability` and `Next action by` are gone from the live DB — don't try to set them, and don't quote `Weighted $/mo` (its Probability input no longer exists) without flagging it to Mattie.

Then write the **tour card** as a dated block in the page **body** (append, never overwrite prior entries). Fixed schema, every time:

```
## YYYY-MM-DD — Tour card (tour by <guide>)

- **Tally status:** none / tour-interest (Ek61oX) submitted / intake (kdkGYr) submitted
- **Interest:** <units + count + timing, verbatim-sourced — plus any open questions>
- **Tour:** <date> · given by <name>
- **About the team**
  - **Company:** <name>
  - **What they build:** <1–2 lines, their words>
  - **Team & size:** <who, how many>
  - **Funding:** <stage/amount>
  - **Traction:** <what's shipped, who's using it>
  - **Why they fit the room:** <the specific reason, not a compliment>
  - **Links:** <site | personal | repo>
- **Commitments**
  - Theirs: <what> — owner <name>, by <date>
  - Ours: <what> — owner <name>, by <date>
- **Sources:** Pocket recording <id> · email thread <id> · <claim>: [transcript-verbatim] / [pocket-generated]
```

**About the team** is the NT review section — the wider team reads it to decide on the application, so its schema stays identical across every prospect. Don't drop a bullet because you lack the fact; write "not established" and let the gap be visible.

**Confidential facts get flagged in place, not omitted.** Unannounced funding, a raise in progress, anything they shared in confidence: keep it in the card with an inline ⚠️ and an explicit "don't repeat outside pipeline." The flag travels with the fact — cutting it means the next reader rediscovers it from scratch and may repeat it.

## Step 5 — Nexudus: seed the person record

**This is a deliberate post-tour create.** The Nexudus docs frame the account as a post-signature system — [`mission-robotics-ops/ops/nexudus/source-of-truth-plan.md`](../../../new-theory/mission-robotics-ops/ops/nexudus/source-of-truth-plan.md) builds contracts in Phase 2, after paper. We seed the **Coworker record only** at tour time, on purpose, so the member backend is the one place a person exists from first contact. **No contract, no tariff, no billing.** `AutoRaiseInvoices` stays false; contract creation is Mattie-gated and stays in the UI.

Follow the create sequence in that plan's **Imports** section:

1. Mint a bearer token — `POST /api/token`, **form-encoded** body (not JSON).
2. Dedupe by email via the search-paged endpoint (`/spaces/coworkers/search/{page}/{size}?search=`). The paged `GET /api/spaces/coworkers` 500s account-wide — don't use it.
3. Create — `POST /api/spaces/coworkers` with `FullName`, `Email`, `CoworkerType`, `CompanyName`, `CountryId` (US = **1221**), `SimpleTimeZoneId` (Pacific = **2006**), `Notes`.
4. Verify — `GET /api/spaces/coworkers?Coworker_Email=...`.
5. Notes backfill — `Notes` is silently dropped on create. GET the full record, set `Notes`, `PUT` to the **collection** URL with the whole record (there is no PATCH, and `PUT /{id}` 405s).

No email, no record — rows without an email go to `work/manual-add.csv` for hand entry. **Never fabricate an email.** Validation errors surface one at a time; fix, rerun, repeat. Reruns are safe (dedupe by email, Notes self-heal).

**Company rides the `CompanyName` string.** Multi-person teams are modeled with Nexudus **Teams**, which is a manual UI step — **flag it for Mattie, don't attempt it from a script**.

**Nexudus Notes stay bland and factual** — tour date, tier interest, timing. Nothing else. No candid pipeline reads, no deal posture, no funding detail, no confidential anything. Nexudus is shared ops surface and `mission-robotics-ops/CLAUDE.md` walls pipeline/CRM content out of it. The candid version lives in the Notion card; these two records are deliberately different.

Good: `Toured 2026-08-03. Interested in one dedicated desk, timing ~Sept.`
Bad: anything with a rate, a probability, a read on the person, or an unannounced raise.

## Step 6 — Ledger the commitments

Both sides' commitments come out of the tour card and go two places:

- **Notion `Next action`** — the single concrete next step, with its date in `Next Followup`.
- **A review list surfaced to Mattie in the closeout report** — every item, whose it is, and when it's due.

**Her owed items are hers to fire.** If a commitment is a Luma write, an invite, an intro, or anything member- or public-facing, it goes on her list as a staged action with the payload ready — the skill does not execute it. Our commitments that are genuinely ours (send the intake link, file the card, seed Nexudus) get done in this pass and reported as done.

## Closeout report

End the run with: template used and why, the draft staged (and where), Notion property changes as `<Property>: <old> → <new>` plus the per-stage count snapshot with deltas, Nexudus record created or skipped with the reason, and the two-column commitments list with owners and dates. Name anything that came from `[pocket-generated]` text and stayed unconfirmed.
