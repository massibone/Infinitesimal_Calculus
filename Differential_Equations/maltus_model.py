import numpy as np
import matplotlib.pyplot as plt

def malthus_model(N0, r, t):
    # Calculate the population size at time t using the Malthus model
    N = N0 * np.exp(r * t)
    return N

# Set the initial population size, growth rate, and time range
N0 = 100  # Initial population size
r = 0.02  # Growth rate
t = np.linspace(0, 10, 100)  # Time range from 0 to 10 with 100 points

# Calculate the population size over time
population = malthus_model(N0, r, t)

# Plot the population growth
plt.plot(t, population, 'b-', label='Malthus Model')
plt.title('Malthus Model - Population Growth')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend()
plt.grid(True)
plt.show()
