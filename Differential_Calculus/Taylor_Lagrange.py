import numpy as np
import matplotlib.pyplot as plt

def taylor_lagrange(function, x0, n, interval):
    """
    Calcola e restituisce l'approssimazione di Taylor della funzione data con il resto secondo Lagrange.
    
Parametri:
    - function: la funzione da approssimare
    - x0: il punto di espansione
    - n: il grado massimo dell'approssimazione
    - interval: l'intervallo su cui calcolare l'approssimazione

    Restituisce:
    - x_vals: i valori dell'ascissa
    - y_vals: i valori dell'approssimazione di Taylor
    - r_vals: i valori del resto secondo Lagrange
    """

    x_vals = np.linspace(interval[0], interval[1], 1000)
    y_vals = np.zeros_like(x_vals)
    r_vals = np.zeros_like(x_vals)

    for i, x in enumerate(x_vals):
        y = 0.0
        r = 0.0
        for k in range(n + 1):
            # Calcola l'approssimazione di Taylor al grado k
            y += function(x0) * (x - x0) ** k / np.math.factorial(k)

            if k == n:
                # Calcola il resto secondo Lagrange al grado k
                r = np.abs(function(x) - y)

        y_vals[i] = y
        r_vals[i] = r

    return x_vals, y_vals, r_vals


# Esempio di utilizzo
