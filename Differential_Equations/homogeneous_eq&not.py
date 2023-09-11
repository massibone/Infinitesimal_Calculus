import numpy as np
import matplotlib.pyplot as plt

# Definizione dell'equazione differenziale omogenea
def homogeneous_eq(y, t):
    return -2 * y

# Definizione dell'equazione differenziale non omogenea
def non_homogeneous_eq(y, t):
    return -2 * y + np.sin(t)

# Definizione del dominio t
t = np.linspace(0, 10, 100)

# Risoluzione dell'equazione differenziale omogenea
y_homogeneous = np.exp(-2 * t)

# Risoluzione dell'equazione differenziale non omogenea
y_non_homogeneous = np.exp(-2 * t) - 0.4 * np.cos(t) + 0.2 * np.sin(t)

# Tracciamento delle soluzioni
plt.plot(t, y_homogeneous, label='Omogenea')
plt.plot(t, y_non_homogeneous, label='Non omogenea')

# Configurazione del grafico
plt.title("Equazioni differenziali omogenee e non omogenee")
plt.xlabel("Tempo")
plt.ylabel("y(t)")
plt.legend()

# Mostra il grafico
plt.show()
