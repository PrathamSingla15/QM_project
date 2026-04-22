# Course Content Mapping
## TQM Course Tools and Concepts Mapped to the E-Rickshaw App Project

**Team B | Total Quality Management (TQM) Course Project**
**Date: April 2026**

---

## 1. Executive Summary

This document provides a structured inventory of every TQM tool and concept introduced across the ten chapters of the course, mapped systematically to the E-Rickshaw app project undertaken by Team B. The project addresses the unreliable, opaque, and inconvenient ride experience faced by students who depend on e-rickshaws on campus, proposing a mobile application that digitises booking, payment, and driver coordination. The purpose of this mapping is to demonstrate that the analytical techniques selected for the project are grounded in the course curriculum and that choices regarding non-application are deliberate and reasoned. Across approximately fifty distinct concepts, nine tools have been developed into full project artifacts (including an Ishikawa diagram, a Pareto analysis, an Affinity Diagram, a Relations Diagram, a SIPOC, two-state process flowcharts, FMEA, and a PDCA roadmap), eight further concepts directly frame the analytical narrative without producing standalone artifacts, and a small cluster of tools has been honestly set aside as inapplicable at this stage of development.

---

## 2. Master Inventory

### 2.1 Chapter 1: TQM Fundamentals, 5S, and Continuous Improvement

**Garvin's 8 Dimensions of Quality**
Garvin's framework identifies eight independent dimensions -- performance, features, reliability, conformance, durability, serviceability, aesthetics, and perceived quality -- through which a product or service can be evaluated by customers.
*Applicability:* The framework is directly applicable as a conceptual lens on the e-rickshaw ride experience. Students evaluate the service on performance (punctuality), features (payment options), and reliability (consistent availability), making Garvin's dimensions a useful vocabulary for structuring the gap analysis. It is used as a referenced concept rather than a standalone artifact because the project's survey already operationalised these dimensions as specific questionnaire items.

**RATER Model**
RATER is a service-quality evaluation framework comprising five dimensions: Reliability, Assurance, Tangibles, Empathy, and Responsiveness, adapted from the SERVQUAL instrument.
*Applicability:* The model is directly applicable to the current e-rickshaw service, which fails on Reliability (unpredictable arrival), Responsiveness (no communication channel between driver and student), and Tangibles (no digital interface or fare display). It is referenced in the gap analysis section of the report but not constructed as a scored artifact, because the survey data are sufficient to make the point without a formal SERVQUAL gap calculation.

**Cost of Quality (PAF Model)**
The Prevention-Appraisal-Failure model categorises quality-related costs into prevention costs (actions to avoid defects), appraisal costs (inspection and measurement), and failure costs (internal and external consequences of defects).
*Applicability:* PAF is applicable as a conceptual frame: the app development investment represents a prevention cost, and the daily student time lost to missed or delayed rides represents a quantifiable external failure cost. A formal PAF accounting table is not produced because the project lacks audited financial data, but the reasoning is woven into the problem justification.

**TQM Principles**
TQM principles encompass customer focus, total employee involvement, process-centred thinking, integrated systems, strategic and systematic approach, continual improvement, fact-based decision making, and communications.
*Applicability:* These principles underpin the entire project philosophy. Customer focus drives the user-centred app design; fact-based decision making is operationalised through the student survey; continual improvement is formalised in the PDCA cycle. They are foundational context rather than discrete artifacts.

**Seven Steps of TQM Implementation**
This is a sequential framework guiding an organisation from identifying the problem through selecting corrective actions, implementing solutions, monitoring results, and standardising improvements.
*Applicability:* The seven-step structure maps loosely onto the project's DMAIC-adjacent methodology -- problem identification (survey), root-cause analysis (Ishikawa, Pareto), solution design (app), and monitoring (PDCA). It is not rendered as a standalone artifact because the PDCA cycle and project narrative already cover this sequence.

**5S (Sort, Set in Order, Shine, Standardize, Sustain)**
5S is a workplace organisation methodology in which Sort eliminates unnecessary items, Set in Order arranges remaining items for efficiency, Shine maintains cleanliness, Standardize establishes consistent procedures, and Sustain embeds the discipline over time.
*Applicability:* 5S applies meaningfully to the physical pickup point standardisation proposed in the solution -- defining designated waiting zones (Sort and Set in Order), maintaining clean boarding areas (Shine), establishing signage standards (Standardize), and building habits through app-enforced check-ins (Sustain). It also informs the principle of visual clarity in the app's UI design. This is referenced as a concept rather than a full artifact.

**Continuous Improvement**
Continuous improvement is the ongoing, incremental effort to improve products, services, and processes, typically enacted through iterative cycles such as PDCA.
*Applicability:* Continuous improvement is central to the PDCA artifact produced by the team. The rollout roadmap in Section 7 of this document operationalises the concept into defined review intervals post-launch.

**SWOT Analysis**
SWOT analysis is a structured planning technique that evaluates internal Strengths and Weaknesses alongside external Opportunities and Threats facing a project or organisation.
*Applicability:* A SWOT analysis could have been applied to the e-rickshaw ecosystem to frame strategic positioning of the app, but the project team chose the Ishikawa diagram and survey data as more operationally precise tools for root-cause scoping. SWOT is therefore not produced as an artifact in this project.

---

### 2.2 Chapter 2: The Basic 7 QC Tools

**Histograms**
A histogram is a bar chart representing the frequency distribution of a continuous variable, used to reveal the shape, spread, and central tendency of a data set.
*Applicability:* A histogram of student-reported wait times (drawn from the survey) is produced in the analysis to show the distribution of delays and confirm that the mean wait time substantially exceeds an acceptable threshold. This is a referenced visual rather than a full standalone artifact.

**Run Charts**
A run chart plots data points over time in sequence, allowing teams to identify trends, shifts, or cycles in a process before applying formal control limits.
*Applicability:* A run chart would be useful for tracking average wait time by day of week over several weeks. The project currently lacks time-series data from the field; the concept is discussed in the SPC roadmap for the post-pilot phase.

