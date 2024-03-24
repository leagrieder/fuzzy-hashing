import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
mean = 3480
std_dev = 1734

# Generate data points for the x-axis
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

# Calculate the corresponding probability density function (PDF) values
pdf = (1/(std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5*((x - mean) / std_dev)**2)

# Plot the Gaussian distribution
plt.plot(x, pdf, color='blue', label='Gaussian Distribution')

# Add a vertical line at the mean value
plt.axvline(x=mean, color='red', linestyle='--', label='Mean')

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.title('Gaussian Distribution (μ=3480, σ=1734)')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
