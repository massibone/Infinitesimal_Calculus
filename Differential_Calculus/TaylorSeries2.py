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

# Funzione logaritmo
def logarithm(x0, k):
    if k == 0:
        return np.log(x0)
    else:
        return (-1) ** (k - 1) * (k - 1) / (x0 ** k)

# Parametri dell'approssimazione di Taylor
x0 = 1.0  # Punto di espansione
n = 5     # Grado massimo dell'approssimazione

# Intervallo su cui calcolare l'approssimazione
interval = (0.1, 2.0)

# Calcolo dell'approssimazione di Taylor per le funzioni
x_vals_exp, y_vals_exp = taylor_series(exponential, x0, n, interval)
x_vals_sin, y_vals_sin = taylor_series(sine, x0, n, interval)
x_vals_log, y_vals_log = taylor_series(logarithm, x0, n, interval)

# Plot delle approssimazioni di Taylor
plt.figure(figsize=(10, 6))
plt.plot(x_vals_exp, y_vals_exp, label='e^x')
plt.plot(x_vals_sin, y_vals_sin, label='sin(x)')
plt.plot(x_vals_log, y_vals_log, label='log(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Approssimazione di Taylor di grado {n}')
plt.legend()
plt.grid(True)
plt.show()