**Pareto Charts**
A Pareto chart combines a sorted bar chart with a cumulative percentage line to identify the "vital few" causes or categories that account for the majority of a problem's impact, based on the 80/20 principle.
*Applicability:* This is one of the nine full artifacts produced by the team. Survey respondents were asked to rank their top pain points, and the results are visualised as a Pareto chart showing that the combination of unpredictable wait times and cash-only payment accounts for over 70 percent of dissatisfaction. The artifact resides in `analysis/03_pareto/`.

**Flow Charts (Process Flowcharts)**
A process flowchart is a diagrammatic representation of the sequential steps in a process, using standardised symbols to distinguish decision points, activities, inputs, and outputs.
*Applicability:* Two flowcharts are produced as full artifacts -- one mapping the current-state e-rickshaw boarding process and one mapping the proposed future-state process enabled by the app. These are stored in `analysis/04_flowcharts/`.

**Scatter Diagrams**
A scatter diagram plots two variables on perpendicular axes to reveal the direction, form, and strength of their relationship.
*Applicability:* A scatter plot of destination distance versus reported ride time is discussed in the analysis section to check for anomalies in fare consistency. The plot is produced from survey data but is not a primary artifact -- it is referenced in the analysis narrative.

**Cause and Effect Diagram (Ishikawa / Fishbone)**
An Ishikawa diagram organises potential causes of a problem into major categories -- typically the 6 Ms: Man, Machine, Method, Material, Measurement, and Mother Nature (Environment) -- branching from a central effect arrow, enabling structured root-cause analysis.
*Applicability:* This is the anchor artifact of the root-cause analysis phase. The team applied the 6M framework to the effect "Students experience unreliable, inconvenient e-rickshaw service," producing a comprehensive Fishbone diagram. The artifact is stored in `analysis/01_ishikawa/`.

**Control Charts**
Control charts (Shewhart charts) plot a process metric over time with a centre line and upper and lower control limits derived from process data, distinguishing common-cause variation from special-cause signals.
*Applicability:* Control charts are not produced in this project phase because no longitudinal process data have been collected. The concept is discussed in the rollout roadmap as the appropriate tool once three months of wait-time data are available post-launch.

---

### 2.3 Chapter 3: The New 7 QC Tools

**Affinity Diagrams (KJ Method)**
An Affinity Diagram organises large volumes of qualitative information -- ideas, observations, or issues -- into natural groupings based on affinity, enabling teams to make sense of complex, unstructured data.
*Applicability:* The team applied the Affinity Diagram to 47 open-ended survey responses and brainstorming output from a group session, clustering observations into five thematic groupings: Scheduling and Availability, Payment and Fare Transparency, Safety and Trust, Physical Infrastructure, and Driver Communication. This is a full artifact stored in `analysis/06_affinity/`.

**Relations Diagram (Interrelationship Diagram)**
A Relations Diagram maps cause-and-effect relationships among a set of issues by drawing directional arrows between them, then counting in-arrows (effects) and out-arrows (drivers) to identify root drivers and key outcomes.
*Applicability:* The team constructed a Relations Diagram for the five thematic clusters identified in the Affinity Diagram. The analysis confirmed that "Scheduling and Availability" has the highest out-arrow count and is therefore the primary systemic driver, which directly informs the app's core feature prioritisation. This artifact resides in `analysis/07_relations/`.

**Tree Diagrams**
A Tree Diagram breaks a goal or category down into successively finer levels of detail, resembling an organisational chart, to expose all contributing sub-tasks or sub-causes.
*Applicability:* A Tree Diagram could be used to decompose the system requirement "Improve ride reliability" into functional sub-requirements of the app. The team chose to defer this to the system design phase and instead used the SIPOC and flowchart for structural scoping. The tool is not produced as a project artifact.

**Matrix Diagrams**
A Matrix Diagram displays the relationship between two or more sets of items in a grid format, using symbols to indicate the strength of each relationship, commonly used for QFD-style analysis.
*Applicability:* A Matrix Diagram could correlate student pain points with proposed app features to support feature prioritisation. The team's Pareto analysis and Relations Diagram together serve this prioritisation function, making a standalone Matrix Diagram redundant at this stage. It is not produced.

**Arrow Diagrams (PERT/CPM)**
An Arrow Diagram represents the sequence and dependency of activities in a project schedule, enabling identification of the critical path and estimation of project duration under uncertainty.
*Applicability:* The tool is not applied to this project. The app rollout timeline is short (one academic semester), and the iterative PDCA cycle already captures scheduling logic at the level of granularity appropriate to a student project. A full PERT network would over-complicate a compact schedule.

**PDPC (Process Decision Programme Chart)**
PDPC anticipates what can go wrong during implementation of a plan by systematically mapping potential obstacles at each step and identifying countermeasures before they are needed.
*Applicability:* PDPC could add value in anticipating adoption risks (e.g., driver resistance to the app, payment gateway failures). The team has addressed these risks qualitatively in the FMEA and PDCA artifacts. A standalone PDPC is not produced, but the logic of pre-emptive countermeasure planning is embedded in the FMEA severity-and-occurrence scoring.

**Matrix Data Analysis**
Matrix Data Analysis (also called principal component analysis in a quality context) is a numerical technique that reduces a large data matrix to its principal components, enabling visualisation of complex multi-variable relationships.
*Applicability:* This tool is not applied. The project data set is not large enough, and the team's analysis questions do not require dimensionality reduction. The FMEA's Risk Priority Number (RPN) scoring and the Pareto prioritisation together cover the quantitative ranking needs of the project.

---

### 2.4 Chapter 4: Statistical Process Control (SPC)

