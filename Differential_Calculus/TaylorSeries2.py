import numpy as np
import matplotlib.pyplot as plt

def taylor_series(function, x0, n, interval):
    """
    Calcola e restituisce l'approssimazione di Taylor della funzione data.

    Parametri:
    - function: la funzione da approssimare
    - x0: il punto di espansione
    - n: il grado massimo dell'approssimazione
    - interval: l'intervallo su cui calcolare l'approssimazione
    
Restituisce:
    - x_vals: i valori dell'ascissa
    - y_vals: i valori dell'approssimazione di Taylor
    """

    x_vals = np.linspace(interval[0], interval[1], 1000)
    y_vals = np.zeros_like(x_vals)

    for i, x in enumerate(x_vals):
        y = 0.0

        for k in range(n + 1):
            # Calcola l'approssimazione di Taylor al grado k
            y += function(x0, k) * (x - x0) ** k / np.math.factorial(k)

        y_vals[i] = y

    return x_vals, y_vals
# Esempio di utilizzo

# Definizione delle funzioni da approssimare

# Funzione esponenziale
def exponential(x0, k):
    return x0 ** k

# Funzione seno
def sine(x0, k):
    if k % 2 == 0:
        return 0.0
    else:
        return (-1) ** ((k - 1) // 2) / np.math.factorial(k)
