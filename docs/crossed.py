import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.0  # Charge
m = 1.0  # Mass
B = np.array([0, 0, 1])  # Magnetic field in z-direction
E = np.array([1, 0, 0])  # Electric field in x-direction
dt = 0.01  # Time step
t_max = 10  # Maximum time

# Initialize
r = np.array([0, 0, 0], dtype=float)
v = np.array([0, 1, 0], dtype=float)  # Initial velocity in y-direction
positions = []

# Simulation loop
for _ in range(int(t_max / dt)):
    F = q * (E + np.cross(v, B))  # Lorentz force with crossed fields
    a = F / m  # Acceleration
    v += a * dt  # Update velocity
    r += v * dt  # Update position
    positions.append(r.copy())

positions = np.array(positions)

# Plot trajectory
plt.figure(figsize=(6,6))
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("Charged Particle in Crossed Electric and Magnetic Fields")
plt.grid()

# Save the figure as a PNG file
plt.savefig("crossed_fields_trajectory.png")  # Save the plot to a file

# Show the plot
plt.show()
