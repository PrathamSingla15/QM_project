# E-Rickshaw Service Quality at IIT Roorkee: Problem Framing and Solution Design

**Team A | Total Quality Management Course Project**
**IIT Roorkee | Academic Year 2025-26**

---

## Table of Contents

1. Executive Summary
2. Problem Statement
3. Stakeholder Map
4. Proposed Solution
5. Business Rules and Constraints
6. Edge Case Handling
7. Success Metrics and KPIs
8. Drop-off Location List (IIT Roorkee - April 2026)

---

## 1. Executive Summary

IIT Roorkee's campus e-rickshaw service connects hostels, academic blocks, and common facilities across a large, spread-out campus. Despite being the primary short-distance transit option for students, the service suffers from four compounding failures: route mismatches that force unnecessary detours, a forced-fill policy that holds passengers until all seats are occupied, a cash-only payment model with measurable fare leakage, and systematic empty return trips that reduce driver earnings and asset utilization. These four pain points are not isolated - they form a reinforcing cycle that depresses demand, hurts driver income, and erodes service quality over time.

The proposed solution is a mobile application serving both students and drivers. Students gain proximity-based E-rick discovery, real-time passenger and drop-off visibility, seat booking with a fixed campus drop-off list, and in-app wallet payment. Drivers gain a passenger management interface, offline boarding entry, and a "Reached" confirmation workflow. A 1-minute boarding window with a Rs. 5 cancellation fee replaces informal waiting norms. The target outcomes are average boarding wait below 2 minutes, payment leakage below 0.01%, and empty return trips below 10% of driver shifts. All current baseline figures are planning-phase estimates; post-pilot measurement will establish the actual benchmark.

---

## 2. Problem Statement

### Campus Context

IIT Roorkee spans approximately 365 acres. The distance between the main hostel cluster and the far academic departments is sufficient that walking is impractical during peak hours, especially in summer heat or monsoon rain. Campus e-rickshaws are the default short-haul transport for a student population of roughly 7,000. Each e-rickshaw is a 4-seat electric vehicle licensed to operate within campus boundaries. Drivers are individual contractors - not salaried employees - so their income depends directly on the number of completed trips per hour.

### Pain Point 1: Route Mismatch Wastes Time in Emergencies

When 4 passengers board with 4 distinct destinations, the driver must serve all stops, turning a 4-minute direct ride into a 12-15 minute multi-stop detour (student-reported estimate, not measured). Students heading to an exam or a scheduled viva have no visibility into where co-passengers are going before they board. A student who would otherwise walk 3 minutes ends up spending 15 minutes in a detour-heavy ride. This unpredictability is highest during transition periods between lectures, precisely when punctuality matters most.

### Pain Point 2: Forced-Fill Delay

Drivers informally enforce a policy of not departing until all 4 seats are filled. At low-demand periods - early morning, post-lunch lull, late evening - a student may wait 10-20 minutes before the vehicle departs (student-reported; no systematic measurement exists). This makes the service unreliable for anyone with a fixed appointment. The forced-fill policy is rational for drivers (maximizes per-trip revenue) but irrational for service quality and overall demand. Students who experience repeated delays shift to walking or cycling, reducing fill rates further and reinforcing the driver's incentive to wait longer.

### Pain Point 3: Payment Leakage

The current system is entirely cash-based. Fares are paid informally - typically Rs. 10-20 per trip depending on distance. Students report that fare collection is inconsistent: drivers sometimes forget to collect, students sometimes underpay or board without paying in the rush of a full vehicle, and there is no audit trail. Drivers estimate (informally, not systematically) that 5-8% of trips generate no fare or a reduced fare. This is material for a contractor earning on a per-trip basis. Cash handling also creates friction - no change, denomination mismatches, and social awkwardness when a student tries to avoid payment.

### Pain Point 4: Empty Return Trips

