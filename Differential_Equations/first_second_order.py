import numpy as np
import matplotlib.pyplot as plt
# Definizione dell'equazione lineare del primo ordine
def first_order_eq(y, t):
    return -0.5 * y

# Definizione dell'equazione lineare del secondo ordine
def second_order_eq(y, t):
    return -0.5 * y - 2 * np.sin(t)

# Definizione del dominio t
t = np.linspace(0, 10, 100)

# Risoluzione dell'equazione lineare del primo ordine
y_first_order = np.exp(-0.5 * t)

# Risoluzione dell'equazione lineare del secondo ordine
y_second_order = np.exp(-0.5 * t) + np.sin(t)

# Tracciamento delle soluzioni
plt.plot(t, y_first_order, label='Primo ordine')
plt.plot(t, y_second_order, label='Secondo ordine')

# Configurazione del grafico
plt.title("Equazioni lineari del primo e secondo ordine")
plt.xlabel("Tempo")
plt.ylabel("y(t)")
plt.legend()

# Mostra il grafico
plt.show()
