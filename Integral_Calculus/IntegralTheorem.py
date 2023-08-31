import numpy as np
import matplotlib.pyplot as plt

def integral_function(x):
    # Define the function for integration here
    return x ** 2  # Example function: x^2

def derivative_function(x):
    # Define the derivative of the function here
    return 2 * x  # Example derivative: 2x

# Define the interval for calculation
a = 0  # Lower limit
b = 2  # Upper limit

# Calculate the definite integral using the integral function
definite_integral = np.linspace(a, b, 100)
integral_values = [integral_function(x) for x in definite_integral]

# Calculate the antiderivative (indefinite integral) using the derivative function
indefinite_integral = np.linspace(a, b, 100)
antiderivative_values = [derivative_function(x) for x in indefinite_integral]

# Plot the definite integral and antiderivative
plt.figure(figsize=(10, 6))

# Plot the definite integral
plt.subplot(2, 1, 1)
plt.plot(definite_integral, integral_values, 'b-', linewidth=2)
plt.fill_between(definite_integral, 0, integral_values, alpha=0.3, color='blue')
plt.title('Definite Integral')
plt.xlabel('x')
plt.ylabel('y')

# Plot the antiderivative (indefinite integral)
plt.subplot(2, 1, 2)
plt.plot(indefinite_integral, antiderivative_values, 'r-', linewidth=2)
plt.title('Antiderivative (Indefinite Integral)')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()
