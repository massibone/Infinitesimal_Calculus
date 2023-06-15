import numpy as np
import matplotlib.pyplot as plt

# Definizione delle funzioni
def f1(x, y):
    return x * y * np.exp(-x**2 - y**2)

def f2(x, y):
    return x * y**2 * np.exp(-x**4 - y**2)

# Definizione del dominio delle funzioni
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calcolo dei valori delle funzioni
Z1 = f1(X, Y)
Z2 = f2(X, Y)

# Individuazione dei punti di massimo e minimo
min1 = np.unravel_index(np.argmin(Z1), Z1.shape)
max1 = np.unravel_index(np.argmax(Z1), Z1.shape)

min2 = np.unravel_index(np.argmin(Z2), Z2.shape)
max2 = np.unravel_index(np.argmax(Z2), Z2.shape)

# Creazione del grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.imshow(Z1, cmap='cool', origin='lower', extent=[-2, 2, -2, 2])
ax1.plot(min1[1]/100, min1[0]/100, 'ro', label='Minimo')
ax1.plot(max1[1]/100, max1[0]/100, 'bo', label='Massimo')
ax1.set_title('f(x, y) = xy e^(-x^2 - y^2)')
ax1.legend()

ax2.imshow(Z2, cmap='cool', origin='lower', extent=[-2, 2, -2, 2])
ax2.plot(min2[1]/100, min2[0]/100, 'ro', label='Minimo')
ax2.plot(max2[1]/100, max2[0]/100, 'bo', label='Massimo')
ax2.set_title('f(x, y) = xy^2 e^(-x^4 - y^2)')
ax2.legend()

plt.tight_layout()

# Visualizzazione del grafico
plt.show()
