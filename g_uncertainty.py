import numpy as np
import matplotlib.pyplot as plt

# --- Measurement ---
pendulum_length = 1.255  # Example measurement (replace with your value)
length_resolution = 0.001
uncertainty_length = length_resolution / 2

time_measurements_10_oscillations = np.array([
    20.15, 20.22, 20.08, 20.18, 20.25,
    20.11, 20.20, 20.16, 20.23, 20.19
]) # Example data (replace with your values)
num_measurements = len(time_measurements_10_oscillations)
mean_time_10 = np.mean(time_measurements_10_oscillations)
standard_deviation_time = np.std(time_measurements_10_oscillations, ddof=1)
uncertainty_mean_time_10 = standard_deviation_time / np.sqrt(num_measurements)

period = mean_time_10 / 10
uncertainty_period = uncertainty_mean_time_10 / 10

# --- Calculation of g ---
pi = np.pi
calculated_g = (4 * pi**2 * pendulum_length) / (period**2)
print(f"Calculated Gravitational Acceleration (g): {calculated_g:.2f} m/s²")

# --- Uncertainty Propagation ---
relative_uncertainty_g = np.sqrt((uncertainty_length / pendulum_length)**2 + (2 * uncertainty_period / period)**2)
uncertainty_g = calculated_g * relative_uncertainty_g
print(f"Uncertainty in Gravitational Acceleration (δg): {uncertainty_g:.2f} m/s²")

# --- Visualization ---
plt.figure(figsize=(6, 4))
plt.errorbar(calculated_g, 1, xerr=uncertainty_g, fmt='o', capsize=5, label='g') # Swapped x and y for horizontal error bar
plt.xlabel('Gravitational Acceleration (m/s²)')
plt.title('Calculated g with Uncertainty')
plt.yticks([])  # Remove y-axis ticks
plt.legend()
plt.grid(True, alpha=0.5)
plt.savefig('g_uncertainty.png')
plt.show()