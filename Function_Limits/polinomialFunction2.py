import numpy as np
import matplotlib.pyplot as plt

# Definizione delle funzioni polinomiali
def f(x):
    return x**3 - 4*x + 5

def g(x):
    return x**3

# Definizione degli estremi del dominio della funzione
a = -10
b = 10

# Creazione di un array di valori equispaziati nel dominio delle funzioni
x = np.linspace(a, b, 1000)

# Calcolo dei limiti delle funzioni per x che tende a +infinito
lim_f = np.inf
lim_g = np.inf

# Creazione del grafico delle funzioni e dei loro limiti
fig, ax = plt.subplots()
ax.plot(x, f(x), label='f(x) = x^3 - 4x + 5')
ax.plot(x, g(x), label='g(x) = x^3')
ax.axhline(lim_f, color='gray', linestyle='--', label='lim x->+inf f(x)')
ax.axhline(lim_g, color='gray', linestyle='--', label='lim x->+inf g(x)')
ax.legend()
plt.show()
