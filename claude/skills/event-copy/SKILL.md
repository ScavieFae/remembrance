---
name: event-copy
description: Draft event copy in Mattie's voice — newsletter blurbs, Luma event descriptions and listings, invite copy, blast copy, forwardable event one-paragraphs. Use for anything an audience reads about an event we host, co-host, or lend the venue to. This is her EVENT register (image-first, receipt-backed, warm by invitation), NOT the sectioned executive-email register and NOT the casual burst voice.
---

# Mattie's event-copy register

Event copy is a third register, and it fails in two directions. Pulled toward `executive-email` it grows bold full-sentence headers and a sectioned recap shape, which reads like a memo about an event instead of an invitation to one. Pulled toward `draft-mattie` it collapses into stacked fragments and spec-sheet listing, which is exactly the draft Mattie rejected in her own hand (specimen 1b below, superseded within sixty seconds).

What she actually writes: **an image, then an arc, then receipts, then the logistics, flat and last.** Complete sentences the whole way, clauses leaning into each other, no adjective doing work a number could do.

**Draft from the specimens, not from the rules.** Read all four before writing a word; the sentences teach the register better than the rules can, and the rules exist mostly to stop you undoing them.

## Step 0 — load the event card. This is a gate, not a suggestion.

Input is an event. Before composing anything, find its card in `operation-logvy/events/cards/<slug>.md`. The card is the context slot: date, venue, class, hosts, Luma id, speaker state, public-copy constraints, the log of what's already been said to whom.

- **The card is where facts come from.** Broad search is the fallback for color and quotes, not for facts. (Mattie, 7/29: cards are the context slot; search still has value, but for color.)
- **No card → STOP and propose creating one.** Per the event-reply standing step in `newt/docs/operations/inbox-system-notes.md` (2026-07-28): any work touching an event runs an event-card check first, proposes a card if missing, and pulls card context into the write. **Never write event copy from a blank page.** Schema and rules: `operation-logvy/events/cards/README.md`.
- **Read the card's `## Boot` and `## Assets` first**, then anything already sent to a counterparty — the card quotes it precisely so the next piece of copy doesn't contradict it.
- **Constraints on the card override this skill.** Cards inline the expensive constraints on purpose (README rule 11, "paid for in blood"). If the card says a listing is a co-host's to publish, or a speaker is unconfirmed, that governs.
- **Facts that could be wrong say so.** If the card marks something `[unverified]` or `[candidate, not committed]`, it does not go in public copy as fact. An unsent draft renders identically to sent mail — the card's whole reason for existing is that this already cost us a day.

**Boilerplate slots pull VERBATIM from `newt/docs/devrel/blurbs.md`.** New Theory copy, Mission Robotics copy, the one-liners. Copy-paste, never reassemble, never re-derive. That page also holds the two constraints most likely to break a listing:
- **Khosla never appears in public copy** — no Luma page, no venue listing, no sponsor credit, no deck that leaves the room. Partner-forward email only.
- **NT and MR are distinct entities with different slots.** MR takes the venue slot; NT takes the co-host / company / speaker slot. The known bug is a sentence that fuses them ("our office doubles as a lab"). It reads as one entity and it is wrong.
- No internal R&D specifics — problem-area level only. No "90% less data," no geometric deep learning.

---

## Specimens — read all four before drafting

### 1. The forwardable event blurb (Mattie-sent 2026-07-07, 67 words)

Written for Kristopher Floyd to forward to Cerebral Valley. Approved verbatim in `blurbs.md`; the canonical shape for CVs, newsletters, partner forwards, and any "send me a couple lines" ask.

> Embodied Metal is a robotics hackathon where your model wakes up in a body. Teams get real robots including a G1 humanoid, SO-101 arms, and rovers to collect data and code Saturday, train overnight, and demo their robot's new power at Sunday's live judging. 80 curated spots, closing in on 300 applications; sponsors include Rerun, Modal, and LiveKit. July 17–19 at Mission Robotics, SF. luma.com/embodied-metal

### 1b. The version she wrote first and replaced within the minute (same send, 42 words)

She sent this, then immediately sent the version above as "the correct one." **This is the highest-value specimen in the file** — it is the register's failure mode in her own handwriting, corrected by her.

> Embodied Metal — a 3-day robotics hackathon at Mission Robotics in SF's Mission District, July 17–19. Teams build on real robots — G1 humanoid, SO-101 arms, and more — with Modal, Rerun, and Savant sponsoring. 180+ registered. luma.com/embodied-metal

What she fixed, and what you must not undo: the opener moved from a **category** ("a 3-day robotics hackathon at X") to an **image** ("where your model wakes up in a body"). The middle moved from a static spec ("teams build on real robots") to an **arc with a clock** (collect Saturday → train overnight → demo Sunday). The dashes-as-spec-punctuation became clauses. The receipt got sharper: "180+ registered" became "80 curated spots, closing in on 300 applications," which is the same fact carrying the scarcity. Date and venue stayed exactly where they were — last, flat, unlabeled.

