


import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Definizione della funzione
def f(x):
    return 1 / np.sqrt(1 - 0.9 * np.sin(x)**2)

# Calcola l'integrale definito della funzione f(x) da 0 a pi (o ad altri limiti, se necessario)
result, _ = quad(f, 0, np.pi)

print("Risultato dell'integrale definito:", result)

# Creazione di un array di valori x per il grafico
x = np.linspace(0, 2 * np.pi, 1000)
y = f(x)

# Plot della funzione
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafico della funzione")
plt.grid(True)

plt.show()
