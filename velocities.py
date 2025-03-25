import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # Mass of the Sun (kg)

# Masses and radii of Earth, Mars, Jupiter, Venus, Saturn, Mercury, Uranus, and Neptune (in SI units)
celestial_bodies = {
    'Earth': {'M': 5.972e24, 'R': 6.371e6},  # Mass and radius of Earth
    'Mars': {'M': 0.64171e24, 'R': 3.396e6},  # Mass and radius of Mars
    'Jupiter': {'M': 1.898e27, 'R': 6.991e7},  # Mass and radius of Jupiter
    'Venus': {'M': 4.867e24, 'R': 6.0518e6},  # Mass and radius of Venus
    'Saturn': {'M': 5.683e26, 'R': 5.8232e7},  # Mass and radius of Saturn
    'Mercury': {'M': 0.33011e24, 'R': 2.4397e6},  # Mass and radius of Mercury
    'Uranus': {'M': 8.681e25, 'R': 2.5362e7},  # Mass and radius of Uranus
    'Neptune': {'M': 1.024e26, 'R': 2.4622e7}  # Mass and radius of Neptune
}

# Calculate the first, second, and third cosmic velocities for each body
def calculate_velocities(body):
    M = body['M']
    R = body['R']
    
    # First cosmic velocity (orbital velocity)
    v1 = np.sqrt(G * M / R)
    
    # Second cosmic velocity (escape velocity)
    v2 = np.sqrt(2 * G * M / R)
    
    # Third cosmic velocity (solar escape velocity)
    # Using Earth's values for simplicity in this calculation
    R_sun = 1.496e11  # Average distance from Earth to Sun in meters
    v3 = np.sqrt((2 * G * M_sun / R_sun) + (v2**2 / 2))
    
    return v1, v2, v3

# Create a figure for the velocities
fig, ax = plt.subplots(figsize=(12,8))

# Loop over celestial bodies and calculate velocities
for body_name, body in celestial_bodies.items():
    v1, v2, v3 = calculate_velocities(body)
    
    # Plot the velocities for each body
    ax.plot([1, 2, 3], [v1, v2, v3], label=body_name)

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['First Cosmic Velocity', 'Second Cosmic Velocity', 'Third Cosmic Velocity'])
ax.set_xlabel('Cosmic Velocities')
ax.set_ylabel('Velocity (m/s)')
ax.set_title('Escape and Cosmic Velocities for Earth, Mars, Jupiter, Venus, Saturn, Mercury, Uranus, and Neptune')
ax.legend()
ax.grid(True)

# Save the first plot as an image
plt.savefig('cosmic_velocities_combined.png')

# Show the first plot
plt.show()

# Create individual plots for each velocity type

# First Cosmic Velocity Plot
plt.figure(figsize=(12, 8))
for body_name, body in celestial_bodies.items():
    v1, _, _ = calculate_velocities(body)
    plt.plot(body_name, v1, 'o', label=body_name)

plt.xlabel('Celestial Bodies')
plt.ylabel('First Cosmic Velocity (m/s)')
plt.title('First Cosmic Velocities (Orbital Velocities) for Celestial Bodies')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('first_cosmic_velocity.png')
plt.show()

# Second Cosmic Velocity Plot
plt.figure(figsize=(12, 8))
for body_name, body in celestial_bodies.items():
    _, v2, _ = calculate_velocities(body)
    plt.plot(body_name, v2, 'o', label=body_name)

plt.xlabel('Celestial Bodies')
plt.ylabel('Second Cosmic Velocity (Escape Velocity) (m/s)')
plt.title('Second Cosmic Velocities (Escape Velocities) for Celestial Bodies')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('second_cosmic_velocity.png')
plt.show()

# Third Cosmic Velocity Plot
plt.figure(figsize=(12, 8))
for body_name, body in celestial_bodies.items():
    _, _, v3 = calculate_velocities(body)
    plt.plot(body_name, v3, 'o', label=body_name)

plt.xlabel('Celestial Bodies')
plt.ylabel('Third Cosmic Velocity (Solar Escape Velocity) (m/s)')
plt.title('Third Cosmic Velocities (Solar Escape Velocities) for Celestial Bodies')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('third_cosmic_velocity.png')
plt.show()
