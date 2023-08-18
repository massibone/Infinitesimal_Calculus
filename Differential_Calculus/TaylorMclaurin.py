import numpy as np
import matplotlib.pyplot as plt

# Definisci la funzione per cui calcolare la serie di Taylor-Maclaurin
def funzione(x):
    return np.sin(x)  # Esempio di una funzione (puoi modificarla)

# Definisci il punto in cui calcolare la serie di Taylor-Maclaurin
punto = np.pi / 4

# Definisci l'intervallo di valori di x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Calcola i termini della serie di Taylor-Maclaurin
termine_0 = funzione(punto)
termine_1 = funzione(punto) * (x - punto)
termine_2 = funzione(punto) * (x - punto)**2 / 2

# Calcola la serie di Taylor-Maclaurin del secondo ordine
serie_taylor = termine_0 + termine_1 + termine_2

# Crea il grafico
fig, ax = plt.subplots()

# Grafico della funzione originale
ax.plot(x, funzione(x), label='Funzione originale')

# Grafico della serie di Taylor-Maclaurin del secondo ordine
ax.plot(x, serie_taylor, label='Serie di Taylor-Maclaurin (ordine 2)')

# Mostra la legenda
ax.legend()

# Mostra il grafico
plt.tight_layout()
plt.show()
