"""
build_conceptual_diagrams.py
TQM Project — Team D (conceptual diagrams sub-task)

Renders presentation-grade versions of:
  1. Ishikawa (Fishbone)           -> 01_ishikawa/diagram.png
  2. 5 Whys                        -> 02_five_whys/diagram.png
  3. SIPOC                         -> 04_sipoc/diagram.png
  4. Relations / Interrelationship -> 09_relations/diagram.png

Run with:
    /home/pratham/pratham/QM_project/.venv/bin/python build_conceptual_diagrams.py

Design contract (shared across all four figures):
 - Canvas >= 18 x 11 in (Ishikawa / Relations go bigger). DPI = 200.
 - White background, bbox_inches='tight', pad_inches=0.4.
 - DejaVu Sans body, DejaVu Serif titles.
 - Title 26pt bold (top-left via ax.text, NOT suptitle) + 16pt subtitle (muted).
 - Accent rule: 2in x 0.05in terracotta rectangle under the title.
 - Footer: "TQM Tool: <name> - Ref. Ch.<N> <module>" 10pt italic muted.
 - Axes turned off (we are drawing, not plotting).
"""

from __future__ import annotations

import os
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle

# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------
INK         = "#1B1A17"
TERRACOTTA  = "#E85D2F"
SAGE        = "#7C8F7C"
MAROON      = "#8A1A2B"
MUTED       = "#A39A87"
RULE        = "#D9D2C0"
PANEL_FILL  = "#FAF7EF"
ACCENT_FILL = "#FCEDE1"
WHITE       = "#FFFFFF"

BASE = "/home/pratham/pratham/QM_project/deliverables/analysis"

# Global rcParams so every figure is typographically consistent.
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
})


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------
def draw_title(ax, title: str, subtitle: str, x: float = 0.02, y_title: float = 0.965,
               y_rule: float = 0.935, y_sub: float = 0.905,
               title_size: int = 26, sub_size: int = 16,
               rule_w: float = 0.11):
    """Place a top-left serif title, accent rule, and muted subtitle.

    The accent rule sits BETWEEN the title and the subtitle so it never
    overlaps text. Coordinates are axes-fraction units.
    """
    ax.text(x, y_title, title,
            transform=ax.transAxes,
            ha="left", va="top",
            fontsize=title_size, fontweight="bold",
            fontfamily="DejaVu Serif",
            color=INK)
    # accent rule (inline here for deterministic vertical ordering)
    rule = Rectangle((x, y_rule - 0.004), rule_w, 0.006,
                     transform=ax.transAxes,
                     facecolor=TERRACOTTA, edgecolor="none",
                     clip_on=False, zorder=10)
    ax.add_patch(rule)
    ax.text(x, y_sub, subtitle,
            transform=ax.transAxes,
            ha="left", va="top",
            fontsize=sub_size, color="#6E6A60")


def accent_rule(ax, x: float = 0.02, y: float = 0.935, w: float = 0.11,
                h: float = 0.006, color: str = TERRACOTTA):
    """Back-compat shim. draw_title already emits the accent rule, so this
    helper is now a no-op and is kept only so older call sites remain valid.
    """
    return None


def footer(fig, text: str):
    fig.text(0.04, 0.015, text,
             style="italic", color=MUTED, size=10)


def save(fig, folder: str, filename: str = "diagram.png"):
    path = os.path.join(BASE, folder, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=200, bbox_inches="tight",
                pad_inches=0.4, facecolor="white")
    size_kb = os.path.getsize(path) / 1024.0
    plt.close(fig)
    print(f"  Saved: {path}  ({size_kb:.1f} KB)")
    return path, size_kb


