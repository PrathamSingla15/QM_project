---
title: "App Slides Presenter Guide"
subtitle: "Slides 9 to 13 - Proposed Solution Overview - Live demo script and refinements"
author: "Group 2, TQM Course Project, IIT Roorkee"
date: "April 2026"
---

# How to use this guide

These five slides (9 to 13) are your live product demo. The audience will watch
the app on the projector while you narrate. The slide itself is a reminder
card, not a reading document, so the rule is simple:

- The slide shows a **screenshot + 2 or 3 short bullets**.
- You speak in **plain sentences**, pointing at specific parts of the UI.
- The live app does the work of proving the product actually runs.

For each slide below you will find four sections:

1. **What is on the slide today** - a quick summary so you know what the
   audience is seeing.
2. **What to refine** - small content changes that make the bullets land
   harder in a live demo.
3. **Presenter script** - word for word, in simple English. Read it out
   loud once. It should take about 60 to 75 seconds per slide.
4. **Live demo sequence** - exactly what to click, in order, while you
   speak. This is the part that separates a confident demo from a shaky
   one.

Total target time for the five slides: **5 to 6 minutes**.

Keep your cursor steady, do not rush the clicks, and speak one sentence
at a time.

\newpage

# Slide 9 - App - Student Map

## What is on the slide today

- A screenshot of the student view with the SVG campus map on the left,
  four E-rick cards in the centre, and a wallet panel on the right.
- Two bullets:
  - 100 m proximity radius shows all drivable options without overwhelming the view.
  - Passenger count and destination visibility per E-rick lets the user pre-match intent.

## What to refine

The two bullets are correct but they speak about the feature, not about
what the student feels. For a live demo, replace with three crisper
bullets that answer the three questions the audience has when they look
at the screen:

- **What is on this screen.** Live map. Four E-ricks. Each card shows the
  driver, current passenger count, and existing passengers' drop-offs.
- **Which pain point it kills.** Route mismatch. You can see before
  booking whether the ride is going where you are going.
- **Why 100 m.** Campus distances are short; anything further is not a
  usable ride.

Also, move the "Wallet Rs 180" highlight to this slide so the audience
notices the wallet is already pre-loaded. It makes the next slide's
payment demo feel natural.

## Presenter script

> "This is the student's first screen. When you open the app, you see
> every E-rickshaw within a 100 metre radius on a live campus map.
>
> Look at the middle column. Each card shows the E-rick ID, the driver's
> name, how many seats are already filled, and - and this is the
> important part - where each existing passenger is going.
>
> So before you book, you can see that ER-01 has two passengers both
> heading to Central Library. If your destination is also near the
> library, you book that one. If not, you pick ER-04 which is going
> somewhere else.
>
> This solves our first pain point, route mismatch. Today on campus, you
> board an E-rick and only then find out it is going to take a detour.
> Here, the information is in front of you before you commit."

## Live demo sequence

1. Open the app at the Student view.
2. Move the mouse slowly across the four E-ricks on the map, then across
   the four cards. Say the line "Every E-rick within 100 m".
3. Point at ER-01. Read out the two drop-offs.
4. Point at ER-02 which is full. Say "Full E-ricks turn dark red so you
   don't waste a tap."
5. Hover over the "Wallet Rs 180" pill in the top right. Say "Your
   wallet is visible at all times, so you always know if you can afford
   the ride."

\newpage

# Slide 10 - App - Booking + Countdown

## What is on the slide today

- Two screenshots: the booking modal (left) and the active countdown
  state (right).
- Three bullets:
  - Drop-off dropdown backed by 43 grouped campus locations; single tap confirms.
  - 60-second countdown ensures minimal wait time.
  - Expired booking auto-cancels and debits Rs 5.

## What to refine

The bullets are strong, but add a line that makes the 60 seconds feel
like a **commitment device**, not a timer. In TQM language this is a
**Poka-yoke** (error-proofing) - it prevents the behaviour that creates
the problem (students booking then not showing up). Say the word
"commitment" out loud. That is the story.

