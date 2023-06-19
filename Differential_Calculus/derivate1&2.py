import numpy as np
import matplotlib.pyplot as plt

# Definisci la funzione da analizzare
def funzione(x):
    return np.sin(x)  # Esempio di una funzione (puoi modificarla)

# Definisci l'intervallo di valori di x
x = np.linspace(-10, 10, 1000)

# Calcola la derivata prima
derivata_prima = np.gradient(funzione(x), x)

# Calcola la derivata seconda
derivata_seconda = np.gradient(derivata_prima, x)

# Crea il grafico
fig, axs = plt.subplots(3, 1)

# Grafico della funzione
axs[0].plot(x, funzione(x))
axs[0].set_title('Funzione originale')

# Grafico della derivata prima
axs[1].plot(x, derivata_prima)
axs[1].set_title('Derivata prima')

# Grafico della derivata seconda
axs[2].plot(x, derivata_seconda)
axs[2].set_title('Derivata seconda')

# Mostra il grafico
plt.tight_layout()
plt.show()