# ---------------------------------------------------------------------------
# 1. ISHIKAWA (Fishbone)
# ---------------------------------------------------------------------------
def render_ishikawa() -> tuple[str, float]:
    """6M fishbone. Spine + 6 ribs + ~4 sub-cause twigs per rib.

    Data coords: 0..19 horizontal, 0..11 vertical (matches 19x11 canvas so
    1 data unit == 1 inch => trivial to reason about sizing).
    """
    fig = plt.figure(figsize=(19, 11), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    # Title block
    draw_title(
        ax,
        "Ishikawa (Fishbone) - Root causes of E-rick service inefficiency",
        "6M categorisation with sub-causes ranked by survey evidence",
        rule_w=0.105,  # ~2 in on a 19-in canvas
    )

    # --- Effect box (head of the fish) ------------------------------------
    head_w, head_h = 3.5, 1.3
    head_x = 19 - 0.4 - head_w     # right margin ~0.4 in
    head_y = 5.2 - head_h / 2      # vertically centred on spine (y=5.2)
    head = FancyBboxPatch((head_x, head_y), head_w, head_h,
                          boxstyle="round,pad=0.04,rounding_size=0.18",
                          linewidth=0, facecolor=TERRACOTTA,
                          zorder=4)
    ax.add_patch(head)
    ax.text(head_x + head_w / 2, head_y + head_h / 2,
            "E-Rickshaw service\ninefficiency on campus",
            ha="center", va="center",
            fontsize=14, fontweight="bold", color="white", zorder=5)

    # --- Spine ------------------------------------------------------------
    spine_y = 5.2
    spine_x0 = 1.2
    spine_x1 = head_x  # stops right at the head
    ax.annotate("",
                xy=(spine_x1 - 0.05, spine_y),
                xytext=(spine_x0, spine_y),
                arrowprops=dict(arrowstyle="-|>", lw=3.5,
                                color=TERRACOTTA,
                                mutation_scale=22),
                zorder=3)

    # --- Rib geometry ------------------------------------------------------
    # 3 upper ribs (Man, Method, Measurement), 3 lower (Machine, Material, Environment).
    # Each rib is a 45-deg diagonal line of length ~5 in. Upper ribs go up-right
    # (end point above spine), lower ribs go down-right.
    rib_len = 5.0
    dx = rib_len * math.cos(math.radians(45))  # ~3.54
    dy = rib_len * math.sin(math.radians(45))  # ~3.54

    # Spine-attach x-positions for the 3 upper / 3 lower ribs. Distribute
    # evenly between spine_x0+1.5 and spine_x1-0.6.
    upper_attach_x = [3.4, 7.5, 11.6]
    lower_attach_x = [4.6, 8.7, 12.8]

    # (name, rib_color, subcauses list)
    upper_ribs = [
        ("MAN", INK,    ["Untrained drivers", "No shift scheduling",
                          "Rude behaviour", "Exam-week fatigue"]),
        ("METHOD", "#3A4A3A",
                         ["Rigid 4-passenger rule", "No zone routing",
                          "Cash-only payment", "No destination aggregation"]),
        ("MEASUREMENT", "#5A1620",
                         ["No wait-time KPI", "No passenger audit",
                          "No fare reconciliation", "No satisfaction tracking"]),
    ]
    lower_ribs = [
        ("MACHINE", INK, ["No GPS", "Limited battery",
                          "Aging vehicles", "No capacity sensor"]),
        ("MATERIAL", "#3A4A3A",
                         ["No signage", "No route maps",
                          "No fare chart", "No queue system"]),
        ("ENVIRONMENT", "#5A1620",
                         ["Scattered layout", "Weather variability",
                          "Peak-hour clustering", "Night demand gaps"]),
    ]

    def draw_rib(ax, attach_x: float, attach_y: float, end_x: float,
                 end_y: float, label: str, rib_color: str,
                 subcauses: list[str], upper: bool):
        # Rib line
        ax.plot([attach_x, end_x], [attach_y, end_y],
                color=rib_color, linewidth=2.2, solid_capstyle="round",
                zorder=2)

        # Category box at the far end of the rib
        box_w, box_h = 2.0, 0.55
        bx = end_x - box_w / 2
        by = end_y - box_h / 2 + (0.1 if upper else -0.1)
        cat = FancyBboxPatch((bx, by), box_w, box_h,
                             boxstyle="round,pad=0.02,rounding_size=0.12",
                             linewidth=1.6, edgecolor=rib_color,
                             facecolor=PANEL_FILL, zorder=5)
        ax.add_patch(cat)
        ax.text(end_x, by + box_h / 2, label,
                ha="center", va="center",
                fontsize=13.5, fontweight="bold", color=rib_color, zorder=6)

        # Sub-cause twigs along the rib.
        # Place 4 twigs at fractions 0.25, 0.45, 0.65, 0.85 along the rib,
        # each twig horizontal, length 1.6. Text sits just to the left of the
        # twig's outer tip so nothing overlaps the box.
        twig_fracs = [0.22, 0.42, 0.62, 0.82]
        twig_len = 1.55
        for i, sc in enumerate(subcauses):
            f = twig_fracs[i]
            tx_attach = attach_x + (end_x - attach_x) * f
            ty_attach = attach_y + (end_y - attach_y) * f
            # Horizontal twig — extend LEFT (toward the head) so it stays
            # inside the fan defined by the rib.
            tx_tip = tx_attach - twig_len
            ty_tip = ty_attach
            ax.plot([tx_attach, tx_tip], [ty_attach, ty_tip],
                    color=INK, linewidth=1.0, alpha=0.75, zorder=2)
            # Label at the outer tip (left side of twig).
            ax.text(tx_tip - 0.05, ty_tip + (0.18 if upper else -0.18),
                    sc,
                    ha="right",
                    va="bottom" if upper else "top",
                    fontsize=11.5, color=INK, zorder=3)

    for attach_x, (label, color, subs) in zip(upper_attach_x, upper_ribs):
        end_x = attach_x + dx
        end_y = spine_y + dy
        draw_rib(ax, attach_x, spine_y, end_x, end_y, label, color, subs,
                 upper=True)

    for attach_x, (label, color, subs) in zip(lower_attach_x, lower_ribs):
        end_x = attach_x + dx
        end_y = spine_y - dy
        draw_rib(ax, attach_x, spine_y, end_x, end_y, label, color, subs,
                 upper=False)

    # --- Legend (bottom-left) ---------------------------------------------
    leg_x, leg_y = 0.5, 0.55
    leg_w, leg_h = 4.8, 1.15
    legend_bg = FancyBboxPatch((leg_x, leg_y), leg_w, leg_h,
                               boxstyle="round,pad=0.02,rounding_size=0.08",
                               linewidth=0.8, edgecolor=RULE,
                               facecolor=PANEL_FILL, zorder=1)
    ax.add_patch(legend_bg)
    ax.text(leg_x + 0.18, leg_y + leg_h - 0.20, "Rib colour key",
            ha="left", va="top", fontsize=11, fontweight="bold", color=INK)

    key_entries = [
        (INK,       "Man / Machine"),
        ("#3A4A3A", "Method / Material"),
        ("#5A1620", "Measurement / Environment"),
    ]
    for i, (c, lbl) in enumerate(key_entries):
        yy = leg_y + leg_h - 0.45 - i * 0.22
        ax.plot([leg_x + 0.22, leg_x + 0.72], [yy, yy],
                color=c, linewidth=2.2, solid_capstyle="round")
        ax.text(leg_x + 0.85, yy, lbl,
                ha="left", va="center", fontsize=10.5, color=INK)

    footer(fig, "TQM Tool: Ishikawa (Fishbone) - Ref. Ch.2 Basic 7 QC Tools")
    return save(fig, "01_ishikawa")


# ---------------------------------------------------------------------------
# 2. 5 WHYS
# ---------------------------------------------------------------------------
def render_five_whys() -> tuple[str, float]:
    """Vertical cascade: problem -> 5 whys -> root cause.

    Canvas 13 x 13. Data coords: 0..13 both axes.
    """
    fig = plt.figure(figsize=(13, 13), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 13)
    ax.set_axis_off()

    draw_title(
        ax,
        "5 Whys - Drilling from symptom to systemic root cause",
        "Why students waste time waiting for E-rickshaws",
        rule_w=0.155,  # ~2 in on a 13-in canvas
    )

    # Box stack parameters
    box_w = 9.0
    box_x = (13 - box_w) / 2     # centred
    top_y = 11.15                # top of the problem box
    gap = 0.35

    # Heights: problem 1.1, each why 1.05, root-cause 1.4
    problem_h = 1.10
    why_h = 1.05
    root_h = 1.45

    whys = [
        "Why 1:  Drivers wait until 4 passengers are on board before starting.",
        "Why 2:  Driver earnings are tied to per-seat fill, not per-ride revenue.",
        "Why 3:  No zone-aggregation aligns demand with driver availability.",
        "Why 4:  Booking demand is not visible to drivers ahead of time.",
        "Why 5:  There is no digital booking and aggregation layer.",
    ]

    # --- Problem box (terracotta) -----------------------------------------
    problem_y = top_y - problem_h
    pb = FancyBboxPatch((box_x, problem_y), box_w, problem_h,
                        boxstyle="round,pad=0.05,rounding_size=0.15",
                        linewidth=0, facecolor=TERRACOTTA, zorder=4)
    ax.add_patch(pb)
    ax.text(box_x + box_w / 2, problem_y + problem_h / 2,
            "Symptom: Students waste time waiting for E-rickshaws.",
            ha="center", va="center",
            fontsize=15, fontweight="bold", color="white", zorder=5)

    # Running y cursor (bottom of last drawn block)
    cursor = problem_y

    # Side rail geometry (we'll compute final bounds after drawing whys)
    why_top_y = None   # y of top of Why 1 box
    why_bot_y = None   # y of bottom of Why 5 box

    # --- 5 Why boxes ------------------------------------------------------
    for i, text in enumerate(whys):
        # Arrow from previous block to this one
        arrow_top_y = cursor
        arrow_bot_y = cursor - gap + 0.05
        ax.annotate("",
                    xy=(box_x + box_w / 2, arrow_bot_y),
                    xytext=(box_x + box_w / 2, arrow_top_y),
                    arrowprops=dict(arrowstyle="-|>", lw=2.5,
                                    color=TERRACOTTA, mutation_scale=22),
                    zorder=3)
        # "Why?" side label next to the arrow
        ax.text(box_x + box_w / 2 + 0.35,
                (arrow_top_y + arrow_bot_y) / 2,
                "Why?", style="italic", color=MUTED,
                fontsize=11, ha="left", va="center", zorder=3)

        wy_top = cursor - gap
        wy_bot = wy_top - why_h
        wb = FancyBboxPatch((box_x, wy_bot), box_w, why_h,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            linewidth=1.5, edgecolor=INK,
                            facecolor=PANEL_FILL, zorder=4)
        ax.add_patch(wb)
        ax.text(box_x + 0.35, wy_bot + why_h / 2, text,
                ha="left", va="center",
                fontsize=13.5, color=INK, zorder=5)

        if i == 0:
            why_top_y = wy_top
        if i == 4:
            why_bot_y = wy_bot
        cursor = wy_bot

    # --- Arrow to root cause ----------------------------------------------
    arrow_top_y = cursor
    arrow_bot_y = cursor - gap + 0.05
    ax.annotate("",
                xy=(box_x + box_w / 2, arrow_bot_y),
                xytext=(box_x + box_w / 2, arrow_top_y),
                arrowprops=dict(arrowstyle="-|>", lw=2.8,
                                color=MAROON, mutation_scale=24),
                zorder=3)

    # --- Root cause box (maroon) ------------------------------------------
    root_w = 10.0
    root_x = (13 - root_w) / 2
    root_y_top = cursor - gap
    root_y_bot = root_y_top - root_h
    rb = FancyBboxPatch((root_x, root_y_bot), root_w, root_h,
                        boxstyle="round,pad=0.05,rounding_size=0.18",
                        linewidth=0, facecolor=MAROON, zorder=4)
    ax.add_patch(rb)
    ax.text(root_x + root_w / 2, root_y_bot + root_h / 2,
            "Root cause: Absence of an app-based booking and aggregation layer.",
            ha="center", va="center",
            fontsize=15.5, fontweight="bold", color="white", zorder=5)

    # --- Sidebar rail: "Proximate" (upper 2-3) vs "Structural" (lower 2-3)
    rail_x = box_x + box_w + 0.4
    ax.plot([rail_x, rail_x], [why_bot_y, why_top_y],
            color=INK, linewidth=1.2, solid_capstyle="round", zorder=2)
    # Ticks at top and bottom of rail
    for yy in (why_top_y, why_bot_y):
        ax.plot([rail_x - 0.08, rail_x + 0.08], [yy, yy],
                color=INK, linewidth=1.2, zorder=2)
    mid_y = (why_top_y + why_bot_y) / 2
    # A mid tick to separate the two halves
    ax.plot([rail_x - 0.08, rail_x + 0.08], [mid_y, mid_y],
            color=INK, linewidth=1.0, zorder=2)
    # Labels
    ax.text(rail_x + 0.2, (why_top_y + mid_y) / 2, "Proximate\ncauses",
            ha="left", va="center", fontsize=11, color=INK,
            fontweight="bold")
    ax.text(rail_x + 0.2, (mid_y + why_bot_y) / 2, "Structural\ncauses",
            ha="left", va="center", fontsize=11, color=MAROON,
            fontweight="bold")

    footer(fig, "TQM Tool: 5 Whys - Ref. Ch.2 Basic 7 QC Tools")
    return save(fig, "02_five_whys")


# ---------------------------------------------------------------------------
# 3. SIPOC
# ---------------------------------------------------------------------------
def render_sipoc() -> tuple[str, float]:
    """5-column SIPOC table, hand-drawn with Rectangle.

    Canvas 18 x 10. Data coords: 0..18 horizontal, 0..10 vertical.
    """
    fig = plt.figure(figsize=(18, 10), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.set_axis_off()

    draw_title(
        ax,
        "SIPOC - Current E-rickshaw ride as a service process",
        "Suppliers, Inputs, Process, Outputs, Customers (pre-intervention state)",
        rule_w=0.11,
    )

    # --- Table geometry ---------------------------------------------------
    n_cols = 5
    table_left = 0.6
    table_right = 17.4
    table_w = table_right - table_left
    col_w = table_w / n_cols

    header_top = 8.2
    header_h = 1.15

    body_top = header_top - header_h - 0.12
    n_rows = 5
    row_h = 1.10
    body_bottom = body_top - n_rows * row_h

    headers = [
        ("S", "Suppliers", TERRACOTTA),
        ("I", "Inputs",    MUTED),
        ("P", "Process",   MAROON),
        ("O", "Outputs",   SAGE),
        ("C", "Customers", INK),
    ]

    content = {
        "S": [
            "E-rickshaw drivers",
            "Campus administration\n(route policy)",
            "Electricity provider\n(vehicle charging)",
            "Cash currency\n(student wallets)",
            "Campus security\n(identity checks)",
        ],
        "I": [
            "Driver availability",
            "Vehicle battery charge",
            "Fare rate",
            "Student transport demand",
            "Ride capacity (4 seats)",
        ],
        "P": [
            "1. Student walks\n    to pickup",
            "2. Waits for\n    4 passengers",
            "3. Driver selects route\n    by majority",
            "4. Pays cash\n    at drop-off",
            "5. Driver returns\n    to home zone",
        ],
        "O": [
            "Passenger transport\ncompleted",
            "Driver revenue\n(partial cash)",
            "Student time cost\n(wait + detour)",
            "Reconciled cash\n(leakage-prone)",
            "Campus traffic\nand parking events",
        ],
        "C": [
            "Students\n(direct customer)",
            "Drivers\n(revenue beneficiary)",
            "Campus administration\n(indirect)",
            "Adjacent campus\ncommunity",
            "Future: campus\nmobility dashboard",
        ],
    }

    # --- Draw header tabs -------------------------------------------------
    for i, (letter, name, color) in enumerate(headers):
        x = table_left + i * col_w
        # header rect
        rect = Rectangle((x, header_top - header_h), col_w, header_h,
                         linewidth=0, facecolor=color, zorder=3)
        ax.add_patch(rect)
        # Letter
        ax.text(x + col_w / 2, header_top - 0.40,
                letter, ha="center", va="center",
                fontsize=26, fontweight="bold", color="white", zorder=4)
        # Name
        ax.text(x + col_w / 2, header_top - 0.88,
                name, ha="center", va="center",
                fontsize=13, color="white", zorder=4)

    # --- Draw body grid + cell content ------------------------------------
    for row in range(n_rows):
        for col_i, (letter, _, color) in enumerate(headers):
            x = table_left + col_i * col_w
            y = body_top - (row + 1) * row_h
            cell = Rectangle((x, y), col_w, row_h,
                             linewidth=0.8, edgecolor=INK,
                             facecolor=PANEL_FILL, zorder=2)
            ax.add_patch(cell)
            # Small coloured tick at the left of each cell (picks up header colour)
            tick = Rectangle((x, y), 0.08, row_h,
                             linewidth=0, facecolor=color, zorder=3)
            ax.add_patch(tick)
            txt = content[letter][row]
            ax.text(x + 0.25, y + row_h / 2, txt,
                    ha="left", va="center",
                    fontsize=12, color=INK, zorder=4)

    # --- Bottom note ------------------------------------------------------
    ax.text(table_left, body_bottom - 0.55,
            ("The current process has no observable KPIs and relies on manual "
             "aggregation at the pickup point."),
            style="italic", color=MUTED, fontsize=12,
            ha="left", va="top")

    footer(fig, "TQM Tool: SIPOC - Ref. Ch.2 Process Scoping")
    return save(fig, "04_sipoc")


# ---------------------------------------------------------------------------
# 4. RELATIONS / INTERRELATIONSHIP
# ---------------------------------------------------------------------------
def render_relations() -> tuple[str, float]:
    """8 nodes on a ring; a 6-node reinforcing loop + 2 off-loop contributing
    causes. Canvas 18 x 13."""
    fig = plt.figure(figsize=(18, 13), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 13)
    ax.set_axis_off()

    draw_title(
        ax,
        "Relations diagram - The reinforcing loop behind poor E-rick service",
        "Cause-effect arrows expose a vicious cycle that will not self-correct without intervention",
        rule_w=0.11,
    )

    # --- Ring geometry ---------------------------------------------------
    # Place ring in lower ~80% of the canvas so title has air.
    cx, cy = 9.0, 5.7
    r_main = 4.3       # radius for the 6 main-loop nodes
    r_off  = 7.0       # radius for the 2 off-loop nodes (further out)
    node_w, node_h = 2.7, 1.0

    # 6 main-loop nodes, evenly distributed. Place Node 1 at top (90 deg),
    # go CLOCKWISE so arrows flow naturally 1->2->3->4->5->6->1.
    main_labels = [
        "Long wait time",                          # 1
        "Students avoid E-ricks",                  # 2
        "Fewer riders",                            # 3
        "Lower driver earnings",                   # 4
        "Fewer active E-ricks\n(drivers switch jobs)",   # 5
        "Longer wait times\n(feedback)",           # 6
    ]
    # Angles: start at 90 deg, step -60 (clockwise).
    main_angles = [math.radians(90 - 60 * i) for i in range(6)]
    main_pos = [(cx + r_main * math.cos(a), cy + r_main * math.sin(a))
                for a in main_angles]

    # 2 off-loop nodes placed on the right, above-right of Node 2. They both
    # feed into Node 1 (Long wait time) and Node 2 (Students avoid E-ricks),
    # which live at 12 o'clock and ~2 o'clock respectively, so the right
    # edge of the canvas is the natural home for them.
    off_labels = ["Cash leakage", "Route detours"]
    off_pos = [
        (16.0, 9.3),   # upper-right
        (16.0, 7.0),   # mid-right, just above Node 2
    ]

    def draw_node(center, label, border_color, lw):
        x = center[0] - node_w / 2
        y = center[1] - node_h / 2
        node = FancyBboxPatch((x, y), node_w, node_h,
                              boxstyle="round,pad=0.04,rounding_size=0.14",
                              linewidth=lw, edgecolor=border_color,
                              facecolor=PANEL_FILL, zorder=4)
        ax.add_patch(node)
        ax.text(center[0], center[1], label,
                ha="center", va="center",
                fontsize=12.5, color=INK, fontweight="bold", zorder=5)

    # Draw main-loop nodes with maroon borders (thicker)
    for pos, lbl in zip(main_pos, main_labels):
        draw_node(pos, lbl, MAROON, 2.0)
    # Draw off-loop nodes with muted borders
    for pos, lbl in zip(off_pos, off_labels):
        draw_node(pos, lbl, MUTED, 1.2)

    # --- Anchor helper: pick an edge point on the node rectangle nearest
    # to a target point, so arrows visibly attach to the box border.
    def anchor(center, toward):
        cx0, cy0 = center
        tx, ty = toward
        vx, vy = tx - cx0, ty - cy0
        if vx == 0 and vy == 0:
            return center
        hw, hh = node_w / 2 + 0.05, node_h / 2 + 0.05
        # Parametric scale to hit rectangle edge.
        sx = hw / abs(vx) if vx != 0 else float("inf")
        sy = hh / abs(vy) if vy != 0 else float("inf")
        s = min(sx, sy)
        return (cx0 + vx * s, cy0 + vy * s)

    # --- Main-loop arrows (1->2->3->4->5->6->1) ---------------------------
    for i in range(6):
        src = main_pos[i]
        dst = main_pos[(i + 1) % 6]
        src_pt = anchor(src, dst)
        dst_pt = anchor(dst, src)
        arr = FancyArrowPatch(src_pt, dst_pt,
                              connectionstyle="arc3,rad=0.18",
                              arrowstyle="-|>",
                              mutation_scale=20,
                              linewidth=2.6, color=MAROON, zorder=3)
        ax.add_patch(arr)

    # --- Off-loop contributing-cause arrows (dashed, muted) --------------
    # Cash leakage (off_pos[0]) -> Node 1 (Long wait time) and Node 2 (Students avoid)
    # Route detours (off_pos[1]) -> Node 1 and Node 2
    off_to_main = [
        (off_pos[0], main_pos[0]),  # cash -> long wait time
        (off_pos[0], main_pos[1]),  # cash -> students avoid
        (off_pos[1], main_pos[0]),  # route -> long wait
        (off_pos[1], main_pos[1]),  # route -> students avoid
    ]
    for src, dst in off_to_main:
        src_pt = anchor(src, dst)
        dst_pt = anchor(dst, src)
        arr = FancyArrowPatch(src_pt, dst_pt,
                              connectionstyle="arc3,rad=-0.15",
                              arrowstyle="-|>",
                              mutation_scale=16,
                              linewidth=1.6, color=MUTED,
                              linestyle=(0, (5, 3)), zorder=3)
        ax.add_patch(arr)

    # --- Central "Vicious cycle" annotation -------------------------------
    center_w, center_h = 2.3, 1.0
    cxbox = cx - center_w / 2
    cybox = cy - center_h / 2
    center_box = FancyBboxPatch((cxbox, cybox), center_w, center_h,
                                boxstyle="round,pad=0.04,rounding_size=0.12",
                                linewidth=1.5, edgecolor=INK,
                                facecolor="white", zorder=6)
    ax.add_patch(center_box)
    ax.text(cx, cy + 0.15, "Vicious cycle",
            ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK, zorder=7)
    # Tiny infinity-ish icon made of two arcs
    r_ico = 0.22
    left_c = (cx - 0.22, cy - 0.28)
    right_c = (cx + 0.22, cy - 0.28)
    circle_l = mpatches.Arc(left_c, r_ico * 2, r_ico * 2,
                            theta1=0, theta2=360,
                            linewidth=1.4, color=MAROON, zorder=7)
    circle_r = mpatches.Arc(right_c, r_ico * 2, r_ico * 2,
                            theta1=0, theta2=360,
                            linewidth=1.4, color=MAROON, zorder=7)
    ax.add_patch(circle_l)
    ax.add_patch(circle_r)

    # --- Legend (bottom-left, well clear of Node 4 at the bottom of ring)
    lx, ly = 0.5, 0.5
    lw_leg, lh_leg = 4.6, 1.35
    legend_bg = FancyBboxPatch((lx, ly), lw_leg, lh_leg,
                               boxstyle="round,pad=0.02,rounding_size=0.1",
                               linewidth=0.8, edgecolor=RULE,
                               facecolor=PANEL_FILL, zorder=2)
    ax.add_patch(legend_bg)
    ax.text(lx + 0.2, ly + lh_leg - 0.22, "Legend",
            ha="left", va="top", fontsize=11.5, fontweight="bold",
            color=INK)
    # maroon sample
    ax.annotate("",
                xy=(lx + 1.1, ly + lh_leg - 0.60),
                xytext=(lx + 0.25, ly + lh_leg - 0.60),
                arrowprops=dict(arrowstyle="-|>", lw=2.5,
                                color=MAROON, mutation_scale=16),
                zorder=3)
    ax.text(lx + 1.25, ly + lh_leg - 0.60,
            "Reinforcing loop (maroon)",
            ha="left", va="center", fontsize=11, color=INK)
    # muted dashed sample
    ax.annotate("",
                xy=(lx + 1.1, ly + 0.35),
                xytext=(lx + 0.25, ly + 0.35),
                arrowprops=dict(arrowstyle="-|>", lw=1.5,
                                color=MUTED, mutation_scale=14,
                                linestyle=(0, (5, 3))),
                zorder=3)
    ax.text(lx + 1.25, ly + 0.35,
            "Contributing causes (muted)",
            ha="left", va="center", fontsize=11, color=INK)

    footer(fig, "TQM Tool: Relations diagram - Ref. Ch.3 New 7 QC Tools")
    return save(fig, "09_relations")


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------
def main():
    results = []
    results.append(("01_ishikawa",  *render_ishikawa()))
    results.append(("02_five_whys", *render_five_whys()))
    results.append(("04_sipoc",     *render_sipoc()))
    results.append(("09_relations", *render_relations()))
    print("\nSummary:")
    for name, path, kb in results:
        print(f"  {name:<16} {kb:7.1f} KB   {path}")


if __name__ == "__main__":
    main()
