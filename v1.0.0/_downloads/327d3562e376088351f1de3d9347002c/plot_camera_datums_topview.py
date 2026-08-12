"""
Top-view plan of a river reach showing:
- River corridor with a gently wobbling shoreline
- Camera mast and camera on the near shore
- Camera field of view in plan view
- Ground control points (2x2 black/white checkerboards):
  5 on the opposite bank and 3 on the near shore
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import transforms


def draw_checkerboard(ax, center_x, center_y, size=0.9, angle_deg=0.0, zorder=6):
    """Draw a 2x2 black-and-white checkerboard centered at (x, y)."""
    half = size / 2.0
    cell = size / 2.0

    # Build a local transform so boards can be rotated while staying centered.
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


# --- Geometry -----------------------------------------------------------
x = np.linspace(0.0, 30.0, 500)

# Near shoreline with gentle natural wobble.
y_near = 10.0 + 0.15 * np.sin(2.0 * np.pi * x / 20.0) + 0.08 * np.sin(2.0 * np.pi * x / 13.5)

# Opposite shoreline kept mostly straight.
river_width = 13.0
y_far = y_near + river_width + 0.05 * np.sin(2.0 * np.pi * x / 30.0)

# Camera location (near-shore side, slightly inland).
cam_x = 15.0
cam_y = np.interp(cam_x, x, y_near) - 6.0

# Camera viewing direction and FoV angle in plan view.
view_heading_deg = 90.0
fov_half_angle_deg = 33.0
fov_range = 66.0


def ray_endpoint(x0, y0, angle_deg, length):
    rad = np.deg2rad(angle_deg)
    return x0 + length * np.cos(rad), y0 + length * np.sin(rad)


fov_left = ray_endpoint(cam_x, cam_y, view_heading_deg + fov_half_angle_deg, fov_range)
fov_right = ray_endpoint(cam_x, cam_y, view_heading_deg - fov_half_angle_deg, fov_range)

# GCPs on opposite bank (5) and near shore (3)
far_gcp_x = np.array([5.2, 10.5, 16.5, 19.5, 24.3])
far_gcp_y = np.interp(far_gcp_x, x, y_far) + np.array([1.0, 1.4, 1.3, 1.8, 1.2])

near_gcp_x = np.array([12.8, 14.2, 16.2])
near_gcp_y = np.interp(near_gcp_x, x, y_near) - np.array([1.0, 1.4, 1.1])

# --- Figure -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7))

# 1. Land background
ax.fill_between(x, y_near - 9.0, y_far + 6.0, color="#c8a96e", alpha=1.0, zorder=0)

# 2. Water body and shorelines
ax.fill_between(x, y_near, y_far, color="#5b9bd5", alpha=0.45, zorder=1)
ax.plot(x, y_near, color="#1a6fab", linewidth=2.0, zorder=2)
ax.plot(x, y_far, color="#1a6fab", linewidth=2.0, zorder=2)

# 3. Camera mast and body (top view)
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

# Lens marker at the camera front.
lens_x, lens_y = ray_endpoint(cam_x, cam_y, view_heading_deg, 0.8)
ax.add_patch(plt.Circle((lens_x, lens_y), 0.12, facecolor="#888888", edgecolor="black", linewidth=0.7, zorder=7))

# 4. Field of view
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
ax.plot([cam_x, fov_right[0]], [cam_y, fov_right[1]], color="green", linewidth=1.5, linestyle="--", zorder=4, label="Camera field of view")

# 5. Draw checkerboard GCPs
for gx, gy in zip(far_gcp_x, far_gcp_y):
    draw_checkerboard(ax, gx, gy, size=0.9, angle_deg=8.0)

for gx, gy in zip(near_gcp_x, near_gcp_y):
    draw_checkerboard(ax, gx, gy, size=0.9, angle_deg=-12.0)

# Legend proxy for checkerboards
ax.plot([], [], color="black", linewidth=2, label="GCP checkerboards")

# 6. Labels
ax.text(cam_x - 0.3, cam_y - 2.0, "Camera", fontsize=10, color="#222222")
# ax.text(far_gcp_x[2], far_gcp_y[2] + 1.1, "Opposite bank: 5 GCPs", ha="center", fontsize=10)
# ax.text(near_gcp_x[1], near_gcp_y[1] - 1.2, "Near shore: 3 GCPs", ha="center", fontsize=10)

# --- Axes styling -------------------------------------------------------
ax.set_xlim(-1, 30)
ax.set_ylim(0, 30)
ax.set_aspect("equal")
ax.set_xlabel("Along-river distance (m)", fontsize=12)
ax.set_ylabel("Across-river distance (m)", fontsize=12)
ax.set_title("River top view: camera setup, field of view and GCP checkerboards", fontsize=12)
ax.grid(True, linestyle=":", alpha=0.4)
ax.legend(loc="lower right", fontsize=11, framealpha=0.85)

plt.tight_layout()
# plt.savefig("top_view_camera_gcps.png", dpi=150, bbox_inches="tight")
plt.show()
