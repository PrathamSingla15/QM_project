"""
build_process_diagrams.py
TQM Project - Team D
Presentation-grade process/operational diagrams:
  05 Flowchart (current vs future)
  06 FMEA table
  07 PDCA cycle
  08 Affinity diagram

Run: /home/pratham/pratham/QM_project/.venv/bin/python build_process_diagrams.py
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Wedge, Polygon, Circle

# ---------------------------------------------------------------------------
# Shared palette, constants, helpers
# ---------------------------------------------------------------------------
INK         = "#1B1A17"
TERRACOTTA  = "#E85D2F"
TERRACOTTA2 = "#C94A1F"   # deeper terracotta variant
SAGE        = "#7C8F7C"
MAROON      = "#8A1A2B"
MUTED       = "#A39A87"
SOFT_MUTED  = "#6E6A60"
RULE        = "#D9D2C0"
PANEL       = "#FAF7EF"
ACCENT_FILL = "#FCEDE1"
SUCCESS_FIL = "#EFF2EB"
MAROON_TINT = "#F4E2E5"
WHITE       = "#FFFFFF"

BASE = "/home/pratham/pratham/QM_project/deliverables/analysis"

BODY_FONT  = "DejaVu Sans"
TITLE_FONT = "DejaVu Serif"


def draw_title(fig, title, subtitle, x_in=0.4,
               title_top_in=None, sub_top_in=None, rule_top_in=None):
    """Top-left title block drawn in figure-inch coordinates.

    x_in           - left margin of title, in inches
    title_top_in   - vertical location of title baseline, in inches from fig
                     BOTTOM. If None, computed as (fh - 0.45).
    sub_top_in     - subtitle top position in inches from fig bottom.
    rule_top_in    - top of terracotta accent rule in inches from fig bottom.

    All three text/rule items are rendered with transform=fig.transFigure so
    they remain precisely positioned regardless of individual axes aspect.
    """
    fw, fh = fig.get_size_inches()
    if title_top_in is None:
        title_top_in = fh - 0.45
    if sub_top_in is None:
        sub_top_in = title_top_in - 0.50
    if rule_top_in is None:
        # Rule sits clear of subtitle descender
        rule_top_in = sub_top_in - 0.45

    # Convert inches to figure fraction
    x_frac = x_in / fw
    y_title = title_top_in / fh
    y_sub = sub_top_in / fh
    y_rule = rule_top_in / fh

    fig.text(x_frac, y_title, title,
             ha="left", va="top",
             fontsize=26, fontweight="bold",
             family=TITLE_FONT, color=INK)
    fig.text(x_frac, y_sub, subtitle,
             ha="left", va="top",
             fontsize=16, color=SOFT_MUTED, family=BODY_FONT)

    rule_w_frac = 2.0 / fw
    rule_h_frac = 0.05 / fh
    rect = Rectangle((x_frac, y_rule), rule_w_frac, rule_h_frac,
                     transform=fig.transFigure,
                     facecolor=TERRACOTTA, edgecolor="none", zorder=10)
    fig.add_artist(rect)


def draw_footer(fig, tool_name, chapter_ref, module):
    fig.text(0.04, 0.015,
             f"TQM Tool: {tool_name} - Ref. Ch.{chapter_ref} {module}",
             style="italic", color=MUTED, size=10, family=BODY_FONT)


def save_png(fig, folder, filename="diagram.png", dpi=200):
    out = os.path.join(BASE, folder, filename)
    fig.savefig(out, dpi=dpi, bbox_inches="tight", pad_inches=0.4,
                facecolor="white")
    plt.close(fig)
    size = os.path.getsize(out)
    print(f"  Saved: {out}  ({size/1024:.0f} KB)")
    return size


# ---------------------------------------------------------------------------
# 05 - Flowchart: Current vs Future state
# ---------------------------------------------------------------------------
def render_flowchart():
    print("Building 05_flowchart_current_vs_future ...")
    fig = plt.figure(figsize=(20, 13), facecolor="white")
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 13)
    ax.set_axis_off()

    # Title + subtitle
    draw_title(
        fig,
        "Process flow - Current state vs. App-mediated future state",
        "Boxes: activity steps.  Diamonds: decision / delay.  "
        "Red fill: pain point.  Green fill: improvement.",
        x_in=0.55,
    )

    # Dashed vertical divider down the middle
    ax.plot([10.0, 10.0], [0.55, 10.7],
            color=RULE, linewidth=1.5, linestyle=(0, (6, 4)), zorder=1)

    # Panel headers
    ax.text(5.0, 10.55, "Current State",
            ha="center", va="center",
            fontsize=20, fontweight="bold", family=BODY_FONT, color=INK)
    ax.text(15.0, 10.55, "Future State (app-mediated)",
            ha="center", va="center",
            fontsize=20, fontweight="bold", family=BODY_FONT, color=INK)

    # Panel header underline
    ax.plot([2.5, 7.5], [10.25, 10.25], color=INK, linewidth=0.9)
    ax.plot([12.0, 18.0], [10.25, 10.25], color=INK, linewidth=0.9)

    # ----- Step definitions -----
    # kind: 'rect' or 'diamond'
    # role: 'neutral' | 'pain' | 'improve'
    # sub: optional sub-annotation shown to the right (muted text)
    current_steps = [
        ("rect",    "Student arrives at E-rick pickup point",            "neutral", None),
        ("diamond", "Is there an E-rick waiting?",                       "neutral", "No -> wait until one arrives"),
        ("rect",    "Driver will not depart until 4 passengers board",   "pain",    None),
        ("diamond", "Does route align with your destination?",           "neutral", "No -> loop back, re-board later"),
        ("rect",    "Board E-rick with 3 others",                        "neutral", None),
        ("rect",    "Driver serves farthest drop-off first or last",     "neutral", None),
        ("rect",    "Each student drops off in sequence",                "neutral", None),
        ("rect",    "Pay cash at drop-off",                              "pain",    "Leakage"),
        ("rect",    "Driver returns to home zone empty",                 "pain",    "Empty return"),
    ]
    future_steps = [
        ("rect",    "Student opens campus E-rick app",                           "neutral", None),
        ("rect",    "Sees E-ricks within 100 m with passenger counts / ETAs",    "improve", None),
        ("rect",    "Taps to book a seat; picks drop-off from campus dropdown",  "improve", None),
        ("rect",    "60-second boarding countdown starts",                       "neutral", None),
        ("diamond", "Did student reach the E-rick in 60 s?",                     "neutral", "No -> auto-cancel + Rs.5 fee"),
        ("rect",    "Boards E-rick; driver taps 'Reached' to confirm",           "improve", None),
        ("rect",    "Route auto-aggregates by destination similarity",           "improve", None),
        ("rect",    "Wallet auto-debits at drop-off",                            "improve", "Leakage eliminated"),
        ("rect",    "App shows nearby bookings for the return trip",             "improve", "Empty return eliminated"),
    ]

    # Geometry
    top_y       = 9.6            # center-y of first step
    step_gap    = 1.00           # vertical spacing between step centers
    box_w, box_h = 5.6, 0.78
    diamond_w, diamond_h = 5.6, 1.00

    def role_style(role):
        if role == "pain":
            return dict(fc=MAROON_TINT, ec=MAROON, tc=MAROON)
        if role == "improve":
            return dict(fc=SUCCESS_FIL, ec=SAGE, tc=INK)
        return dict(fc=PANEL, ec=INK, tc=INK)

    def draw_step(cx, cy, kind, label, role, sub):
        st = role_style(role)
        if kind == "rect":
            x0, y0 = cx - box_w / 2, cy - box_h / 2
            patch = FancyBboxPatch(
                (x0, y0), box_w, box_h,
                boxstyle="round,pad=0.22,rounding_size=0.14",
                facecolor=st["fc"], edgecolor=st["ec"],
                linewidth=1.4, zorder=3,
            )
            ax.add_patch(patch)
            ax.text(cx, cy, label,
                    ha="center", va="center",
                    fontsize=12.2, family=BODY_FONT, color=st["tc"],
                    zorder=4)
            top_anchor = cy + box_h / 2
            bot_anchor = cy - box_h / 2
        else:
            pts = [
                (cx, cy + diamond_h / 2),
                (cx + diamond_w / 2, cy),
                (cx, cy - diamond_h / 2),
                (cx - diamond_w / 2, cy),
            ]
            patch = Polygon(pts, closed=True,
                            facecolor=st["fc"], edgecolor=st["ec"],
                            linewidth=1.4, zorder=3)
            ax.add_patch(patch)
            ax.text(cx, cy, label,
                    ha="center", va="center",
                    fontsize=12.2, fontweight="bold",
                    family=BODY_FONT, color=st["tc"], zorder=4)
            top_anchor = cy + diamond_h / 2
            bot_anchor = cy - diamond_h / 2

        if sub:
            ax.text(cx + box_w / 2 + 0.25, cy, sub,
                    ha="left", va="center",
                    fontsize=10, style="italic",
                    family=BODY_FONT, color=SOFT_MUTED, zorder=4)

        return top_anchor, bot_anchor

    def draw_arrow(cx, y_from, y_to):
        ax.annotate(
            "", xy=(cx, y_to), xytext=(cx, y_from),
            arrowprops=dict(arrowstyle="-|>", lw=1.8,
                            color=INK, mutation_scale=18),
            zorder=2,
        )

    def render_panel(cx, steps):
        anchors = []
        for i, (kind, label, role, sub) in enumerate(steps):
            cy = top_y - i * step_gap
            ta, ba = draw_step(cx, cy, kind, label, role, sub)
            anchors.append((ta, ba))
        for i in range(len(steps) - 1):
            _, ba = anchors[i]
            ta_next, _ = anchors[i + 1]
            draw_arrow(cx, ba - 0.02, ta_next + 0.02)

    render_panel(5.0, current_steps)
    render_panel(15.0, future_steps)

    # Legend at bottom center
    legend_y = 0.70
    lx0 = 3.5
    items = [
        (MAROON_TINT, MAROON, "Maroon-tinted = current pain point"),
        (SUCCESS_FIL, SAGE,   "Sage-tinted = future-state improvement"),
        (PANEL,       INK,    "Cream = neutral step / decision"),
    ]
    # Centered group: compute widths
    swatch_w = 0.55
    gap_in_item = 0.25
    inter_item = 1.1
    # approximate text widths so group can be centered
    total_w = 0
    widths = []
    for _, _, lab in items:
        # crude estimate: 0.12 inches per char at 12pt; in data units the
        # canvas is 20 wide -> ~ 0.12 per char
        text_w = len(lab) * 0.11
        widths.append(text_w)
        total_w += swatch_w + gap_in_item + text_w
    total_w += inter_item * (len(items) - 1)
    start_x = (20 - total_w) / 2
    cur_x = start_x
    for (fc, ec, lab), tw in zip(items, widths):
        ax.add_patch(Rectangle((cur_x, legend_y - 0.18), swatch_w, 0.36,
                               facecolor=fc, edgecolor=ec, linewidth=1.2))
        ax.text(cur_x + swatch_w + gap_in_item, legend_y, lab,
                ha="left", va="center", fontsize=11,
                family=BODY_FONT, color=INK)
        cur_x += swatch_w + gap_in_item + tw + inter_item

    draw_footer(fig, "Process Flowchart", "2", "Basic 7 QC Tools")
    return save_png(fig, "05_flowchart_current_vs_future")


# ---------------------------------------------------------------------------
# 06 - FMEA table
# ---------------------------------------------------------------------------
FMEA_ROWS = [
    # (id, failure_mode, effect, S, cause, O, current_control, D, RPN, mitigation)
    (1,  "Seat-stealing",
         "Booked student displaced",
         6, "No physical reservation enforcement", 3,
         "None", 5, 90,
         "Driver 'Reached' press locks seat to physically-present student."),
    (2,  "Driver mistakenly taps 'Reached'",
         "Ride billed without boarding",
         4, "UI button too accessible", 4,
         "None", 3, 48,
         "5-second undo toast after tap."),
    (3,  "Wallet insufficient at ride-end",
         "Unpaid fare; driver dispute",
         5, "No pre-ride balance check", 5,
         "None", 4, 100,
         "Rs.50 soft debt cap; block new bookings until cleared."),
    (4,  "Race: two bookings same seat",
         "Double booking conflict",
         5, "Concurrent API writes", 2,
         "None", 2, 20,
         "Server-side first-write-wins; loser gets alternate E-rick."),
    (5,  "Mid-ride drop-off change",
         "Route disruption; fare error",
         4, "No lock after boarding", 4,
         "None", 5, 80,
         "Lock after driver taps 'Reached'; visible banner."),
    (6,  "Driver offline / GPS lost",
         "Ride stuck; students stranded",
         7, "Network gaps on campus", 3,
         "None", 6, 126,
         "30-sec heartbeat; offline-continuation banner; fare reconciled on reconnect."),
    (7,  "Capacity full + offline passenger add",
         "Overcrowding; safety risk",
         5, "No hard capacity check", 5,
         "Verbal rule", 2, 50,
         "Reducer-level hard block with clear error."),
    (8,  "Cancellation-fee dispute",
         "User frustration; churn",
         4, "No in-app dispute channel", 5,
         "Verbal complaint", 6, 120,
         "One-tap dispute; 24h admin review."),
    (9,  "Student repeated no-shows",
         "Driver revenue loss; trust erosion",
         5, "No accountability system", 4,
         "None", 3, 60,
         "3-strikes 7-day rule; 1-hour cooldown; reputation meter."),
    (10, "Two E-ricks at same location",
         "Student confusion; missed ride",
         3, "No differentiation in UI", 6,
         "None", 4, 72,
         "Stacked card list ordered by passenger count + drop-off alignment."),
]


def _wrap_text(text, width):
    """Simple word-wrap into a multi-line string, given a target char width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def render_fmea():
    print("Building 06_fmea ...")
    fig = plt.figure(figsize=(20, 12.5), facecolor="white")
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12.5)
    ax.set_axis_off()

    draw_title(
        fig,
        "FMEA - Failure mode and effects analysis of the proposed app",
        "Ten edge cases scored Severity x Occurrence x Detection.  "
        "Top-3 RPN rows highlighted in terracotta.",
        x_in=0.55,
    )

    # Column layout (widths sum to 17.5, left edge x=1.25)
    col_defs = [
        ("#",                0.40,  "center", 4),
        ("Failure Mode",     2.80,  "left",   26),
        ("Effect",           2.10,  "left",   22),
        ("S",                0.70,  "center", 2),
        ("Cause",            2.45,  "left",   26),
        ("O",                0.70,  "center", 2),
        ("Current Control",  2.45,  "left",   22),
        ("D",                0.70,  "center", 2),
        ("RPN",              0.90,  "center", 4),
        ("Mitigation",       4.20,  "left",   40),
    ]

    x_left = 1.25
    col_edges = [x_left]
    for _, w, _, _ in col_defs:
        col_edges.append(col_edges[-1] + w)

    # Sort rows by RPN descending
    sorted_rows = sorted(FMEA_ROWS, key=lambda r: r[8], reverse=True)

    header_h = 0.70
    row_h    = 0.85
    table_top_y = 10.20
    header_y0 = table_top_y - header_h

    # Header row
    for ci, (label, w, _, _) in enumerate(col_defs):
        x0 = col_edges[ci]
        ax.add_patch(Rectangle(
            (x0, header_y0), w, header_h,
            facecolor=INK, edgecolor="white", linewidth=0.8, zorder=2,
        ))
        ax.text(x0 + w / 2, header_y0 + header_h / 2, label,
                ha="center", va="center",
                fontsize=13, fontweight="bold", color="white",
                family=BODY_FONT, zorder=3)

    # Data rows
    n_rows = len(sorted_rows)
    for ri, row in enumerate(sorted_rows):
        y0 = header_y0 - (ri + 1) * row_h
        is_top3 = ri < 3

        base_fill = PANEL if (ri % 2 == 1) else "white"
        fill = ACCENT_FILL if is_top3 else base_fill

        # full-row background (so alternating/highlight shows through)
        ax.add_patch(Rectangle(
            (col_edges[0], y0), sum(c[1] for c in col_defs), row_h,
            facecolor=fill, edgecolor="none", zorder=2,
        ))

        # cell borders and text
        row_values = [
            str(row[0]),
            row[1],
            row[2],
            str(row[3]),
            row[4],
            str(row[5]),
            row[6],
            str(row[7]),
            str(row[8]),
            row[9],
        ]

        for ci, ((_, w, align, wrap_w), val) in enumerate(zip(col_defs, row_values)):
            x0 = col_edges[ci]
            # Vertical dividers (light rule)
            ax.plot([x0 + w, x0 + w], [y0, y0 + row_h],
                    color=RULE, linewidth=0.6, zorder=3)

            # Text
            wrapped = _wrap_text(val, wrap_w) if wrap_w else val
            tc = INK
            fw = "normal"
            size = 11
            if col_defs[ci][0] == "RPN":
                fw = "bold"
                size = 12
                if is_top3:
                    tc = MAROON

            if align == "center":
                tx = x0 + w / 2
                ha = "center"
            else:
                tx = x0 + 0.18
                ha = "left"

            ax.text(tx, y0 + row_h / 2, wrapped,
                    ha=ha, va="center",
                    fontsize=size, color=tc, fontweight=fw,
                    family=BODY_FONT, linespacing=1.15, zorder=4)

        # Horizontal rule under each row
        ax.plot([col_edges[0], col_edges[-1]], [y0, y0],
                color=RULE, linewidth=0.6, zorder=3)

    # Outer table frame
    total_w = sum(c[1] for c in col_defs)
    table_bot_y = header_y0 - n_rows * row_h
    ax.add_patch(Rectangle(
        (x_left, table_bot_y), total_w, table_top_y - table_bot_y,
        facecolor="none", edgecolor=INK, linewidth=1.3, zorder=5,
    ))

    # Legend (top-3 swatch)
    leg_y = table_bot_y - 0.5
    ax.add_patch(Rectangle((x_left, leg_y - 0.22), 0.42, 0.30,
                           facecolor=ACCENT_FILL, edgecolor=TERRACOTTA,
                           linewidth=1.2))
    ax.text(x_left + 0.55, leg_y - 0.07,
            "Top-3 RPN rows highlighted in terracotta.  "
            "RPN = S x O x D; higher values mean higher risk and priority.",
            ha="left", va="center", fontsize=11,
            family=BODY_FONT, color=INK)

    draw_footer(fig, "FMEA", "10", "Reliability & Risk")
    return save_png(fig, "06_fmea")


