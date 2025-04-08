import numpy as np
import matplotlib.pyplot as plt

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

num_drops_list = [100, 1000, 10000, 100000]
estimates_buffon = []
# Calculate estimates outside the plotting loop for efficiency
for n in num_drops_list:
    pi_est, _ = estimate_pi_buffon(n)
    estimates_buffon.append(pi_est)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(num_drops_list, estimates_buffon, marker='o')
ax.axhline(np.pi, color='r', linestyle='--', label='True Pi')
ax.set_xlabel('Number of Needle Drops')
ax.set_ylabel('Estimated Pi')
ax.set_title('Convergence of Pi Estimate (Buffon\'s Needle)')
ax.set_xscale('log')
ax.legend()
ax.grid(True)

fig.savefig('buffon_needle_convergence.png') # Save the plot
plt.show()