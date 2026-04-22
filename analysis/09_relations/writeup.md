# 09  - Interrelationship (Relations) Diagram

## Tool
Interrelationship Diagram (also called the Relations Diagram or ID). Reference: Ch.3 New 7 QC Tools.

## Purpose
The Interrelationship Diagram is a network tool that maps cause-and-effect relationships among a set of issues when those relationships are complex, nonlinear, and mutually reinforcing. Unlike the Ishikawa diagram (which connects causes to a single effect), the Relations Diagram allows any node to be both a cause and an effect, making it suitable for revealing vicious cycles and reinforcing feedback loops. Nodes with many outgoing arrows are root drivers; nodes with many incoming arrows are key symptoms. The tool is used when a problem resists simple linear analysis.

## Application in Our Project
We mapped eight nodes that describe the self-reinforcing failure system of the current E-rickshaw service: Long wait time, Route detours, Cash leakage, Students avoid E-ricks, Lower driver earnings, Fewer active E-ricks, Longer waits (feedback loop close), and Poor service perception. Directed arrows show which node causes or worsens which other node. Arrows are distinguished by type: bold arrows (drawn in maroon) denote the main reinforcing loop, while thin arrows (drawn in muted grey) indicate contributing causes that feed into the loop or branch off it.

## Key Findings and Insights
The primary reinforcing loop is: Long wait time causes Students to avoid E-ricks, which reduces ridership and lowers driver earnings, which causes some drivers to exit the service (Fewer active E-ricks), which extends wait times further (Longer waits closes the loop back to Long wait time). This is a classic demand-and-supply vicious cycle: poor service drives away users, and fewer users degrade service quality for those who remain. Three contributing causes (Route detours, Cash leakage, Poor service perception) each feed additional negative energy into the loop without being part of its core structure. This distinction matters: fixing route detours without breaking the main loop will reduce degradation speed but will not reverse the trajectory.

## How It Informs the Solution
The Relations Diagram identifies the minimum intervention needed to break the reinforcing loop. The loop runs through the nodes "Students avoid" and "Fewer active E-ricks." The app breaks the loop at both points simultaneously: proximity discovery and guaranteed seating reduces the reason for avoidance, while the return-trip booking feature (driver sees nearby demand) prevents driver exits due to low earnings from empty returns. The diagram also explains why a partial fix (say, only adding GPS without fixing the fill-rule or payment) would be insufficient: it would reduce one contributing cause but leave the reinforcing loop intact.
