import numpy as np
import matplotlib.pyplot as plt

# Definizione della parametrizzazione del toro
def torus_param(u, v):
    R = 3  # Raggio maggiore del toro
    r = 1  # Raggio minore del toro
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    return x, y, z

# Parametri per la griglia
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 2*np.pi, 100)
U, V = np.meshgrid(u, v)

# Calcolo delle coordinate x, y, z del toro
X, Y, Z = torus_param(U, V)

# Calcolo delle derivate parziali rispetto a u e v
R = 3  # Raggio maggiore del toro
r = 1  # Raggio minore del toro

dx_du = -(R + r * np.cos(V)) * np.sin(U)
dx_dv = -r * np.sin(V) * np.cos(U)

dy_du = (R + r * np.cos(V)) * np.cos(U)
dy_dv = -r * np.sin(V) * np.sin(U)

dz_du = np.zeros_like(U)
dz_dv = r * np.cos(V)

# Matrice jacobiana
J = np.array([[dx_du, dx_dv],
              [dy_du, dy_dv],
              [dz_du, dz_dv]])

# Visualizzazione della matrice jacobiana
fig, ax = plt.subplots(3, 2, figsize=(8, 12))

ax[0, 0].imshow(dx_du, cmap='hot', origin='lower')
ax[0, 0].set_title('dx/du')

ax[0, 1].imshow(dx_dv, cmap='hot', origin='lower')
ax[0, 1].set_title('dx/dv')

ax[1, 0].imshow(dy_du, cmap='hot', origin='lower')
ax[1, 0].set_title('dy/du')

ax[1, 1].imshow(dy_dv, cmap='hot', origin='lower')
ax[1, 1].set_title('dy/dv')

ax[2, 0].imshow(dz_du, cmap='hot', origin='lower')
ax[2, 0].set_title('dz/du')

ax[2, 1].imshow(dz_dv, cmap='hot', origin='lower')
ax[2, 1].set_title('dz/dv')

plt.tight_layout()
plt.show()
