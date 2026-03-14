"""
Cross-section view of a stream showing:
- River bed bathymetry
- Water level
- Two overlapping staff gauges spanning the full bathymetry range
- Camera on a mast on one side
- Camera field of view (dotted lines to lowest/highest visible point)
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# --- Geometry -----------------------------------------------------------
# Cross-section x-coordinates (m, left bank to right bank)
x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
# Bed elevation (m)
z_bed = np.array([3.8, 4.0, 3.2, 2.8, 2.0, 1.2, 0.8, 1.0, 1.8, 2.5, 3.2, 4.0, 3.8])

water_level = 3.2          # m
z_min = z_bed.min()        # deepest point
z_surface_at_x = np.minimum(z_bed, water_level)

# Camera side: left bank (x = 0)
mast_x = 0.0              # m  (just outside the left bank)
mast_base = 4.0            # ground elevation at mast base
mast_height = 4.0          # height of mast above base
camera_z = mast_base + mast_height  # camera elevation

# Staff gauge positions (left bank side)
gauge_x_1 = 12.0            # first staff gauge
gauge_x_2 = 8.0            # second staff gauge (overlaps with first)

# Staff gauge vertical extents
gauge1_bottom = z_bed[6] - 0.1    # slightly below local bed
gauge1_top = water_level - 1.0    # above water level
gauge2_bottom = water_level -1.3  # overlaps with top of gauge 1
gauge2_top = 4.5                  # 

gauge_width = 0.25         # visual width of staff gauge bar

# Field of view: from camera to the lowest visible point and
# to the far bank (highest visible edge)
fov_near_x = 2.0    # closest staff gauge as near edge of FoV
fov_near_z = z_bed[1]
fov_far_x = x[-2]         # far bank
fov_far_z = z_bed[-2]

# cross section coordinates
cross_x = np.array([2, gauge_x_2-0.25, gauge_x_2-0.25, gauge_x_1-0.25, gauge_x_1-0.25, 22, 22])
cross_z = np.array([z_bed.max(), z_bed.max(), gauge2_bottom + 0.2, gauge2_bottom + 0.2, gauge1_bottom + 0.2, gauge1_bottom + 0.2, z_bed.max()])


# --- Figure -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7))

# 1. Fill water body
ax.fill_between(
    x,
    z_surface_at_x,
    water_level,
    where=(z_bed <= water_level),
    color="#5b9bd5",
    alpha=0.45,
    label="Water body",
)

# 2. Water surface line
x_wet = x[z_bed <= water_level]
# ax.hlines(
#     water_level,
#     x_wet[0],
#     x_wet[-1],
#     colors="#1a6fab",
#     linewidths=2,
#     linestyles="-",
#     label=f"Water level ({water_level:.1f} m)",
# )
ax.hlines(
    water_level,
    x[0],
    x[-1],
    colors="#1a6fab",
    linewidths=2,
    linestyles="-",
    label=f"Water level ({water_level:.1f} m)",
    zorder=0
)


# 3. River bed bathymetry
ax.fill_between(x, z_bed, z_bed.min() - 0.5, color="#c8a96e", alpha=1.0, zorder=1)
ax.plot(x, z_bed, color="#7a5c2e", linewidth=2, label="River bed", zorder=1)

# 4. Staff gauge helper function
def draw_staff_gauge(ax, gx, z_bot, z_top, width, color_a, color_b, label=None):
    """Draw a banded staff gauge at position gx from z_bot to z_top."""
    band_height = 0.2
    z = z_bot
    first = True
    while z < z_top:
        top = min(z + band_height, z_top)
        color = color_a if int(round((z - z_bot) / band_height)) % 2 == 0 else color_b
        rect = mpatches.FancyBboxPatch(
            (gx - width / 2, z),
            width,
            top - z,
            boxstyle="square,pad=0",
            facecolor=color,
            edgecolor="black",
            linewidth=0.5,
            zorder=4,
        )
        ax.add_patch(rect)
        if first and label:
            # invisible proxy for legend
            ax.plot([], [], color=color_a, linewidth=6, label=label)
            first = False
        z += band_height
    # Outline
    rect_outline = mpatches.FancyBboxPatch(
        (gx - width / 2, z_bot),
        width,
        z_top - z_bot,
        boxstyle="square,pad=0",
        facecolor="none",
        edgecolor="black",
        linewidth=1.2,
        zorder=5,
    )
    ax.add_patch(rect_outline)

draw_staff_gauge(ax, gauge_x_1, gauge1_bottom, gauge1_top, gauge_width,
                 "#e8e8e8", "#333333")
draw_staff_gauge(ax, gauge_x_2, gauge2_bottom, gauge2_top, gauge_width,
                 "#e8e8e8", "#111111")

# Tick marks and labels on gauge 1
for elev in np.arange(np.ceil(gauge1_bottom), np.floor(gauge1_top) + 0.5, 0.5):
    ax.hlines(elev, gauge_x_1 + gauge_width / 2, gauge_x_1 + gauge_width / 2 + 0.15,
              colors="black", linewidths=1, zorder=6)
    ax.text(gauge_x_1 + gauge_width / 2 + 0.18, elev, f"{elev:.1f}",
            va="center", ha="left", fontsize=9, zorder=6)

# Tick marks and labels on gauge 2
for elev in np.arange(np.ceil(gauge2_bottom), np.floor(gauge2_top) + 0.5, 0.5):
    ax.hlines(elev, gauge_x_2 + gauge_width / 2, gauge_x_2 + gauge_width / 2 + 0.15,
              colors="black", linewidths=1, zorder=6)
    ax.text(gauge_x_2 + gauge_width / 2 + 0.18, elev, f"{elev:.1f}",
            va="center", ha="left", fontsize=9, zorder=6)

# 5. Camera mast
mast_color = "#555555"
ax.plot([mast_x, mast_x], [mast_base, camera_z], color=mast_color, linewidth=4,
        solid_capstyle="round", zorder=5)
# Mast base plate
ax.plot([mast_x - 0.3, mast_x + 0.3], [mast_base, mast_base],
        color=mast_color, linewidth=3, zorder=5)

# Camera body (small rectangle at top of mast)
cam_w, cam_h = 0.5, 0.35
camera_body = mpatches.FancyBboxPatch(
    (mast_x - cam_w / 2, camera_z - cam_h / 2),
    cam_w, cam_h,
    boxstyle="round,pad=0.05",
    facecolor="#222222",
    edgecolor="black",
    linewidth=1,
    zorder=6,
)
ax.add_patch(camera_body)
# Lens circle
lens = plt.Circle((mast_x + cam_w / 2 - 0.05, camera_z), 0.1,
                   color="#888888", zorder=7)
ax.add_patch(lens)
ax.plot([], [], color="#222222", linewidth=6)  # legend proxy

# 6. Field of view lines (from camera to near/far extremes)
ax.plot(
    [mast_x, fov_near_x], [camera_z, fov_near_z],
    color="orange", linewidth=1.5, linestyle="--", zorder=3,
    label="Camera field of view",
)
ax.plot(
    [mast_x, fov_far_x], [camera_z, fov_far_z],
    color="orange", linewidth=1.5, linestyle="--", zorder=3,
)
# # Shade the FoV cone lightly
# fov_poly_x = [mast_x, fov_near_x, fov_far_x]
# fov_poly_z = [camera_z, fov_near_z, fov_far_z]
# ax.fill(fov_poly_x, fov_poly_z, color="orange", alpha=0.08, zorder=2)

# 7. cross section
ax.plot(cross_x, cross_z, color="red", linewidth=1.5, linestyle="--", zorder=3, label="Cross section")

# 8. Annotations
ax.annotate(
    "Water level",
    xy=(x_wet[-1], water_level),
    xytext=(x_wet[-1] + 0.3, water_level + 0.25),
    fontsize=12, color="#1a6fab",
    arrowprops=dict(arrowstyle="-|>", color="#1a6fab", lw=1),
)
ax.text(gauge_x_1, gauge1_top + 0.1, "Gauge 1", ha="center", fontsize=10,
        color="black", zorder=7)
ax.text(gauge_x_2, gauge2_top + 0.1, "Gauge 2", ha="center", fontsize=10,
        color="black", zorder=7)
ax.text(mast_x, camera_z + 0.35, "Camera", ha="center", fontsize=10,
        color="#222222", zorder=7)

# --- Axes styling -------------------------------------------------------
ax.set_xlim(-3, 26)
ax.set_ylim(z_bed.min() - 0.8, camera_z + 1.2)
ax.set_xlabel("Cross-section distance (m)", fontsize=12)
ax.set_ylabel("Elevation (m)", fontsize=12)
ax.set_title("Stream cross-section: bathymetry, water level,\nstaff gauges and camera setup", fontsize=12)
ax.legend(loc="upper right", fontsize=12, framealpha=0.85)
ax.set_aspect("equal")
ax.grid(True, linestyle=":", alpha=0.4)

plt.tight_layout()
# plt.savefig("cross_section_camera_gauges.png", dpi=150, bbox_inches="tight")
# plt.show()
