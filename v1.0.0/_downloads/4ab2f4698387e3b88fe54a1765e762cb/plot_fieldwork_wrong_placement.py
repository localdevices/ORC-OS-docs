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

from matplotlib import transforms

# --- Geometry -----------------------------------------------------------
# Cross-section x-coordinates (m, left bank to right bank)
x = np.array([-3, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
# Bed elevation (m)
z_bed = np.array([3.8, 3.8, 4.0, 3.2, 2.8, 2.0, 1.2, 0.8, 1.0, 1.8, 2.5, 3.2, 4.0, 3.8])

water_level = 2.5          # m
z_min = z_bed.min()        # deepest point
z_surface_at_x = np.minimum(z_bed, water_level)

# Camera side: left bank (x = 0)
mast_x = 0.0              # m  (just outside the left bank)
mast_base = 3.8            # ground elevation at mast base
mast_height = 5.0          # height of mast above base
camera_z = mast_base + mast_height  # camera elevation

# Staff gauge positions (left bank side)
gauge_x_1 = 12.0            # first staff gauge
gauge_x_2 = 8.0            # second staff gauge (overlaps with first)

# Staff gauge vertical extents
gauge1_bottom = z_bed[6] - 0.1    # slightly below local bed
gauge1_top = water_level + 2.0    # above water level

gauge_width = 0.25         # visual width of staff gauge bar

# Field of view: from camera to the lowest visible point and
# to the far bank (highest visible edge)
fov_near_x = 4.0    # closest staff gauge as near edge of FoV
fov_near_z = z_bed[1] - 5
fov_far_x = x[-2]         # far bank
fov_far_z = z_bed[-2]

# compute angle of the camera according to field of view lines
def compute_angle(x0, z0, x1, z1):
    return np.arctan2(z1 - z0, x1 - x0)
angle_near = compute_angle(mast_x, camera_z, fov_near_x, fov_near_z)
angle_far = compute_angle(mast_x, camera_z, fov_far_x, fov_far_z)

angle_av = 0.5 * (angle_near + angle_far)


def plot_cam_position(ax, title, correct, x_offset, y_offset, rotation, plot_legend):
    # Build a local transform so that camera can be rotated
    mast_x_trans = mast_x + x_offset
    mast_base_trans = mast_base + y_offset
    camera_z_trans = camera_z + y_offset

    t = transforms.Affine2D().rotate_deg_around(mast_x_trans, camera_z_trans, np.rad2deg(angle_av) + rotation) + ax.transData
    t_lines = transforms.Affine2D().rotate_deg_around(mast_x_trans, camera_z_trans, rotation) + ax.transData

    # 1. Fill water body
    ax.fill_between(
        x,
        z_surface_at_x,
        water_level,
        # where=(z_bed <= water_level),
        color="#5b9bd5",
        alpha=0.45,
        label="Water body",
    )

    # 2. Water surface line
    x_wet = x[z_bed <= water_level]
    ax.hlines(
        water_level,
        x[0],
        x[-1],
        colors="#1a6fab",
        linewidths=2,
        linestyles="-",
        zorder=0
    )

    # 3. River bed bathymetry
    ax.fill_between(x, z_bed, z_bed.min() - 3.5, color="#c8a96e", alpha=1.0, zorder=1)
    ax.plot(x, z_bed, color="#7a5c2e", linewidth=2, label="River bed", zorder=1)

    # 4. Camera mast
    mast_color = "#555555"
    ax.plot([mast_x_trans, mast_x_trans], [mast_base_trans, camera_z_trans], color=mast_color, linewidth=4,
            solid_capstyle="round", zorder=5)
    # Mast base plate
    ax.plot([mast_x_trans - 0.3, mast_x_trans + 0.3], [mast_base_trans, mast_base_trans],
            color=mast_color, linewidth=3, zorder=5)

    # Camera body (small rectangle at top of mast)
    cam_w, cam_h = 0.5, 0.35
    camera_body = mpatches.FancyBboxPatch(
        (mast_x_trans - cam_w / 2, camera_z_trans - cam_h / 2),
        cam_w, cam_h,
        boxstyle="round,pad=0.05",
        facecolor="#222222",
        edgecolor="black",
        transform=t,
        linewidth=1,
        zorder=6,
    )
    ax.add_patch(camera_body)
    # Lens circle
    lens = plt.Circle((mast_x_trans + cam_w / 2 - 0.05, camera_z_trans), 0.1, transform=t,
                    color="#888888", zorder=7)
    ax.add_patch(lens)
    ax.plot([], [], color="#222222", linewidth=6)  # legend proxy

    # 6. Field of view lines (from camera to near/far extremes)
    ax.plot(
        [mast_x_trans, fov_near_x + x_offset], [camera_z_trans, fov_near_z + y_offset],
        transform=t_lines,
        color="green", linewidth=1.5, linestyle="--", zorder=0,
        label="Camera field of view",
    )
    ax.plot(
        [mast_x_trans, fov_far_x + x_offset], [camera_z_trans, fov_far_z + y_offset],
        transform=t_lines,
        color="green", linewidth=1.5, linestyle="--", zorder=0,
    )
    if correct:
        ax.plot(0, 0, marker="$\checkmark$", markersize=20, markeredgecolor="#33FF33", markerfacecolor="none", markeredgewidth=5)
    else:
        ax.plot(0, 0, marker="X", markersize=20, markeredgecolor="red", markerfacecolor="red", markeredgewidth=4)

    # --- Axes styling -------------------------------------------------------
    ax.set_xlim(-3.0, 24)
    ax.set_ylim(z_bed.min() - 3.5, camera_z + 1.2)
    ax.set_xlabel("Cross-section distance (m)", fontsize=12)
    ax.set_ylabel("Elevation (m)", fontsize=12)
    ax.set_title(title, fontsize=12)
    if plot_legend:
        ax.legend(loc="upper right", fontsize=12, framealpha=0.85)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.4)



titles = [
    f"$\\bf{{a}}$.Camera at a good position and rotation, both sides visible",
    f"$\\bf{{b}}$.Camera rotated too much upwards, seeing sky",
    f"$\\bf{{c}}$.Camera rotated too much down, missing parts of far shore",
    f"$\\bf{{d}}$.Camera too close to see entire cross-section",
    ]

rotations = [0.0, 15.0, -7.0, -25.0]
offset_xs = [0.0, 0.0, 0.0, 6.0]
offset_ys = [0.0, 0.0, 0.0, -1.3]


# --- Figure -------------------------------------------------------------
fig, axs = plt.subplots(figsize=(16, 10), nrows=2, ncols=2)

for n, (ax, title, x_offset, y_offset, rotation) in enumerate(zip(axs.flat, titles, offset_xs, offset_ys, rotations)):
    if n == 0:
        plot_legend = True
        correct = True
    else:
        plot_legend = False
        correct = False

    plot_cam_position(ax, title, correct=correct, x_offset=x_offset, y_offset=y_offset, rotation=rotation, plot_legend=plot_legend)


plt.tight_layout()
# plt.savefig("cross_section_camera_gauges.png", dpi=150, bbox_inches="tight")
plt.show()
