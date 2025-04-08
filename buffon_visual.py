import numpy as np
import matplotlib.pyplot as plt

def visualize_buffon(num_visualizations, needle_length=1, line_spacing=1):
    """Visualizes Buffon's Needle drops."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hlines(np.arange(0, 3 * line_spacing, line_spacing), -1, 2, colors='black', linestyles='dashed')
    crossings = 0
    for _ in range(num_visualizations):
        y_center = np.random.uniform(0, line_spacing)
        angle = np.random.uniform(0, np.pi)
        x_center = np.random.uniform(0, 1)  # Center x for visualization
        dx = (needle_length / 2) * np.cos(angle)
        dy = (needle_length / 2) * np.sin(angle)
        y1 = y_center - dy
        y2 = y_center + dy

        crossed = (y1 < 0 < y2) or \
                  (y1 < line_spacing < y2) or \
                  (y1 < 2 * line_spacing < y2)

        if crossed:
            crossings += 1
            color = 'red'
        else:
            color = 'blue'

        ax.plot([x_center - dx, x_center + dx], [y1, y2], color=color, linewidth=1)

    if crossings > 0:
        estimated_pi = (2 * needle_length * num_visualizations) / (line_spacing * crossings)
        ax.set_title(f"Buffon's Needle Simulation ({num_visualizations} drops)\nEstimated Pi = {estimated_pi:.4f}")
    else:
        ax.set_title(f"Buffon's Needle Simulation ({num_visualizations} drops)\nNo Crossings Observed")

    ax.set_xlabel("x-position")
    ax.set_ylabel("y-position")
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 2.5 * line_spacing)
    ax.set_aspect('equal', adjustable='box')
    fig.savefig('buffon_needle_visualization.png') # Save the plot
    plt.show()

visualize_buffon(50)