"""
build_all_diagrams.py
TQM Project — Team D
Generates 8 analysis diagrams (Pareto is pre-built by Team C-2).
Run with: /home/pratham/pratham/QM_project/.venv/bin/python build_all_diagrams.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd
import os
import textwrap
import csv
import math

# ── Palette ──────────────────────────────────────────────────────────────────
INK       = "#1B1A17"
TERRACOTA = "#E85D2F"
SAGE      = "#7C8F7C"
MAROON    = "#8A1A2B"
OFFWHITE  = "#F6F2EA"
MUTED     = "#A39A87"
LIGHTBG   = "#EDE8DE"

BASE = "/home/pratham/pratham/QM_project/deliverables/analysis"

def footer(ax, tool_name, chapter_ref):
    ax.annotate(
        f"TQM Tool: {tool_name} — Ref. Ch.{chapter_ref}",
        xy=(0.5, -0.01), xycoords="axes fraction",
        ha="center", va="top", fontsize=9, color=MUTED,
        annotation_clip=False
    )

def save(fig, folder, filename="diagram.png"):
    path = os.path.join(BASE, folder, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight",
                facecolor=OFFWHITE)
    print(f"  Saved: {path}")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════
# 01 — ISHIKAWA (Fishbone)
# ═══════════════════════════════════════════════════════════════════════════
def build_ishikawa():
    print("Building 01_ishikawa …")
    fig, ax = plt.subplots(figsize=(16, 10), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(8, 9.6, "Ishikawa (Fishbone) Diagram",
            ha="center", va="top", fontsize=16, fontweight="bold", color=INK)
    ax.text(8, 9.15, "Effect: E-Rickshaw Service Inefficiency on Campus",
            ha="center", va="top", fontsize=12, color=MAROON, fontweight="bold")

    # Head box (effect)
    head_x, head_y = 15.2, 5.0
    ax.annotate("",
                xy=(head_x, head_y), xytext=(13.8, head_y),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=MAROON))
    effect_box = FancyBboxPatch((13.82, 4.2), 1.5, 1.6,
                                boxstyle="round,pad=0.1",
                                linewidth=2, edgecolor=MAROON,
                                facecolor="#F9D9D9")
    ax.add_patch(effect_box)
    ax.text(14.57, 5.0, "Service\nInefficiency",
            ha="center", va="center", fontsize=8.5, fontweight="bold",
            color=MAROON)

    # Main spine
    ax.annotate("",
                xy=(13.8, 5.0), xytext=(1.5, 5.0),
                arrowprops=dict(arrowstyle="-", lw=2.5, color=INK))

    # Ribs: (x of rib base on spine, side, label, subcauses)
    ribs = [
        (3.2,  "top", "Man", [
            "Untrained drivers",
            "No shift scheduling",
            "Rude behaviour reports",
            "Driver fatigue (exam weeks)"
        ]),
        (6.2,  "top", "Machine", [
            "No GPS tracking",
            "Limited battery range",
            "Aging vehicle fleet",
            "No capacity sensor"
        ]),
        (9.8,  "top", "Method", [
            "Rigid 4-passenger fill rule",
            "No zone-based routing",
            "Cash-only payment",
            "No destination aggregation"
        ]),
        (3.2,  "bot", "Material", [
            "No signage at pickup points",
            "No printed route maps",
            "No fare chart displayed",
            "No queue management"
        ]),
        (6.8,  "bot", "Measurement", [
            "No wait-time KPI tracked",
            "No passenger count audit",
            "No fare reconciliation",
            "No satisfaction tracking"
        ]),
        (10.5, "bot", "Environment", [
            "Scattered campus layout",
            "Weather variability",
            "Peak-hour clustering",
            "Night-time demand gaps"
        ]),
    ]

    rib_colors_top = [SAGE, "#5A7FA5", TERRACOTA]
    rib_colors_bot = ["#8B6F47", "#6A5ACD", "#4A7C59"]

    for i, (xb, side, label, subs) in enumerate(ribs):
        is_top = (side == "top")
        col_set = rib_colors_top if is_top else rib_colors_bot
        cidx = i % 3
        rib_color = col_set[cidx]

        rib_tip_y = 7.6 if is_top else 2.4
        sign = 1 if is_top else -1

        # Diagonal rib
        ax.annotate("",
                    xy=(xb + 0.6, 5.0), xytext=(xb - 0.4, rib_tip_y),
                    arrowprops=dict(arrowstyle="-", lw=2.0, color=rib_color))

        # Rib label box
        lbl_y = 7.85 if is_top else 2.1
        ax.text(xb - 0.4, lbl_y, label,
                ha="center", va="center",
                fontsize=11, fontweight="bold", color="white",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=rib_color,
                          edgecolor="none"))

        # Sub-causes — branch off rib as small perpendicular lines
        for j, sub in enumerate(subs):
            t = 0.2 + j * 0.22          # param along rib 0→1
            rx = (xb - 0.4) + t * ((xb + 0.6) - (xb - 0.4))
            ry = rib_tip_y + t * (5.0 - rib_tip_y)

            # small horizontal branch
            branch_x = rx - 0.9 * (1 - t)
            branch_y = ry + sign * 0.0  # same y
            ax.plot([rx, branch_x], [ry, ry], lw=1.2, color=rib_color, alpha=0.8)

            ha = "right"
            ax.text(branch_x - 0.05, ry, sub,
                    ha=ha, va="center", fontsize=7.5, color=INK,
                    bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                              edgecolor=rib_color, alpha=0.85, linewidth=0.6))

    footer(ax, "Ishikawa (Fishbone) Diagram", "2 Basic 7 QC Tools")
    save(fig, "01_ishikawa")


# ═══════════════════════════════════════════════════════════════════════════
# 02 — 5 WHYS
# ═══════════════════════════════════════════════════════════════════════════
def build_five_whys():
    print("Building 02_five_whys …")
    fig, ax = plt.subplots(figsize=(10, 14), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis("off")

    ax.text(5, 13.6, "5 Whys Analysis",
            ha="center", va="top", fontsize=16, fontweight="bold", color=INK)

    entries = [
        ("Problem Statement",
         "Why do students waste time waiting for E-ricks?",
         "#E8F4F8", "#2980B9"),
        ("Why 1",
         "Drivers wait until 4 passengers are filled before departing.",
         "#EDF7ED", SAGE),
        ("Why 2",
         "Driver earning is tied to seat-fills per trip, not per ride completed.",
         "#EDF7ED", SAGE),
        ("Why 3",
         "No zone-aggregation aligns student demand spatially in advance.",
         "#EDF7ED", SAGE),
        ("Why 4",
         "Bookings are not visible to drivers ahead of departure time.",
         "#EDF7ED", SAGE),
        ("Why 5",
         "There is no digital booking system linking students to nearby E-ricks.",
         "#EDF7ED", SAGE),
        ("Root Cause",
         "Absence of an app-based booking and aggregation layer.",
         "#F9E8E8", MAROON),
    ]

    box_h = 1.3
    box_w = 8.0
    box_x = 1.0
    gap   = 0.45
    start_y = 13.0

    positions = []
    for k, (tag, text, face, border) in enumerate(entries):
        y_top = start_y - k * (box_h + gap)
        positions.append(y_top)

        rect = FancyBboxPatch((box_x, y_top - box_h), box_w, box_h,
                               boxstyle="round,pad=0.1",
                               linewidth=2.0, edgecolor=border,
                               facecolor=face)
        ax.add_patch(rect)

        ax.text(box_x + 0.35, y_top - 0.28, tag,
                ha="left", va="top", fontsize=9, fontweight="bold",
                color=border)
        wrapped = textwrap.fill(text, width=62)
        ax.text(box_x + 0.35, y_top - 0.55, wrapped,
                ha="left", va="top", fontsize=10, color=INK,
                linespacing=1.4)

        # Arrow down to next box
        if k < len(entries) - 1:
            arrow_y_start = y_top - box_h - 0.02
            arrow_y_end   = y_top - box_h - gap + 0.02
            ax.annotate("",
                        xy=(5.0, arrow_y_end),
                        xytext=(5.0, arrow_y_start),
                        arrowprops=dict(arrowstyle="-|>",
                                        lw=2.0, color=INK,
                                        mutation_scale=18))

    footer(ax, "5 Whys Root Cause Analysis", "2 Basic 7 QC Tools")
    save(fig, "02_five_whys")


# ═══════════════════════════════════════════════════════════════════════════
# 04 — SIPOC
# ═══════════════════════════════════════════════════════════════════════════
def build_sipoc():
    print("Building 04_sipoc …")
    fig, ax = plt.subplots(figsize=(18, 10), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(9, 9.7, "SIPOC — Current E-Rick Ride Process",
            ha="center", va="top", fontsize=16, fontweight="bold", color=INK)

    headers = ["Suppliers (S)", "Inputs (I)", "Process (P)", "Outputs (O)", "Customers (C)"]
    header_colors = ["#2C5F8A", "#3A7A4F", TERRACOTA, "#7A4F3A", "#5A3A7A"]

    col_data = [
        # Suppliers
        [
            "E-rickshaw drivers",
            "Campus administration\n(route policy)",
            "Electricity provider\n(charging infrastructure)",
            "Cash currency\n(fare payment medium)"
        ],
        # Inputs
        [
            "Driver availability\n& shift coverage",
            "Battery charge level\nper trip",
            "Fare rate schedule",
            "Student ride demand\n(uncoordinated)",
            "Physical ride capacity\n(4 seats)"
        ],
        # Process steps
        [
            "1. Student waits at\n   pickup point",
            "2. Board when 4\n   passengers assembled",
            "3. Driver chooses route\n   by majority preference",
            "4. Drop-off students\n   in sequence",
            "5. Pay cash at\n   each drop-off",
            "6. Driver returns\n   empty to home zone"
        ],
        # Outputs
        [
            "Passenger transport\n(primary service)",
            "Revenue for driver\n(per filled trip)",
            "Time-cost to student\n(wait + detour)",
            "Reconciled cash\n(partial, error-prone)"
        ],
        # Customers
        [
            "Students (primary\nservice recipients)",
            "Drivers (income\nbeneficiaries)",
            "Campus admin\n(indirect: traffic\n& parking relief)"
        ]
    ]

    col_w = 18 / 5
    header_h = 1.0
    body_top = 8.6
    body_h = 8.0

    for ci, (hdr, col, hcol) in enumerate(zip(headers, col_data, header_colors)):
        x0 = ci * col_w
        # Header
        hrect = FancyBboxPatch((x0 + 0.06, 9.0 - 0.5), col_w - 0.12, 0.7,
                               boxstyle="round,pad=0.05",
                               facecolor=hcol, edgecolor="none")
        ax.add_patch(hrect)
        ax.text(x0 + col_w / 2, 8.68, hdr,
                ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")

        # Body background
        brect = FancyBboxPatch((x0 + 0.06, 0.4), col_w - 0.12, body_h - 0.2,
                               boxstyle="round,pad=0.05",
                               facecolor="white", edgecolor=MUTED, linewidth=0.8)
        ax.add_patch(brect)

        # Row items
        row_h = (body_h - 0.4) / max(len(col), 1)
        for ri, item in enumerate(col):
            iy = body_h + 0.4 - (ri + 0.5) * row_h - 0.1
            # Bullet line
            ax.text(x0 + 0.3, iy + 0.05, "•", ha="left", va="center",
                    fontsize=11, color=hcol)
            ax.text(x0 + 0.55, iy, item,
                    ha="left", va="center", fontsize=8.8, color=INK,
                    linespacing=1.3)
            # Divider
            if ri < len(col) - 1:
                dy = body_h + 0.4 - (ri + 1) * row_h - 0.1
                ax.plot([x0 + 0.15, x0 + col_w - 0.15], [dy, dy],
                        lw=0.5, color=MUTED, alpha=0.5)

        # Column divider
        if ci < 4:
            ax.plot([x0 + col_w, x0 + col_w], [0.35, 9.1],
                    lw=1.2, color=MUTED, alpha=0.6)

    # Outer border
    outer = FancyBboxPatch((0.03, 0.3), 17.94, 8.85,
                           boxstyle="round,pad=0.05",
                           facecolor="none", edgecolor=INK, linewidth=1.5)
    ax.add_patch(outer)

    footer(ax, "SIPOC Diagram", "2 Process Scoping")
    save(fig, "04_sipoc")


# ═══════════════════════════════════════════════════════════════════════════
# 05 — FLOWCHART Current vs Future
# ═══════════════════════════════════════════════════════════════════════════
def build_flowchart():
    print("Building 05_flowchart_current_vs_future …")
    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(18, 14),
                                      facecolor=OFFWHITE)
    for ax in [ax_l, ax_r]:
        ax.set_facecolor(OFFWHITE)
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 14)
        ax.axis("off")

    fig.suptitle("Process Flowchart: Current State vs Future State (App)",
                 fontsize=16, fontweight="bold", color=INK, y=0.99)

    def draw_box(ax, x, y, w, h, text, shape="rect",
                 fc="white", ec=INK, fontsize=9):
        """Draw a flowchart box. shape: rect | diamond | oval"""
        if shape == "oval":
            ellipse = mpatches.Ellipse((x + w/2, y + h/2), w, h,
                                       facecolor=fc, edgecolor=ec, linewidth=1.5)
            ax.add_patch(ellipse)
        elif shape == "diamond":
            cx, cy = x + w/2, y + h/2
            diamond = plt.Polygon(
                [[cx, cy + h/2], [cx + w/2, cy],
                 [cx, cy - h/2], [cx - w/2, cy]],
                closed=True, facecolor=fc, edgecolor=ec, linewidth=1.5
            )
            ax.add_patch(diamond)
        else:
            rect = FancyBboxPatch((x, y), w, h,
                                  boxstyle="round,pad=0.1",
                                  facecolor=fc, edgecolor=ec, linewidth=1.5)
            ax.add_patch(rect)
        wrapped = textwrap.fill(text, width=22)
        ax.text(x + w/2, y + h/2, wrapped,
                ha="center", va="center", fontsize=fontsize,
                color=INK, linespacing=1.3)

    def arrow(ax, x1, y1, x2, y2, label="", color=INK):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", lw=1.5, color=color,
                                    mutation_scale=14))
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx + 0.12, my, label, fontsize=7.5, color=TERRACOTA)

    # ── Current State (Left) ───────────────────────────────────────────────
    ax_l.text(4, 13.7, "CURRENT STATE", ha="center", va="top",
              fontsize=13, fontweight="bold", color=MAROON)

    bw, bh = 5.2, 0.7
    bx = 1.4
    steps_c = [
        (13.0, "Student arrives at\npickup point", "oval", "#E8F4F8", "#2980B9"),
        (11.9, "Waits for 4 passengers\nto assemble", "rect", "#FFF5E6", TERRACOTA),
        (10.8, "Wait > 15 min?", "diamond", "#FDECEA", MAROON),
        (9.7,  "Checks if route\naligns with destination", "rect", "#FFF5E6", TERRACOTA),
        (8.6,  "Route acceptable?", "diamond", "#FDECEA", MAROON),
        (7.5,  "Boards E-rickshaw", "rect", "#EDF7ED", SAGE),
        (6.4,  "Driver serves farthest\ndrop-off first", "rect", "#FFF5E6", TERRACOTA),
        (5.3,  "Drops off each\nstudent in sequence", "rect", "#FFF5E6", TERRACOTA),
        (4.2,  "Student pays cash\n(error-prone)", "rect", "#FDECEA", MAROON),
        (3.1,  "Driver returns\nempty to start zone", "rect", "#FFF5E6", TERRACOTA),
        (2.0,  "END", "oval", "#E8F4F8", "#2980B9"),
    ]

    for (yt, txt, shp, fc, ec) in steps_c:
        draw_box(ax_l, bx, yt - bh/2, bw, bh, txt, shp, fc, ec, fontsize=8.5)

    # Arrows
    for k in range(len(steps_c) - 1):
        y1 = steps_c[k][0] - bh/2
        y2 = steps_c[k+1][0] + bh/2
        arrow(ax_l, bx + bw/2, y1, bx + bw/2, y2)

    # Delay branch from diamond 1 (>15 min)
    ax_l.annotate("", xy=(bx - 0.6, steps_c[1][0]),
                  xytext=(bx, steps_c[2][0]),
                  arrowprops=dict(arrowstyle="-|>", lw=1.2, color=TERRACOTA,
                                  connectionstyle="arc3,rad=-0.3"))
    ax_l.text(bx - 1.3, steps_c[2][0] - 0.1, "Yes\n(abandon)", fontsize=7,
              color=TERRACOTA, ha="center")
    ax_l.text(bx + bw + 0.1, steps_c[2][0], "No", fontsize=7.5, color=SAGE)

    # Route branch
    ax_l.text(bx - 1.1, steps_c[4][0] - 0.1, "No\n(boards anyway\nor leaves)",
              fontsize=7, color=TERRACOTA, ha="center")
    ax_l.text(bx + bw + 0.1, steps_c[4][0], "Yes", fontsize=7.5, color=SAGE)

    # ── Future State (Right) ───────────────────────────────────────────────
    ax_r.text(4, 13.7, "FUTURE STATE (APP)", ha="center", va="top",
              fontsize=13, fontweight="bold", color="#2A6F3F")

    steps_f = [
        (13.0, "Student opens app", "oval", "#E8F4F8", "#2980B9"),
        (11.9, "Sees E-ricks within 100m\nwith matching destinations", "rect", "#EDF7ED", SAGE),
        (10.8, "Any suitable E-rick\nfound?", "diamond", "#EDF7ED", SAGE),
        (9.7,  "Taps to book +\nselects drop-off point", "rect", "#EDF7ED", SAGE),
        (8.6,  "60-sec countdown to\nreach E-rick", "rect", "#FFF5E6", TERRACOTA),
        (7.5,  "Student boards;\nDriver taps 'Reached'", "rect", "#EDF7ED", SAGE),
        (6.4,  "Ride starts;\nroute shown in app", "rect", "#EDF7ED", SAGE),
        (5.3,  "Student dropped\nat selected point", "rect", "#EDF7ED", SAGE),
        (4.2,  "Auto fare deducted\nfrom wallet", "rect", "#EDF7ED", SAGE),
        (3.1,  "Driver sees nearby\nbookings for return trip", "rect", "#EDF7ED", SAGE),
        (2.0,  "END", "oval", "#E8F4F8", "#2980B9"),
    ]

    for (yt, txt, shp, fc, ec) in steps_f:
        draw_box(ax_r, bx, yt - bh/2, bw, bh, txt, shp, fc, ec, fontsize=8.5)

    for k in range(len(steps_f) - 1):
        y1 = steps_f[k][0] - bh/2
        y2 = steps_f[k+1][0] + bh/2
        arrow(ax_r, bx + bw/2, y1, bx + bw/2, y2)

    # No branch
    ax_r.text(bx - 1.2, steps_f[2][0], "No:\nAlert + suggest\nschedule", fontsize=7,
              color=TERRACOTA, ha="center")
    ax_r.text(bx + bw + 0.1, steps_f[2][0], "Yes", fontsize=7.5, color=SAGE)

    # Divider
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.04, 0.97],
                              transform=fig.transFigure,
                              color=MUTED, lw=1.5, linestyle="--"))

    # Footers per axis
    ax_l.annotate("TQM Tool: Process Flowchart — Ref. Ch.2 Basic 7 QC Tools",
                  xy=(0.5, -0.01), xycoords="axes fraction",
                  ha="center", va="top", fontsize=9, color=MUTED,
                  annotation_clip=False)
    ax_r.annotate("TQM Tool: Process Flowchart — Ref. Ch.2 Basic 7 QC Tools",
                  xy=(0.5, -0.01), xycoords="axes fraction",
                  ha="center", va="top", fontsize=9, color=MUTED,
                  annotation_clip=False)
    save(fig, "05_flowchart_current_vs_future")


# ═══════════════════════════════════════════════════════════════════════════
# 06 — FMEA
# ═══════════════════════════════════════════════════════════════════════════
FMEA_DATA = [
    # (id, failure_mode, effect, S, cause, O, current_control, D, RPN, mitigation)
    (1,  "Seat-stealing",
     "Booked student displaced", 6, "No physical reservation enforcement", 3,
     "None", 5, 90,
     "Driver 'Reached' press locks seat to physically-present student"),
    (2,  "Driver mistakenly\ntaps 'Reached'",
     "Ride billed without boarding", 4, "UI button too accessible", 4,
     "None", 3, 48,
     "5-second undo toast after tap"),
    (3,  "Wallet insufficient\nat ride-end",
     "Unpaid fare; driver dispute", 5, "No pre-ride balance check", 5,
     "None", 4, 100,
     "Rs.50 soft debt cap; block new bookings until cleared"),
    (4,  "Race: two bookings\nsame seat",
     "Double booking conflict", 5, "Concurrent API writes", 2,
     "None", 2, 20,
     "Server-side first-write-wins; loser gets alternate E-rick"),
    (5,  "Mid-ride drop-off\nchange",
     "Route disruption; fare error", 4, "No lock after boarding", 4,
     "None", 5, 80,
     "Lock destination after 'Reached'; visible banner"),
    (6,  "Driver goes offline\n/ GPS lost",
     "Ride stuck; students stranded", 7, "Network gaps on campus", 3,
     "None", 6, 126,
     "30-sec heartbeat; offline banner; fare finalised on reconnect"),
    (7,  "Capacity full +\noffline passenger add",
     "Overcrowding; safety risk", 5, "No hard capacity check", 5,
     "Verbal rule", 2, 50,
     "Reducer-level hard block with clear error message"),
    (8,  "Cancellation-fee\ndispute",
     "User frustration; churn", 4, "No in-app dispute channel", 5,
     "Verbal complaint", 6, 120,
     "One-tap dispute; 24-hour admin review SLA"),
    (9,  "Student repeated\nno-shows",
     "Driver revenue loss; trust erosion", 5, "No accountability system", 4,
     "None", 3, 60,
     "3-strikes 7-day rule; 1-hour cooldown; reputation meter"),
    (10, "Two E-ricks at\nsame location",
     "Student confusion; missed ride", 3, "No differentiation in UI", 6,
     "None", 4, 72,
     "Stacked card list by passenger count + drop-off alignment"),
]

def build_fmea():
    print("Building 06_fmea …")

    # Write CSV
    csv_path = os.path.join(BASE, "06_fmea", "fmea.csv")
    headers_csv = ["#", "Failure Mode", "Effect", "Severity (S)",
                   "Cause", "Occurrence (O)", "Current Control",
                   "Detection (D)", "RPN", "Mitigation"]
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(headers_csv)
        for row in FMEA_DATA:
            w.writerow([
                row[0],
                row[1].replace("\n", " "),
                row[2],
                row[3], row[4], row[5], row[6], row[7], row[8],
                row[9].replace("\n", " ")
            ])
    print(f"  Saved CSV: {csv_path}")

    # Sort by RPN descending for display
    sorted_data = sorted(FMEA_DATA, key=lambda x: x[8], reverse=True)

    fig, ax = plt.subplots(figsize=(22, 12), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.axis("off")

    ax.text(0.5, 0.98, "FMEA — Failure Mode and Effects Analysis",
            ha="center", va="top", transform=ax.transAxes,
            fontsize=16, fontweight="bold", color=INK)
    ax.text(0.5, 0.945, "E-Rickshaw App — Edge Case Risk Assessment (sorted by RPN descending)",
            ha="center", va="top", transform=ax.transAxes,
            fontsize=10, color=MUTED)

    col_labels = ["#", "Failure Mode", "Effect", "S", "Cause", "O",
                  "Current Control", "D", "RPN", "Mitigation"]
    col_widths = [0.025, 0.11, 0.10, 0.03, 0.12, 0.03, 0.10, 0.03, 0.04, 0.16]
    col_x = []
    cx = 0.01
    for w in col_widths:
        col_x.append(cx)
        cx += w

    table_top = 0.90
    row_h = 0.073
    header_h = 0.05

    # Header
    for ci, (lbl, cx2, cw) in enumerate(zip(col_labels, col_x, col_widths)):
        hrect = plt.Rectangle((cx2, table_top - header_h),
                               cw - 0.004, header_h,
                               transform=ax.transAxes,
                               facecolor=INK, edgecolor="none",
                               clip_on=False)
        ax.add_patch(hrect)
        ax.text(cx2 + cw/2 - 0.002, table_top - header_h/2, lbl,
                ha="center", va="center", transform=ax.transAxes,
                fontsize=8.5, fontweight="bold", color="white")

    top3_rpn = sorted([r[8] for r in FMEA_DATA], reverse=True)[:3]

    for ri, row in enumerate(sorted_data):
        y_top = table_top - header_h - ri * row_h
        is_top3 = row[8] in top3_rpn

        row_fc = "#FFE8E8" if is_top3 else ("white" if ri % 2 == 0 else "#F5F1EB")

        row_vals = [
            str(row[0]),
            row[1],
            row[2],
            str(row[3]),
            row[4],
            str(row[5]),
            row[6],
            str(row[7]),
            str(row[8]),
            row[9]
        ]

        for ci, (val, cx2, cw) in enumerate(zip(row_vals, col_x, col_widths)):
            rrect = plt.Rectangle((cx2, y_top - row_h),
                                   cw - 0.004, row_h,
                                   transform=ax.transAxes,
                                   facecolor=row_fc,
                                   edgecolor=MUTED, linewidth=0.5,
                                   clip_on=False)
            ax.add_patch(rrect)

            cell_color = INK
            fw = "normal"
            if ci == 8 and is_top3:
                cell_color = MAROON
                fw = "bold"

            wrapped_val = textwrap.fill(val.replace("\n", " "), width=max(12, int(cw * 100)))
            ax.text(cx2 + cw/2 - 0.002, y_top - row_h/2, wrapped_val,
                    ha="center", va="center", transform=ax.transAxes,
                    fontsize=7.2, color=cell_color, fontweight=fw,
                    linespacing=1.2)

    # Top-3 legend
    leg_y = table_top - header_h - len(sorted_data) * row_h - 0.025
    lrect = plt.Rectangle((0.01, leg_y - 0.025), 0.02, 0.02,
                           transform=ax.transAxes,
                           facecolor="#FFE8E8", edgecolor=MAROON, linewidth=1)
    ax.add_patch(lrect)
    ax.text(0.035, leg_y - 0.015, "Highlighted rows = Top 3 RPN (highest risk)",
            transform=ax.transAxes, fontsize=8.5, va="center", color=MAROON)

    ax.annotate("TQM Tool: FMEA — Ref. Ch.10 Reliability & Risk",
                xy=(0.5, 0.01), xycoords="axes fraction",
                ha="center", va="bottom", fontsize=9, color=MUTED,
                annotation_clip=False)
    save(fig, "06_fmea")


# ═══════════════════════════════════════════════════════════════════════════
# 07 — PDCA Cycle
# ═══════════════════════════════════════════════════════════════════════════
def build_pdca():
    print("Building 07_pdca …")
    fig, ax = plt.subplots(figsize=(12, 10), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.text(0, 1.12, "PDCA Cycle — E-Rickshaw App Improvement",
            ha="center", va="center", fontsize=16, fontweight="bold", color=INK)

    quadrants = [
        ("PLAN",  90,  "#5A7FA5", "#EAF1F8",
         ["Identify pain points\n(Ishikawa, Pareto)",
          "Define KPIs: avg wait,\nleakage %, empty-return %",
          "Design app MVP",
          "Select pilot zone"]),
        ("DO",    0,   "#3A7A4F", "#EDF7ED",
         ["Develop app MVP",
          "Onboard 5 E-ricks\nand 50 students",
          "Run 2-week pilot\nin one zone"]),
        ("CHECK", 270, TERRACOTA, "#FFF5E6",
         ["Measure KPIs vs baseline",
          "Survey user satisfaction",
          "Compare wait times,\nleakage, empty trips",
          "Review driver feedback"]),
        ("ACT",   180, MAROON, "#F9E8E8",
         ["Standardise winning features",
          "Iterate on surfaced issues",
          "Expand to full campus",
          "Update driver SOPs"]),
    ]

    R_outer = 0.82
    R_inner = 0.28
    R_label = 0.60
    R_text  = 0.78  # used for offset but text drawn in wedge

    for label, start_angle, color, face_color, bullets in quadrants:
        end_angle = start_angle + 90
        theta_mid = math.radians((start_angle + end_angle) / 2)

        wedge = mpatches.Wedge(
            (0, 0), R_outer, start_angle, end_angle,
            width=R_outer - R_inner,
            facecolor=face_color, edgecolor=color, linewidth=2.5
        )
        ax.add_patch(wedge)

        # Label position (midway in wedge, outer part)
        lx = R_label * math.cos(theta_mid)
        ly = R_label * math.sin(theta_mid)

        ax.text(lx, ly, label,
                ha="center", va="center",
                fontsize=15, fontweight="bold", color=color)

        # Bullet text
        tx = 0.42 * math.cos(theta_mid)
        ty = 0.42 * math.sin(theta_mid)

        bullet_text = "\n".join([f"• {b}" for b in bullets])
        ax.text(tx, ty, bullet_text,
                ha="center", va="center",
                fontsize=7.5, color=INK, linespacing=1.5,
                multialignment="left")

    # Inner circle
    inner_circle = plt.Circle((0, 0), R_inner, color=INK, zorder=5)
    ax.add_patch(inner_circle)
    ax.text(0, 0, "PDCA\nCycle", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=6)

    # Circular arrows (between quadrant labels)
    for angle in [45, 135, 225, 315]:
        theta = math.radians(angle)
        arrow_r = R_outer + 0.07
        ax.annotate("",
                    xy=(arrow_r * math.cos(math.radians(angle - 15)),
                        arrow_r * math.sin(math.radians(angle - 15))),
                    xytext=(arrow_r * math.cos(math.radians(angle + 15)),
                            arrow_r * math.sin(math.radians(angle + 15))),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle=f"arc3,rad=0.5",
                                    color=INK, lw=1.5,
                                    mutation_scale=14))

    ax.annotate("TQM Tool: PDCA Cycle — Ref. Ch.1 TQM Fundamentals",
                xy=(0.5, 0.0), xycoords="axes fraction",
                ha="center", va="bottom", fontsize=9, color=MUTED,
                annotation_clip=False)
    save(fig, "07_pdca")


# ═══════════════════════════════════════════════════════════════════════════
# 08 — AFFINITY DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════
def build_affinity():
    print("Building 08_affinity …")

    themes = [
        ("A — Schedule Reliability", "#2C5F8A", "#EAF1F8", [
            "Fixed schedule like a shuttle bus\nwould help.",
            "An app would save so much waiting\ntime at Main Gate.",
            "Book in advance for post-class\npickup.",
        ]),
        ("B — Payment & Fare Transparency", "#3A7A4F", "#EDF7ED", [
            "Per-seat fare makes more sense\nthan paying full for detours.",
            "Drivers should carry change.",
            "Install a visible fare chart.",
        ]),
        ("C — Availability Gaps", TERRACOTA, "#FFF5E6", [
            "Late-night availability is the\nbiggest issue for library-goers.",
            "Reduce the 4-seat minimum\nduring off-peak hours.",
        ]),
        ("D — Safety & Identity", MAROON, "#F9E8E8", [
            "Make a dedicated women's E-rick\nduring late hours.",
            "Show driver name and photo\nfor safety.",
        ]),
        ("E — Zone Aggregation", "#5A3A7A", "#F0EAF8", [
            "GPS tracking so I know when\nthe e-rick will arrive.",
            "Separate E-ricks for hostels vs\nacademic zones.",
            "Allow group-booking with friends\nfor the same E-rick.",
        ]),
        ("F — Driver Experience", "#7A4F1A", "#F8F0E8", [
            "Drivers are rude when the ride\nis for a short distance.",
        ]),
    ]

    fig, ax = plt.subplots(figsize=(16, 12), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis("off")

    ax.text(8, 11.7, "Affinity Diagram — Student Feedback Themes",
            ha="center", va="top", fontsize=16, fontweight="bold", color=INK)
    ax.text(8, 11.2, "Clustered from Q22 open-text survey responses (N=150)",
            ha="center", va="top", fontsize=10, color=MUTED)

    # 2 rows x 3 cols
    cols, rows = 3, 2
    cell_w = 16 / cols
    cell_h = 9.8 / rows
    pad = 0.25

    for idx, (title, color, bg, items) in enumerate(themes):
        col = idx % cols
        row = idx // cols
        x0 = col * cell_w + pad
        y0 = 10.8 - (row + 1) * cell_h + pad
        w  = cell_w - 2 * pad
        h  = cell_h - 2 * pad

        # Card background
        card = FancyBboxPatch((x0, y0), w, h,
                              boxstyle="round,pad=0.15",
                              facecolor=bg, edgecolor=color, linewidth=2.0)
        ax.add_patch(card)

        # Theme header
        hdr_rect = FancyBboxPatch((x0, y0 + h - 0.52), w, 0.52,
                                  boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor="none")
        ax.add_patch(hdr_rect)
        ax.text(x0 + w/2, y0 + h - 0.26, title,
                ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")

        # Items
        item_y = y0 + h - 0.75
        for item in items:
            ax.text(x0 + 0.2, item_y, "\u2022 " + item,
                    ha="left", va="top", fontsize=8.5, color=INK,
                    linespacing=1.35)
            # Count lines
            n_lines = item.count("\n") + 1
            item_y -= 0.25 * n_lines + 0.2

    footer(ax, "Affinity Diagram", "3 New 7 QC Tools")
    save(fig, "08_affinity")


# ═══════════════════════════════════════════════════════════════════════════
# 09 — RELATIONS DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════
def build_relations():
    print("Building 09_relations …")
    fig, ax = plt.subplots(figsize=(14, 10), facecolor=OFFWHITE)
    ax.set_facecolor(OFFWHITE)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.text(0, 3.85, "Interrelationship (Relations) Diagram",
            ha="center", va="top", fontsize=16, fontweight="bold", color=INK)
    ax.text(0, 3.45, "Causal feedback loop — E-Rickshaw service system",
            ha="center", va="top", fontsize=10, color=MUTED)

    # Nodes arranged in a ring
    nodes = [
        ("Long wait\ntime",           0,     3.0,  MAROON,    "#F9E8E8"),
        ("Route\ndetours",            2.55,  1.8,  TERRACOTA, "#FFF0E0"),
        ("Cash\nleakage",             3.2,  -0.5,  TERRACOTA, "#FFF0E0"),
        ("Students\navoid E-ricks",   1.8,  -2.5,  MAROON,    "#F9E8E8"),
        ("Lower driver\nearnings",   -0.0,  -3.2,  "#5A3A7A",  "#F0EAF8"),
        ("Fewer active\nE-ricks",    -2.5,  -2.0,  "#2C5F8A",  "#EAF1F8"),
        ("Longer waits\n(feedback)",  -3.2,  0.5,  MAROON,    "#F9E8E8"),
        ("Poor service\nperception",  -1.5,  2.4,  "#7A4F1A",  "#F8F0E8"),
    ]

    node_pos = {name: (x, y) for name, x, y, c, fc in nodes}

    # Draw nodes
    for name, x, y, color, fc in nodes:
        box = FancyBboxPatch((x - 0.8, y - 0.45), 1.6, 0.9,
                             boxstyle="round,pad=0.1",
                             facecolor=fc, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, name, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color=color,
                linespacing=1.3)

    # Directed edges (from, to, label, is_reinforcing)
    edges = [
        # Main reinforcing loop (clockwise)
        ("Long wait\ntime",          "Students\navoid E-ricks",  "causes",    True),
        ("Students\navoid E-ricks",  "Lower driver\nearnings",   "reduces",   True),
        ("Lower driver\nearnings",   "Fewer active\nE-ricks",    "leads to",  True),
        ("Fewer active\nE-ricks",    "Longer waits\n(feedback)", "worsens",   True),
        ("Longer waits\n(feedback)", "Long wait\ntime",          "reinforces", True),
        # Secondary connections
        ("Long wait\ntime",          "Poor service\nperception",  "",          False),
        ("Route\ndetours",           "Students\navoid E-ricks",  "",          False),
        ("Cash\nleakage",            "Lower driver\nearnings",   "",          False),
        ("Route\ndetours",           "Long wait\ntime",          "",          False),
        ("Poor service\nperception", "Fewer active\nE-ricks",    "",          False),
        ("Cash\nleakage",            "Students\navoid E-ricks",  "",          False),
    ]

    for (src, dst, lbl, reinforcing) in edges:
        sx, sy = node_pos[src]
        dx, dy = node_pos[dst]
        color = MAROON if reinforcing else MUTED
        lw = 2.2 if reinforcing else 1.0
        style = "arc3,rad=0.25"
        ax.annotate("",
                    xy=(dx, dy),
                    xytext=(sx, sy),
                    arrowprops=dict(
                        arrowstyle="-|>",
                        connectionstyle=style,
                        color=color, lw=lw,
                        mutation_scale=14,
                    ))

    # Legend
    ax.plot([2.5, 3.0], [-3.2, -3.2], lw=2.2, color=MAROON)
    ax.annotate("", xy=(3.0, -3.2), xytext=(2.95, -3.2),
                arrowprops=dict(arrowstyle="-|>", color=MAROON, lw=2.2,
                                mutation_scale=12))
    ax.text(3.1, -3.2, "Reinforcing loop", fontsize=8.5, va="center", color=MAROON)
    ax.plot([2.5, 3.0], [-3.55, -3.55], lw=1.0, color=MUTED)
    ax.annotate("", xy=(3.0, -3.55), xytext=(2.95, -3.55),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.0,
                                mutation_scale=12))
    ax.text(3.1, -3.55, "Contributing cause", fontsize=8.5, va="center", color=MUTED)

    footer(ax, "Interrelationship (Relations) Diagram", "3 New 7 QC Tools")
    save(fig, "09_relations")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== Building TQM Analysis Diagrams ===\n")
    build_ishikawa()
    build_five_whys()
    build_sipoc()
    build_flowchart()
    build_fmea()
    build_pdca()
    build_affinity()
    build_relations()
    print("\n=== All diagrams built successfully ===")
