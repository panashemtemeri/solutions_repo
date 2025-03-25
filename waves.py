import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1.0  # Amplitude of the waves
lambda_ = 1.0  # Wavelength (for simplicity)
k = 2 * np.pi / lambda_  # Wave number
omega = 2 * np.pi  # Angular frequency (for simplicity)
t = 0  # Initial time (can be varied to observe time evolution)
radius = 5  # Radius of the circle around which the sources are placed

# Function to calculate the wave displacement from a single source
def wave_displacement(x, y, source, k, omega, t, A):
    r = np.sqrt((x - source[0])**2 + (y - source[1])**2)  # Distance from source
    return A * np.sin(k * r - omega * t)  # Displacement from this source

# Function to create regular polygons
def generate_polygon(n_sources, radius):
    angles = np.linspace(0, 2*np.pi, n_sources, endpoint=False)
    return np.array([(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles])

# Create grid for the water surface
x_grid, y_grid = np.meshgrid(np.linspace(-8, 8, 200), np.linspace(-8, 8, 200))

# List of different polygons (square, triangle, pentagon)
polygons = [4, 3, 5]
for n_sources in polygons:
    sources = generate_polygon(n_sources, radius)
    
    # Initialize z_grid for this polygon
    z_grid = np.zeros_like(x_grid)
    
    # Superposition of waves from all sources
    for source in sources:
        z_grid += wave_displacement(x_grid, y_grid, source, k, omega, t, A)
    
    # Plotting the interference pattern
    plt.figure(figsize=(8, 6))
    plt.contourf(x_grid, y_grid, z_grid, cmap='RdBu', levels=100)
    plt.colorbar(label='Displacement')
    plt.title(f'Interference Pattern from Waves Emitted by Sources in a {n_sources}-gon')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    
    # Save the plot as an image
    plt.savefig(f'interference_pattern_{n_sources}_gon.png')
    plt.close()  # Close the plot to avoid displaying multiple images at once

print("Images saved successfully.")
