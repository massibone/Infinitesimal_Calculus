import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_limit():
    # Defining the symbolic variable
    x = sp.Symbol('x')

    # Defining the function
    numerator = x**(2/3)
    denominator = x**2 + 3*sp.sqrt(x)**3 + x
    function = numerator / denominator

    # Computing the limit
    real_limit = sp.limit(sp.re(function), x, 0)
    imaginary_limit = sp.limit(sp.im(function), x, 0)

    # Creating an array of x values around 0
    x_values = np.linspace(-0.1, 0.1, 1000)

    # Computing the real and imaginary parts of the function values
    real_values = [sp.re(function.subs(x, val)) for val in x_values]
    imaginary_values = [sp.im(function.subs(x, val)) for val in x_values]

    # Plotting the real part
    plt.subplot(2, 1, 1)
    plt.plot(x_values, real_values, label='Real Part')
    plt.axhline(y=real_limit, color='r', linestyle='--', label='Limit')
    plt.xlabel('x')
    plt.ylabel('Re[f(x)]')
    plt.title('Limit of (x**(2/3))/(x**2 + 3 sqrt(x)**3 + x) as x approaches 0')
    plt.legend()
    plt.grid(True)

    # Plotting the imaginary part
    plt.subplot(2, 1, 2)
    plt.plot(x_values, imaginary_values, label='Imaginary Part')
    plt.axhline(y=imaginary_limit, color='r', linestyle='--', label='Limit')
    plt.xlabel('x')
    plt.ylabel('Im[f(x)]')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Calling the function to plot the limit
plot_limit()
