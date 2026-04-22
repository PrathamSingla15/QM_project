# 06  - FMEA: Failure Mode and Effects Analysis

## Tool
Failure Mode and Effects Analysis (FMEA). Reference: Ch.10 Reliability Engineering and Risk Analysis.

## Purpose
FMEA is a systematic, proactive method for identifying how a product, process, or system might fail, assessing the severity of each failure's effect on the end-user, estimating how likely each failure is to occur, and evaluating how detectable each failure is before it reaches the customer. For each failure mode, three scores (Severity, Occurrence, Detection, each on a 1-10 scale) are multiplied to produce a Risk Priority Number (RPN). High RPN items require the most urgent mitigation. FMEA is applied before launch to prevent failures rather than react to them.

## Application in Our Project
We applied FMEA to ten edge cases identified during the design review of the E-rickshaw app. These edge cases represent scenarios that do not occur in the current cash-and-manual system but emerge specifically because the app introduces digital booking, wallet payments, real-time location tracking, and the "Reached" driver confirmation flow. Severity, Occurrence, and Detection scores were assigned using judgement calibrated to campus scale: a "10" in Severity would be a safety incident; a "10" in Occurrence would be an event that happens on every ride. The resulting table is sorted by RPN in descending order. The full table is also exported as fmea.csv for reuse in the presentation deck and the React prototype's test-case documentation.

## Key Findings and Insights
The three highest-RPN items reveal a pattern:
- **Driver goes offline / GPS lost (RPN 126)**: The highest risk because it combines a mid-ride safety concern (Severity 7) with poor detectability (Detection 6). The app must assume connectivity can fail and handle it gracefully in the client, not just in the server.
- **Cancellation-fee dispute (RPN 120)**: High because there is currently no in-app resolution path, meaning disputes escalate to verbal confrontations. Detection is poor because there is no audit trail.
- **Wallet insufficient at ride-end (RPN 100)**: Uniquely dangerous because the failure occurs after the service has been delivered, leaving the driver with no recourse. A pre-ride balance check or soft debt cap is mandatory, not optional.

## How It Informs the Solution
Each mitigation listed in the FMEA maps to a specific app business rule or UI requirement. The top-3 RPN mitigations, in particular, become P0 requirements for the MVP: a 30-second heartbeat with offline-continuation mode, a one-tap dispute flow, and a Rs. 50 soft debt cap with booking block. FMEA also clarifies that three of the ten edge cases (seat-stealing, race condition, driver mistake) require server-side enforcement, not UI warnings alone, which has direct implications for the backend architecture.
