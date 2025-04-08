import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters for the population distributions
population_size = 10000
uniform_low = 0
uniform_high = 10
exponential_scale = 2
binomial_n = 10
binomial_p = 0.5

# Generate population datasets
uniform_population = np.random.uniform(uniform_low, uniform_high, population_size)
exponential_population = np.random.exponential(exponential_scale, population_size)
binomial_population = np.random.binomial(binomial_n, binomial_p, population_size)

# Visualize the population distributions
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(uniform_population, kde=True)
plt.title('Uniform Population Distribution')

plt.subplot(1, 3, 2)
sns.histplot(exponential_population, kde=True)
plt.title('Exponential Population Distribution')

plt.subplot(1, 3, 3)
sns.histplot(binomial_population, kde=True, discrete=True)
plt.title('Binomial Population Distribution')

plt.tight_layout()
plt.savefig('population_distributions.png') # Save the plot as 'population_distributions.png'
plt.show()