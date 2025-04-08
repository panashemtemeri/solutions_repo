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
plt.figure(figsize=(8, 8))
plt.scatter(points[inside, 0], points[inside, 1], color='blue', s=1, label='Inside Circle')
plt.scatter(points[~inside, 0], points[~inside, 1], color='red', s=1, label='Outside Circle')
circle = plt.Circle((0, 0), 1, edgecolor='black', facecolor='none')
plt.gca().add_patch(circle)
plt.title(f'Estimating Pi (Circle, {num_iterations} points)\nEstimated Pi = {estimated_pi:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.savefig('monte_carlo_pi_circle_plot.png') # Save the plot
plt.show()