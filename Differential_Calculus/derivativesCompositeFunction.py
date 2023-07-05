import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione composta
def f(x):
    return x**2 + 2*x + 1

# Calcolo della derivata della funzione composta
def f_prime(x):
    # Utilizziamo la libreria SymPy per calcolare la derivata simbolicamente
    expr = sp.symbols('x')
    f_expr = f(expr)
    f_prime_expr = sp.diff(f_expr, expr)
    f_prime_func = sp.lambdify(expr, f_prime_expr)
    return f_prime_func(x)

# Intervallo di valori x
x = np.linspace(-5, 5, 100)

# Calcolo dei valori della funzione composta e della sua derivata
y = f(x)
y_prime = f_prime(x)

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, y_prime, label="f'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Funzione composta f(x) e sua derivata f'(x)")
plt.legend()
plt.grid(True)
plt.show()