Also: the right screenshot on the current slide is tiny. In the refined
version, put the countdown screenshot slightly bigger and crop out the
unused whitespace.

Refined bullet list:

- **Dropdown with all 43 real IITR locations** - 4 groups: hostels,
  departments, gates, facilities.
- **60-second countdown = commitment** - Poka-yoke. Stops students from
  booking and not showing up.
- **Rs 5 auto-cancel fee** - soft enforcement. Not a punishment, a
  nudge.

## Presenter script

> "This is what happens the moment you tap 'Book Seat'. A small window
> opens. You pick your drop-off from a dropdown, and the dropdown is
> organised into four groups - hostels, academic departments, gates, and
> campus facilities. All 43 real locations. One tap to confirm.
>
> The second screen is the most important one. As soon as you confirm,
> a 60 second countdown starts. This is not just a timer. In TQM we
> call this a Poka-yoke, an error-proofing mechanism. It forces the
> student to actually reach the E-rick in one minute.
>
> If you don't reach in time, the booking is auto-cancelled and 5 rupees
> are deducted from your wallet as a cancellation fee. This is the
> smallest nudge possible - not a punishment, just enough to make
> students commit only when they really mean to board."

## Live demo sequence

1. Click **Book Seat** on ER-01 card.
2. In the booking modal, open the drop-off dropdown. Scroll through the
   4 groups (hostels, departments, gates, facilities) slowly so the
   audience sees the scale.
3. Pick "Govinda Bhawan" or any hostel. Point at the Rs 10 fare line.
4. Click **Confirm - Start 60 s Hold**.
5. As the countdown ring starts, narrate: "See the ring? That is your
   commitment."
6. Point at the wallet pill in the top right - it should now say "Rs 5
   held". Say: "Five rupees are held, not yet deducted."
7. **Do not** wait for the countdown to expire live. Click **Cancel
   Booking** manually instead, so you can move on.

\newpage

# Slide 11 - App - Wallet & Payment

## What is on the slide today

- A single screenshot of the Wallet panel showing a Rs 180 balance,
  TOP UP Rs 50 and +Rs 100 buttons, and two recent rides.
- Three bullets:
  - Wallet holds a booking-side 'hold' so fare appears debited immediately on booking.
  - Ride history is immutable - every debit and cancellation fee surfaces transparently.
  - Pre-linked driver accounts eliminate manual transfer step.

## What to refine

Strong technical content but missing the business insight. The wallet
directly kills **Pain Point 3: Payment Leakage** (the cash-missing
problem). Make that connection explicit.

Also add: **"Why this matters to the driver"** - the driver gets paid
automatically on ride completion. No "bhaiya, mere paas change nahi hai"
situation. Add this because drivers are stakeholders too.

Refined bullets:

- **Kills Pain Point 3 - payment leakage.** Auto-debit on drop-off means
  no missed fares. Zero leakage.
- **Driver sees money immediately.** Pre-linked driver account, instant
  credit. No cash, no change, no awkwardness.
- **Transparent ride history.** Every debit and every Rs 5 cancellation
  fee is logged. Students can dispute in one tap.

## Presenter script

> "This is the wallet. It is the part of the app that solves our biggest
> driver-side pain point: payment leakage.
>
> Today, students pay in cash. Drivers carry no change, some students
> forget to pay when they are running to class, and drivers have no way
> to track who owes what. Our survey found that 47 percent of students
> admitted to at least one payment-related issue.
>
> In our app, the student pre-loads the wallet. When you book a ride,
> five rupees are held. When the driver marks 'Reached' and the ride
> completes, the full fare is auto-debited from the wallet and credited
> to the driver's linked account instantly. No cash, no change, no
> disputes.
>
> The ride history is immutable. Every debit, every cancellation fee,
> every top-up is logged. So if something looks wrong, the student can
> raise a dispute with one tap."

## Live demo sequence

1. Switch to the Student view if you are not already there.
2. Point at the wallet panel on the right. Read out the balance: "Rs
   180 pre-loaded."
3. Click **TOP UP Rs 50**. Point at the balance: "Now Rs 230. In
   production this would hit a UPI gateway."