# ---------------------------------------------------------------------------
# 07 - PDCA Cycle
# ---------------------------------------------------------------------------
def render_pdca():
    print("Building 07_pdca ...")
    fig = plt.figure(figsize=(14, 12), facecolor="white")
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal")
    ax.set_axis_off()

    draw_title(
        fig,
        "PDCA - Plan-Do-Check-Act rollout for the E-rick app",
        "Iterative deployment grounded in measurement;  "
        "one full cycle = 4 - 6 weeks per zone.",
        x_in=0.55,
    )

    # Wedge spec (matplotlib angles are counter-clockwise from +x axis)
    # PLAN top-right    : 45 - 135
    # ACT  top-left     : 135 - 225
    # CHECK bottom-left : 225 - 315
    # DO   bottom-right : 315 - 45   (angle wraps through 360)
    quadrants = [
        dict(name="PLAN",  start=45,  end=135, color=TERRACOTTA, alpha=0.88,
             letter="P",
             bullets=[
                 "Identify pain points",
                 "Define wait and leakage KPIs",
                 "Design MVP and pilot zone",
             ]),
        dict(name="ACT",   start=135, end=225, color=INK,        alpha=0.92,
             letter="A",
             bullets=[
                 "Standardise winning features",
                 "Iterate on new pain points",
                 "Update driver SOPs",
             ]),
        dict(name="CHECK", start=225, end=315, color=MAROON,     alpha=0.90,
             letter="C",
             bullets=[
                 "Measure KPIs vs baseline",
                 "Collect satisfaction survey",
                 "Run Pareto on complaints",
             ]),
        dict(name="DO",    start=315, end=405, color=SAGE,       alpha=0.90,
             letter="D",
             bullets=[
                 "Build MVP and onboard E-ricks",
                 "Recruit 50 pilot users",
                 "Run 2-week pilot",
             ]),
    ]

    R_outer = 1.05
    R_inner_text = 0.28
    R_letter = 0.86     # letter sits on outer rim
    R_bullets = 0.58    # bullets in the mid-wedge band

    for q in quadrants:
        wedge = Wedge(
            (0, 0), R_outer, q["start"], q["end"],
            facecolor=q["color"], alpha=q["alpha"],
            edgecolor="white", linewidth=4, zorder=2,
        )
        ax.add_patch(wedge)

    for q in quadrants:
        theta_mid = math.radians((q["start"] + q["end"]) / 2)
        # Letter on the outer rim
        lx = R_letter * math.cos(theta_mid)
        ly = R_letter * math.sin(theta_mid)
        ax.text(lx, ly + 0.04, q["letter"],
                ha="center", va="center",
                fontsize=54, fontweight="bold",
                family=TITLE_FONT, color="white", zorder=5)
        ax.text(lx, ly - 0.13, q["name"],
                ha="center", va="center",
                fontsize=14, fontweight="bold",
                family=BODY_FONT, color="white", zorder=5)

        # Bullets in the mid-wedge band - single line each, larger type so
        # they are legible from the back row of a lecture hall.
        bx = R_bullets * math.cos(theta_mid)
        by = R_bullets * math.sin(theta_mid)
        text = "\n".join([f"- {b}" for b in q["bullets"]])
        ax.text(bx, by, text,
                ha="center", va="center",
                fontsize=14, color="white",
                family=BODY_FONT, linespacing=1.55,
                multialignment="left", zorder=5)

    # Central circle - sized to fit PDCA + Cycle labels without collision.
    # No inner arrow icon (it previously overlapped the PDCA wordmark).
    ax.add_patch(Circle((0, 0), R_inner_text,
                        facecolor="white", edgecolor=INK,
                        linewidth=2, zorder=6))
    ax.text(0, 0.06, "PDCA", ha="center", va="center",
            fontsize=22, fontweight="bold", family=TITLE_FONT, color=INK,
            zorder=7)
    ax.text(0, -0.09, "Cycle", ha="center", va="center",
            fontsize=13, family=BODY_FONT, color=SOFT_MUTED, zorder=7)

    # Directional arrows between quadrants (clockwise flow outside the donut)
    # Clockwise order: PLAN -> DO -> CHECK -> ACT -> PLAN
    # Boundary angles (deg) between adjacent quadrants in clockwise direction:
    # PLAN -> DO boundary at 45 deg (between PLAN 45..135 and DO 315..45);
    # curve slightly outside R_outer
    r_arc = R_outer + 0.04
    transitions = [
        # (from_angle_deg, to_angle_deg) small curved segment across the split
        # clockwise means from_angle > to_angle in standard math convention
        (60, 30),     # PLAN -> DO  (across the 45-degree split)
        (330, 300),   # DO -> CHECK (across the 315-degree split)
        (240, 210),   # CHECK -> ACT (across the 225-degree split)
        (150, 120),   # ACT -> PLAN (across the 135-degree split)
    ]
    for a_from, a_to in transitions:
        p1 = (r_arc * math.cos(math.radians(a_from)),
              r_arc * math.sin(math.radians(a_from)))
        p2 = (r_arc * math.cos(math.radians(a_to)),
              r_arc * math.sin(math.radians(a_to)))
        arrow = FancyArrowPatch(
            p1, p2,
            connectionstyle="arc3,rad=-0.35",
            arrowstyle="-|>", mutation_scale=16,
            lw=1.8, color=INK, zorder=6,
        )
        ax.add_patch(arrow)

    draw_footer(fig, "PDCA Cycle", "1", "TQM Fundamentals")
    return save_png(fig, "07_pdca")