After completing a set of drop-offs, drivers return to their home zone or a preferred pickup point. This return leg is typically empty - no passengers, no revenue, no asset utilization. On a campus where demand is geographically clustered by timetable, a driver who completes a trip to the far academic zone at 9:15 AM (when all students have already reached class) faces a dead-mile return with no pickup opportunity. Based on informal observation, empty returns may account for 25-35% of vehicle operating time (planning-phase estimate, to be measured in the pilot survey).

### Systems-Thinking Observation: The Vicious Cycle

The four pain points do not operate independently. Payment leakage reduces driver income, which increases pressure to enforce forced-fill waiting to maximize per-trip revenue, which increases student wait time and unpredictability, which reduces demand among students who have alternatives, which reduces fill rates and makes forced-fill waits even longer, which further pressures driver income. Route mismatches add trip time without adding revenue, reinforcing the same income pressure. Empty returns compound it. The system is in a self-reinforcing degradation loop - each failure mode tightens the others. Any single-point intervention (e.g., enforcing a no-wait policy without fixing payment) will be resisted by drivers with legitimate economic justification. An effective solution must address all four pain points simultaneously.

---

## 3. Stakeholder Map

### Stakeholder Summary

The service involves five distinct stakeholder groups. Students are the primary customers and app users. Drivers are both service providers and a key secondary customer of the economic model. Campus administration sets policy and contractual terms. Campus security controls identity and gate access. A payment gateway vendor handles the financial infrastructure.

| Stakeholder | Primary Interest | Influence Level | Current Pain | What They Gain |
|---|---|---|---|---|
| Students | Reliable, fast, affordable transport | High (demand-side) | Unpredictable wait times, route detours, cash friction | Predictable boarding, upfront drop-off visibility, seamless wallet payment |
| Drivers (E-rick operators) | Maximize trips per hour and minimize dead miles | High (supply-side) | Income loss from leakage, empty returns, informal fill wait | Auto-fare collection, passenger demand signal, reduced empty returns via return-pickup |
| Campus Administration | Service quality, safety, contractual compliance | High (policy) | No data on service utilization or quality metrics | Usage analytics, audit trail, leverage to enforce service standards |
| Campus Security | Identity verification, gate-access control | Medium (gate ops) | No passenger identity log, security incidents hard to trace | Digital passenger manifest per trip, accountability chain |
| Payment Gateway Vendor | Transaction volume, integration uptime | Low (external infra) | N/A | Revenue from transaction fees, B2B campus contract |

---

## 4. Proposed Solution

The solution is a mobile application with separate interfaces for students and drivers. The underlying architecture supports real-time state synchronization so that passenger count, drop-off assignments, and driver location are consistent across all devices in a given trip at all times.

### 4.1 Student Features

**Proximity Discovery.** The student opens the app and sees a live map centered on their current location. All E-ricks within a 100-meter radius appear as pins. The radius threshold ensures only operationally reachable vehicles are shown - not vehicles 500 meters away that will fill before the student arrives.

**Ride Visibility.** Tapping any E-rick pin opens a detail card showing the current passenger count (e.g., "2/4 seats") and each booked passenger's drop-off point drawn from the fixed campus location list. This gives the student the information they need to decide whether the route aligns with their destination before booking. A student going to the Main Library who sees two passengers heading to Kasturba Bhawan and one to the Sports Complex can make an informed decision about whether to board or wait for a better-aligned vehicle.

**Booking.** The student taps "Book Seat" and selects their drop-off from a dropdown populated with the fixed campus location list (see Section 8). The booking is submitted to the server. If the seat is available, it is reserved. If two students submit simultaneously, the server applies first-write-wins and returns a "Seat taken" error to the slower submission with a nearest-alternative suggestion.

**Wallet Payment.** The student's in-app wallet is pre-loaded via bank transfer or UPI top-up. On booking confirmation, no charge is made yet. When the driver presses "Reached" to confirm the student has boarded, the fare is auto-deducted from the wallet in a single server-side transaction. The driver's account is pre-linked; no manual transfer is required. The student receives a push notification with the deducted amount and remaining balance.

### 4.2 Driver Features

