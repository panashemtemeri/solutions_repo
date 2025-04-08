import numpy as np
import matplotlib.pyplot as plt

# --- Measurement ---
pendulum_length = 1.255  # Example measurement in meters
length_resolution = 0.001  # meters
uncertainty_length = length_resolution / 2
print(f"Measured Pendulum Length (L): {pendulum_length:.3f} m")
print(f"Uncertainty in Length (δL): {uncertainty_length:.4f} m")

# --- Simulate Data Collection (for demonstration) ---
np.random.seed(42)  # for reproducibility
mean_time_10 = 20.18  # Example mean time
std_dev_time = 0.05   # Example standard deviation
num_measurements = 10
time_measurements_10_oscillations = np.random.normal(mean_time_10, std_dev_time, num_measurements)

formatted_times = [f"{t:.2f}" for t in time_measurements_10_oscillations]
print(f"\nIndividual Time Measurements for 10 Oscillations (t₁₀): {formatted_times} s")

# --- Calculations ---
period = np.mean(time_measurements_10_oscillations) / 10
uncertainty_mean_time_10 = np.std(time_measurements_10_oscillations, ddof=1) / np.sqrt(num_measurements)
uncertainty_period = uncertainty_mean_time_10 / 10

print(f"Period of Oscillation (T): {period:.4f} s")
print(f"Uncertainty in Period (δT): {uncertainty_period:.4f} s")

pi = np.pi
calculated_g = (4 * pi**2 * pendulum_length) / (period**2)
relative_uncertainty_g = np.sqrt((uncertainty_length / pendulum_length)**2 + (2 * uncertainty_period / period)**2)
uncertainty_g = calculated_g * relative_uncertainty_g

print(f"Calculated Gravitational Acceleration (g): {calculated_g:.2f} m/s²")
print(f"Uncertainty in Gravitational Acceleration (δg): {uncertainty_g:.2f} m/s²")

# --- Visualization of Time Measurements ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(time_measurements_10_oscillations, bins='auto', edgecolor='black', alpha=0.7)
ax.axvline(np.mean(time_measurements_10_oscillations), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {np.mean(time_measurements_10_oscillations):.2f} s')
ax.set_xlabel('Time for 10 Oscillations (s)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Time Measurements')
ax.legend()
ax.grid(True, alpha=0.5)

fig.savefig('pendulum_time_distribution.png') # Save the plot
plt.show()