**X-bar/R Charts**
X-bar/R charts monitor the mean and range of a continuous measurement (e.g., cycle time, dimension) sampled in rational subgroups over time, distinguishing common-cause variation from special-cause signals.
*Applicability:* X-bar/R charts are directly applicable to monitoring e-rickshaw wait times once the app is operational and collecting timestamped ride requests. The concept is used to frame the post-launch monitoring design (Section 7), but the tool cannot be applied now because no time-series data exist. It is a referenced concept.

**p/np Charts**
p charts monitor the proportion of defective units in a sample, and np charts monitor the count of defective units; both apply to attribute data where each item is classified as conforming or non-conforming.
*Applicability:* A p chart could monitor the proportion of ride requests that result in a "no-show" (a defective service event). This is discussed conceptually in the rollout roadmap but is not produced as a current artifact, pending data collection.

**c/u Charts**
c charts monitor the count of defects per inspection unit, and u charts monitor the defect rate when inspection unit size varies; both apply to attribute data where multiple defects can occur per item.
*Applicability:* A u chart could track the number of service complaints per hundred rides once the app is deployed and complaint logging is in place. This is a post-launch consideration and is not applied in the current project phase.

**Common vs Special Causes of Variation**
Common causes are the inherent, stable sources of variation in any process, while special causes are assignable, non-random events that signal a process change requiring investigation.
*Applicability:* This distinction is conceptually relevant to the root-cause analysis. The Ishikawa diagram separates structural, systemic causes (common-cause analogues: lack of scheduling infrastructure) from event-specific disruptions (special-cause analogues: driver absence on a given day). The concept is invoked in the analysis narrative.

**In-Control vs Out-of-Control Processes**
A process is in statistical control when all variation is attributable to common causes; it is out of control when a special cause is detectable through a control chart rule violation.
*Applicability:* The concept is referenced in the SPC rollout discussion. Before the app is deployed, the e-rickshaw service can be characterised as an out-of-control process with undefined and shifting process parameters -- a point used rhetorically to justify the need for digitisation and data collection.

---

### 2.5 Chapter 5: Process Capability

**Cp (Process Capability Index)**
Cp measures the ratio of the specification width to the process spread (six standard deviations), indicating whether the process is inherently capable of meeting specification limits, irrespective of centring.
*Applicability:* Cp is not applicable in the current project phase because there are no established specification limits (SLAs) for wait time and no stable, in-control process from which to estimate the process standard deviation. Post-launch, once a wait-time SLA (e.g., "95 percent of rides begin within 5 minutes of request") is formalised, Cp becomes an appropriate performance metric.

**Cpk (Centred Process Capability Index)**
Cpk adjusts for process centering by taking the minimum of the ratios of the distance from the mean to each specification limit divided by three standard deviations, penalising processes that are off-target.
*Applicability:* The same constraint applies as for Cp. Cpk is the more practically useful index once a two-sided or one-sided wait-time SLA is set, because the process mean is unlikely to be centred at the mid-point of the acceptable range. It is listed in the post-launch roadmap.

**Voice of Process vs Voice of Customer**
The Voice of Customer (VoC) represents what customers require (specification limits), while the Voice of Process (VoP) represents what the process actually delivers (process variation), and process capability analysis bridges the two.
*Applicability:* The VoC/VoP distinction frames the entire project: the VoC (student expectation of reliable, prompt service) is captured through the survey, and the VoP (current erratic performance) is described through the root-cause analysis. The conceptual frame is used in the problem statement narrative.

**Process Centering and Spread**
Process capability requires that the process mean be close to the target value (centering) and that variation around the mean be small (spread), with both dimensions necessary for a capable process.
*Applicability:* These concepts inform the Taguchi loss function discussion (Section 5, referenced concept) and the post-launch SPC design. They are conceptually referenced rather than numerically applied.

**Three Reasons for Process Failure**
Process failure occurs due to: (1) the process average being off-target, (2) the process spread being too wide, or (3) the process being out of statistical control.
*Applicability:* The current e-rickshaw service can be described as failing on all three dimensions -- off-target average wait times, extremely wide variation in wait time, and no control mechanism. This framing is used in the problem justification narrative.

---

### 2.6 Chapter 6: Six Sigma

**Sigma Metric**
The sigma metric expresses process performance as the number of standard deviations between the process mean and the nearest specification limit, with higher sigma levels indicating fewer defects and better process capability.
*Applicability:* The sigma metric is referenced as a framing device. If a successful ride is defined as one that commences within five minutes of request, and approximately 40 percent of rides are reported as delayed beyond this threshold (per survey data), the implied defect rate is roughly 400,000 DPMO, corresponding to slightly below two sigma -- a characterisation that underscores the severity of the problem.

**DPMO Table by Sigma Level**
The DPMO (Defects Per Million Opportunities) table maps sigma levels to defect rates, ranging from approximately 690,000 DPMO at one sigma to 3.4 DPMO at six sigma (assuming the standard 1.5 sigma shift).
*Applicability:* The DPMO concept is applied conceptually to quantify the scale of payment leakage and service failures. A formal DPMO calculation is included in the analysis narrative as a referenced concept rather than a standalone artifact.

**The 1.5 Sigma Shift**
The 1.5 sigma shift is the empirical correction applied to long-term process performance to account for process drift over time, resulting in the standard Six Sigma target of 3.4 DPMO at the six-sigma level.
*Applicability:* The concept is mentioned for completeness in the analysis narrative but has no direct numerical application in the current project phase, which relies on survey estimates rather than process data.

**DMAIC (Define, Measure, Analyse, Improve, Control)**
DMAIC is the structured problem-solving methodology underpinning Six Sigma projects: defining the problem, measuring the current state, analysing root causes, improving the process, and controlling the improved state.
*Applicability:* The project's overall structure follows a DMAIC-adjacent logic -- the student survey defines and measures the problem, the Ishikawa and Pareto tools analyse it, the app design addresses the Improve phase, and the PDCA cycle and SPC roadmap address Control. DMAIC is not applied as a formal Six Sigma project because the team is not conducting a statistically rigorous intervention, but its logic permeates the methodology.

---

### 2.7 Chapter 7: Acceptance Sampling

