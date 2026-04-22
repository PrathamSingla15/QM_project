# 08  - Affinity Diagram

## Tool
Affinity Diagram (KJ Method). Reference: Ch.3 New 7 QC Tools.

## Purpose
The Affinity Diagram, developed by Jiro Kawakita (the KJ Method), is a qualitative synthesis tool for organising large volumes of unstructured verbal data (opinions, ideas, observations) into meaningful thematic clusters. Unlike quantitative tools that count and rank, the Affinity Diagram preserves the nuance and variety of individual voices. It is particularly valuable when the research input is open-ended survey responses, ethnographic notes, or brainstorming outputs. The process of clustering forces the analyst to identify underlying commonality rather than treating each response as independent.

## Application in Our Project
We applied the Affinity Diagram to Q22 of our survey, which was an open-text field asking respondents for any additional comments or suggestions. From 150 respondents, a subset of non-empty responses was collected and reviewed. Each distinct idea was treated as a separate card. Cards were then grouped by underlying theme rather than by surface topic. Six themes emerged: Schedule Reliability, Payment and Fare Transparency, Availability Gaps, Safety and Identity, Zone Aggregation, and Driver Experience. The themes were selected to be mutually exclusive and collectively exhaustive of the response content.

## Key Findings and Insights
Three findings are significant:
- Schedule Reliability is the most populated theme, with responses referencing shuttle-style scheduling, app-based advance booking, and fixed-time pickup. This strongly corroborates the Pareto chart's top finding and provides the qualitative texture that the quantitative pain-point count cannot: students do not just want shorter waits, they want predictable, schedulable service.
- The Safety and Identity theme contains responses that quantitative survey items did not capture at all. The request for a dedicated women's E-rick during late hours and the request to display driver identity information represent a genuine unmet need that the app can address at low marginal cost (driver photo and name in the booking card).
- Zone Aggregation responses (GPS tracking, hostels vs academic zones, group booking) are technically sophisticated; students have already articulated the solution architecture independently, validating the technical direction of the app.

## How It Informs the Solution
Theme D (Safety and Identity) drives a specific app feature: the driver profile card (photo, name, rating) visible before the student boards. This feature was not in the original MVP spec but is now included based on affinity findings. Theme E (Zone Aggregation) confirms that the backend zone-mapping and group-booking features are user-desired, not just technically convenient. Theme C (Availability Gaps) supports the business case for off-peak scheduling, which the Act phase of the PDCA cycle should address after the pilot.
