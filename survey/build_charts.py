"""
build_charts.py  —  Presentation-grade survey charts (NYT-wayfinding style)
Regenerates all 5 survey PNGs at 200 DPI with consistent brand rules.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter

# ─────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────
DATA_CSV = "/home/pratham/pratham/QM_project/deliverables/survey/responses.csv"
OUT_DIR  = "/home/pratham/pratham/QM_project/deliverables/survey/charts"
os.makedirs(OUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# PALETTE
# ─────────────────────────────────────────────
C_TERRA   = "#E85D2F"   # primary accent / bar fill
C_INK     = "#1B1A17"   # text / axis lines
C_SAGE    = "#7C8F7C"   # secondary / positive
C_MAROON  = "#8A1A2B"   # critical / negative
C_MUTED   = "#A39A87"   # muted gray
C_RULE    = "#D9D2C0"   # light rule / gridlines
C_BG      = "#FFFFFF"   # background

FOOTER_TXT = (
    "Source: campus E-rick student survey  (n=150, synthetic pilot data, seed=20260421)"
)

# ─────────────────────────────────────────────
# GLOBAL RCPARAMS
# ─────────────────────────────────────────────
plt.rcParams.update({
    "font.family":          "DejaVu Sans",
    "font.size":            13,
    "axes.labelsize":       16,
    "axes.titlesize":       14,
    "xtick.labelsize":      13,
    "ytick.labelsize":      13,
    "legend.fontsize":      13,
    "axes.spines.top":      False,
    "axes.spines.right":    False,
    "axes.spines.left":     True,
    "axes.spines.bottom":   True,
    "axes.grid":            False,
    "figure.facecolor":     C_BG,
    "axes.facecolor":       C_BG,
    "savefig.facecolor":    C_BG,
})

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def style_spines(ax, color=C_INK, lw=0.8):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(color)
        ax.spines[side].set_linewidth(lw)


def add_title_block(ax, title, subtitle=None, title_size=22, sub_size=14):
    """Left-aligned title + accent rule + subtitle above a single axes.
    Uses axes-fraction coords; suited for single-axes figures where top margin
    is set low enough (top ≈ 0.65–0.70) to leave room above the axes."""
    from matplotlib.lines import Line2D
    # Title
    ax.text(
        0, 1.20, title,
        transform=ax.transAxes,
        fontsize=title_size, fontweight="bold",
        color=C_INK, ha="left", va="bottom",
        fontfamily="DejaVu Serif",
        clip_on=False,
    )
    # Terracotta accent rule — 4 pts below title baseline
    line = Line2D(
        [0, 0.22], [1.15, 1.15],
        transform=ax.transAxes,
        color=C_TERRA, linewidth=3.5,
        solid_capstyle="butt",
        clip_on=False,
    )
    ax.add_artist(line)
    # Subtitle — sits comfortably below the rule
    if subtitle:
        ax.text(
            0, 1.04, subtitle,
            transform=ax.transAxes,
            fontsize=sub_size, color=C_MUTED,
            ha="left", va="bottom",
            clip_on=False,
        )


def add_fig_title_block(fig, title, subtitle=None,
                        x=0.06, y_title=0.97,
                        title_size=22, sub_size=14,
                        rule_width=0.28):
    """Left-aligned title block placed in figure coordinates.
    Use this for multi-axes figures where add_title_block in axes coords
    would overlap subplot titles."""
    from matplotlib.lines import Line2D
    # Title
    fig.text(x, y_title, title,
             fontsize=title_size, fontweight="bold",
             color=C_INK, ha="left", va="bottom",
             fontfamily="DejaVu Serif")
    # Accent rule — uses figure-DPI-aware pixel height; placed via figure transFigure
    # y_rule is y_title minus ~0.035 figure fraction (≈22pt gap on 10" fig)
    y_rule = y_title - 0.040
    fig.add_artist(
        Line2D(
            [x, x + rule_width], [y_rule, y_rule],
            transform=fig.transFigure,
            color=C_TERRA, linewidth=3.5,
            solid_capstyle="butt",
            clip_on=False,
        )
    )
    if subtitle:
        fig.text(x, y_rule - 0.022, subtitle,
                 fontsize=sub_size, color=C_MUTED,
                 ha="left", va="bottom")


def add_footer(fig, text=FOOTER_TXT):
    fig.text(
        0.06, 0.018, text,
        fontsize=10, style="italic",
        color=C_MUTED, ha="left", va="bottom",
    )


def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=200, bbox_inches="tight",
                pad_inches=0.35, facecolor=C_BG)
    plt.close(fig)
    size_kb = os.path.getsize(path) / 1024
    print(f"  {path}  ({size_kb:.1f} KB)")
    return path


# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
df = pd.read_csv(DATA_CSV)

# ═══════════════════════════════════════════════════════════════
# 1. WAIT TIMES HISTOGRAM
# ═══════════════════════════════════════════════════════════════
def chart_histogram():
    wait = df["q5_wait_minutes"].dropna()
    mean_v   = wait.mean()          # 8.23
    median_v = wait.median()        # 7.0
    pct90    = wait.quantile(0.9)   # 13.0

    fig, ax = plt.subplots(figsize=(14, 7.5), constrained_layout=False)
    fig.subplots_adjust(left=0.08, right=0.95, top=0.68, bottom=0.13)

    ax.hist(wait, bins=30, range=(0, 30),
            color=C_TERRA, alpha=0.88,
            edgecolor=C_INK, linewidth=0.8)

    # Reference lines
    ax.axvline(mean_v, color=C_INK, linewidth=2.0, linestyle="-", zorder=4)
    ax.axvline(median_v, color=C_SAGE, linewidth=2.0, linestyle="--", zorder=4)

    # Callout box helper
    ymax = ax.get_ylim()[1]
    def callout(x, label, color, xoffset=0.3):
        ax.annotate(
            label,
            xy=(x, ymax * 0.97),
            xytext=(x + xoffset, ymax * 0.97),
            fontsize=12, color=color,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, lw=0.8),
            ha="left" if xoffset >= 0 else "right",
        )

    callout(mean_v,   f"Mean {mean_v:.1f} min",   C_INK,   xoffset=0.35)
    callout(median_v, f"Median {median_v:.0f} min", C_SAGE, xoffset=-2.8)

    # Stats annotation block (top-right)
    stats_txt = (
        f"n = 150\n"
        f"mean  {mean_v:.1f} min\n"
        f"median  {median_v:.0f} min\n"
        f"90th pct  {pct90:.0f} min"
    )
    ax.text(
        0.70, 0.80, stats_txt,
        transform=ax.transAxes,
        fontsize=12, color=C_INK, va="top", ha="left",
        linespacing=1.6,
        bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=C_RULE, lw=0.8),
    )

    # Axes
    ax.set_xlim(0, 30)
    ax.set_xticks(range(0, 31, 5))
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.set_xlabel("Wait time (minutes)", fontsize=16)
    ax.set_ylabel("Number of respondents", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=13)

    style_spines(ax)

    add_title_block(
        ax,
        title="How long students wait to board an E-rickshaw",
        subtitle="Self-reported peak-hour wait time,  n=150",
    )
    add_footer(fig)

    save(fig, "wait_times_histogram.png")


# ═══════════════════════════════════════════════════════════════
# 2. PAIN POINTS PARETO
# ═══════════════════════════════════════════════════════════════
def chart_pareto():
    # Parse Q12
    all_vals = []
    for v in df["q12_issues_faced"].dropna():
        all_vals.extend([x.strip() for x in str(v).split(";")])

    counts = Counter(all_vals)
    counts.pop("none_of_these", None)

    label_map = {
        "long_wait":           "Long wait time",
        "payment_issue":       "Payment issues",
        "no_night_availability": "No night availability",
        "route_detour":        "Route detours",
        "empty_return_seen":   "Empty return seen",
        "rude_driver":         "Rude driver",
    }

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    keys   = [label_map.get(k, k) for k, _ in sorted_items]
    vals   = [v for _, v in sorted_items]
    total  = sum(vals)
    cumulative = [sum(vals[:i+1]) / total * 100 for i in range(len(vals))]

    top3_pct = cumulative[2]  # 56.8%

    fig, ax1 = plt.subplots(figsize=(14, 7.5), constrained_layout=False)
    fig.subplots_adjust(left=0.08, right=0.90, top=0.68, bottom=0.18)

    x = np.arange(len(keys))
    bars = ax1.bar(x, vals, color=C_TERRA, edgecolor=C_INK, linewidth=0.8, zorder=3)

    # Bar top annotations
    for bar, val in zip(bars, vals):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.8,
            str(val),
            ha="center", va="bottom", fontsize=12, color=C_INK,
        )

    ax1.set_xticks(x)
    ax1.set_xticklabels(keys, rotation=20, ha="right", fontsize=13)
    ax1.set_xlabel("Pain point", fontsize=16)
    ax1.set_ylabel("Mentions (count)", fontsize=16)
    ax1.tick_params(axis="y", labelsize=13)
    style_spines(ax1)

    # Secondary axis — cumulative %
    ax2 = ax1.twinx()
    ax2.plot(x, cumulative, color=C_INK, marker="o",
             markersize=8, linewidth=2.5, zorder=5)
    ax2.set_ylim(0, 110)
    ax2.set_ylabel("Cumulative %", fontsize=16)
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax2.tick_params(axis="y", labelsize=13)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color(C_INK)
    ax2.spines["right"].set_linewidth(0.8)

    # 80% reference line
    ax2.axhline(80, color=C_MUTED, linestyle="--",
                linewidth=1.4, zorder=2)
    ax2.text(len(keys) - 0.05, 81.5, "80% threshold",
             ha="right", va="bottom", fontsize=11, color=C_MUTED)

    # Legend
    bar_patch = mpatches.Patch(color=C_TERRA, label="Mentions")
    line_handle, = ax1.plot([], [], color=C_INK, marker="o",
                            markersize=7, linewidth=2, label="Cumulative %")
    ax1.legend(
        handles=[bar_patch, line_handle],
        loc="upper right", fontsize=13,
        frameon=True, framealpha=0.95,
        edgecolor=C_RULE,
    )

    add_title_block(
        ax1,
        title="Pareto — Student-reported E-rick pain points",
        subtitle=f"Top three issues account for {top3_pct:.1f}% of mentions",
    )
    add_footer(fig)

    save(fig, "pain_points_pareto.png")


# ═══════════════════════════════════════════════════════════════
# 3. LIKERT DISTRIBUTIONS (4×2 grid)
# ═══════════════════════════════════════════════════════════════
def chart_likert():
    left_cols = [
        ("q6_detour_freq",           "Detour frequency (Q6)"),
        ("q7_payment_issue_freq",     "Payment issue freq (Q7)"),
        ("q10_night_availability",    "Night availability (Q10)"),
        ("q11_overall_satisfaction",  "Overall satisfaction (Q11)"),
    ]
    right_cols = [
        ("q14_app_willingness",       "App willingness (Q14)"),
        ("q15_1min_window_comfort",   "1-min window comfort (Q15)"),
        ("q16_wallet_comfort",        "Wallet comfort (Q16)"),
        ("q18_fee_acceptance",        "Fee acceptance (Q18)"),
    ]

    fig, axes = plt.subplots(
        4, 2, figsize=(16, 11),
        constrained_layout=False,
    )
    fig.subplots_adjust(
        left=0.09, right=0.97,
        top=0.76, bottom=0.08,
        hspace=0.60, wspace=0.25,
    )

    x_ticks = [1, 2, 3, 4, 5]

    for row in range(4):
        for col, (col_list, color) in enumerate(
            [(left_cols, C_SAGE), (right_cols, C_TERRA)]
        ):
            col_name, col_label = col_list[row]
            ax = axes[row][col]

            vc = df[col_name].value_counts().sort_index()
            # Ensure all 1-5 present
            vc = vc.reindex(x_ticks, fill_value=0)

            bars = ax.bar(vc.index, vc.values,
                          color=color, edgecolor=C_INK,
                          linewidth=0.7, width=0.65, zorder=3)

            # Bar-top counts
            for bar, cnt in zip(bars, vc.values):
                if cnt > 0:
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.5,
                        str(cnt),
                        ha="center", va="bottom", fontsize=10, color=C_INK,
                    )

            ax.set_title(col_label, fontsize=14, fontweight="bold",
                         color=C_INK, pad=6)
            ax.set_xticks(x_ticks)
            ax.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=13)
            ax.tick_params(axis="y", labelsize=12)

            # x-label only on bottom row
            if row == 3:
                ax.set_xlabel("Response (1–5)", fontsize=14)

            # y-label only on left column
            if col == 0:
                ax.set_ylabel("Respondents", fontsize=14)

            style_spines(ax)

            # Extend y a bit so bar-top labels don't clip
            ax.set_ylim(0, vc.values.max() * 1.18)

    add_fig_title_block(
        fig,
        title="Likert distributions — Current pain vs willingness to adopt",
        subtitle="Left column: current experience   /   Right column: willingness to adopt the app",
        x=0.09, y_title=0.97,
        rule_width=0.30,
    )

    add_footer(fig)
    save(fig, "likert_distributions.png")


# ═══════════════════════════════════════════════════════════════
# 4. WALLET WILLINGNESS BAR
# ═══════════════════════════════════════════════════════════════
def chart_wallet():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7),
                                    constrained_layout=False)
    fig.subplots_adjust(left=0.08, right=0.97,
                        top=0.76, bottom=0.13, wspace=0.30)

    # ── Left: Q16 Likert distribution ──
    q16 = df["q16_wallet_comfort"].value_counts().sort_index().reindex([1,2,3,4,5], fill_value=0)
    bars = ax1.bar(q16.index, q16.values,
                   color=C_TERRA, edgecolor=C_INK,
                   linewidth=0.8, width=0.65, zorder=3)

    for bar, cnt in zip(bars, q16.values):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(cnt),
            ha="center", va="bottom", fontsize=12, color=C_INK,
        )

    pct_45 = (df["q16_wallet_comfort"] >= 4).sum() / len(df) * 100
    ax1.text(
        0.96, 0.97,
        f"{pct_45:.1f}% rated 4 or 5",
        transform=ax1.transAxes, fontsize=12,
        color=C_INK, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=C_RULE, lw=0.8),
    )

    ax1.set_xticks([1, 2, 3, 4, 5])
    ax1.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=13)
    ax1.set_xlabel("Response (1=Very Uncomfortable, 5=Very Comfortable)", fontsize=13)
    ax1.set_ylabel("Number of respondents", fontsize=16)
    ax1.set_title("Wallet comfort (Q16)", fontsize=14, fontweight="bold",
                  color=C_INK, pad=6)
    ax1.set_ylim(0, q16.values.max() * 1.18)
    style_spines(ax1)

    # ── Right: Q17 histogram ──
    q17 = df["q17_topup_amount"].dropna()
    mean17   = q17.mean()    # ₹245.5
    median17 = q17.median()  # ₹230

    ax2.hist(q17, bins=20, color=C_TERRA, alpha=0.88,
             edgecolor=C_INK, linewidth=0.8, zorder=3)

    ax2.axvline(median17, color=C_SAGE, linewidth=2.0,
                linestyle="--", zorder=5, label=f"Median ₹{median17:.0f}")
    ax2.axvline(mean17,   color=C_INK,  linewidth=2.0,
                linestyle="-",  zorder=5, label=f"Mean ₹{mean17:.0f}")

    ax2.legend(fontsize=12, frameon=True, framealpha=0.95,
               edgecolor=C_RULE, loc="upper right")

    # Stats annotation
    ax2.text(
        0.96, 0.97,
        f"mean  ₹{mean17:.0f}\nmedian  ₹{median17:.0f}",
        transform=ax2.transAxes, fontsize=12,
        color=C_INK, ha="right", va="top",
        linespacing=1.7,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=C_RULE, lw=0.8),
    )

    ax2.set_xlabel("Top-up amount (₹)", fontsize=16)
    ax2.set_ylabel("Number of respondents", fontsize=16)
    ax2.set_title("Expected top-up amount (Q17)", fontsize=14, fontweight="bold",
                  color=C_INK, pad=6)
    style_spines(ax2)

    add_fig_title_block(
        fig,
        title="In-app wallet — comfort and expected balance",
        subtitle="Q16 Likert distribution (left) and Q17 planned top-up amount (right)",
        x=0.06, y_title=0.97,
        rule_width=0.30,
    )
    add_footer(fig)

    save(fig, "wallet_willingness_bar.png")


# ═══════════════════════════════════════════════════════════════
# 5. CORRELATION HEATMAP
# ═══════════════════════════════════════════════════════════════
def chart_heatmap():
    heatmap_cols = [
        "q4_rides_per_week",
        "q5_wait_minutes",
        "q6_detour_freq",
        "q7_payment_issue_freq",
        "q8_late_incidents",
        "q9_driver_courtesy",
        "q10_night_availability",
        "q11_overall_satisfaction",
        "q14_app_willingness",
        "q15_1min_window_comfort",
        "q16_wallet_comfort",
        "q18_fee_acceptance",
        "q20_share_dropoff",
        "q21_dedicated_vs_whatsapp",
    ]

    label_map = {
        "q4_rides_per_week":        "Rides/week (Q4)",
        "q5_wait_minutes":          "Wait time (Q5)",
        "q6_detour_freq":           "Detour freq (Q6)",
        "q7_payment_issue_freq":    "Payment issues (Q7)",
        "q8_late_incidents":        "Late incidents (Q8)",
        "q9_driver_courtesy":       "Driver courtesy (Q9)",
        "q10_night_availability":   "Night avail. (Q10)",
        "q11_overall_satisfaction": "Overall sat. (Q11)",
        "q14_app_willingness":      "App willingness (Q14)",
        "q15_1min_window_comfort":  "1-min window (Q15)",
        "q16_wallet_comfort":       "Wallet comfort (Q16)",
        "q18_fee_acceptance":       "Fee acceptance (Q18)",
        "q20_share_dropoff":        "Share drop-off (Q20)",
        "q21_dedicated_vs_whatsapp":"Dedicated app (Q21)",
    }

    corr = df[heatmap_cols].corr()
    corr.columns = [label_map[c] for c in corr.columns]
    corr.index   = [label_map[c] for c in corr.index]

    fig, ax = plt.subplots(figsize=(13, 11), constrained_layout=False)
    fig.subplots_adjust(left=0.22, right=0.90, top=0.68, bottom=0.22)

    sns.heatmap(
        corr,
        ax=ax,
        cmap="RdBu_r",
        center=0,
        vmin=-1, vmax=1,
        annot=True,
        fmt=".2f",
        annot_kws={"size": 10, "color": C_INK},
        linewidths=0.5,
        linecolor="white",
        cbar_kws={
            "label": "Pearson r",
            "shrink": 0.75,
            "ticks": [-1, -0.5, 0, 0.5, 1],
        },
    )

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=35, ha="right", fontsize=12,
    )
    ax.set_yticklabels(
        ax.get_yticklabels(),
        rotation=0, fontsize=12,
    )

    # Colorbar label size
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label("Pearson r", fontsize=13)

    add_title_block(
        ax,
        title="Pain drives openness — correlation matrix",
        subtitle="Pearson r between pain indicators and solution willingness",
    )

    # Footnote highlight below footer
    fig.text(
        0.06, 0.003,
        "Highlight: r(Q7 payment, Q16 wallet) = 0.40;  r(Q11 satisfaction, Q14 app_will) = −0.27",
        fontsize=10, style="italic", color=C_MUTED,
        ha="left", va="bottom",
    )

    add_footer(fig)
    save(fig, "correlation_heatmap.png")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating charts …")
    print()

    print("1/5  wait_times_histogram")
    chart_histogram()

    print("2/5  pain_points_pareto")
    chart_pareto()

    print("3/5  likert_distributions")
    chart_likert()

    print("4/5  wallet_willingness_bar")
    chart_wallet()

    print("5/5  correlation_heatmap")
    chart_heatmap()

    print()
    print("Done.")
