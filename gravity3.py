import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24   # Mass of Earth (kg)
R_earth = 6371e3  # Radius of Earth (m)

# Define a function to simulate the trajectory for different initial conditions
def simulate_trajectory(altitude, initial_velocity):
    initial_position = R_earth + altitude  # Position relative to Earth's center
    v_x = 0  # No velocity in the x-direction
    v_y = initial_velocity  # Tangential velocity in the y-direction

    # Define the system of equations for motion (in polar coordinates)
    def equations(t, state):
        r, theta, v_r, v_theta = state  # r is radial distance, theta is angle, v_r is radial velocity, v_theta is angular velocity
        a_r = -G * M / r**2  # Gravitational acceleration in radial direction
        drdt = v_r
        dthetadt = v_theta / r  # Angular velocity
        dv_rdt = v_theta**2 / r - a_r  # Radial acceleration
        dv_thetadt = 0  # No angular acceleration (no torque in this scenario)
        return [drdt, dthetadt, dv_rdt, dv_thetadt]

    # Initial state vector: [r, theta, v_r, v_theta]
    initial_state = [initial_position, 0, 0, initial_velocity]

    # Time span for the simulation
    t_span = (0, 3600 * 2)  # Simulate for 2 hours
    t_eval = np.linspace(t_span[0], t_span[1], 1000)

    # Solve the system of differential equations
    solution = solve_ivp(equations, t_span, initial_state, t_eval=t_eval)

    # Extract the radial distance (r) and angular position (theta) from the solution
    r = solution.y[0]
    theta = solution.y[1]

    # Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y

# Example 1: Payload released from 500 km altitude with 10000 m/s velocity
altitude1 = 500000  # 500 km above Earth's surface
initial_velocity1 = 10000  # m/s (in the tangential direction)

# Example 2: Payload released from 200 km altitude with 8000 m/s velocity
altitude2 = 200000  # 200 km above Earth's surface
initial_velocity2 = 8000  # m/s (in the tangential direction)

# Example 3: Payload released from 1000 km altitude with 12000 m/s velocity
altitude3 = 1000000  # 1000 km above Earth's surface
initial_velocity3 = 12000  # m/s (in the tangential direction)

# Simulate trajectories for the three examples
x1, y1 = simulate_trajectory(altitude1, initial_velocity1)
x2, y2 = simulate_trajectory(altitude2, initial_velocity2)
x3, y3 = simulate_trajectory(altitude3, initial_velocity3)

# Plot the trajectories of the payload for all three examples
plt.figure(figsize=(10, 8))

# Plotting each trajectory
plt.plot(x1, y1, label="500 km, 10000 m/s")
plt.plot(x2, y2, label="200 km, 8000 m/s")
plt.plot(x3, y3, label="1000 km, 12000 m/s")

# Mark Earth in the center
plt.scatter(0, 0, color='red', label='Earth')

# Add labels and title
plt.title('Trajectory of Freely Released Payloads Near Earth')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Save the plot as an image
plt.savefig('payload_trajectories_comparison.png')

# Show the plot
plt.show()
