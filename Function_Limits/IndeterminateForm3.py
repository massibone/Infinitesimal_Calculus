import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos, cot, lambdify

# Definizione della variabile simbolica
x = symbols('x')

# Definizione della funzione
f = (1 - cos(2*x)) * cot(x)

# Creazione di una funzione numpy per il grafico
f_np = lambdify(x, f, 'numpy')

# Generazione dei valori x
x_vals = np.linspace(-10, 10, 1000)

# Calcolo dei valori y corrispondenti
y_vals = f_np(x_vals)

# Creazione del grafico
plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafico di f(x) = (1 - cos(2x)) * cot(x)')
plt.grid(True)
plt.show()
