import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.exp(x)

def f2(x):
    return x**3

def tangent_line(f, x0):
    # Calcola la pendenza della retta tangente
    slope = f_prime(x0)

    # Calcola il termine noto dell'equazione della retta
    y_intercept = f(x0) - slope * x0

    # Restituisce la funzione della retta tangente
    return lambda x: slope * x + y_intercept

def f_prime(x):
    # Calcola la derivata della funzione f(x)
    return np.exp(x)  # Derivata di f1(x)

# Punto di ascissa x = 2
x0 = 2

# Funzione f1(x) e sua retta tangente
x_values = np.linspace(0, 4, 100)
y_values = f1(x_values)
tangent_f1 = tangent_line(f1, x0)
tangent_values_f1 = tangent_f1(x_values)

# Funzione f2(x) e sua retta tangente
y_values_f2 = f2(x_values)
tangent_f2 = tangent_line(f2, x0)
tangent_values_f2 = tangent_f2(x_values)

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f1(x) = e^x')
plt.plot(x_values, tangent_values_f1, label='Tangente a f1(x)')
plt.plot(x_values, y_values_f2, label='f2(x) = x^3')
plt.plot(x_values, tangent_values_f2, label='Tangente a f2(x)')
plt.scatter(x0, f1(x0), color='red', label='Punto di tangenza (x0, f1(x0))')
plt.scatter(x0, f2(x0), color='blue', label='Punto di tangenza (x0, f2(x0))')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Equazione della retta tangente ai punti di tangenza')
plt.legend()
plt.grid(True)
plt.show()