### 2. The personal invite (Mattie-sent 2026-07-23 via Luma, 46 words)

To Sergii Zhuk for Bay Area Frontier Research Club #15. He replied and signed up.

> Hey Sergii! This is the research night I promised you'd be on the list for. Embodied AI papers over dinner, plus a live robot demo on our floor. First hardware edition of the series and I'd love to have you in the room Wednesday.

Four sentences. The callback carries the opener, the sensory pair carries the middle, the edition marker earns the attention, and the close is a door held open rather than a command. One exclamation mark, in the greeting, where it is register rather than noise. No date line — the Luma card underneath carries the date, so "Wednesday" is just a word in the last sentence.

### 3. The pre-event logistics blast (Mattie-sent 2026-07-16 via Luma to the full Embodied Metal list)

Note this is **not** the version staged for her in the repo — she wrote her own. Prose quoted in full; the schedule block is abridged here for length and should be read in the same shape she used, one line per item, time first.

> Hey everyone,
>
> We're excited to see you tomorrow for The Embodied Metal Hackathon.
>
> A quick note up front: we expect a full house, so please plan to arrive early, check in, and claim your spot. Doors open Friday at 4:00 PM for registration, wristband pickup, and team formation. If we hit capacity, we may not be able to accommodate late arrivals.
>
> Location: 3001 19th St, San Francisco, CA, 94608
>
> The goal for Friday is simple: get checked in, form your team, get matched with a robot, and start hacking. We'll have opening remarks from the hosts and sponsors, and rapid-fire crash courses walking you through everything you need to know to hack on a robot.
>
> Here's the weekend flow:
>
> **Friday**
> 4:00 PM — Doors open, registration, wristband pickup, team formation
> 5:30 PM — Opening remarks
> Evening — Team formation, robot selection, live idea pitches, and start hacking
> 10:00 PM — Space closes for overnight
>
> [Saturday and Sunday follow the same shape — day, then time-first lines, meals included]
>
> More details, updates, and prize info will be shared in the WhatsApp group. Make sure you've joined here: [link]
>
> See you tomorrow,
> Mattie & The Embodied Metal Hackathon Team

The one thing that matters goes above the schedule, not inside it — *arrive early, here's the consequence if you don't*. Then the intent line ("the goal for Friday is simple") tells people what the day is for before it tells them what happens when. Only then the times.

### 4. The slot fill (Mattie-sent 2026-07-28 to Miguel Villafuerte, SF Hardware Meetup #137)

A co-host asked for "a couple lines" for his Luma listing. She did not write new copy — she pulled both approved blurbs and, critically, **named the slots** rather than letting him assign them by feel:

> **New Theory (company slot):** New Theory AI is building foundation world models for robotics – giving machines enough understanding of the physical world to act in places and situations they're seeing for the first time. We're building toward a model that lets anyone teach a robot a new task in under five minutes.

> **Mission Robotics (venue slot):** Mission Robotics is building the beating heart of robotics in the Mission, bringing together the leading builders, founders, and mad scientists making embodied AI a reality. If your robot got you kicked out of a WeWork, we want you here. www.missionrobotics.ai

And she handed over the motion without holding it hostage: *"feel free to go ahead and upload your favorite to Luma."*

---

## Reference-grade — structure you may borrow, sentences you may not

These shipped, but Mattie did not write the prose. Use their **shape**; do not treat their lines as voice.

**The two-event newsletter** (`operation-logvy/events/week-2026-07-27-content.md`) — Scav-drafted, Mattie-approved, confirmed sent 7/27 to all 1,531 MR-calendar contacts. The only verified newsletter send in the estate, so its structure is approved by use: a one-line frame ("Two research nights on our floor this week."), then one **bold date + event name** header per event, then a dense paragraph carrying speakers with affiliations, the sensory detail, the admission gate, and the link inline, then a one-line close.

**The Embodied Metal Luma listing** (`newt/docs/projects/2026-07-hackathon/luma-copy.md`) — Scav-drafted; the repo doc and the live page are known to have diverged, and the file contains the failure this skill firewalls against ("Spots are limited and curated. Apply now."). Reference for section ordering on a long listing only.

**The sponsor spec paragraph** (Rerun, 6/18, hers but a private sales document): *"60-80 hackers, plus another 40-60 coming through over the weekend. 6,000 sq ft, every team gets a robot (hands; arms; a humanoid among a few), full-stack builds (record, train, ship)."* Corroborates how she stacks receipts — bare, comma-spliced, zero adjectives. Private register, do not publish.

