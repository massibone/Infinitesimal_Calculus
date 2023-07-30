import numpy as np
import matplotlib.pyplot as plt

# Funzione per calcolare l'integrale complesso
def cauchy_integral(z, f, radius, num_points=500):
    theta = np.linspace(0, 2 * np.pi, num_points)
    points = z + radius * np.exp(1j * theta)
    values = f(points)
    integral = np.sum(values) * (2 * np.pi * radius) / num_points
    return integral
