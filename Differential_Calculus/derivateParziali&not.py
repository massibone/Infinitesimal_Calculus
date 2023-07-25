import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione
def f(x, y):
    return x**2 + y**3

# Definizione del dominio della funzione
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calcolo delle derivate parziali
df_dx = 2 * X
df_dy = 3 * Y**2

# Calcolo delle derivate non parziali
delta_x = 0.001
delta_y = 0.001
df_dx_np = (f(X + delta_x, Y) - f(X, Y)) / delta_x
df_dy_np = (f(X, Y + delta_y) - f(X, Y)) / delta_y

# Calcolo della differenza tra derivate parziali e non parziali
diff_dx = np.abs(df_dx - df_dx_np)
diff_dy = np.abs(df_dy - df_dy_np)

# Creazione del grafico delle differenze
plt.subplot(2, 1, 1)
plt.imshow(diff_dx, cmap='hot', origin='lower')
plt.colorbar()
plt.title('Differenza tra derivate parziali e non parziali (x)')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 1, 2)
plt.imshow(diff_dy, cmap='hot', origin='lower')
plt.colorbar()
plt.title('Differenza tra derivate parziali e non parziali (y)')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()

# Visualizzazione del grafico
plt.show()
