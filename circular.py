import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.0  # Charge
m = 1.0  # Mass
B = np.array([0, 0, 1])  # Magnetic field (z-direction)
v0 = np.array([1, 0, 0], dtype=float)  # Initial velocity (x-direction)
dt = 0.01  # Use a float value for dt
a = np.array([0, 0, 1], dtype=float)
t_max = 10  # Maximum time

# Initialize position and velocity
r = np.array([0, 0, 0], dtype=float)  # Initial position
v = v0
positions = []

# Simulation loop
for _ in range(int(t_max / dt)):
    F = q * np.cross(v, B)  # Lorentz force
    a = F / m  # Acceleration
    v += a * dt
    r += v * dt
    positions.append(r.copy())

positions = np.array(positions)

# Plot trajectory
plt.figure(figsize=(6,6))
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("Charged Particle in a Uniform Magnetic Field")
plt.grid()

# Save the figure as a PNG file
plt.savefig("particle_trajectory.png")  # Save the plot to a file

# Show the plot
plt.show()