**Her own May 19 draft**, superseded: *"…where robots, models, and devs shape reality. Two days in a whirring Mission factory loft with 80+ builders shipping across the entire electric stack, from funded robotics founders to mad science garage hackers."* Two months before specimen 1. "Shape reality" is the vaguer ancestor of "wakes up in a body," and **"funded" is now forbidden in outreach copy** (6/17). Anti-specimen.

**The member welcome / happy-hour email** (7/14 mail-merge, hers) uses emoji bullets and closes "Best, Mattie." It is operational onboarding, and its register is off her public canon. Do not import it.

---

## The observed rules

Every rule below is observed at least twice across the specimens. Anything seen once is in Candidates and does not bind.

**Open on the image, never the category.** "Where your model wakes up in a body," not "a 3-day robotics hackathon at Mission Robotics." "This is the research night I promised you'd be on the list for," not "Join us for FRC #15." Observed three times, including one live self-correction (1b→1) and one two-month revision (May → July). The category is what the event *is filed as*; the image is what happens to the person in the room.

**The body is an arc with a clock in it.** Verbs in sequence: *collect data and code Saturday, train overnight, and demo at Sunday's live judging*. *Get checked in, form your team, get matched with a robot, and start hacking.* A reader should be able to feel time passing. Static description of features is the 1b failure.

**Receipts are bare numbers and real names, placed after the arc and before the logistics.** "80 curated spots, closing in on 300 applications; sponsors include Rerun, Modal, and LiveKit." "60-80 hackers… 6,000 sq ft." Names carry affiliation depth where there's room: "Jose M. Alvarez, Director of Research at NVIDIA (Autonomous Vehicle Applied Research, Sanja Fidler's Spatial Intelligence Lab)." One number per fact, matching the ledger — an unresolved number gets resolved, not averaged.

**Scarcity is stated as a fact with its consequence, never as pressure.** "80 curated spots." "Approval-gated and capacity-capped." "We expect a full house, so please plan to arrive early… if we hit capacity, we may not be able to accommodate late arrivals." Observed three times. She never writes "limited spots," "filling fast," or "don't miss out" — those appear only in drafts she didn't write.

**Logistics land last and flat, and their shape depends on the surface.** Forwardable blurb: one unlabeled trailing line, *date – venue, city – link*. Personal invite riding on a Luma card: no date line at all, just the day as a word in the closing sentence. Newsletter: the date leads the bolded header. Blast: location on its own line above the schedule, schedule grouped by day with the time first.

**The CTA is a door, not an imperative.** "I'd love to have you in the room Wednesday." "See you tomorrow." "Request a spot and we'll curate fast: [link]." A forwardable blurb often has no CTA at all — the bare link is the CTA. Warmth comes from the invitation, never from adjectives or exclamation marks.

**Person changes with the surface.** Forwardable blurb is fully third person, no "we" — because a stranger's newsletter will print it. Invites, blasts, and newsletters are first-person plural, "we" and "our." Observed twice each. Getting this wrong is the fastest tell that copy was assembled rather than written.

**Sensory nouns do the work adjectives would.** "Papers over dinner." "A live robot demo." "G1 humanoid, SO-101 arms, and rovers." "3D-printed clubs working the green." Present in every specimen without exception. If a phrase could describe any event, it is not finished.

**Complete sentences, hypotactic gait, one fragment maximum.** Clauses lean into each other with *and / so / plus / which*. Concision comes from word choice, not from chopping. Specimen 2 is 46 words and four complete sentences.

**Exclamation marks are earned, one per piece at most, in the greeting.** Specimen 2 has exactly one. Specimens 1, 1b, 3, and 4 have zero.

**Length bands.** Forwardable blurb: 55–70 words, four sentences plus a link. Personal invite: 40–50 words, three to four sentences. Newsletter entry: 90–110 words per event, plus a frame line and a one-line close. Logistics blast: prose capped near 130 words wrapped around the schedule block, which runs as long as it must.

**The edition or series marker earns attention.** "First hardware edition of the series." "#15." "Their 137th." It is a receipt about the thing's history, and it costs three words.

---

## Candidates — observed once, not yet law

Do not apply these as rules; use them if they fit and note the second sighting so they can promote.

- *"A quick note up front:"* as the lead for the single thing that matters in a logistics blast (specimen 3).
- An intent line before the schedule — *"The goal for Friday is simple: …"* (specimen 3).
- Naming the next channel at the end of a blast (WhatsApp group + link) (specimen 3).
- Mass-blast sign-off as *"Mattie & The [Event] Team"* rather than *"– Mattie"* (specimen 3).
- The semicolon joining the receipt clause to the sponsor list (specimen 1).
- A frame line opening a multi-event newsletter and a one-line close after it — approved by send, but Scav-written, so it needs a Mattie-authored sighting to promote (reference newsletter).

---

## Firewall — three registers this must not become

