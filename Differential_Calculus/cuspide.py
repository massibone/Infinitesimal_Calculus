import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.abs(x)**(1/3)

def f_prime(x):
    return np.sign(x) * (1/3) * np.abs(x)**(-2/3)

def cusps():
    # Trova i punti in cui la derivata è indefinita (tangente verticale)
    cusps = []

    # Intervallo di valori x per la ricerca dei punti di tangenza
    x_values = np.linspace(-1, 1, 1000)

    for x in x_values:
        if np.isnan(f_prime(x)):
            cusps.append(x)

    return cusps

# Crea un array di valori x nell'intervallo desiderato
x = np.linspace(-1, 1, 100)

# Calcola i valori della funzione e della derivata prima
y = f(x)
y_prime = f_prime(x)

# Trova i punti di tangenza (cuspidi)
cusps = cusps()

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, y_prime, label="f'(x)")
plt.scatter(cusps, [0] * len(cusps), color='red', label='Punti di tangenza (cuspidi)')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Grafico della funzione e della sua derivata prima")
plt.legend()
plt.grid(True)
plt.show()

