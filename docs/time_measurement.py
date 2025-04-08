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

print(f"Individual Time Measurements for 10 Oscillations (t₁₀): {[f'{t:.2f}' for t in time_measurements_10_oscillations]} s")
print(f"Mean Time for 10 Oscillations (⟨t₁₀⟩): {mean_time_10:.2f} s")
print(f"Standard Deviation of Time Measurements (σ): {standard_deviation_time:.2f} s")
print(f"Uncertainty in Mean Time for 10 Oscillations (δ⟨t₁₀⟩): {uncertainty_mean_time_10:.2f} s")

# Create a simple plot (e.g., a histogram) of the time measurements
plt.figure(figsize=(8, 6))
plt.hist(time_measurements_10_oscillations, bins='auto', edgecolor='black', alpha=0.7)
plt.xlabel('Time for 10 Oscillations (s)')
plt.ylabel('Frequency')
plt.title('Distribution of Time Measurements')
plt.grid(True, alpha=0.5)
plt.savefig('time_measurements_histogram.png') # Save the plot
plt.show()