**"Reached" Confirmation.** When a booked student physically boards the vehicle, the driver presses the "Reached" button next to that student's name in the trip panel. This action serves three functions: it locks the student's seat, triggers fare deduction from the student's wallet, and records the boarding timestamp. The action has a 5-second undo window to handle accidental taps. After the window closes, the transaction is considered confirmed and can only be reversed through the dispute flow.

**Offline Passenger Entry.** If a student boards physically without having booked in-app - for example, a student who does not have the app or whose app is offline - the driver can add them manually. The driver selects "Add Offline Passenger," enters the drop-off location from the same fixed campus list, and the app updates the visible passenger count and drop-off list for all other passengers in real time. Offline passengers pay cash; the driver's in-app ledger notes the offline entry for record-keeping purposes.

### 4.3 Wallet and Payment

The wallet operates as a pre-paid balance with a soft credit limit. Students top up via UPI or bank transfer. Fares are auto-deducted at boarding confirmation. If the wallet balance is insufficient at the time of deduction, the ride completes and the wallet is allowed to go negative up to a Rs. 50 soft cap. The negative balance is treated as a debt - it is cleared on the next top-up, and new bookings are blocked until the debt reaches zero. This design avoids stranding a student mid-campus due to a payment failure while still enforcing financial accountability.

Driver accounts receive fare credits in real time. Drivers can withdraw accumulated balance to a linked bank account through a standard settlement flow outside the scope of this document.

### 4.4 Map and Discovery

The map layer polls the server for E-rick positions at a configurable heartbeat interval (target: every 5-10 seconds). Each E-rick transmits GPS coordinates and current passenger state. If an E-rick stops transmitting (driver goes offline or network drops), the server marks it as "connection lost" after 30 seconds and removes it from active discovery until the heartbeat resumes. Students already in a trip with that driver see a "Connection issue - ride continues offline" banner; fare finalization happens on reconnect.

When two E-ricks occupy the same map location (e.g., both waiting at Main Gate), the map renders a stacked card list in a side panel rather than overlapping pins. The user selects the preferred vehicle based on visible passenger count and drop-off alignment.

---

## 5. Business Rules and Constraints

**1-Minute Boarding Window.** After a student confirms a booking, a 60-second countdown begins. The student must physically reach the E-rick and be confirmed by the driver (via "Reached") within that window. If the countdown expires without a "Reached" action, the booking is automatically cancelled, Rs. 5 is deducted from the student's wallet as a cancellation fee, and the seat is released for new bookings. The Rs. 5 fee is a deterrent against casual over-booking, not a revenue mechanism; it is credited to a platform escrow account and is subject to refund via the dispute flow.

**Seat Capacity.** Each E-rick has a hard capacity of 4 seats. The system enforces this at the booking level - once 4 seats are booked or occupied (including offline passengers added by the driver), no further bookings are accepted for that vehicle. Offline passengers added by the driver count against capacity; the app raises a hard block if the driver attempts to add a fifth passenger.

**Zone-Based Driver Homing.** Drivers are assigned a home zone at registration. When returning from a drop-off run, the app can suggest pickup opportunities along the return route to the home zone, targeting the empty-return problem. The zone assignment is an administrative configuration parameter; the logic for return-trip suggestion is out of scope for this document's version.

**Drop-off List.** The campus location list used in the app's drop-off dropdown is the official IIT Roorkee destination list confirmed in April 2026, comprising 43 locations across Hostels, Academic Departments, Gates, and Campus Facilities. The full list is provided in Section 8.

**Cash Fares for Offline Passengers.** Offline passengers added by the driver are not subject to in-app fare deduction. The driver collects cash as usual. The app records the offline entry for audit purposes but does not attempt to charge a wallet that may not exist.

---

## 6. Edge Case Handling

The table below defines the system behavior for each identified edge case. Rationale follows each entry.