**Acceptable Quality Level (AQL)**
AQL defines the maximum percentage of defective items in a lot that a consumer considers acceptable as a process average, used to design sampling plans for incoming or outgoing inspection.
*Applicability:* Not applicable. The e-rickshaw app project is a service design and implementation effort, not a manufacturing or procurement context in which lots of items are inspected. There is no physical lot to sample.

**Limiting Quality Level (LQL) / Lot Tolerance Percent Defective (LTPD)**
LQL defines the worst quality level in a lot that a consumer is willing to accept with a specified low probability, acting as the upper bound for acceptable defect rates in an acceptance sampling plan.
*Applicability:* Not applicable for the same reasons as AQL. No lot-inspection decision context exists in this project.

**Producer's Risk (Type I Error / Alpha)**
Producer's risk is the probability that a sampling plan will reject a lot of acceptable quality, resulting in a financial loss for the producer through unnecessary rework or rejection.
*Applicability:* Not applicable in this project context.

**Consumer's Risk (Type II Error / Beta)**
Consumer's risk is the probability that a sampling plan will accept a lot of unacceptable quality, allowing defective items to reach the customer.
*Applicability:* Not applicable in this project context.

**Operating Characteristic (OC) Curves**
OC curves plot the probability of lot acceptance against the true lot defect rate for a given sampling plan, allowing designers to balance producer and consumer risks.
*Applicability:* Not applicable in this project context. The entire Chapter 7 toolkit belongs to a manufacturing or procurement quality control paradigm that has no structural analogue in a real-time digital service application.

---

### 2.8 Chapter 8: Taguchi Methods

**Taguchi Loss Function**
The Taguchi Loss Function quantifies the cost of deviation from a target value using a quadratic function, demonstrating that any departure from the target -- even within specification limits -- incurs a societal loss.
*Applicability:* The loss function is directly applicable as a conceptual frame for the boarding time standard. If the target boarding time is defined as one minute from app-request to driver arrival, any deviation -- whether the ride arrives in 30 seconds or 5 minutes -- incurs a loss proportional to the square of the deviation. This framing is used in the analysis narrative to argue against a mere "within-specification" standard and in favour of a target-value approach. It is a referenced concept.

**Robust Design**
Robust Design is the Taguchi approach to engineering products and processes so that their performance is insensitive to uncontrollable noise factors (environmental variation, component tolerances, user behaviour), achieved through design of experiments on control parameters.
*Applicability:* The concept informs the app design philosophy -- the system should remain functional and deliver acceptable service despite noise factors such as peak-demand surges, driver GPS inaccuracy, or campus Wi-Fi variability. This is referenced in the design rationale but does not generate a formal experiment because the project is a student-scale intervention.

**Target Value and Variation Elimination**
Taguchi's fundamental philosophy holds that quality is maximised not by conforming to specification limits but by consistently hitting the target value and reducing variation around it to the minimum achievable.
*Applicability:* This principle directly complements the process capability discussion (Section 2.5) and the SPC roadmap. It reinforces why the project goal is framed as reducing wait-time variation to near zero rather than simply reducing the proportion of rides exceeding a threshold. It is a referenced concept embedded in the problem statement.

---

### 2.9 Chapter 9: Quality Award Models

**Deming Prize**
The Deming Prize is a Japanese quality award established in 1951, recognising organisations that have achieved distinguished performance improvement through the application of TQM.
*Applicability:* Not applicable as a project-level tool. The Deming Prize is an organisational self-assessment and award framework designed for entire enterprises, not appropriate for a student project of limited scope.

**Malcolm Baldrige National Quality Award (MBNQA)**
The MBNQA is a US national quality award whose criteria cover leadership, strategy, customers, measurement and analysis, workforce, operations, and results, serving both as an award and a self-assessment framework.
*Applicability:* The Baldrige criteria provide a useful vocabulary for thinking about what a mature e-rickshaw operation would look like, particularly the customer and results dimensions. However, applying the full Baldrige framework would be disproportionate for a student-scale project. It is not applied as a project artifact.

**EFQM Excellence Model**
The EFQM model is a European quality framework evaluating organisations across enablers (leadership, people, strategy, partnerships, processes) and results (people, customer, society, and business results).
*Applicability:* Similar to MBNQA, the EFQM model is an organisational-level framework unsuitable for a bounded student project. Not applied.

**Australian Quality Award**
The Australian Quality Award follows a framework similar to MBNQA, emphasising leadership, strategy, information, people, customer focus, and business results.
*Applicability:* Not applicable. The geographic and organisational scope of this award is irrelevant to the campus-based project context.

**Baldrige Criteria for Performance Excellence**
The Baldrige Criteria are the scoring dimensions of the MBNQA framework, used by organisations for self-assessment and continuous improvement benchmarking.
*Applicability:* See MBNQA entry. Not applied as a standalone artifact.

**Self-Assessment Process**
Quality award frameworks prescribe self-assessment processes in which organisations score themselves against defined criteria, identify gaps, and prioritise improvement actions.
*Applicability:* The concept of structured self-assessment is analogous to the team's gap analysis approach using RATER and Garvin's dimensions. It is not applied formally, but the logic of self-assessment against defined criteria is embedded in the problem diagnosis phase.

---

### 2.10 Chapter 10: Reliability

**MTBF (Mean Time Between Failures)**
MTBF is the average operating time between failures for a repairable system, used to characterise the reliability of components or systems.
*Applicability:* MTBF is conceptually applicable to the e-rickshaw app infrastructure -- specifically to the payment gateway and GPS tracking module, which are system components whose failure directly disrupts service. The FMEA artifact scores the failure modes and effects of these components, making MTBF the conceptual backdrop for the reliability analysis. The metric is referenced rather than computed because no failure data exist yet.

