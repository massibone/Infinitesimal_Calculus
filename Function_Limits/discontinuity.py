import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione


def f(x):
    return (1 / x)


# Creazione di un array di valori x
x = np.linspace(-10, 10, 1000)

# Calcolo dei valori di y corrispondenti
y = f(x)

# Individuazione dei punti di discontinuità
discontinuity_first = [0]  # Punto di discontinuità di prima specie
discontinuity_second = []  # Punti di discontinuità di seconda specie
discontinuity_third = []  # Punti di discontinuità di terza specie

for i in range(len(x) - 1):
    if abs(y[i] - y[i + 1]) > 10:  # Condizione per la discontinuità di seconda specie
        discontinuity_second.append((x[i] + x[i + 1]) / 2)
    # Condizione per la discontinuità di terza specie
    elif np.isnan(y[i]) or np.isnan(y[i + 1]):
        discontinuity_third.append((x[i] + x[i + 1]) / 2)

# Creazione del grafico
plt.plot(x, y, label='f(x)')
plt.scatter(discontinuity_first, [0] * len(discontinuity_first),
            color='red', marker='o', label='Discontinuità di prima specie')
plt.scatter(discontinuity_second, [0] * len(discontinuity_second),
            color='green', marker='o', label='Discontinuità di seconda specie')
plt.scatter(discontinuity_third, [0] * len(discontinuity_third),
            color='blue', marker='o', label='Discontinuità di terza specie')
plt.ylim(-10, 10)  # Limiti dell'asse y
plt.axhline(0, color='black', linewidth=0.5)  # Asse x
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Punti di discontinuità')
plt.legend()
plt.grid(True)

# Visualizzazione del grafico
plt.show()