| # | Scenario | System Behavior | Rationale |
|---|---|---|---|
| 1 | Seat-stealing: another student physically boards before the booking student arrives | Driver's "Reached" press locks the seat to whoever is physically present. The booking student's reservation is cancelled, Rs. 5 cancellation fee is waived, and the student receives a "Seat taken - booking refunded" toast notification. | Physical presence verified by the driver is more reliable than app state. The driver has no incentive to misidentify a passenger. Waiving the fee ensures the inconvenienced student is not penalized for an event outside their control. |
| 2 | Driver accidentally presses "Reached" for the wrong passenger | A 5-second undo toast appears on the driver's screen. If the driver taps "Undo" within the window, the action is reversed with no charge to the student's wallet. After 5 seconds, the transaction is confirmed and can only be reversed through the dispute flow, which requires admin review. | A short undo window balances error correction against gaming - a driver cannot use "undo" to repeatedly cancel confirmed fares. The 5-second window is long enough for a careful tap but short enough to prevent deliberate reversal after the passenger has exited. |
| 3 | Student's wallet balance is insufficient at fare deduction time | The ride completes normally. The wallet balance goes negative, up to a Rs. 50 soft cap. The negative balance is shown prominently in the wallet screen. New bookings are blocked until the debt is cleared. The next top-up first applies to clear the negative balance before adding new funds. | Blocking the ride at boarding would strand the student on campus, which is a worse outcome than a small negative balance. The Rs. 50 cap limits the platform's credit exposure to a manageable amount per student. |
| 4 | Two students attempt to book the last available seat within milliseconds of each other | The server applies first-write-wins at the database transaction level. The student whose request arrives first gets the seat confirmed. The other student receives a "Seat taken" notification immediately, along with a suggestion of the nearest available E-rick with open seats. | Atomic transactions at the server prevent double-booking. The nearest-alternative suggestion reduces the friction of rejection and keeps the user in the booking flow. |
| 5 | A booked passenger wants to change their drop-off location mid-ride | Drop-off changes are allowed until the driver presses "Reached" for that passenger's boarding confirmation. Once "Reached" is pressed, the drop-off is locked. A banner reading "En route - destination fixed" appears on the student's screen if they attempt to edit after locking. | Locking the drop-off at boarding confirmation gives co-passengers reliable route information from the moment the trip starts. Allowing changes before boarding accommodates legitimate last-minute decisions without destabilizing the committed route. |
| 6 | Driver's phone loses GPS signal or goes offline mid-trip | The server detects a missed heartbeat after 30 seconds. All passengers in the trip receive a "Connection issue - ride continues offline" banner. The trip record remains open. When the driver reconnects, the final state (drop-offs completed, fare adjustments) is synchronized and fare finalization runs at that point. | The ride should not be interrupted or fares charged incorrectly because of a network event outside the driver's control. Delaying finalization to reconnect preserves data integrity without disrupting the physical ride. |
| 7 | Driver attempts to add an offline passenger to a vehicle already at 4-seat capacity | The app displays a hard block: "Vehicle at capacity (4/4). Cannot add passenger." No passenger entry is created. The driver is not permitted to override this block. | Hard capacity enforcement is a safety and regulatory constraint. The app cannot participate in overloading the vehicle. The error message is clear so the driver can direct the would-be passenger to the next available vehicle. |
| 8 | Student disputes a Rs. 5 cancellation fee they believe was applied incorrectly | The student taps "Dispute" on the relevant entry in their ride history. The dispute is logged with a timestamp and submitted for admin review. The admin has a 24-hour window to resolve the case. During the review period, the disputed fee is placed in escrow and does not reflect as a debt blocking new bookings. | A lightweight dispute channel with a fixed resolution window gives students recourse without requiring synchronous interaction. The 24-hour window is operationally feasible for a campus-scale admin team and short enough to not leave students in limbo for days. |
| 9 | A student repeatedly fails to board within the 1-minute window (no-shows) | After 3 no-shows within any rolling 7-day window, the student's account is placed in a 1-hour booking cooldown. During the cooldown, new bookings are blocked. A "Reliability meter" visible in the wallet screen tracks the student's no-show history and resets after 30 days of clean behavior. | Repeat no-shows impose real costs - they block seats for other students and waste driver wait time. The escalating consequence is proportionate: a first no-show pays Rs. 5, a pattern triggers a temporary booking suspension. The 30-day reset avoids permanent penalization for a brief bad streak. |
| 10 | Two E-ricks are at the same GPS location simultaneously | The map does not overlay their pins. Instead, a side panel opens automatically listing both vehicles as stacked cards, each showing passenger count and drop-off destinations. The student selects the preferred vehicle from the list. | Overlapping map pins create ambiguity about which vehicle is being selected. The stacked card list preserves the full information needed for an informed booking decision (passenger count, drop-off alignment) while resolving the visual conflict. |