**MIL-STD-721C Definition of Reliability**
MIL-STD-721C defines reliability as the probability that an item will perform its intended function for a specified interval under stated conditions, providing a precise, probabilistic framing for reliability analysis.
*Applicability:* This definition is cited in the FMEA artifact to frame the reliability standard against which each identified failure mode is evaluated: "the probability that the app delivers a confirmed booking within 60 seconds under normal campus network conditions."

**Reliability vs Quality**
Quality is the conformance of a product or service to requirements at a point in time, while reliability extends this to conformance over time under real operating conditions.
*Applicability:* The distinction is directly relevant: the app may function correctly at launch (quality) but degrade under sustained load or after software updates (reliability). The FMEA addresses both dimensions -- immediate failure modes and degradation-over-time scenarios.

**Failure Analysis**
Failure analysis systematically investigates the causes of component or system failures to identify root causes, categorise failure modes, and recommend corrective actions.
*Applicability:* FMEA (Failure Mode and Effects Analysis) is the team's primary reliability artifact, produced at `analysis/05_fmea/`. It applies failure analysis methodology to the proposed app's components, including GPS tracking, payment processing, driver assignment logic, and user authentication, scoring each failure mode on Severity, Occurrence, and Detectability to compute a Risk Priority Number.

**Cost of Unreliability**
The cost of unreliability encompasses all direct and indirect costs arising from system failures, including repair costs, lost production, warranty claims, customer defection, and reputational damage.
*Applicability:* The cost of unreliability is woven into the project's justification narrative: every missed or failed booking due to app downtime has a computable cost in student time lost and driver income foregone. The PAF model (Section 2.1) and the Taguchi loss function (Section 2.8) together provide the quantitative vocabulary for this cost discussion.

---

## 3. Applicability Summary Matrix

| Tool / Concept | Module | Applicable? | Where Used in Project |
|---|---|---|---|
| Garvin's 8 Dimensions | Ch.1 | Medium | Conceptual lens on ride experience; gap analysis narrative |
| RATER Model | Ch.1 | High | Service quality gap analysis; referenced concept |
| Cost of Quality (PAF) | Ch.1 | Medium | Problem justification; frames app dev as prevention cost |
| TQM Principles | Ch.1 | Medium | Underpins project philosophy throughout |
| Seven Steps of TQM | Ch.1 | Low | Loosely mapped to project phases; not standalone artifact |
| 5S | Ch.1 | Medium | Pickup-point standardisation; app UI clarity; referenced concept |
| Continuous Improvement | Ch.1 | High | Core of PDCA artifact; rollout roadmap |
| SWOT Analysis | Ch.1 | Low | Not produced; superseded by survey and Ishikawa |
| Histograms | Ch.2 | Medium | Wait-time distribution plot; referenced visual from survey data |
| Run Charts | Ch.2 | Low | Discussed for post-launch use; no current time-series data |
| Pareto Charts | Ch.2 | High | Full artifact -- pain-point prioritisation; `analysis/03_pareto/` |
| Flow Charts | Ch.2 | High | Full artifact -- current and future state; `analysis/04_flowcharts/` |
| Scatter Diagrams | Ch.2 | Medium | Distance vs ride-time plot; referenced in analysis narrative |
| Cause & Effect (Ishikawa) | Ch.2 | High | Full artifact -- 6M root-cause analysis; `analysis/01_ishikawa/` |
| Control Charts | Ch.2 | Low | Post-launch concept; no current longitudinal data |
| Affinity Diagrams (KJ) | Ch.3 | High | Full artifact -- survey clustering; `analysis/06_affinity/` |
| Relations Diagram | Ch.3 | High | Full artifact -- driver identification; `analysis/07_relations/` |
| Tree Diagrams | Ch.3 | Low | Not produced; scope covered by SIPOC and flowcharts |
| Matrix Diagrams | Ch.3 | Low | Not produced; Pareto and Relations serve prioritisation |
| Arrow Diagrams (PERT) | Ch.3 | N/A | Not applicable; schedule too compact; PDCA covers iteration |
| PDPC | Ch.3 | Low | Risk logic embedded in FMEA; not standalone artifact |
| Matrix Data Analysis | Ch.3 | N/A | Not applicable; no large multivariate data set |
| X-bar/R Charts | Ch.4 | Medium | Post-launch SPC design; conceptually referenced |
| p/np Charts | Ch.4 | Low | Post-launch no-show monitoring; not current artifact |
| c/u Charts | Ch.4 | Low | Post-launch complaint monitoring; not current artifact |
| Common vs Special Causes | Ch.4 | Medium | Root-cause narrative; Ishikawa framing |
| In-Control vs Out-of-Control | Ch.4 | Medium | Problem statement framing; SPC rollout discussion |
| Cp | Ch.5 | N/A | No stable process or SLA yet; post-launch metric |
| Cpk | Ch.5 | N/A | No stable process or SLA yet; post-launch metric |
| Voice of Process vs Customer | Ch.5 | Medium | Problem statement framing; survey as VoC |
| Process Centering and Spread | Ch.5 | Low | Taguchi discussion and post-launch SPC narrative |
| Three Reasons for Process Failure | Ch.5 | Medium | Problem justification narrative |
| Sigma Metric | Ch.6 | Medium | DPMO framing of service failures; referenced concept |
| DPMO Table | Ch.6 | Medium | Payment leakage quantification; referenced concept |
| 1.5 Sigma Shift | Ch.6 | Low | Mentioned for completeness; no numerical application |
| DMAIC | Ch.6 | Medium | Project structure follows DMAIC logic; not formal Six Sigma |
| AQL | Ch.7 | N/A | No lot-inspection context in real-time service |
| LQL / LTPD | Ch.7 | N/A | No lot-inspection context in real-time service |
| Producer's Risk (Type I) | Ch.7 | N/A | No sampling decision context |
| Consumer's Risk (Type II) | Ch.7 | N/A | No sampling decision context |
| OC Curves | Ch.7 | N/A | No sampling plan context |
| Taguchi Loss Function | Ch.8 | Medium | Boarding-time deviation framing; referenced concept |
| Robust Design | Ch.8 | Low | Informs app design philosophy; not formal experiment |
| Target Value + Variation Elimination | Ch.8 | Medium | Reinforces SPC and Cpk post-launch goals |
| Deming Prize | Ch.9 | N/A | Organisational award; not applicable at project scale |
| MBNQA | Ch.9 | N/A | Organisational framework; not applicable at project scale |
| EFQM | Ch.9 | N/A | Organisational framework; not applicable at project scale |
| Australian Quality Award | Ch.9 | N/A | Organisational framework; not applicable at project scale |
| Baldrige Criteria | Ch.9 | N/A | Organisational framework; not applicable at project scale |
| Self-Assessment Process | Ch.9 | Low | Logic embedded in gap analysis; not standalone artifact |
| MTBF | Ch.10 | Medium | Conceptual backdrop for FMEA; app component reliability |
| MIL-STD-721C Definition | Ch.10 | Medium | Reliability standard cited in FMEA artifact |
| Reliability vs Quality | Ch.10 | Medium | FMEA addresses both dimensions |
| Failure Analysis | Ch.10 | High | Full artifact -- FMEA; `analysis/05_fmea/` |
| Cost of Unreliability | Ch.10 | Medium | Problem justification; combined with PAF framing |

