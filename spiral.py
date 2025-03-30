import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.0  # Charge
m = 1.0  # Mass
B = np.array([0, 0, 1])  # Magnetic field (z-direction)
v0 = np.array([1, 1, 1], dtype=float)  # Initial velocity (x and z components)
dt = 0.01  # Time step
t_max = 10  # Maximum time

# Initialize position and velocity
r = np.array([0, 0, 0], dtype=float)
v = v0
positions = []

# Simulation loop
for _ in range(int(t_max / dt)):
    F = q * np.cross(v, B)
    a = F / m
    v += a * dt
    r += v * dt
    positions.append(r.copy())

positions = np.array(positions)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_zlabel("Z position")
ax.set_title("Helical Motion in a Magnetic Field")

# Save the figure as a PNG file
plt.savefig("helical_motion.png")  # Save the plot to a file

# Show the plot
plt.show()