---

## 7. Success Metrics and KPIs

The following metrics define measurable success for the post-pilot evaluation. Current baseline figures are planning-phase estimates derived from informal student interviews and driver conversations. They are not measured data. The post-pilot survey (targeting 2 weeks of instrumented operation with 3-5 volunteer drivers and 50+ student users) will establish the actual pre-intervention baseline against which the system is evaluated.

**Average Boarding Wait Time.** Current estimate: 5-15 minutes at peak hours (student-reported). Target after app deployment: under 2 minutes from booking to "Reached" confirmation. Measurement method: server-side timestamp delta between booking event and "Reached" event, averaged across all completed trips per week.

**Payment Leakage Rate.** Current estimate: 5-8% of trips generate no fare or a reduced fare (driver-reported, informal). Target: below 0.01% of app-mediated trips (equivalent to approximately 1 missed fare per 10,000 trips). Measurement method: ratio of trips where "Reached" was confirmed but wallet deduction failed or was disputed, divided by total completed trips.

**Driver Empty-Return Percentage.** Current estimate: 25-35% of vehicle operating time is empty-return miles (planning-phase observation, not measured). Target: below 10% of driver shift time within 3 months of full deployment. Measurement method: GPS trace analysis - time between last "Reached" of a trip and first new booking acceptance, relative to total shift time.

**Student Net Promoter Score (NPS).** No current baseline exists. Target: NPS of +25 or above at the 3-month post-launch survey. Measurement method: in-app survey prompt after every 10th completed trip, asking the standard "How likely are you to recommend this service?" question on a 0-10 scale.

**App Weekly Active Students (WAS).** Target: 60% of the student body using the app at least once per week within 3 months of campus-wide launch. Measurement method: unique student accounts with at least one completed booking per 7-day rolling window, divided by total registered student population. This metric is the leading indicator of network effect - the app only improves route alignment as more students use it.

All five metrics should be tracked in a monthly dashboard visible to campus administration. Metrics that miss targets at the 3-month checkpoint should trigger a structured PDCA review cycle.

---

## 8. Drop-off Location List (IIT Roorkee - April 2026)

The following 43 campus locations form the confirmed drop-off selection list for both the student booking screen and the driver's offline passenger entry panel. This list was finalised in April 2026 and supersedes all earlier planning-phase drafts. Any future additions or removals must go through campus administration and be updated in the backend configuration, which propagates to both interfaces on next app sync.

### Hostels

Azad Bhawan, Ravindra Bhawan, Govinda Bhawan, Himalaya Bhawan, Vivekananda Bhawan, Vigyan Bhawan, Jawahar Bhawan, Sarojini Bhawan, Kasturba Bhawan, Rajeev Bhawan, Cautley Bhawan, Rajendra Bhawan, Radhakrishnan Bhawan, Ganga Bhawan

### Academic Departments

Metallurgical Engineering, Chemical Engineering, Hydrology, Earthquake Engineering, Earth Sciences, Civil Engineering, Architecture & Planning, Mechanical - East Block, Mechanical - West Block, Electrical Engineering, ECE, CSE, Chemical Sciences, Physics, HSS, Biotechnology

### Gates

Main Gate, Back Gate, South Gate, Solani Gate

### Campus Facilities

APJ Block, GB Block, Central Library, DOMS, Institute Hospital, Campus Temple, SAC (Student Activity Centre), MAC (Multi-Activity Centre), ICC (Indoor Complex)
