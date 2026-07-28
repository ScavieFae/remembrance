---
name: inbound-reply
description: Reply to an inbound Mission Robotics Tally submission — draft a from-Morrigan tour invite, send it via AgentMail with Mattie CC'd, and add/update the prospect in the Notion DB. Use when Mattie shares a Tally Forms notification (short tour-interest form Ek61oX or long intake kdkGYr) and wants the inbound handled.
---

# Inbound reply — Mission Robotics Tally submission

The repeatable loop for an inbound Tally form fill: **read the submission → draft the from-Morrigan invite → send via AgentMail (CC Mattie) → log to the Prospects DB.** This is the front door of the [[pipeline]]; once they reply and book, the `pipeline` skill takes over (Toured → intake, etc.).

Revise this skill every time Mattie edits a draft outside its slots — the connective tissue she changes is the signal.

## Step 1 — Read the submission

A Tally notification (from `notifications@tally.so`, sent to Mattie + morrigan) carries: name, email, space interest (Floating Desk / Permanent / Robot Bay / Office), and "What are you building, and who is it for?". Pull all four.

## Step 2 — Draft the reply (from Morrigan, CC Mattie)

This is the canonical, Mattie-approved shape (Vrijen Attawar, 2026-06-29):

> Hi [Name]! Thanks for reaching out about a [tier — e.g. floating desk] at Mission Robotics. We'd love to have you by to see the space and learn more about what you're building.
>
> Does a time here work for you?
> https://calendly.com/mattie-newtheory/mattie-in-person-meet
>
> I'm cc'ing Mattie here — she'll take it from here.
>
> — Morrigan
> Mission Robotics

**Drafting rules (these are load-bearing — read [[feedback_hook_from_experience]] + [[feedback_hollow_relevance_assertion]]):**

- **Short wins.** No pricing, no events, no intake — those come post-tour. The job here is a booked visit.
- **Don't repeat their submission back.** Restating what they're building in nicer words is a book-report tell — the market smells it. "learn more about what you're building" is the honest-empty default and it carries fine.
- **Only hook on something real.** A hook is allowed ONLY if it carries info from our side they don't have — a floor observation, a verbatim, an earned POV on their problem. If we don't have one, use the generic line. Honest-empty beats fake-clever. Never manufacture relevance ("exactly the kind of problem the room is full of" = hollow, cut it).
- **From Morrigan, not Mattie.** Morrigan sends; the "I'm cc'ing Mattie — she'll take it from here" line does the handoff. Sign `— Morrigan / Mission Robotics`.

## Step 3 — Send via AgentMail

Send from `morrigan@missionrobotics.ai`, CC `mattie@newtheory.ai`. Key at `~/.config/agentmail/key`. See [[reference-agentmail]].

```bash
KEY=$(cat ~/.config/agentmail/key)
curl -s -X POST "https://api.agentmail.to/v0/inboxes/morrigan@missionrobotics.ai/messages/send" \
  -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d '{"to":"[their email]","cc":"mattie@newtheory.ai","subject":"Come see Mission Robotics","text":"[body with \n line breaks]"}'
```

**Always surface the draft to Mattie for review and wait for her go before sending — no auto-send (policy as of 2026-06-29).** External/irreversible (see [[feedback_confirm_before_prod]]). Revisit letting Morrigan fire low-stakes tour invites unprompted once the drafts are consistently clean. The CC to Mattie replaces the usual morrigan-CC (Morrigan is the sender here, so her inbox already has the thread).

**CC Mattie on ALL Morrigan outbound, not just tour invites (Mattie, 2026-07-06).** Any email Morrigan sends — tour invites, intake handling, event replies, anything — CCs `mattie@newtheory.ai` unless Mattie waives it for a specific send. See [[feedback_morrigan_cc_mattie]].

## Step 4 — Add / update the Prospects DB

**Dispatch to a subagent** (Notion payloads are verbose). DB: https://app.notion.com/p/82afb1807fd04ef3a68a774c6e35a02a

The inbound Tally fill often **auto-creates a stub row** already — match by email first and UPDATE, don't create a duplicate.

Exact field names + valid options (learned 2026-06-29; schema re-verified against live DB 2026-07-28 — use these strings verbatim):
- **Stage** → `Qualified` (inbound + two-way contact + fit signal = Qualified, weight 0.20)
- **Tier interest** (NOT "Space interest") → `Floating desk` / `Permanent desk` / `Private office` / `Just curious` / `Multi-tier` — note lowercase second word. (`Robot bay` is NOT a live option — robot-bay interest goes in the log-block prose.)
- **$/mo (MRR)** → the tier's current rate (floating 200 / permanent 400)
- **Source** → `Tally form` — but only if Source is empty; never overwrite an existing original-touch Source (e.g. `Event`). Original touch wins; the Tally fill goes in the log block.
- **Category** → `Lead` (tenant prospect). `Tenant` = signed/committed; `Community` = non-tenant peer. There is no "tenant Lead."
- **Need/Commitment** ← their "what they're building" text
- **Email**, **Org** (domain), **Last touch** (today), **Next action** + **Next Followup** (date, ~1 week out)
- REMOVED 2026-07-28: `Probability` and `Next action by` do not exist in the live schema (batch run hit both). `Next Followup` is the live date field.
- Only use EXISTING fields/options. If one's missing, surface to Mattie — never invent.

Also append a dated log block to the page BODY:
```
## YYYY-MM-DD — Inbound Tally + tour invite sent
- Inbound via [short Ek61oX / long kdkGYr] Tally form: interested in a [tier].
- Building: [their text].
- Tour invite sent from morrigan@missionrobotics.ai, CC mattie@newtheory.ai — Calendly link, Mattie taking it from here.
```

## After they reply

Booked a tour → advance to **Toured** and hand to the `pipeline` skill (Toured → intake #2, same-day). No reply in ~5 days → `pipeline` re-engage template.
