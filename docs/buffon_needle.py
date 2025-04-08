import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def estimate_pi_buffon(num_drops, needle_length=1, line_spacing=1):
    """Estimates pi using Buffon's Needle method."""
    crossings = 0
    for _ in range(num_drops):
        # Random position of the needle's center
        y_center = np.random.uniform(0, line_spacing)
        # Random angle of the needle (0 to pi)
        angle = np.random.uniform(0, np.pi)
        # Vertical distance from the center to the ends of the needle
        half_length_proj = (needle_length / 2) * np.sin(angle)

        if y_center - half_length_proj < 0 or y_center + half_length_proj > line_spacing:
            crossings += 1

    if crossings > 0:
        pi_estimate = (2 * needle_length * num_drops) / (line_spacing * crossings)
    else:
        pi_estimate = np.inf  # Avoid division by zero
    return pi_estimate, crossings

def visualize_buffon(num_needles, needle_length=1, line_spacing=1):
    """Visualizes Buffon's Needle drops."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hlines(np.arange(0, 3 * line_spacing, line_spacing), -1, 2, colors='black', linestyles='dashed')
    crossings_visual = 0
    for _ in range(num_needles):
        y_center = np.random.uniform(0, line_spacing)
        angle = np.random.uniform(0, np.pi)
        x_center = np.random.uniform(0, 1)  # Center x for visualization
        dx = (needle_length / 2) * np.cos(angle)
        dy = (needle_length / 2) * np.sin(angle)
        y1 = y_center - dy
        y2 = y_center + dy

        crossed = False
        if (y1 < 0 and y2 > 0) or (y1 < line_spacing and y2 > line_spacing) or \
           (y1 < 2 * line_spacing and y2 > 2 * line_spacing):
            crossed = True
            crossings_visual += 1
            color = 'red'
        else:
            color = 'blue'

        ax.plot([x_center - dx, x_center + dx], [y1, y2], color=color, linewidth=1)

    if crossings_visual > 0:
        estimated_pi_visual = (2 * needle_length * num_needles) / (line_spacing * crossings_visual)
        ax.set_title(f"Buffon's Needle Simulation ({num_needles} drops)\nEstimated Pi (Visual) = {estimated_pi_visual:.4f}")
    else:
        ax.set_title(f"Buffon's Needle Simulation ({num_needles} drops)\nNo Crossings Observed")

    ax.set_xlabel("x-position")
    ax.set_ylabel("y-position")
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 2.5 * line_spacing)
    ax.set_aspect('equal', adjustable='box')
    fig.savefig('buffon_needle_visualization.png') # Save the plot
    plt.show()

num_drops = 10000
estimated_pi_buffon, num_crosses = estimate_pi_buffon(num_drops)
print(f"Estimated Pi (Buffon's Needle, {num_drops} drops): {estimated_pi_buffon}")
print(f"Number of Crossings: {num_crosses}")

# Visualize a subset of the drops
visualize_buffon(50)