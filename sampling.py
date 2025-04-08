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

populations = {
    'Uniform': uniform_population,
    'Exponential': exponential_population,
    'Binomial': binomial_population
}

sample_sizes = [5, 10, 30, 50]
num_samples = 1000

fig, axes = plt.subplots(len(populations), len(sample_sizes) + 1, figsize=(18, 12))

for i, (pop_name, population) in enumerate(populations.items()):
    # Plot the population distribution
    sns.histplot(population, kde=True, ax=axes[i, 0])
    axes[i, 0].set_title(f'{pop_name} Population')

    # Plot the sampling distributions for different sample sizes
    for j, sample_size in enumerate(sample_sizes):
        sample_means = [np.mean(np.random.choice(population, sample_size, replace=True)) for _ in range(num_samples)]
        sns.histplot(sample_means, kde=True, ax=axes[i, j + 1])
        axes[i, j + 1].set_title(f'Sample Means (n={sample_size})')

plt.tight_layout()
plt.savefig('clt_simulation.png')  # Save the plot
plt.show()