import numpy as np
import matplotlib.pyplot as plt

# Definizione dell'equazione logistica (teorema di Verhulst)
def logistic_equation(y, r, K):
    return r * y * (1 - y/K)

# Parametri dell'equazione logistica
r = 2.5  # tasso di crescita
K = 100  # capacità di carico

# Definizione del dominio t
t = np.linspace(0, 10, 100)

# Risoluzione dell'equazione logistica
y0 = 10  # condizione iniziale
y = np.zeros_like(t)
y[0] = y0
for i in range(1, len(t)):
    y[i] = logistic_equation(y[i-1], r, K)

# Tracciamento della soluzione
plt.plot(t, y, label='Soluzione')

# Configurazione del grafico
plt.title("Equazione logistica (Teorema di Verhulst)")
plt.xlabel("Tempo")
plt.ylabel("Popolazione")
plt.legend()

# Mostra il grafico
plt.show()
