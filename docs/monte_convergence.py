import numpy as np
import matplotlib.pyplot as plt

def estimate_pi_circle(num_points):
    """Estimates pi using the Monte Carlo method with a circle."""
    points = np.random.uniform(-1, 1, size=(num_points, 2))
    distances_squared = np.sum(points**2, axis=1)
    inside_circle = distances_squared <= 1
    num_inside = np.sum(inside_circle)
    pi_estimate = 4 * (num_inside / num_points)
    return pi_estimate, points, inside_circle

num_points_list = [100, 1000, 10000, 100000, 1000000]
estimates = []

# Calculate estimates more efficiently outside the plotting loop
for n in num_points_list:
    pi_est, _, _ = estimate_pi_circle(n)
    estimates.append(pi_est)

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(num_points_list, estimates, marker='o')
ax.axhline(np.pi, color='r', linestyle='--', label='True Pi')
ax.set_xlabel('Number of Points')
ax.set_ylabel('Estimated Pi')
ax.set_title('Convergence of Pi Estimate (Circle)')
ax.set_xscale('log')
ax.legend()
ax.grid(True)

fig.savefig('monte_carlo_pi_circle_convergence.png') # Save the plot
plt.show()