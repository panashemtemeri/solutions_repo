## Python Implementation
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the forced damped pendulum equation
def forced_damped_pendulum(t, y, b, A, omega):
    theta, omega_dot = y
    dtheta_dt = omega_dot
    domega_dt = -b * omega_dot - np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Parameters
b = 0.2  # Damping coefficient
A = 1.2  # Driving amplitude
omega = 2/3  # Driving frequency

# Initial conditions
t_span = (0, 100)
y0 = [0.1, 0.0]  # Initial angle and angular velocity
t_eval = np.linspace(*t_span, 2000)

# Solve the differential equation
sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval, args=(b, A, omega))

# Plot the time evolution of theta
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label='Theta (rad)')
plt.xlabel('Time')
plt.ylabel('Theta (rad)')
plt.title('Time Evolution of Forced Damped Pendulum')
plt.legend()
plt.grid()
plt.show()

# Phase portrait
plt.figure(figsize=(6, 6))
plt.plot(sol.y[0], sol.y[1], label='Phase Portrait')
plt.xlabel('Theta (rad)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Phase Space Trajectory')
plt.legend()
plt.grid()
plt.show()
