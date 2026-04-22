# 02  - 5 Whys Root Cause Analysis

## Tool
5 Whys Analysis. Reference: Ch.2 Basic 7 QC Tools (Root Cause Analysis techniques).

## Purpose
The 5 Whys is an iterative interrogative technique in which a problem statement is challenged with "Why?" at each step until the root cause is exposed, typically after five iterations. The method resists the temptation to treat symptoms as causes. It is most effective when the causal chain is linear and organizational, rather than statistical, in nature. The result is a single root cause statement that can be acted upon directly.

## Application in Our Project
The starting problem statement was: "Why do students waste time waiting for E-ricks?" We applied five successive "Why?" challenges. The chain progressed from the observable symptom (waiting) to operational policy (fill-before-dispatch), to incentive structure (earnings tied to seat-fills), to coordination failure (no demand aggregation), to information gap (no advance booking visibility), and finally to the technological gap (no digital booking system). The drill-down was kept strictly causal at each level rather than jumping to conclusions.

## Key Findings and Insights
The most important finding is that the waiting problem is not a driver behaviour problem; it is an incentive-and-information design problem. Drivers are rationally responding to an earnings model that rewards only full-capacity departures. This means:
- Disciplining or incentivising drivers without changing the booking system will not resolve the root cause.
- The root cause is structural and lies at the system-design level, not at the individual-agent level.
- Why 3 (no zone-aggregation) explains why even a willing driver cannot depart early: without knowing whether nearby students are heading to compatible destinations, early departure is economically irrational.

## How It Informs the Solution
The root cause statement, "Absence of an app-based booking and aggregation layer," is a direct specification for the solution. The proximity-discovery feature (students see nearby E-ricks with destination overlays) and the 1-minute boarding window address Why 4 and Why 5. The per-seat fare model and wallet payment together realign driver incentives (Why 2). Zone-based demand aggregation in the backend addresses Why 3. The 5 Whys analysis therefore provides the logical justification for each core app feature, ensuring that the solution is not over-engineered and does not include features that do not map to a identified causal link.
