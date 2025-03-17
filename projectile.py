import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
v0 = 20  # initial velocity in m/s
angles = [30, 45, 60]  # launch angles in degrees
g = 9.81  # acceleration due to gravity in m/s^2

# Time of flight function
def calculate_trajectory(v0, angle):
    angle_rad = np.radians(angle)  # Convert angle to radians
    t_flight = 2 * v0 * np.sin(angle_rad) / g  # Total time of flight
    t = np.linspace(0, t_flight, num=500)  # Time intervals for plotting

    # Horizontal and vertical components of velocity
    vx = v0 * np.cos(angle_rad)
    vy = v0 * np.sin(angle_rad)

    # Calculate the x and y positions at each time step
    x = vx * t
    y = vy * t - 0.5 * g * t**2
    return x, y

# Plot the trajectory for each angle
plt.figure(figsize=(10, 6))
for angle in angles:
    x, y = calculate_trajectory(v0, angle)
    plt.plot(x, y, label=f'{angle}°')

# Labels and title
plt.title('Projectile Motion for Different Angles')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig('projectile_motion.png')  # Save the image to the current directory

# Show the plot
plt.show()
