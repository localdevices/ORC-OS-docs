"""
Combined survey plot with two stacked subplots:
- Top row: top-view river plan with camera FoV and GCP checkerboards
- Bottom row: cross-section with water level, staff gauge datum, and GCP datum
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import transforms


def draw_checkerboard(ax, center_x, center_y, size=0.9, angle_deg=0.0, zorder=6):
    """Draw a 2x2 black-and-white checkerboard centered at (x, y)."""
    half = size / 2.0
    cell = size / 2.0
    t = transforms.Affine2D().rotate_deg_around(center_x, center_y, angle_deg) + ax.transData

    cells = [
        (-half, -half, "white"),
        (0.0, -half, "black"),
        (-half, 0.0, "black"),
        (0.0, 0.0, "white"),
    ]
    for dx, dy, color in cells:
        patch = mpatches.Rectangle(
            (center_x + dx, center_y + dy),
            cell,
            cell,
            facecolor=color,
            edgecolor="black",
            linewidth=0.7,
            transform=t,
            zorder=zorder,
        )
        ax.add_patch(patch)

    outline = mpatches.Rectangle(
        (center_x - half, center_y - half),
        size,
        size,
        facecolor="none",
        edgecolor="black",
        linewidth=1.0,
        transform=t,
        zorder=zorder + 0.1,
    )
    ax.add_patch(outline)


def draw_staff_gauge(ax, gx, z_bot, z_top, width, color_a, color_b):
    """Draw a banded staff gauge at position gx from z_bot to z_top."""
    band_height = 0.2
    z = z_bot
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
        z += band_height

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


def ray_endpoint(x0, y0, angle_deg, length):
    """Return endpoint of a ray defined by origin, angle, and length."""
    rad = np.deg2rad(angle_deg)
    return x0 + length * np.cos(rad), y0 + length * np.sin(rad)


def draw_top_view(ax):
    """Top-view subplot with camera FoV and GCP checkerboards."""
    x = np.linspace(0.0, 30.0, 500)
    y_near = 10.0 + 0.15 * np.sin(2.0 * np.pi * x / 20.0) + 0.08 * np.sin(2.0 * np.pi * x / 13.5)
    river_width = 13.0
    y_far = y_near + river_width + 0.05 * np.sin(2.0 * np.pi * x / 30.0)

    cam_x = 15.0
    cam_y = np.interp(cam_x, x, y_near) - 6.0
    view_heading_deg = 90.0
    fov_half_angle_deg = 33.0
    fov_range = 66.0

    fov_left = ray_endpoint(cam_x, cam_y, view_heading_deg + fov_half_angle_deg, fov_range)
    fov_right = ray_endpoint(cam_x, cam_y, view_heading_deg - fov_half_angle_deg, fov_range)

    far_gcp_x = np.array([5.2, 10.5, 16.5, 19.5, 24.3])
    far_gcp_y = np.interp(far_gcp_x, x, y_far) + np.array([1.0, 1.4, 1.3, 1.8, 1.2])

    near_gcp_x = np.array([12.8, 14.2, 16.2])
    near_gcp_y = np.interp(near_gcp_x, x, y_near) - np.array([1.0, 1.4, 1.1])

    y_cross = np.linspace(2.0, 28.0, 12) + (np.random.rand(12) - 0.5)
    x_cross = np.ones(len(y_cross)) * (cam_x - 2.0)  # location of cross section top view


    ax.fill_between(x, y_near - 9.0, y_far + 6.0, color="#c8a96e", alpha=1.0, zorder=0)
    ax.fill_between(x, y_near, y_far, color="#5b9bd5", alpha=0.45, zorder=1)
    ax.plot(x, y_near, color="#1a6fab", linewidth=2.0, zorder=2)
    ax.plot(x, y_far, color="#1a6fab", linewidth=2.0, zorder=2)
    ax.plot(x_cross, y_cross, color="#1f4aa8", linewidth=1.5, linestyle="--", marker="o", zorder=3, label="Cross-section survey")
    mast_color = "#555555"
    ax.add_patch(plt.Circle((cam_x, cam_y), 0.35, facecolor=mast_color, edgecolor="black", linewidth=0.8, zorder=5))

    camera_body = mpatches.FancyBboxPatch(
        (cam_x - 0.65, cam_y - 0.28),
        1.3,
        0.56,
        boxstyle="round,pad=0.05",
        facecolor="#222222",
        edgecolor="black",
        linewidth=1.0,
        zorder=6,
    )
    rot = transforms.Affine2D().rotate_deg_around(cam_x, cam_y, view_heading_deg) + ax.transData
    camera_body.set_transform(rot)
    ax.add_patch(camera_body)

    lens_x, lens_y = ray_endpoint(cam_x, cam_y, view_heading_deg, 0.8)
    ax.add_patch(plt.Circle((lens_x, lens_y), 0.12, facecolor="#888888", edgecolor="black", linewidth=0.7, zorder=7))

    fov_poly = mpatches.Polygon(
        [(cam_x, cam_y), fov_left, fov_right],
        closed=True,
        facecolor="green",
        edgecolor="none",
        alpha=0.10,
        zorder=3,
    )
    ax.add_patch(fov_poly)

    ax.plot([cam_x, fov_left[0]], [cam_y, fov_left[1]], color="green", linewidth=1.5, linestyle="--", zorder=4)
    ax.plot(
        [cam_x, fov_right[0]],
        [cam_y, fov_right[1]],
        color="green",
        linewidth=1.5,
        linestyle="--",
        zorder=4,
        label="Camera field of view",
    )

    for gx, gy in zip(far_gcp_x, far_gcp_y):
        draw_checkerboard(ax, gx, gy, size=0.9, angle_deg=8.0)
    for gx, gy in zip(near_gcp_x, near_gcp_y):
        draw_checkerboard(ax, gx, gy, size=0.9, angle_deg=-12.0)

    ax.plot([], [], color="black", linewidth=2, label="Ground control points")
    ax.text(cam_x - 0.3, cam_y - 2.0, "Camera", fontsize=13, color="#222222")

    ax.set_xlim(-1, 30)
    ax.set_ylim(0, 30)
    ax.set_aspect("equal")
    ax.set_xlabel("Along-river distance (m)", fontsize=15)
    ax.set_ylabel("Across-river distance (m)", fontsize=15)
    ax.set_title("Top view: camera setup, FoV and Ground Control Points", fontsize=15)
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="lower left", fontsize=11, framealpha=0.85)


def draw_cross_section(ax):
    """Cross-section subplot with water levels and datums."""
    x = np.array([0, 2, 4, 6, 8, 11, 14, 17, 19, 20.5, 23, 26, 28])
    z_bed = np.array([3.8, 4.0, 3.2, 3.1, 2.9, 2.7, 1.2, 1.0, 1.8, 2.5, 2.9, 4.0, 3.8])

    cross_x = x[1:-1]
    cross_y = z_bed[1:-1]

    water_level = 2.9
    z_surface_at_x = np.minimum(z_bed, water_level)

    mast_x = 2.0
    mast_base = 4.0
    mast_height = 5.0
    camera_z = mast_base + mast_height

    gauge_x_1 = 17.0
    gauge1_bottom = z_bed[7] - 0.1
    gauge1_top = water_level + 2.0
    gauge_width = 0.25

    fov_near_x = 4.0
    fov_near_z = z_bed[2]
    fov_far_x = x[-2]
    fov_far_z = z_bed[-2]

    # compute angle of the camera according to field of view lines
    def compute_angle(x0, z0, x1, z1):
        return np.arctan2(z1 - z0, x1 - x0)
    angle_near = compute_angle(mast_x, camera_z, fov_near_x, fov_near_z)
    angle_far = compute_angle(mast_x, camera_z, fov_far_x, fov_far_z)

    angle_av = 0.5 * (angle_near + angle_far)

    # Build a local transform so that camera can be rotated
    t = transforms.Affine2D().rotate_deg_around(mast_x, camera_z, np.rad2deg(angle_av)) + ax.transData

    ax.fill_between(
        x,
        z_surface_at_x,
        water_level,
        where=(z_bed <= water_level),
        color="#5b9bd5",
        alpha=0.45,
        label="Water body",
    )
    ax.hlines(water_level, x[0], x[-1], colors="#1a6fab", linewidths=2, linestyles="-", zorder=0)

    ax.fill_between(x, z_bed, z_bed.min() - 3.5, color="#c8a96e", alpha=1.0, zorder=1)
    ax.plot(x, z_bed, color="#7a5c2e", linewidth=2, label="River bed", zorder=1)
    ax.plot(cross_x, cross_y, color="#1f4aa8", linewidth=1.5, linestyle="--", marker="o", zorder=2, label="Cross-section survey")
    draw_staff_gauge(ax, gauge_x_1, gauge1_bottom, gauge1_top, gauge_width, "#e8e8e8", "#333333")

    for elev in np.arange(np.ceil(gauge1_bottom), np.floor(gauge1_top) + 0.5, 0.5):
        ax.hlines(
            elev,
            gauge_x_1 + gauge_width / 2,
            gauge_x_1 + gauge_width / 2 + 0.15,
            colors="black",
            linewidths=1,
            zorder=6,
        )
        ax.text(
            gauge_x_1 + gauge_width / 2 + 0.18,
            elev,
            f"{elev:.1f}",
            va="center",
            ha="left",
            fontsize=12,
            zorder=6,
        )

    mast_color = "#555555"
    ax.plot([mast_x, mast_x], [mast_base, camera_z], color=mast_color, linewidth=4, solid_capstyle="round", zorder=5)
    ax.plot([mast_x - 0.3, mast_x + 0.3], [mast_base, mast_base], color=mast_color, linewidth=3, zorder=5)

    cam_w, cam_h = 0.5, 0.35
    camera_body = mpatches.FancyBboxPatch(
        (mast_x - cam_w / 2, camera_z - cam_h / 2),
        cam_w,
        cam_h,
        boxstyle="round,pad=0.05",
        facecolor="#222222",
        edgecolor="black",
        transform=t,
        linewidth=1,
        zorder=6,
    )
    ax.add_patch(camera_body)
    lens = plt.Circle((mast_x + cam_w / 2 - 0.05, camera_z), 0.1, transform=t, color="#888888", zorder=7)
    ax.add_patch(lens)

    ax.plot(
        [mast_x, fov_near_x],
        [camera_z, fov_near_z],
        color="green",
        linewidth=1.5,
        linestyle="--",
        zorder=3,
        label="Camera field of view",
    )
    ax.plot([mast_x, fov_far_x], [camera_z, fov_far_z], color="green", linewidth=1.5, linestyle="--", zorder=3)

    ax.hlines(
        [z_bed.min() - 3.0, gauge1_bottom],
        x[0],
        x[-1],
        colors=["#494949", "#0E981C"],
        linestyles="dashed",
        linewidths=1,
        zorder=7,
    )

    x_wet = x[z_bed <= water_level]
    ax.annotate(
        "Water level",
        xy=(x_wet[-1], water_level),
        xytext=(x_wet[-1] + 0.3, water_level + 0.25),
        fontsize=13,
        color="#1a6fab",
        arrowprops=dict(arrowstyle="-|>", color="#1a6fab", lw=1),
    )
    ax.annotate(
        "Local gauge datum",
        xy=(gauge_x_1, gauge1_bottom),
        xytext=(gauge_x_1 + 4.5, gauge1_bottom + 0.3),
        fontsize=12,
        color="black",
        zorder=7,
    )
    ax.annotate(
        "GCP datum",
        xy=(gauge_x_1, z_bed.min() - 3.0),
        xytext=(gauge_x_1 + 0.5, z_bed.min() - 2.7),
        fontsize=12,
        color="black",
        zorder=7,
    )

    datum_levels = [z_bed.min() - 3.0, gauge1_bottom]
    arrow_x_positions = [gauge_x_1 - 1.5, gauge_x_1 + 1.5]
    arrow_annotations = ["GCP water level", "Local gauge water level"]
    colors = ["#494949", "#0E981CFF"]

    for datum_z, arrow_x, annotation, color in zip(datum_levels, arrow_x_positions, arrow_annotations, colors):
        ax.annotate(
            "",
            xy=(arrow_x, water_level),
            xytext=(arrow_x, datum_z),
            arrowprops=dict(arrowstyle="->", color=color, lw=1.2),
            zorder=8,
        )
        mid_z = (water_level + datum_z) / 2.0
        ax.text(
            arrow_x + 0.4,
            mid_z,
            annotation,
            ha="center",
            va="center",
            rotation=90,
            fontsize=12,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.75, pad=1.5),
            zorder=9,
        )

    ax.text(gauge_x_1, gauge1_top + 0.1, "Staff gauge", ha="center", fontsize=12, color="black", zorder=7)
    ax.text(mast_x, camera_z + 0.35, "Camera", ha="center", fontsize=12, color="#222222", zorder=7)

    ax.set_xlim(0.0, 28)
    ax.set_ylim(z_bed.min() - 3.5, camera_z + 1.2)
    ax.set_aspect("equal")
    ax.set_xlabel("Cross-section distance (m)", fontsize=14)
    ax.set_ylabel("Elevation (m)", fontsize=14)
    ax.set_title("Cross-section: water levels, datums and camera setup", fontsize=15)
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="upper right", fontsize=11, framealpha=0.85)


# --- Combined figure ----------------------------------------------------
fig, (ax_top, ax_xs) = plt.subplots(
    2,
    1,
    figsize=(14, 13),
    gridspec_kw={"height_ratios": [1.0, 1.0]},
)

draw_top_view(ax_top)
draw_cross_section(ax_xs)

fig.suptitle("Survey overview: plan view and cross-section", fontsize=14, y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.savefig("camera_datums_combined.png", dpi=150, bbox_inches="tight")
plt.show()
