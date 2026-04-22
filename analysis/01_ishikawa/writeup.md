# 01  - Ishikawa (Fishbone) Diagram

## Tool
Ishikawa Cause-and-Effect Diagram (also called Fishbone Diagram). Reference: Ch.2 Basic 7 QC Tools.

## Purpose
The Ishikawa diagram is a structured brainstorming tool that maps all potential causes of a problem onto a visual diagram shaped like a fish skeleton. The "head" is the stated effect or problem, and each "rib" represents a major category of causes. Sub-causes branch off each rib. The tool helps a team move beyond surface symptoms to identify systemic root causes across multiple dimensions before choosing where to intervene.

## Application in Our Project
We applied the 6M+E framework (Man, Machine, Method, Material, Measurement, Environment) to the effect statement "E-Rickshaw service inefficiency on campus." Each category was populated with specific, observed or reported causes drawn from survey data, stakeholder interviews, and team analysis. For example, the Method rib captures the rigid 4-passenger fill rule and cash-only payment, which directly generate the two highest-ranked pain points in our Pareto chart. The Measurement rib reveals that no KPI tracking exists, meaning management has no feedback loop to detect or correct deteriorating service quality.

## Key Findings and Insights
The diagram reveals that the problem is systemic, not attributable to any single cause. The three most actionable clusters are:
- **Method**: The fill-before-dispatch rule and absence of destination aggregation are policy choices that the proposed app directly overrides.
- **Machine**: No GPS tracking means neither students nor drivers have real-time location awareness, making the proximity-discovery feature of the app the primary hardware-side fix.
- **Measurement**: The complete absence of wait-time KPIs, passenger count audits, and fare reconciliation means there is currently no accountability mechanism. The app automatically generates this data as a side-effect of digital transactions and booking logs.

## How It Informs the Solution
The Ishikawa analysis justifies why a point-fix (for instance, just adding a GPS device) would be insufficient. The app MVP must address causes across at least three ribs simultaneously: it must replace cash (Method + Measurement), surface location (Machine), introduce scheduling discipline (Man + Method), and produce audit logs (Measurement). This multi-rib scope is the basis for the app's feature list defined in the solution document.
