import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity (m/s^2)
v0 = 20   # Initial velocity (m/s)
angles = [30, 45, 60]  # Different launch angles
t = np.linspace(0, 4, num=100)  # Time array

# Plot trajectories for different angles
plt.figure(figsize=(8, 5))

for theta in angles:
    theta_rad = np.radians(theta)
    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)

    x = v0x * t
    y = v0y * t - 0.5 * g * t**2

    plt.plot(x, y, label=f'θ = {theta}°')

plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Motion for Different Angles')
plt.legend()
plt.grid()
plt.show()

plt.savefig("projectile_motion.png")  # Save plot as an image

