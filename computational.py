import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the forced damped pendulum equation
def forced_damped_pendulum(t, y, b, A, omega):
    theta, omega_dot = y
    dtheta_dt = omega_dot
    domega_dt = -b * omega_dot - np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Function to simulate and plot results
def simulate_pendulum(b, A, omega, y0, t_span, title):
    t_eval = np.linspace(*t_span, 2000)
    sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval, args=(b, A, omega))
    
    plt.figure(figsize=(10, 5))
    plt.plot(sol.t, sol.y[0], label='Theta (rad)')
    plt.xlabel('Time')
    plt.ylabel('Theta (rad)')
    plt.title(f'Time Evolution: {title}')
    plt.legend()
    plt.grid()
    plt.savefig(f'{title.lower().replace(" ", "_")}_time_evolution.png')
    plt.show()
    
    plt.figure(figsize=(6, 6))
    plt.plot(sol.y[0], sol.y[1], label='Phase Portrait')
    plt.xlabel('Theta (rad)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.title(f'Phase Space: {title}')
    plt.legend()
    plt.grid()
    plt.savefig(f'{title.lower().replace(" ", "_")}_phase_portrait.png')
    plt.show()

# Example simulations with different parameter variations
examples = [
    (0.2, 1.2, 2/3, [0.1, 0.0], (0, 100), 'Moderate Damping and Forcing'),
    (0.1, 1.5, 2/3, [0.1, 0.0], (0, 100), 'Low Damping, High Forcing'),
    (0.5, 0.5, 2/3, [0.1, 0.0], (0, 100), 'High Damping, Low Forcing'),
    (0.2, 1.2, 1.5, [0.1, 0.0], (0, 100), 'Higher Driving Frequency'),
    (0.05, 2.0, 2/3, [0.2, 0.0], (0, 100), 'Weak Damping, Strong Forcing'),
    (0.3, 0.8, 1.2, [0.05, 0.0], (0, 100), 'Moderate Damping and Moderate Forcing'),
    (0.4, 1.0, 0.8, [0.1, 0.0], (0, 100), 'Higher Damping, Lower Frequency'),
    (0.1, 2.5, 2/3, [0.3, 0.0], (0, 100), 'Extreme Forcing with Low Damping'),
]

for params in examples:
    simulate_pendulum(*params)



