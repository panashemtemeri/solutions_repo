import numpy as np
import matplotlib.pyplot as plt

# Assume pendulum_length and period are already calculated
pendulum_length = 1.255  # Example value (replace with your actual value)
period = 2.018       # Example value (replace with your actual value)

calculated_g = (4 * np.pi**2 * pendulum_length) / (period**2)
print(f"Calculated Gravitational Acceleration (g): {calculated_g:.2f} m/s²")

# Create a simple plot (e.g., a bar showing the calculated g)
plt.figure(figsize=(4, 6))
plt.bar(['Calculated g'], [calculated_g], color='skyblue')
plt.ylabel('Acceleration (m/s²)')
plt.title('Calculated Gravitational Acceleration')
plt.grid(axis='y', alpha=0.7)
plt.savefig('calculated_g.png') # Save the plot
plt.show()