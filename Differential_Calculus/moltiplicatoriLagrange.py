import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione da ottimizzare
def f(x, y):
    return x**2 + y**2

# Definizione delle restrizioni
def g(x, y):
    return x + y - 1

# Generazione di punti nel dominio
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Valori della funzione e delle restrizioni
Z_f = f(X, Y)
Z_g = g(X, Y)

# Calcolo dei punti di ottimizzazione
constraint = np.abs(Z_g) < 0.1
optimal_points = np.logical_and(constraint, Z_f == np.min(Z_f[constraint]))

# Creazione del grafico
plt.contour(X, Y, Z_f, levels=20, colors='blue', alpha=0.5)
plt.contour(X, Y, Z_g, levels=[0], colors='red', linestyles='dashed')
plt.scatter(X[optimal_points], Y[optimal_points], color='green', label='Punto di ottimizzazione')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metodo dei moltiplicatori di Lagrange')
plt.legend()

# Visualizzazione del grafico
plt.show()
