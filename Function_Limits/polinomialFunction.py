import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione polinomiale
'''
f(x) = x^3 - 3x^2 + x + 1. 
Gli estremi del dominio della funzione sono a = -2 e b = 4

'''
def f(x):
    return x**3 - 3*x**2 + x + 1

# Definizione degli estremi del dominio della funzione
a = -2
b = 4

# Creazione di un array di valori equispaziati nel dominio della funzione
x = np.linspace(a, b, 1000)

# Calcolo dei limiti della funzione per x che tende a -infinito e a +infinito
lim_inf = -np.inf
lim_sup = np.inf

# Creazione del grafico della funzione e dei suoi limiti
fig, ax = plt.subplots()
ax.plot(x, f(x), label='f(x)')
ax.axhline(lim_inf, color='gray', linestyle='--', label='lim x->-inf')
ax.axhline(lim_sup, color='gray', linestyle='--', label='lim x->+inf')
ax.legend()
plt.show()
