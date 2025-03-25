import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24   # Mass of Earth (kg)

# Define orbital radii (in meters)
radii = np.linspace(7e6, 4.2e7, 10)  # From 7000 km to 42000 km

# Calculate orbital periods using Kepler's Third Law
periods = np.sqrt((4 * np.pi**2 * radii**3) / (G * M))

# Convert periods to hours
periods_hours = periods / 3600

# --- First Plot: T^2 vs. r^3 (Kepler's Third Law) ---
plt.figure(figsize=(8,6))
plt.plot(radii**3, periods**2, 'o-', label="Kepler's Law")
plt.xlabel('Orbital Radius Cubed (m³)')
plt.ylabel('Orbital Period Squared (s²)')
plt.title("Verification of Kepler's Third Law")
plt.legend()
plt.grid(True)
plt.savefig('keplers_third_law_plot.png')  # Save the first plot
plt.show()

# --- Second Plot: Orbital Period vs. Orbital Radius ---
plt.figure(figsize=(8,6))
plt.plot(radii, periods, 's-', label="Orbital Period")
plt.xlabel('Orbital Radius (m)')
plt.ylabel('Orbital Period (s)')
plt.title("Orbital Period vs. Orbital Radius")
plt.legend()
plt.grid(True)
plt.savefig('orbital_period_vs_radius.png')  # Save the second plot
plt.show()

# --- Third Plot: Orbital Period (in hours) vs. Orbital Radius ---
plt.figure(figsize=(8,6))
plt.plot(radii, periods_hours, '^-', label="Orbital Period (hours)")
plt.xlabel('Orbital Radius (m)')
plt.ylabel('Orbital Period (hours)')
plt.title("Orbital Period (hours) vs. Orbital Radius")
plt.legend()
plt.grid(True)
plt.savefig('orbital_period_hours_vs_radius.png')  # Save the third plot
plt.show()
