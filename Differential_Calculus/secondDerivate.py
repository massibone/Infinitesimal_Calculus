import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Definisci la tua funzione qui
    return np.sin(x) + 0.5 * x

def f_prime(x):
    # Calcola la derivata prima della tua funzione
    return np.cos(x) + 0.5

def f_double_prime(x):
    # Calcola la derivata seconda della tua funzione
    return -np.sin(x)

# Crea un array di valori x nell'intervallo desiderato
x = np.linspace(-5, 5, 100)

# Calcola i valori della funzione, derivata prima e derivata seconda
y = f(x)
y_prime = f_prime(x)
y_double_prime = f_double_prime(x)

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, y_prime, label="f'(x)")
plt.plot(x, y_double_prime, label="f''(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Grafico della funzione, derivata prima e derivata seconda")
plt.legend()
plt.grid(True)
plt.show()
