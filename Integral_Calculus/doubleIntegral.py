import numpy as np
import matplotlib.pyplot as plt

# Funzione da integrare
def f(x, y):
    return x**2 + y**2

# Definizione dei limiti di integrazione
x_lower = -1
x_upper = 1
y_lower = -1
y_upper = 1

# Calcolo dell'integrale doppio
integral = 0
n = 100  # Numero di divisioni
dx = (x_upper - x_lower) / n
dy = (y_upper - y_lower) / n

for i in range(n):
    for j in range(n):
        x = x_lower + i * dx
        y = y_lower + j * dy
        integral += f(x, y) * dx * dy

print("Integrale doppio:", integral)

# Creazione del grafico dell'integrale doppio
x = np.linspace(x_lower, x_upper, n)
y = np.linspace(y_lower, y_upper, n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('Integrale doppio')

plt.show()

# Calcolo dell'integrale di linea
t = np.linspace(0, 2*np.pi, 100)  # Parametro t per la curva
integral_line = 0

for i in range(len(t) - 1):
    x1 = np.cos(t[i])
    y1 = np.sin(t[i])
    x2 = np.cos(t[i + 1])
    y2 = np.sin(t[i + 1])
    arc_length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    integral_line += f(x2, y2) * arc_length

print("Integrale di linea:", integral_line)

# Creazione del grafico dell'integrale di linea
fig, ax = plt.subplots()
ax.plot(np.cos(t), np.sin(t), 'r', label='Curva')
ax.set_aspect('equal', 'box')
plt.title('Integrale di linea')
plt.legend()
plt.show()