---

## 4. Shortlist: Tools Applied as Full Artifacts

### 4.1 Ishikawa (Fishbone) Diagram -- Chapter 2

The Ishikawa diagram is the foundational root-cause analysis tool of the project. The team applied the 6M framework (Man, Machine, Method, Material, Measurement, Mother Nature) to the primary effect statement "Students experience unreliable, inconvenient, and opaque e-rickshaw service on campus," systematically populating each bone with causes identified from the student survey and a structured brainstorming session. This approach was chosen over a simple list of problems because the 6M structure forces the team to consider whether a cause is attributable to driver behaviour, vehicle condition, scheduling method, payment infrastructure, data absence, or environmental factors, preventing the common error of treating all causes as equivalent. The diagram directly informs which root causes are addressable by the proposed app and which require institutional intervention beyond the project scope. The artifact is stored in `analysis/01_ishikawa/`.

### 4.2 5 Whys

The 5 Whys technique is applied as a complement to the Ishikawa diagram, drilling into selected high-priority branches of the fishbone to reach the actionable root level. For example, the chain "Students miss rides" leads through "Drivers depart without waiting" to "No mechanism exists to signal that a student has booked" to "No digital booking system exists" -- which is precisely the gap the app addresses. The 5 Whys analysis prevents surface-level solutions (e.g., telling drivers to wait longer) by exposing the structural absence of information infrastructure as the real root cause. While the 5 Whys does not appear as a standalone Chapter 2 tool in the course slides, it is a standard root-cause drilling technique taught in the TQM practice literature and is widely used in conjunction with Ishikawa analysis. The analysis is documented in `analysis/02_five_whys/`.

### 4.3 Pareto Chart -- Chapter 2

The Pareto chart is applied to the ranked survey data on student pain points. Respondents were asked to select their top two pain points from a predefined list, and the resulting frequency data are visualised as a sorted bar chart with a cumulative percentage overlay. The chart demonstrates that "unpredictable wait times" and "cash-only payment" together account for approximately 72 percent of all pain-point selections, validating the 80/20 principle and focusing the solution design on these two areas. This prevents scope creep into secondary issues (such as vehicle comfort or route coverage) that matter but do not constitute the vital few. The Pareto chart provides a defensible, data-driven justification for the app's core feature set. The artifact resides in `analysis/03_pareto/`.

### 4.4 SIPOC -- Adjacent to Chapter 2 Flowcharting

A SIPOC (Suppliers, Inputs, Process, Outputs, Customers) diagram is produced to define the scope of the e-rickshaw service process before flowcharting begins. The SIPOC identifies the suppliers of the service (vehicle operators, campus administration, payment infrastructure), the inputs (ride requests, fares, GPS signals), the high-level process steps (booking, dispatch, boarding, payment, completion), the outputs (completed rides, fare receipts, driver earnings records), and the customers (students, faculty, administration). This scoping exercise prevents the flowchart from either being too narrow (missing key inputs) or too broad (incorporating adjacent administrative processes irrelevant to the app). Though the SIPOC appears adjacent to the basic flowcharting canon of Chapter 2 rather than in it explicitly, it is standard practice in process improvement projects and is included as a project artifact. The artifact is in `analysis/04_flowcharts/sipoc/`.

### 4.5 Process Flowcharts (Current State and Future State) -- Chapter 2

Two process flowcharts are produced using the standard flowchart symbol set from Chapter 2: one documenting the current-state boarding process (from a student deciding to take a ride to completing payment) and one documenting the future-state process enabled by the app. The current-state flowchart exposes seven unnecessary steps, three decision bottlenecks, and two points of information opacity (the student does not know if a rickshaw is available; the driver does not know if a student will arrive). The future-state flowchart shows how the app eliminates these bottlenecks through digital booking, real-time GPS tracking, and automated payment. The two-flowchart approach is a standard before-and-after framing in process improvement work and makes the value proposition of the app visually self-evident. The artifacts are in `analysis/04_flowcharts/`.

### 4.6 FMEA (Failure Mode and Effects Analysis) -- Chapter 10 Reliability

FMEA is the primary reliability and risk management artifact of the project. Each major component of the proposed app (GPS tracking module, payment gateway, driver assignment algorithm, user authentication, notification system) is analysed for its potential failure modes, the effects of each failure on the end user, and the current detection mechanisms. Each failure mode is scored on Severity (1-10), Occurrence likelihood (1-10), and Detectability (1-10), producing a Risk Priority Number (RPN) that ranks failure modes for corrective design action. FMEA is drawn from Chapter 10's reliability content and is an industry-standard tool in software and systems engineering, making it the most appropriate reliability artifact for a technology product project. The highest-RPN failures (payment gateway timeout and GPS signal loss in dense campus areas) directly inform the app's fallback design requirements. The artifact is in `analysis/05_fmea/`.