4. Point at the "Recent Rides" list. Read one entry out:
   "Main Gate to Dept of CSE, minus Rs 10."
5. Say: "Every ride, every fee, logged forever. Zero leakage."

\newpage

# Slide 12 - App - Driver View

## What is on the slide today

- Screenshot of the driver's view with a campus map on the left, a
  passenger manifest in the middle, and a "Shift digest" KPI panel on
  the right.
- Three bullets:
  - 'Mark Reached' locks the seat to the physically-present student (solves seat-stealing).
  - Offline-add handles walk-up passengers and keeps all student apps in sync.
  - Shift digest shows the driver's daily revenue, helping them keep track of their earnings.

## What to refine

Good content. Two refinements:

1. The audience may not know what "seat-stealing" means. Spell it out in
   the script: "Student A books a seat. Student B physically walks up
   and boards before A arrives. Who pays? The app resolves this
   cleanly."
2. Emphasize that this is a **two-sided product**. Most student apps
   ignore the driver. Ours does not. Drivers get a console with their
   own KPIs. This earns their buy-in.

Refined bullets:

- **'Mark Reached' locks the seat.** Physically-present student wins.
  Solves seat-stealing.
- **Offline-add keeps everyone in sync.** If a passenger walks up
  without using the app, the driver adds them in one tap. Other
  students' apps update instantly.
- **Shift digest gives the driver agency.** Today's revenue, today's
  rides, today's fill rate. Drivers are stakeholders, not just
  ride-providers.

## Presenter script

> "The driver's view is often missing from student-side apps. Ours
> doesn't skip it.
>
> On the left, the driver sees their own E-rick on the campus map. In
> the middle, a live manifest of all passengers who have booked or
> boarded. Each passenger row shows their name and drop-off.
>
> Here is the key button - 'Mark Reached'. When a booked student arrives
> at the vehicle, the driver taps this. The app then locks that seat to
> that specific student. This prevents seat-stealing - when one student
> has booked but another physically boards first.
>
> Below the manifest there is an 'Add offline passenger' form. If
> someone walks up without using the app - which will happen often in
> the first few weeks - the driver adds them manually. This updates
> the map for every other student within 100 metres in real time.
>
> And on the right is the shift digest. Today's revenue, rides
> completed, fill rate. This is important for adoption. Drivers will
> only use this app if they can see their own earnings."

## Live demo sequence

1. Click the role switcher in the top right. Pick **Driver**.
2. Wait for the view to load.
3. Point at the campus map: "This is where the driver sees their
   position."
4. Point at the passenger manifest. Read out two rows.
5. Click **Mark Reached** on the first passenger. Wait for the 5-sec
   undo toast to appear. Say: "See the undo? If the driver tapped by
   mistake, they have 5 seconds to reverse."
6. Scroll down to **Add offline passenger**. Type any name like
   "Pratham". Pick "Main Library" from the dropdown. Click **Add**.
7. Quickly switch back to Student view. Say: "Look - the offline
   passenger I just added is now visible to every student on campus."
8. Switch back to Driver. Point at **Shift digest**. Read the KPIs.

\newpage

# Slide 13 - App - Admin Dashboard

## What is on the slide today

- Screenshot of the admin view showing five KPI tiles (completed rides,
  average wait, revenue, leakage, empty return), a fleet table, and a
  live fleet-position map.
- Three bullets:
  - Previously invisible KPIs (wait, leakage, empty return) become first-class metrics.
  - Identifying operational inefficiencies like idle vehicles, empty trips.
  - Live map enables real-time fleet monitoring to prevent congestion.

## What to refine

This slide is the **payoff of the whole TQM lens**. Before our app,
campus admin had no idea what the wait time was, no idea what the
leakage rate was, no idea what the empty-return rate was. None of
those three KPIs existed. Now they are on a single screen, live.

Link this directly to the PDCA **Check** phase - these are the exact
KPIs that the rollout cycle will measure.

Refined bullets:

- **From invisible to first-class.** Avg wait, fare leakage %, empty
  return % - none of these were measured before. Now they are, live.
