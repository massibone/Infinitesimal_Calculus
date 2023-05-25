import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione razionale
def f(x):
    return (x**2 - 3*x + 2) / (x - 2)

# Definizione degli estremi del dominio della funzione
a = -4
b = 4

# Creazione di un array di valori equispaziati nel dominio della funzione
x = np.linspace(a, b, 1000)

# Calcolo dei limiti della funzione per x che tende a 2 e a +/-infinito
lim_2 = np.inf
lim_inf = -np.inf
lim_sup = np.inf

# Creazione del grafico della funzione e dei suoi limiti
fig, ax = plt.subplots()
ax.plot(x, f(x), label='f(x)')
ax.axvline(2, color='gray', linestyle='--', label='x = 2')
ax.axhline(lim_2, color='gray', linestyle='--', label='lim x->2')
ax.axhline(lim_inf, color='gray', linestyle='--', label='lim x->-inf')
ax.axhline(lim_sup, color='gray', linestyle='--', label='lim x->+inf')
ax.legend()
plt.show()
