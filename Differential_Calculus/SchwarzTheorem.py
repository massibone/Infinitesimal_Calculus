import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione
def f(x, y):
    return x**3 + 2*x*y + y**3

# Definizione del dominio della funzione
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calcolo delle derivate miste
d2f_dxdy = np.gradient(np.gradient(f(X, Y), x, axis=1), y, axis=0)
d2f_dydx = np.gradient(np.gradient(f(X, Y), y, axis=0), x, axis=1)

# Creazione del grafico delle derivate miste
plt.subplot(2, 1, 1)
plt.imshow(d2f_dxdy, cmap='hot', origin='lower')
plt.colorbar()
plt.title('Derivata mista d^2f/dxdy')

plt.subplot(2, 1, 2)
plt.imshow(d2f_dydx, cmap='hot', origin='lower')
plt.colorbar()
plt.title('Derivata mista d^2f/dydx')

plt.tight_layout()

# Visualizzazione del grafico
plt.show()
