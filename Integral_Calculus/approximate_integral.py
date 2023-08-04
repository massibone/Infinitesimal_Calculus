import numpy as np
import matplotlib.pyplot as plt

def approximate_integral(function, a, b, n):
    """
    Calcola e restituisce l'approssimazione dell'integrale utilizzando il metodo delle somme rettangolari.

    Parametri:
    - function: la funzione da integrare
    - a: il limite inferiore dell'intervallo di integrazione
    - b: il limite superiore dell'intervallo di integrazione
    - n: il numero di suddivisioni dell'intervallo

    Restituisce:
    - approximation: l'approssimazione dell'integrale
    """

    dx = (b - a) / n  # Larghezza di ogni sottointervallo
    x_vals = np.linspace(a, b, n+1)  # Punti x dei rettangoli
    y_vals = function(x_vals)  # Valori y della funzione

    approximation = np.sum(y_vals) * dx

    return approximation


# Esempio di utilizzo

# Definizione della funzione da integrare
def my_function(x):
    return x ** 2  # Esempio di funzione: x^2

# Parametri dell'integrale approssimato
a = 0  # Limite inferiore dell'intervallo di integrazione
b = 1  # Limite superiore dell'intervallo di integrazione
n = 100  # Numero di suddivisioni dell'intervallo

# Calcolo dell'integrale approssimato
approximation = approximate_integral(my_function, a, b, n)

print(f"Approximation of the integral: {approximation}")


# Plot dell'integrale approssimato come somma di rettangoli
x_vals = np.linspace(a, b, n+1)
y_vals = my_function(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', linewidth=2)
plt.bar(x_vals, y_vals, width=(b-a)/n, alpha=0.5, align='edge', edgecolor='k', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation of Integral using Rectangular Sum')
plt.grid(True)
plt.show()
