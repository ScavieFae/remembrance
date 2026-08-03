---
name: pipeline
description: Move a Mission Robotics tenant/prospect lead between pipeline stages, draft a tenant followup, or answer a common prospect question. Use when Mattie wants to advance a lead (Identified→Qualified→Toured→LOI→Signed), draft a tour/intake/re-engage/close/keep-warm followup, or pull a copy-paste answer on pricing, what's included, capacity, community, move-in, the hackathon, or robots.
---

# Pipeline operations — Mission Robotics tenant pipeline

Operating playbook for the Logvy leasing pipeline. Templates and FAQ bank live in
[`operation-logvy/outreach/pipeline-followups.md`](../../../new-theory/operation-logvy/outreach/pipeline-followups.md) — read it before drafting; it holds the canonical, Mattie-approved copy.

**Closing out a tour goes to [[tour-close]], not here.** That skill runs the full post-tour motion — transcript provenance, the followup composed from the templates below, the stage move plus a tour card in the page body, the Nexudus person record, and the commitments ledger. Use `pipeline` directly for stage moves with no tour attached, and for FAQ answers.

## Stage ladder + entry gates

| Stage | Gates on | Weight (as fraction) |
|---|---|---|
| Identified | name + reason they fit | 0.10 |
| Qualified | two-way contact + real interest + fit signal | 0.20 |
| Toured | booked or completed a visit | 0.40 |
| LOI | verbal/written intent on a specific unit + price | 0.70 |
| Signed | lease executed → Committed Revenue | 1.00 |

Terminal/holding: **Not a Fit** (wrong stage/timing/unfunded), **Lost** (was real, gone cold/elsewhere), **N/A** (not a pipeline entity).

## Drafting a followup

Compose from the **Reusable blocks** (Pricing / Events / Intake-CTA) in pipeline-followups.md — pricing lives there as the single source of truth, edit it in one place. Templatize anything sent more than once.

Match the transition to a template in `pipeline-followups.md`:

1. Qualified → book a tour (Calendly)
2. **Toured → intake form** — the priority one, same-day, canonical approved draft. Intake link: https://tally.so/r/kdkGYr
3. Stalled (~5 days silent) → re-engage — lead with forward cadence, never "sorry for the silence"
4. Intake done → LOI / close — confirm unit + price + start; route payment to **Cam Lindsay** (Head of Ops & Finance, Mercury invoicing)
5. Not a fit → graceful keep-warm — set a concrete revisit trigger + date
6. Toured → community/peer keep-warm — for non-tenant peers/speakers; don't pitch space; Category=Community, keep out of tenant forecast

Voice is MR: direct, operator-to-operator, anti-corporate. Read `operation-logvy/soul.md` + `fodder.md` if a draft drifts. **Always CC morrigan@missionrobotics.ai** — that's the status capture.

**Template-health signal (proactive maintenance):** a template's quality = how *little* Mattie changes OUTSIDE the slots. Slot-fills (`[name]`, `[callback]`) are expected — ignore them. Edits to the **connective tissue** (prose between slots, structure, framing, closing) are the signal the template is missing something — that delta is what to harvest. When reconciling sent mail (or any time a shipped message can be compared to its template), diff against the source template and surface the out-of-slot changes as improvement candidates; a message that changed only slots = clean fit, no change needed. Promote recurring out-of-slot phrasings into better default lines or new blocks. Surface candidates to Mattie — don't silently rewrite canonical templates.

## Answering a prospect question

Pull from the **Common answers (FAQ bank)** in `pipeline-followups.md`: pricing, what's included, capacity, community value-prop, move-in, robots/embodiments. The FAQ pricing is current; the onesheet is stale — trust the bank.

**The close lever is the 6-month commitment discount.** Pricing went term-gated (month-to-month vs 6-month rate) on 2026-07-06 — the old date-gated "lock the rate before July 15" lever is retired, and the pre-step-up numbers ($200 / $400 / $750) are dead. Never quote them. People quoted under the old structure keep their quoted number. The Embodied Metal Hackathon ran July 17-19; it is a past event, not an upcoming draw.

## Updating the Prospects Notion DB

DB: https://app.notion.com/p/82afb1807fd04ef3a68a774c6e35a02a (Operation Logvy Prospects). Dispatch Notion work to a subagent — payloads are verbose.

Schema of record is [`hatchery/projects/notion-prospects/SCHEMA.md`](../../../new-theory/hatchery/projects/notion-prospects/SCHEMA.md) — read it before a write rather than re-deriving from Notion.

When moving a stage, update **all** of:
- **Stage** → new stage
- **Next action** (text) → the concrete next step
- **Next Followup** (date) → when it happens. This is the live cadence field — the one date the pipeline sorts by for "who to touch next."
- **Last touch** → today
- **$/mo (MRR)** → the unit's rate for the deal
- **Tour date** + **Tour guide** → whenever a tour completed, regardless of the resulting Stage. A tour still counts after they convert to LOI/Signed or fall out to Not a Fit / Community / Lost.
- **Email** → capture it the moment you have it (from the thread, the signature, the Morrigan reconcile). Email is the match key for the Morrigan capture loop — a row without an email can't be reliably auto-reconciled. Backfill aggressively.

**Always log to the entry's page body (the detail subpage), not just the properties.** Every touch, update, and verbatim goes into the prospect's Notion page body as a dated log entry (native blocks — `## YYYY-MM-DD — <what happened>` + bullets). Properties = at-a-glance state; the body = the running history (what was said, what was sent, key quotes). Append, never overwrite prior log entries. This is the durable record; the properties just reflect the latest state.

Hard rules:
- **`Probability` and `Next action by` are GONE from the live DB** (deleted 2026-07-28, re-verified 2026-08-03). Don't try to set either — writes fail. The stage weights below still describe the ladder conceptually, but there is nowhere to store them, and `Weighted $/mo` is broken as a result: **never quote a weighted pipeline number without flagging it to Mattie first.**
- **Only use existing fields and existing select options.** Mattie edits the DB live — never add, rename, or invent fields/options. If an option you need doesn't exist, surface it to Mattie; don't create it.
- **The DB has an Email field** — match prospects by **email when present**, fall back to **name** when it's missing. Backfill emails so the Morrigan loop can auto-reconcile.
