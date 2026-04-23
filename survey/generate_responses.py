"""
generate_responses.py
Team C-1 | TQM Course Project | April 2026

Generates 150 synthetic survey responses for the campus E-Rickshaw survey.
All randomness is seeded for reproducibility (seed = 20260421).
"""

import numpy as np
import pandas as pd

# ─────────────────────────────────────────────
# 0. Setup
# ─────────────────────────────────────────────
np.random.seed(20260421)
n = 150
OUT_PATH = "/home/pratham/pratham/QM_project/deliverables/survey/responses.csv"

# ─────────────────────────────────────────────
# 1. Shared latent "pain factor" per respondent
#    Higher pain → more dissatisfied, more issues, more receptive to solutions.
# ─────────────────────────────────────────────
pain = np.clip(np.random.normal(0.55, 0.22, n), 0, 1)

# ─────────────────────────────────────────────
# 2. Demographics
# ─────────────────────────────────────────────

# Q1 — Year of study (1st 25%, 2nd 25%, 3rd 20%, 4th 15%, PG 15%)
year_choices = ["1st", "2nd", "3rd", "4th", "PG"]
year_probs   = [0.25, 0.25, 0.20, 0.15, 0.15]
q1_year = np.random.choice(year_choices, size=n, p=year_probs)

# Q2 — Hostel (Govind & Rajendra slightly heavier; Others normalised)
hostel_choices = ["Govind", "Rajendra", "Cautley", "Jawahar",
                  "Kasturba", "Sarojini", "Ravindra", "Other"]
hostel_probs   = [0.18, 0.17, 0.12, 0.12, 0.12, 0.10, 0.10, 0.09]
q2_hostel = np.random.choice(hostel_choices, size=n, p=hostel_probs)

# Q3 — Department (heavier on CSE / ECE / ME)
dept_choices = ["CSE", "ECE", "ME", "CE", "EE",
                "Chemistry", "Physics", "Maths", "HSS", "Other"]
dept_probs   = [0.18, 0.16, 0.14, 0.10, 0.10,
                0.07, 0.07, 0.07, 0.06, 0.05]
q3_department = np.random.choice(dept_choices, size=n, p=dept_probs)

# Q4 — Rides per week (higher for high-pain respondents who depend on it more)
q4_rides_per_week = np.clip(
    np.round(np.random.normal(8 + pain * 4, 3)),
    0, 25
).astype(int)

# ─────────────────────────────────────────────
# 3. Current Usage & Experience
# ─────────────────────────────────────────────

# Q5 — Average wait time during peak hours (minutes)
#       Log-normal so there are realistic long-tail waits.
#       Tuned so the baseline mean sits near 3.2 min and p90 near 5 min,
#       which matches observed campus E-rick behaviour better than the
#       earlier 7-9 min centre.
q5_wait_minutes = np.clip(
    np.round(np.random.lognormal(np.log(2.2 + pain * 1.8), 0.28)),
    1, 15
).astype(int)

# Q6 — Route detour frequency (Likert 1–5)
q6_detour_freq = np.clip(
    np.round(1 + pain * 3.5 + np.random.normal(0, 0.6, n)),
    1, 5
).astype(int)

# Q7 — Payment issue frequency (Likert 1–5); weaker pain link (rarer problem)
q7_payment_issue_freq = np.clip(
    np.round(1 + pain * 2.8 + np.random.normal(0, 0.7, n)),
    1, 5
).astype(int)

# Q8 — Times late to class/lab last month because of E-rick wait
q8_late_incidents = np.clip(
    np.round(pain * 5 + np.random.normal(0, 1.0, n)),
    0, 15
).astype(int)

# Q9 — Driver courtesy (negative correlation with pain)
q9_driver_courtesy = np.clip(
    np.round(4.2 - pain * 1.6 + np.random.normal(0, 0.6, n)),
    1, 5
).astype(int)

# Q10 — Night-time availability satisfaction (negative correlation with pain)
q10_night_availability = np.clip(
    np.round(2.8 - pain * 1.5 + np.random.normal(0, 0.7, n)),
    1, 5
).astype(int)

# Q11 — Overall satisfaction (strong negative correlation with pain)
q11_overall_satisfaction = np.clip(
    np.round(4.2 - pain * 2.4 + np.random.normal(0, 0.5, n)),
    1, 5
).astype(int)

# ─────────────────────────────────────────────
# 4. Pain-Point Ranking
# ─────────────────────────────────────────────

PAIN_POINTS = [
    "long_wait",
    "route_detour",
    "payment_issue",
    "empty_return_seen",
    "rude_driver",
    "no_night_availability",
    "none_of_these",
]

# Per-issue selection probabilities as a function of pain
# Structured as {issue: (base_prob, pain_multiplier)}
ISSUE_PARAMS = {
    "long_wait":            (0.20, 0.70),
    "route_detour":         (0.15, 0.60),
    "payment_issue":        (0.10, 0.55),
    "empty_return_seen":    (0.12, 0.50),
    "rude_driver":          (0.08, 0.45),
    "no_night_availability":(0.18, 0.55),
}

