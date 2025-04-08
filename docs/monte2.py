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

num_iterations = 10000
estimated_pi, points, inside = estimate_pi_circle(num_iterations)
print(f"Estimated Pi (Circle, {num_iterations} points): {estimated_pi}")

# Visualization
fig, ax = plt.subplots(figsize=(8, 8))  # Create figure and axes object

ax.scatter(points[inside, 0], points[inside, 1], color='blue', s=1, label='Inside Circle')
ax.scatter(points[~inside, 0], points[~inside, 1], color='red', s=1, label='Outside Circle')

circle = plt.Circle((0, 0), 1, edgecolor='black', facecolor='none')
ax.add_patch(circle)

ax.set_title(f'Estimating Pi (Circle, {num_iterations} points)\nEstimated Pi = {estimated_pi:.4f}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal', adjustable='box')
ax.legend()

fig.savefig('monte_carlo_pi_circle.png') # Save the plot using the figure object
plt.show()