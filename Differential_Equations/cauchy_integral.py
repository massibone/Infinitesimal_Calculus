import numpy as np
import matplotlib.pyplot as plt

# Funzione per calcolare l'integrale complesso
def cauchy_integral(z, f, radius, num_points=500):
    theta = np.linspace(0, 2 * np.pi, num_points)
    points = z + radius * np.exp(1j * theta)
    values = f(points)
    integral = np.sum(values) * (2 * np.pi * radius) / num_points
    return integral
# Funzione complessa di esempio
def complex_function(z):
    return np.exp(-z) / (1 + z**2)

# Parametri per il calcolo dell'integrale
center = 0 + 0j  # Centro del cerchio di integrazione
radius = 2  # Raggio del cerchio di integrazione

# Calcolo dell'integrale
integral = cauchy_integral(center, complex_function, radius)

# Tracciamento del cerchio di integrazione
theta = np.linspace(0, 2 * np.pi, 100)
circle_x = center.real + radius * np.cos(theta)
circle_y = center.imag + radius * np.sin(theta)

plt.plot(circle_x, circle_y, color='b', label='Cerchio di integrazione')

# Tracciamento della funzione complessa
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y
W = complex_function(Z)

plt.contourf(X, Y, W.real, levels=20, cmap='RdYlBu')
plt.colorbar(label='Parte reale')

# Etichette degli assi e del titolo
plt.xlabel('Parte reale')
plt.ylabel('Parte immaginaria')
plt.title('Teorema di Cauchy')

# Mostra l'integrale calcolato come testo nel grafico
plt.text(0.1, -4.5, f'Integrale = {integral:.4f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Mostra il grafico
plt.legend()
plt.grid(True)
plt.show()
