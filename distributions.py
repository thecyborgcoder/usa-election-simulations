import numpy as np
import random
import matplotlib.pyplot as plt

# Number of samples
n = 50000
samples = []

# Combined distribution
for _ in range(n):
    normal_sample = np.random.normal(0.5, 0.2)
    normal_sample_clipped = max(0, min(1, normal_sample))
    uniform_sample = np.random.random()
    combined_sample = (normal_sample_clipped + uniform_sample) / 2
    samples.append(combined_sample)

# Two random variables
# for _ in range(n):
#     sample = random.random() * random.random()
#     samples.append(sample)

# Plotting the distribution
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g')
plt.title('Combined Distribution')
plt.xlabel('Value')
plt.ylabel('Percentage')
plt.show()