# ---------------------------------------------------------------------------
# 08 - Affinity Diagram
# ---------------------------------------------------------------------------
def render_affinity():
    print("Building 08_affinity ...")
    fig = plt.figure(figsize=(18, 12), facecolor="white")
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.set_axis_off()

    draw_title(
        fig,
        "Affinity diagram - Themes from 47 open-ended student responses",
        "KJ-method clustering of Q22 free-text feedback.  "
        "Rule size proportional to theme frequency.",
        x_in=0.55,
    )

    themes = [
        ("A. Schedule reliability", TERRACOTTA, 14, [
            "Fixed schedule like a shuttle bus would help.",
            "An app would save so much waiting time at Main Gate.",
            "Book in advance for post-class pickup - we all leave together.",
        ]),
        ("B. Payment and fare transparency", SAGE, 12, [
            "Per-seat fare makes more sense than paying full for detours.",
            "Drivers should carry change; I never have exact money.",
            "Install a visible fare chart - it is different every ride.",
        ]),
        ("C. Availability gaps", MAROON, 9, [
            "Late-night availability is the biggest issue for library-goers.",
            "Reduce the 4-seat minimum during off-peak - even 2 passengers is fine.",
        ]),
        ("D. Safety and identity", INK, 8, [
            "Make a dedicated women's E-rick during late hours.",
            "Show driver name and photo for safety.",
        ]),
        ("E. Zone aggregation", TERRACOTTA2, 10, [
            "GPS tracking so I know exactly when the e-rick will reach.",
            "Separate E-ricks for hostels vs academic area zones.",
            "Allow group-booking with friends for the same E-rick.",
        ]),
        ("F. Driver experience", MUTED, 4, [
            "Drivers are rude when the ride is for a short distance.",
            "Drivers skip short-distance requests during peak hours.",
        ]),
    ]

    # Grid layout: 2 rows x 3 cols
    # Panel region: x in [0.5, 17.5], y in [0.6, 10.4]
    grid_x0, grid_x1 = 0.5, 17.5
    grid_y0, grid_y1 = 0.6, 10.4
    h_gap = 0.4
    v_gap = 0.5
    ncols, nrows = 3, 2
    panel_w = (grid_x1 - grid_x0 - (ncols - 1) * h_gap) / ncols
    panel_h = (grid_y1 - grid_y0 - (nrows - 1) * v_gap) / nrows
    header_strip_h = 0.70

    for idx, (title, color, count, quotes) in enumerate(themes):
        col = idx % ncols
        row = idx // ncols
        x0 = grid_x0 + col * (panel_w + h_gap)
        # First row at TOP of grid
        y0 = grid_y1 - (row + 1) * panel_h - row * v_gap

        # Panel body (cream) with thin ink border
        body = FancyBboxPatch(
            (x0, y0), panel_w, panel_h,
            boxstyle="round,pad=0.02,rounding_size=0.16",
            facecolor=PANEL, edgecolor=INK, linewidth=1.0, zorder=2,
        )
        ax.add_patch(body)

        # Header strip (colored) overlaid on top portion
        header = FancyBboxPatch(
            (x0, y0 + panel_h - header_strip_h),
            panel_w, header_strip_h,
            boxstyle="round,pad=0.02,rounding_size=0.16",
            facecolor=color, edgecolor="none", zorder=3,
        )
        ax.add_patch(header)
        # square off the bottom of the header strip to sit flush with body
        ax.add_patch(Rectangle(
            (x0, y0 + panel_h - header_strip_h),
            panel_w, 0.18,
            facecolor=color, edgecolor="none", zorder=3,
        ))

        ax.text(x0 + 0.30, y0 + panel_h - header_strip_h / 2,
                title,
                ha="left", va="center",
                fontsize=18, fontweight="bold", family=BODY_FONT,
                color="white", zorder=4)

        # Quotes
        quote_area_top = y0 + panel_h - header_strip_h - 0.35
        line_gap = 0.15
        cur_y = quote_area_top
        # Character width tuned so text fits within panel_w (~5.4 inches)
        wrap_w = 48
        for q in quotes:
            wrapped = _wrap_text(q, wrap_w)
            n_lines = wrapped.count("\n") + 1
            ax.text(x0 + 0.35, cur_y,
                    "- " + wrapped,
                    ha="left", va="top",
                    fontsize=11, style="italic",
                    family=BODY_FONT, color=INK,
                    linespacing=1.35, zorder=4)
            cur_y -= 0.30 * n_lines + line_gap

        # Footer count
        ax.text(x0 + panel_w - 0.3, y0 + 0.22,
                f"Theme count: {count} responses",
                ha="right", va="center",
                fontsize=10, family=BODY_FONT, color=SOFT_MUTED, zorder=4)

    draw_footer(fig, "Affinity Diagram", "3", "New 7 QC Tools")
    return save_png(fig, "08_affinity")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Building process/operational diagrams ===\n")
    sizes = {}
    sizes["05_flowchart"] = render_flowchart()
    sizes["06_fmea"]      = render_fmea()
    sizes["07_pdca"]      = render_pdca()
    sizes["08_affinity"]  = render_affinity()
    print("\n=== File sizes (bytes) ===")
    for k, v in sizes.items():
        print(f"  {k}: {v/1024:.1f} KB")
