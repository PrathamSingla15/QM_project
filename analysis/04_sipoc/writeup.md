# 04  - SIPOC Diagram

## Tool
SIPOC (Suppliers, Inputs, Process, Outputs, Customers) Diagram. Reference: Ch.2 Process Scoping and Mapping (closely aligned with Basic 7 QC process analysis tools).

## Purpose
SIPOC is a high-level process scoping tool that maps a process across five dimensions: who supplies what inputs, what steps constitute the process, what outputs result, and who the customers are. It is used at the beginning of any process improvement initiative to establish the boundary of the process under study, align the team on scope, and identify all stakeholders before detailed flowcharting or data collection begins. A SIPOC prevents a team from solving the wrong process or missing key input variables.

## Application in Our Project
We applied SIPOC to document the current E-rickshaw ride process as it operates without the app. The diagram surfaces all four main actors (drivers, campus administration, electricity provider, and cash as a system element) as suppliers. It traces the five key inputs through a six-step process: wait, board, route-by-majority, sequential drop-off, cash payment, and empty return. The outputs include both the desired output (passenger transport) and the undesired outputs (student time-cost and partial cash reconciliation). Campus administration is identified as an indirect customer, a point that is often missed in rider-centric analyses.

## Key Findings and Insights
Three structural gaps become visible in the SIPOC that are not obvious from symptom descriptions alone:
- The process has no feedback loop: outputs (driver revenue, student time-cost) are never measured and never fed back to suppliers (admin policy or driver scheduling).
- "Student demand" appears as an input but is described as "uncoordinated," meaning the process begins with structurally noisy input that no step in the current process corrects for.
- The empty return trip is listed as part of the process, making visible that the system is generating a complete unproductive cycle after every ride. This waste is hidden in a verbal description but stands out immediately in a structured process map.

## How It Informs the Solution
The SIPOC reveals two intervention points that the app must address: the Input stage (aggregating student demand before dispatch) and the Output stage (equipping drivers with nearby booking data to eliminate empty returns). It also clarifies the scope boundary for the pilot: the process from "student books" to "driver reaches next booking" is the complete process to be redesigned. Admin route policy is a constraint (supplier) that the MVP does not change; this keeps the pilot scope manageable.
