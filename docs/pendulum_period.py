import numpy as np
import matplotlib.pyplot as plt

time_measurements_10_oscillations = np.array([
    20.15, 20.22, 20.08, 20.18, 20.25,
    20.11, 20.20, 20.16, 20.23, 20.19
]) # Example measurements in seconds
num_measurements = len(time_measurements_10_oscillations)

mean_time_10 = np.mean(time_measurements_10_oscillations)
standard_deviation_time = np.std(time_measurements_10_oscillations, ddof=1) # Use ddof=1 for sample standard deviation
uncertainty_mean_time_10 = standard_deviation_time / np.sqrt(num_measurements)

period = mean_time_10 / 10
uncertainty_period = uncertainty_mean_time_10 / 10
print(f"Period of Oscillation (T): {period:.3f} s")
print(f"Uncertainty in Period (δT): {uncertainty_period:.3f} s")

# Create a simple plot (e.g., showing the period with error bars)
plt.figure(figsize=(6, 4))
plt.errorbar(1, period, yerr=uncertainty_period, fmt='o', capsize=5, label='Period')
plt.ylabel('Period (s)')
plt.title('Calculated Period with Uncertainty')
plt.xticks([]) # Remove x-axis ticks
plt.legend()
plt.grid(True, alpha=0.5)
plt.savefig('pendulum_period_uncertainty.png') # Save the plot
plt.show()