q12_issues_faced = []
q13_top3_ranked  = []

for i in range(n):
    p_i = pain[i]
    selected = []

    for issue, (base, mult) in ISSUE_PARAMS.items():
        prob = base + mult * p_i
        if np.random.random() < prob:
            selected.append(issue)

    # "none_of_these" only if no real issues were selected
    if len(selected) == 0:
        selected = ["none_of_these"]

    q12_issues_faced.append(";".join(selected))

    # Q13 — Rank top 3 from the selected issues (exclude none_of_these)
    rankable = [s for s in selected if s != "none_of_these"]
    if len(rankable) == 0:
        q13_top3_ranked.append("")
    else:
        # Assign random weights; sort descending → top annoyances first
        weights  = np.random.rand(len(rankable))
        order    = np.argsort(-weights)
        top3     = [rankable[j] for j in order[:3]]
        q13_top3_ranked.append(";".join(top3))

# ─────────────────────────────────────────────
# 5. Proposed Solution Willingness
# ─────────────────────────────────────────────

# Q14 — App-based booking willingness (positive with pain)
q14_app_willingness = np.clip(
    np.round(2.5 + pain * 2.2 + np.random.normal(0, 0.6, n)),
    1, 5
).astype(int)

# Q15 — 1-minute boarding window comfort (positive with pain)
q15_1min_window_comfort = np.clip(
    np.round(3 + pain * 1.2 + np.random.normal(0, 0.8, n)),
    1, 5
).astype(int)

# Q16 — In-app wallet comfort (correlated with pain AND Q7 payment issues).
#        Normalise Q7 and blend it with pain so that the Q7–Q16 correlation
#        lands in the 0.40–0.60 range.
payment_z = (q7_payment_issue_freq - q7_payment_issue_freq.mean()) / (
    q7_payment_issue_freq.std() + 1e-9
)
# Blended latent driver: 55% pain, 45% payment_z → boosts Q7-Q16 correlation
blended = 0.55 * pain + 0.45 * (payment_z * 0.22)   # scale payment_z to ~[0,1]
q16_wallet_comfort = np.clip(
    np.round(2.0 + blended * 2.8 + np.random.normal(0, 0.55, n)),
    1, 5
).astype(int)

# Q17 — Wallet top-up amount ₹ (log-normal, rounded to nearest ₹10)
q17_topup_amount = np.clip(
    np.round(np.random.lognormal(np.log(150 + pain * 100), 0.55) / 10) * 10,
    50, 2000
).astype(int)

# Q18 — ₹5 cancellation fee acceptance (pain-sufferers more accepting)
q18_fee_acceptance = np.clip(
    np.round(2.5 + pain * 1.6 + np.random.normal(0, 0.9, n)),
    1, 5
).astype(int)

# Q19 — Fare preference MCQ
#        Low pain  → [per_seat=0.30, fixed=0.55, no_pref=0.15]
#        High pain → [per_seat=0.65, fixed=0.25, no_pref=0.10]
fare_choices = ["per_seat", "fixed", "no_preference"]
q19_fare_preference = []
for p_i in pain:
    w_per  = 0.30 + 0.35 * p_i
    w_fix  = 0.55 - 0.30 * p_i
    w_none = max(0.05, 0.15 - 0.05 * p_i)
    # Renormalise
    total  = w_per + w_fix + w_none
    probs  = [w_per / total, w_fix / total, w_none / total]
    q19_fare_preference.append(np.random.choice(fare_choices, p=probs))

# Q20 — Willingness to share drop-off location (mildly positive with pain)
q20_share_dropoff = np.clip(
    np.round(3.2 + pain * 0.8 + np.random.normal(0, 0.7, n)),
    1, 5
).astype(int)

# Q21 — Dedicated app vs WhatsApp preference (slightly positive with pain)
q21_dedicated_vs_whatsapp = np.clip(
    np.round(3 + pain * 1.1 + np.random.normal(0, 0.8, n)),
    1, 5
).astype(int)

# ─────────────────────────────────────────────
# 6. Open-Ended Responses
# ─────────────────────────────────────────────

OPEN_TEXT_POOL = [
    "Fixed schedule like a shuttle bus would help.",
    "Late-night availability is the biggest issue for library-goers.",
    "GPS tracking so I know exactly when the e-rick will reach.",
    "Per-seat fare makes more sense than paying full for detours.",
    "Separate E-ricks for hostels vs academic area zones.",
    "Drivers should carry change; I never have exact money.",
    "An app would save so much waiting time at Main Gate.",
    "Make a dedicated women's E-rick during late hours.",
    "Show driver name and photo for safety.",
    "Book in advance for post-class pickup — we all leave together.",
    "Drivers are rude when the ride is for a short distance.",
    "Install a visible fare chart — it's different every ride.",
    "Allow group-booking with friends for the same E-rick.",
    "Reduce the 4-seat minimum during off-peak — even 2 passengers is fine.",
]

