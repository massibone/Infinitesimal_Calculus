import numpy as np
import matplotlib.pyplot as plt

# Definizione dell'equazione differenziale
def separable_equation(y, x):
    return y**2 - x**2

# Definizione del dominio x
x = np.linspace(-5, 5, 100)

# Risoluzione dell'equazione differenziale
y = np.sqrt((x**3)/3 + 5)   # Soluzione dell'equazione differenziale (ottenuta analiticamente)

# Tracciamento della soluzione
plt.plot(x, y, label='Soluzione')

# Configurazione del grafico
plt.title("Equazione differenziale a variabili separabili")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()


# Mostra il grafico
plt.show()