### 4.7 PDCA Cycle -- Chapter 1

The PDCA (Plan-Do-Check-Act) cycle is the governance framework for the entire project roadmap and the proposed post-launch improvement process. In the Plan phase, the student survey and root-cause analysis define requirements and success metrics. In the Do phase, the app is developed and piloted with a small cohort of student volunteers and drivers. In the Check phase, pilot data on wait times, booking completion rates, and payment success rates are compared against the targets established in the Plan phase. In the Act phase, findings from the pilot are used to revise the app design, driver training protocol, and pickup-point signage before campus-wide rollout. The PDCA cycle is chosen over a one-time project delivery model because the e-rickshaw system involves human actors (drivers, students) whose behaviour must be shaped iteratively. The artifact is in `analysis/08_pdca/`.

### 4.8 Affinity Diagram (KJ Method) -- Chapter 3

The Affinity Diagram is applied to 47 open-ended survey responses and approximately 80 brainstorming sticky notes generated during a team ideation session. The team physically (and digitally) sorted these inputs into natural clusters, arriving at five thematic groupings: Scheduling and Availability, Payment and Fare Transparency, Safety and Trust, Physical Infrastructure, and Driver Communication. The Affinity Diagram is essential in this project because the open-ended survey data would otherwise remain an undifferentiated mass of qualitative observations. By imposing thematic structure, the diagram bridges the gap between raw student voices and the structured problem categories that can be entered into the Relations Diagram and addressed in the solution design. The artifact is in `analysis/06_affinity/`.

### 4.9 Relations Diagram (Interrelationship Diagram) -- Chapter 3

The Relations Diagram takes the five thematic clusters from the Affinity Diagram as its nodes and maps the directional causal relationships among them. The analysis reveals that "Scheduling and Availability" is the primary driver cluster (highest out-arrow count), that "Driver Communication" is both a driver and a result (mixed in/out-arrow counts), and that "Payment and Fare Transparency" is a downstream effect cluster (highest in-arrow count) that will partially resolve itself once scheduling reliability is addressed. This driver-effect analysis is critical for feature prioritisation: it confirms that the app's real-time availability display and booking confirmation feature must be built first, with the payment module following. The Relations Diagram prevents the team from prioritising the most visible symptom (cash payment friction) at the expense of the underlying structural driver (scheduling opacity). The artifact is in `analysis/07_relations/`.

---

## 5. Shortlist: Concepts Referenced (Not as Full Artifacts)

### 5.1 RATER Model -- Chapter 1

The RATER model provides the vocabulary for a gap analysis between the current e-rickshaw service and student expectations. The current service is assessed as deficient on Reliability (rides are inconsistent and unpredictable), Responsiveness (no channel for students to communicate needs or receive updates), and Tangibles (no digital interface or fare display board). The model does not generate a numerical SERVQUAL score in this project because doing so would require a matched-pair survey instrument beyond the project's scope, but its five dimensions structure the problem diagnosis narrative and ensure that the solution addresses service quality holistically rather than focusing narrowly on technical features.

### 5.2 Cost of Quality -- PAF Model -- Chapter 1

The PAF model frames the investment in the e-rickshaw app as a prevention cost that is economically justified by the scale of current failure costs. The failure cost side of the equation includes student time wasted waiting (quantified at approximately 15-20 minutes per unsuccessful ride attempt), driver income lost due to inefficient dispatch, and the reputational cost to campus administration of a visibly poor transport service. The prevention cost is the one-time app development and deployment expense. This framing makes the business case for the project in language that resonates with institutional decision-makers and grounds the recommendation in Chapter 1's cost-of-quality logic.

### 5.3 Garvin's 8 Dimensions -- Chapter 1

Garvin's eight dimensions provide a multi-dimensional quality lens through which the ride experience can be systematically evaluated rather than judged through a single metric. The project applies all eight dimensions descriptively: Performance (wait time and ride time), Features (booking, tracking, digital payment), Reliability (consistency across days and demand levels), Conformance (adherence to agreed fare and route), Durability (vehicle condition over time), Serviceability (ease of resolving disputes or errors), Aesthetics (the cleanliness and comfort of the physical ride), and Perceived Quality (students' overall trust in the service). This structured evaluation reveals that the service is weakest on Features, Reliability, and Conformance -- precisely the dimensions that a technology intervention can address.

### 5.4 Histogram and Scatter Diagram -- Chapter 2

A histogram of student-reported wait times is constructed from the survey data to characterise the wait-time distribution. The distribution is right-skewed, with a mode of approximately 5 minutes and a long tail extending to 30 minutes or more, indicating that while many students experience moderate waits, a significant minority experience severely long waits that would be invisible in a simple average. A scatter plot of destination distance against reported ride time is also produced to check for systematic fare anomalies: if shorter routes are taking disproportionately long, that would suggest inefficient driver dispatch rather than traffic conditions. Both plots are referenced in the analysis narrative and appear in the data analysis section of the main report.

### 5.5 X-bar/R Intuition -- Chapter 4

The concept of monitoring a continuous quality characteristic over time using subgroup means and ranges is introduced into the post-launch monitoring design. Once the app is operational, wait time for each ride request constitutes a continuous measurement. Grouping rides by 30-minute time blocks across a day creates rational subgroups from which an X-bar/R chart can be constructed to monitor average wait time and within-block variation. This SPC framing is explained in the rollout roadmap (Section 7) and gives the campus transport coordinator a concrete, statistically grounded monitoring tool to use once sufficient data exist. The concept is not applied now because no data have been collected.

### 5.6 DPMO Framing -- Chapter 6

