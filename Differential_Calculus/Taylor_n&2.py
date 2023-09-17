import numpy as np
import matplotlib.pyplot as plt

def taylor_approximation(f, x, a, n):
    approximation = f(a)
    for i in range(1, n+1):
        derivative = (f(a + 1e-6) - f(a)) / 1e-6  # Calcolo della derivata numerica
        approximation += derivative / np.math.factorial(i) * (x-a)**i
        f = lambda x: derivative  # Aggiornamento della funzione con la derivata calcolata
    return approximation
def function(x):
    return np.sin(x)

x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Approssimazione di Taylor di ordine 4
taylor_order_4 = taylor_approximation(function, x, 0, 4)

# Approssimazione di Taylor di ordine 2
taylor_order_2 = taylor_approximation(function, x, 0, 2)
