import numpy as np
import matplotlib.pyplot as plt

# Definizione dell'equazione differenziale omogenea
def homogeneous_eq(y, t, a, b):
    return -2 * a * y - b * y

# Definizione del dominio t
t = np.linspace(0, 10, 100)

# Parametri dell'equazione differenziale
a = 1.5
b = 2.5

# Risoluzione dell'equazione differenziale omogenea
y_homogeneous = np.exp(-a * t) * (np.cos(np.sqrt(b - a**2) * t) + np.sin(np.sqrt(b - a**2) * t))

# Tracciamento della soluzione
plt.plot(t, y_homogeneous, label='Omogenea')

# Configurazione del grafico
plt.title("Equazione differenziale lineare omogenea")
plt.xlabel("Tempo")
plt.ylabel("y(t)")
plt.legend()

# Mostra il grafico
plt.show()