**1. Not the executive-email register.** Do not import bold full-sentence headers, the sectioned option-recap shape, or "a skim of the bolds tells the story." That structure serves a peer reading an email they may forward; it makes an event listing read like a memo about the event. **Bold appears in exactly one place in this register:** a date + event-name label in a multi-event newsletter. Never a full-sentence header. Never in a Luma description, a blurb, or a personal invite. No "Next step on our end is…" framing — an event's next step is the reader showing up.

**2. Not the casual burst register.** `draft-mattie`'s "short over comprehensive, punchy fragments OK" produces specimen 1b — the spec sheet she threw out. Do not stack fragments. Do not chop sentences for punch. Do not let lowercase-energy openers ("heya," "heck yeah") into anything an audience reads at scale; they belong in a DM. The DNA rules that *do* carry over are What / So What / Now What, no negation leads, telling detail over generic compliment, and concrete asks with a vehicle.

**3. Not LLM event copy.** Cut on sight, no exceptions:
- "Join us for an exciting…" / "You're invited to an unforgettable…" / "We're thrilled to announce…"
- Hype adjectives standing in for receipts: incredible, amazing, unforgettable, world-class, cutting-edge, game-changing, star-studded lineup. If you can't replace it with a number or a proper noun, delete it.
- Urgency theater: "Don't miss out," "Spots are filling fast," "Last chance," "Apply now" as a standalone imperative line, countdown framing.
- Exclamation stacking, and any exclamation outside a greeting.
- Emoji bullets, rocket and fire emoji, emoji as section markers.
- Rule-of-three verb chants — "Build. Ship. Demo." — and any tagline that survives find-and-replacing the event name.
- "Whether you're a X or a Y, there's something for everyone."
- Hashtag piles.
- A closing line that thanks the reader for reading.

**4. The floor crutch.** "On the floor" is killed as a crutch (Mattie, 7/27: *"we lean on it a bit too much"*). This register is the worst offender because every event happens there. Ration the whole floor family — "our floor," "takes over the floor," "on the floor" — to **once per piece, maximum**, and prefer the specific thing: "robots running," "a Franka and a G1 out," "the mini-golf course back in action."

---

## Scrub pass — run before presenting anything

1. **Card check.** Every fact in the draft traces to the event card. Anything that doesn't, either verify it or cut it. Nothing marked `[unverified]` ships as fact.
2. **Boilerplate check.** NT and MR copy is character-identical to `blurbs.md`. Slots are separate and named. No Khosla. No internal R&D specifics. No sentence that fuses the two entities.
3. **Numbers check.** Every number matches the ledger, one number per fact, no averaging an unresolved figure.
4. **Opener check.** Does the first sentence carry an image, or does it name a category? If category, rewrite.
5. **Arc check.** Does the middle move through time, or list features?
6. **Adjective sweep.** Every evaluative adjective either becomes a number, becomes a proper noun, or dies.
7. **Person check.** Third person for the forwardable blurb; first-person plural everywhere else.
8. **Floor-family count.** One, maximum.
9. **Punctuation.** En-dashes (–), never em-dashes. One dash-aside per paragraph. Exclamations at most one, in the greeting.
10. **Banned words.** No "lock / lock in / locked." No "funded" in outreach copy. No hollow assertions ("a sharp bet," "an exciting opportunity") — name the specific true thing.
11. **Fragment count.** One maximum. Complete sentences otherwise.
12. **Generic test.** Find-and-replace the event name with a competitor's. If the copy still reads fine, it isn't finished.

---

## Output contract

- **Return the copy in a fenced block**, ready to paste, with nothing to strip out.
- **Two variants whenever register could reasonably differ** — forwardable-third-person vs. first-person-invite, long-listing vs. tight-slot, blast vs. newsletter entry. Label each with the surface it's for and the word count. One variant only when the surface is unambiguous.
- **State the card you loaded** and, in one line, anything the card left open that the copy had to work around (unconfirmed speaker, unsettled number, listing owned by a co-host).
- **Everything stays draft.** Copy ships only when Mattie sends it or a Luma-gated human publishes it. **Luma writes are Mattie-gated** — never edit a listing, never publish, never fire a blast. If a co-host owns the listing, the deliverable is copy handed to them plus the sentence that hands over the motion without holding it hostage.
- **Flag, don't fix, anything the card marks as a human gate.**
- After a send, the piece is `/absorb` material: diff what she actually shipped against what was staged, and route the deltas to `newt/docs/devrel/voice/deltas.md`. Two sightings promote a candidate here into a rule.

## Final lint (mandatory, last pass)

Run the copy pass against `newt/docs/devrel/voice/style-guide.md` — the usage law: dashes, banned words, density, structure. The guide wins over anything in this file if they ever disagree; it is the living terminus of the /absorb loop.
