# 05  - Process Flowchart: Current State vs Future State

## Tool
Process Flowchart (Current State / Future State comparison). Reference: Ch.2 Basic 7 QC Tools.

## Purpose
A process flowchart documents every step, decision, and flow of a process using standardised symbols: rectangles for process steps, diamonds for decision points, and ovals for start/end terminals. A side-by-side current vs future state comparison is a standard Lean and TQM technique to make the waste in the current process visually explicit and to show exactly which steps the improved process eliminates or replaces. This format is more persuasive than prose descriptions because it makes delays and decision-failures visible as structural features of the process, not as exceptions.

## Application in Our Project
The current state flowchart maps the eight-step ride process as-is: arrival, variable wait, route-alignment check, boarding, farthest-first routing, sequential drop-off, cash payment, and empty return. Two decision diamonds are included: whether wait time exceeds a tolerable threshold (causing some students to abandon the queue) and whether the chosen route is acceptable (causing post-boarding regret but rarely actual exit). The future state flowchart maps the eight-step app-enabled ride: open app, discover nearby E-ricks, book with drop-off selection, 60-second boarding countdown, board and driver taps "Reached," ride starts with known route, auto fare deduction at drop-off, and driver receives next booking data for return trip.

## Key Findings and Insights
The comparison makes three improvements structurally visible:
- The current state has two decision diamonds where students bear the cost of uncertainty (wait-abandon and route-regret). The future state eliminates both by surfacing information before the student leaves their current location.
- The current state's cash payment step is a terminal step with no feedback path. The future state's auto-deduction removes this step entirely, replacing it with a system-generated receipt.
- The empty return is the last step in the current state and generates no revenue. The future state's "Driver sees nearby bookings" step transforms this dead time into productive system capacity.

## How It Informs the Solution
The flowchart comparison is the primary artefact for communicating the value proposition to campus administration and potential pilot drivers. It also confirms that the app introduces exactly one new constraint (the 60-second boarding window) while eliminating three major sources of waste (uncertain wait, cash friction, empty return). The boarding window is a trade-off that must be communicated clearly during onboarding, which is why the FMEA also treats this as an edge-case scenario.
