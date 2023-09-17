import numpy as np
import matplotlib.pyplot as plt

def taylor_approximation(f, x, a, n):
    approximation = f(a)
    for i in range(1, n+1):
        derivative = (f(a + 1e-6) - f(a)) / 1e-6  # Calcolo della derivata numerica
        approximation += derivative / np.math.factorial(i) * (x-a)**i
        f = lambda x: derivative  # Aggiornamento della funzione con la derivata calcolata
    return approximation