The DPMO concept is used to quantify the severity of two specific defect types in the current e-rickshaw service: (1) rides where the student is unable to find a rickshaw at all (a complete service failure), and (2) payment transactions where the fare charged deviates from the agreed rate (payment leakage). If approximately 25 percent of ride-seeking events result in no ride (per survey estimates), the implied DPMO is 250,000, which places the current service at roughly 2.3 sigma. This framing transforms a qualitative complaint into a quantitative benchmark against which the post-app performance can be measured, making the improvement impact legible in the language of Six Sigma.

### 5.7 Taguchi Loss Function -- Chapter 8

The Taguchi loss function is used to argue that a binary pass/fail criterion for ride punctuality (e.g., "within 5 minutes" versus "more than 5 minutes") understates the true cost of service variation. If the target boarding time is defined as 1 minute from app-request confirmation to driver arrival at the designated pickup point, the quadratic loss function assigns a positive and increasing loss to every ride that deviates from this target, whether by 30 seconds or 4 minutes. This framing supports the case for engineering the system toward minimum variation around the target rather than toward mere specification conformance, and it motivates the post-launch Cpk monitoring discussed in the rollout roadmap.

### 5.8 5S -- Chapter 1

The 5S methodology is applied to the physical pickup-point design proposed as part of the solution. Sort: unnecessary barriers and parked vehicles near pickup zones are removed. Set in Order: designated waiting areas are demarcated with paint and signage, and the app designates specific GPS-geofenced pickup coordinates. Shine: the upkeep of pickup areas is assigned to a named campus worker and tracked via the app's admin dashboard. Standardize: the pickup-point layout, signage design, and boarding procedure are documented in a standard operating procedure shared with drivers and campus security. Sustain: compliance is monitored through periodic audits triggered by the PDCA Check phase. 5S is also applied conceptually to the app's user interface: the screen layout eliminates non-essential options (Sort), places the most frequent action (Book a Ride) in the most prominent position (Set in Order), and maintains visual consistency across screens (Standardize).

---

## 6. Honest Skips: Not Applicable

### 6.1 Acceptance Sampling (Chapter 7)

Acceptance sampling is designed for contexts in which discrete lots of physical items are inspected before acceptance or rejection, and a statistical sampling plan balances the risk of accepting bad lots against the cost of rejecting good ones. The e-rickshaw app project involves a real-time, continuous service delivered individually to each student, with no physical lot and no batch inspection decision point. The entire toolkit of Chapter 7 -- AQL, LQL, producer risk, consumer risk, and OC curves -- has no structural analogue in this context and is therefore set aside entirely.

### 6.2 Quality Award Models (Chapter 9)

The Deming Prize, MBNQA, EFQM, Australian Quality Award, and associated Baldrige Criteria are organisational-level performance excellence frameworks designed for self-assessment by entire enterprises or large organisational units. Applying any of these frameworks to a student project of bounded scope would constitute a category error: the models require longitudinal performance data across multiple business functions, leadership systems, and strategic planning processes that simply do not exist at the project level. They are acknowledged as aspirational frameworks for a future, institutionalised e-rickshaw operation but are not applied in the current project.

### 6.3 Arrow Diagram / PERT-CPM (Chapter 3)

The Arrow Diagram and PERT/CPM methodology are appropriate for complex projects with many interdependent activities, long durations, and significant uncertainty in activity completion times. The e-rickshaw app rollout is a single-semester student project with a small number of clearly sequential phases. The PDCA cycle artifact already captures the iterative logic of the rollout, and a Gantt-style timeline suffices for schedule communication. Constructing a PERT network for a project of this scale would add analytical overhead without proportionate insight.

### 6.4 Matrix Data Analysis (Chapter 3)

Matrix Data Analysis (principal component analysis) is a multivariate statistical technique that requires a substantial numerical data matrix with multiple measured variables across many observations. The project's data set -- a student survey with a few hundred responses and a handful of ordinal variables -- does not have the dimensionality or scale to benefit from PCA. The FMEA's RPN scoring and the Pareto analysis together handle all quantitative prioritisation needs of the project without requiring dimensionality reduction.

### 6.5 Process Capability Cp/Cpk (Chapter 5)

Cp and Cpk require a stable, in-control process with known specification limits and sufficient historical data to estimate the process standard deviation reliably. At this stage of the project, the e-rickshaw service has no defined SLA, no in-control process (the current process is erratic and unmonitored), and no longitudinal data on wait times under the proposed app. Process capability analysis is therefore deferred to the post-launch phase, once three months of app-collected ride data are available and a formal wait-time SLA has been negotiated with campus administration. This is an honest acknowledgement of a tool that will become applicable in the future.

---

## 7. Rollout Roadmap for TQM Application

The TQM tools applied in this project are designed for an active intervention phase, but quality management must continue after the app launches if the improvements are to be sustained and deepened.

In the immediate post-launch period (months one through three), the PDCA cycle governs the pilot: the team collects ride-request and completion data from the app backend, compares wait times against the pilot target of a five-minute median, and makes targeted adjustments to the driver-assignment algorithm and pickup-point signage. During this period, the primary monitoring tool is a simple run chart of daily median wait time, which provides a visual trend signal without requiring the statistical infrastructure of a control chart.

After three months of operation, sufficient data will exist to construct X-bar/R charts for wait time, using 30-minute time blocks as rational subgroups. At this point, the process should be assessed for statistical control, and any special-cause signals should be investigated using a new round of Ishikawa and 5 Whys analysis.

At the six-month review, two additional tools become applicable. First, a Cost-of-Quality accounting exercise using the PAF model should quantify the reduction in failure costs (student time saved, driver idle time reduced) against the prevention cost (app maintenance and server hosting), making the return on investment visible to campus administration. Second, once a formal wait-time SLA is established (for example, "ninety percent of rides commence within three minutes of confirmation"), Cpk can be calculated to characterise the capability of the dispatch process relative to this contractual target. These two additions would represent the project's maturation from a student-scale quality intervention into an institutionalised continuous improvement system aligned with Chapter 5 and Chapter 4 of the course curriculum.

---

*End of Course Content Mapping Document*
*Team B | TQM Course Project | April 2026*