- **Powers the PDCA Check phase.** Cycle 1 uses exactly these numbers
  to decide whether to expand or iterate.
- **Live map = operational response.** A stranded vehicle, a bunched
  zone, an idle driver - admin sees it immediately.

## Presenter script

> "This is the admin dashboard. It is the part that makes our project a
> TQM intervention, not just a student convenience app.
>
> Before this app, our institute had no way to measure E-rick service
> quality. How long do students wait? Nobody knew. How much fare leaked
> because of cash issues? Nobody knew. How often does an E-rick return
> empty? Nobody knew. All three of these numbers were invisible.
>
> On this screen they are first-class metrics. 128 rides completed
> today. 4.2 minutes average wait. Rupees 1840 revenue. Zero percent
> leakage because every rupee is wallet-mediated. 11.4 percent empty
> return.
>
> Why does this matter? Because in our PDCA rollout plan, the Check
> phase uses these exact KPIs. We measure them for two weeks, compare
> against baseline, and decide whether to expand the pilot or iterate.
> The admin dashboard is the evidence collector.
>
> The live map at the bottom is for operational response. If a vehicle
> gets stranded or a zone gets over-crowded, the admin can re-route.
> Not just a dashboard - a control room."

## Live demo sequence

1. Click the role switcher. Pick **Admin**.
2. Walk through the five KPI tiles in order. Read each tile's number
   and label.
3. Hover on the leakage tile (0.0%). Say: "Before the app this was
   unknown. Now it's zero, because everything is wallet-debit."
4. Point at the fleet table. Read two rows.
5. Point at the live map. Say: "Admin sees every E-rick's live
   position."
6. Close out: "This is the dashboard that turns our TQM tools from a
   one-time study into a continuous-improvement loop."

\newpage

# Overall tips for the app section

## Flow

The order is deliberate: **Student (9) -> Booking (10) -> Wallet (11)
-> Driver (12) -> Admin (13)**. You are walking the audience through a
ride, end to end. Do not shuffle.

## Transitions between slides

After each slide, add one bridging sentence before you tap "next":

- After slide 9: *"So the student has discovered the E-rick. Now, how
  do they actually book it?"*
- After slide 10: *"The seat is held. Now, how does the money move?"*
- After slide 11: *"The student side is clear. But every good product
  has two sides. Let's look at the driver."*
- After slide 12: *"Both sides are served. But who watches the system
  as a whole?"*
- After slide 13: *"That closes the proposed-solution section. Next,
  we'll cover the risk analysis..."*

## Tone

- **Concrete, not abstract.** Say "128 rides today", not "ride
  completion metrics".
- **Short sentences.** Ten words or fewer per sentence where you can.
- **One pause per click.** Let the screen catch up.

## What NOT to do

- Do not read the slide word for word. The audience can read. Your job
  is to add context.
- Do not switch between Student and Driver views more than twice. It
  gets disorienting.
- Do not let the 60-second countdown expire live. It kills your
  momentum. Cancel manually.
- Do not apologise for the prototype. Say "this is the MVP" instead.

## If something breaks during live demo

- If the dev server stalls: refresh the page. The reducer state resets
  but the layout is the same; no audience will notice.
- If the role switcher does not respond: click on the Student label
  first, then the target role.
- If a click does nothing: narrate over it. "In the production version
  this would open the booking modal. Let me walk you through the logic
  instead."

## Time budget

| Slide | Min | Max |
|---|---:|---:|
| 9  Student Map         | 50 sec | 70 sec |
| 10 Booking + Countdown | 70 sec | 90 sec |
| 11 Wallet              | 50 sec | 70 sec |
| 12 Driver View         | 70 sec | 90 sec |
| 13 Admin Dashboard     | 60 sec | 80 sec |
| **Total**              | **5 min** | **6 min 40 sec** |

Practice twice with a stopwatch. Cut anything that drags.

## Closing reminder

The best live demo is not the one with the flashiest features - it is
the one where the presenter looks like they use the product every day.
Click with purpose, speak with confidence, and leave the technical
jargon for the Q&A.

Good luck. This project is solid.
