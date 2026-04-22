# QM Campus Quality Problem — Project Ideas

> Goal: Identify a genuine, measurable campus quality problem and propose a solution using QM tools (5S, Six Sigma, control charts, fishbone, Pareto, PDCA, etc.)


## PS. E-Rickshaw Service Quality — Wait Time, Routing & Capacity Optimization

**Problem:** Campus e-rickshaws suffer from **three compounding quality failures** that hurt both students and drivers:
1. **Forced batching wait** — E-rickshaws won't depart until 4 seats are filled, causing unpredictable wait times (2 min to 20+ min). Students with urgent needs (exam, lab, viva) are held hostage by the fill rate.
2. **Route conflict among passengers** — When 4 passengers have 4 different destinations, the ride becomes a long, inefficient detour for everyone. A student going to the nearest building ends up touring the entire campus because the driver serves the farthest destination first/last.
3. **Dead-mile empty returns** — After dropping all passengers, the e-rickshaw returns empty to its starting point, wasting time, battery, and earning potential. This is pure non-value-added activity (muda in lean terms).

The result: students avoid e-rickshaws for short trips (lost demand), drivers earn less per hour than they could, and the overall service is perceived as unreliable — a textbook **service quality failure** across all 5 RATER dimensions (Reliability of timing, Assurance of reaching on time, Tangibles of route efficiency, Empathy for urgent needs, Responsiveness to demand).

**Approach:**
- **Data Collection:** Track 80-100 e-rickshaw trips over 2 weeks — record: wait time to fill, number of unique destinations per trip, total ride time, route taken, empty return time, passenger satisfaction (1-5). Also survey 50+ students on frequency of use, reasons for not using, and pain points.
- **Analysis with QM Tools:**
  - **X-bar/R control chart** on wait-to-fill time grouped by time slot (morning/afternoon/evening) — detect out-of-control periods and cyclic patterns (class changeover times vs dead hours)
  - **Histogram** for ride time distribution — expect bimodal (short direct rides vs long multi-stop detours)
  - **p-chart** for proportion of trips exceeding acceptable wait threshold (say >10 min)
  - **Scatter diagram** — number of distinct destinations vs total ride time (expect strong positive correlation proving the route conflict problem)
  - **Pareto chart** for top student complaints (long wait, detour routes, no availability at night, rude drivers, overcharging)
  - **Fishbone diagram (4M + Environment):**
    - *Manpower:* insufficient drivers during peak hours, no shift scheduling
    - *Method:* no zone-based routing, no demand prediction, rigid 4-passenger rule
    - *Machine:* limited battery range forces conservative routing, no GPS/app tracking
    - *Material:* no signage at stops, no route maps, no queue system
    - *Environment:* campus layout with scattered buildings, weather affecting demand
  - **Affinity diagram** to cluster survey responses into themes
  - **Relations diagram** to map cause-effect chains (e.g., long wait → students walk → lower demand → longer wait — a vicious cycle)
  - **Matrix diagram** to evaluate solution options on feasibility vs impact
- **Proposed Solution (using PDCA + 5S):**
  - **Plan:** Introduce zone-based routing (divide campus into 3-4 zones, e-rickshaws serve within zones to minimize detours). Reduce minimum passengers to 2-3 during off-peak. Implement a simple pickup point system with designated stops.
  - **Do:** Pilot with 2-3 e-rickshaws for 1 week on the busiest route
  - **Check:** Compare wait times, ride times, driver earnings, and student satisfaction before vs after using control charts
  - **Act:** Standardize what works, iterate on what doesn't
  - **5S for pickup points:** Sort (remove unofficial stops), Set in Order (numbered/named stops with route maps), Shine (clean waiting area), Standardize (fixed schedule board), Sustain (weekly review)
  - **Lean concept:** Eliminate the "empty return" muda by creating circular routes or having designated return-pickup points where the driver can collect passengers on the way back

**Why this idea is exceptional:**
- Solves for BOTH customers (students) AND service providers (drivers) — rare in QM projects
- Uses the maximum number of tools from your syllabus (basic 7 + new 7 + SQC + 5S + PDCA + lean)
- The "vicious cycle" analysis (low reliability → low demand → worse economics → worse service) shows systems thinking
- Before/after comparison with control charts demonstrates measurable improvement
- Highly original — guaranteed nobody else picks this

---


> **Top Pick Recommendation:** Go with **#11 (E-Rickshaw Service Quality)** — it's the most original, covers the widest range of QM tools, addresses both customer and provider, and demonstrates systems thinking with the vicious cycle analysis. It's the kind of project that stands out in a class where everyone else picks mess food or hostel cleanliness.