# ~35% of respondents provide an open-text response
open_mask    = np.random.random(n) < 0.35
q22_open_text = np.where(
    open_mask,
    np.random.choice(OPEN_TEXT_POOL, size=n),  # always sample; masked below
    ""
)
# Apply mask correctly — sample only for those who respond
sampled_texts = np.random.choice(OPEN_TEXT_POOL, size=n)
q22_open_text = np.where(open_mask, sampled_texts, "")

# ─────────────────────────────────────────────
# 7. Contrarian Handling (~5%)
# ─────────────────────────────────────────────

# 8 high-pain respondents (pain > 0.6) who are tech-averse → reduce app scores
high_pain_idx = np.where(pain > 0.6)[0]
if len(high_pain_idx) >= 8:
    contrarian_tech = np.random.choice(high_pain_idx, size=8, replace=False)
else:
    contrarian_tech = high_pain_idx
q14_app_willingness[contrarian_tech]      = np.clip(q14_app_willingness[contrarian_tech] - 2, 1, 5)
q16_wallet_comfort[contrarian_tech]       = np.clip(q16_wallet_comfort[contrarian_tech] - 2, 1, 5)
q21_dedicated_vs_whatsapp[contrarian_tech]= np.clip(q21_dedicated_vs_whatsapp[contrarian_tech] - 2, 1, 5)

# 7 low-pain respondents (pain < 0.35) who are happy → bump satisfaction up
low_pain_idx = np.where(pain < 0.35)[0]
if len(low_pain_idx) >= 7:
    happy_group = np.random.choice(low_pain_idx, size=7, replace=False)
else:
    happy_group = low_pain_idx
q11_overall_satisfaction[happy_group] = np.clip(q11_overall_satisfaction[happy_group] + 1, 1, 5)
q6_detour_freq[happy_group]           = np.clip(q6_detour_freq[happy_group] + 1, 1, 5)
q7_payment_issue_freq[happy_group]    = np.clip(q7_payment_issue_freq[happy_group] + 1, 1, 5)

# ─────────────────────────────────────────────
# 8. Assemble DataFrame
# ─────────────────────────────────────────────

df = pd.DataFrame({
    "respondent_id":            [f"R{i+1:03d}" for i in range(n)],
    "q1_year":                  q1_year,
    "q2_hostel":                q2_hostel,
    "q3_department":            q3_department,
    "q4_rides_per_week":        q4_rides_per_week,
    "q5_wait_minutes":          q5_wait_minutes,
    "q6_detour_freq":           q6_detour_freq,
    "q7_payment_issue_freq":    q7_payment_issue_freq,
    "q8_late_incidents":        q8_late_incidents,
    "q9_driver_courtesy":       q9_driver_courtesy,
    "q10_night_availability":   q10_night_availability,
    "q11_overall_satisfaction": q11_overall_satisfaction,
    "q12_issues_faced":         q12_issues_faced,
    "q13_top3_ranked":          q13_top3_ranked,
    "q14_app_willingness":      q14_app_willingness,
    "q15_1min_window_comfort":  q15_1min_window_comfort,
    "q16_wallet_comfort":       q16_wallet_comfort,
    "q17_topup_amount":         q17_topup_amount,
    "q18_fee_acceptance":       q18_fee_acceptance,
    "q19_fare_preference":      q19_fare_preference,
    "q20_share_dropoff":        q20_share_dropoff,
    "q21_dedicated_vs_whatsapp":q21_dedicated_vs_whatsapp,
    "q22_open_text":            q22_open_text,
})

# ─────────────────────────────────────────────
# 9. Save
# ─────────────────────────────────────────────
df.to_csv(OUT_PATH, index=False)

# ─────────────────────────────────────────────
# 10. Summary Statistics
# ─────────────────────────────────────────────
print("=" * 60)
print("SURVEY RESPONSE GENERATION — SUMMARY")
print("=" * 60)
print(f"Total respondents       : {len(df)}")
print(f"Mean wait time (Q5)     : {df['q5_wait_minutes'].mean():.2f} min")
print(f"Std  wait time (Q5)     : {df['q5_wait_minutes'].std():.2f} min")

corr_q7_q16 = df["q7_payment_issue_freq"].corr(df["q16_wallet_comfort"])
print(f"Corr(Q7, Q16)           : {corr_q7_q16:.4f}  (target: 0.4–0.6)")

pct_empty_q22 = (df["q22_open_text"] == "").mean() * 100
print(f"% empty Q22             : {pct_empty_q22:.1f}%  (target ~65%)")

print("\nPain-point frequency from Q12:")
from collections import Counter
all_issues = []
for row in df["q12_issues_faced"]:
    all_issues.extend(row.split(";"))
counts = Counter(all_issues)
for issue in PAIN_POINTS:
    pct = counts.get(issue, 0) / n * 100
    print(f"  {issue:<25s}: {counts.get(issue, 0):>4d}  ({pct:5.1f}%)")

print("\nYear distribution (Q1):")
print(df["q1_year"].value_counts().sort_index().to_string())

print("\nFare preference distribution (Q19):")
print(df["q19_fare_preference"].value_counts().to_string())
print("=" * 60)
