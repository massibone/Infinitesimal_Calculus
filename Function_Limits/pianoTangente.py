import numpy as np
import matplotlib.pyplot as plt


# Dati per il calcolo del piano tangente
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Punto nel quale calcolare il piano tangente
x0, y0 = 1, 1
z0 = x0**2 + y0**2

# Calcolo del piano tangente
tangent_plane = z0 + 2*(X-x0) + 2*(Y-y0)

# Plot del grafico della funzione e del piano tangente
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5)
ax.plot_surface(X, Y, tangent_plane, alpha=0.5)

# Etichette degli assi
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Titolo del grafico
plt.title('Piano tangente a z = x^2 + y^2 nel punto (1, 1)')

# Visualizzazione del grafico
plt.show()
