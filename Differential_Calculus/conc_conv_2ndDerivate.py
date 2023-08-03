import numpy as np
import matplotlib.pyplot as plt

# Definisci la funzione da analizzare
def funzione(x):
    return x**3 - 6*x**2 + 9*x + 2  # Esempio di una funzione (puoi modificarla)

# Definisci l'intervallo di valori di x
x = np.linspace(-5, 5, 1000)

# Calcola la derivata seconda
derivata_seconda = np.gradient(np.gradient(funzione(x), x), x)

# Trova gli intervalli di concavità e convessità
intervalli_concavita = np.where(derivata_seconda < 0)
intervalli_convessita = np.where(derivata_seconda > 0)

# Crea il grafico
fig, ax = plt.subplots()

# Grafico della funzione
ax.plot(x, funzione(x), label='Funzione')
ax.set_title('Funzione originale')

# Aggiungi indicatori per la concavità e la convessità
ax.fill_between(x, funzione(x), where=derivata_seconda < 0, color='red', alpha=0.3, label='Concavità')
ax.fill_between(x, funzione(x), where=derivata_seconda > 0, color='green', alpha=0.3, label='Convessità')

# Mostra la legenda
ax.legend()

# Mostra il grafico
plt.tight_layout()
plt.show()
