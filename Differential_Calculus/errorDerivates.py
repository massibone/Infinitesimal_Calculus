import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 3*x + 2

def tangent_line(x, x0):
    return f(x0) + (2*x0 + 3) * (x - x0)

# Intervallo di valori di x
x = np.linspace(-5, 5, 100)

# Punto di valutazione x0
x0 = 2

# Incremento dx
dx = 0.1

# Calcolo delle coordinate dei punti A e B
xA = x0 - dx
yA = f(xA)
xB = x0 + dx
yB = f(xB)

# Calcolo delle coordinate dei punti lungo la retta tangente
xt = np.linspace(xA, xB, 100)
yt = tangent_line(xt, x0)

# Calcolo dell'errore
error = np.abs(yB - yA)

# Creazione del grafico
plt.plot(x, f(x), label='Funzione f(x)')
plt.plot(xt, yt, label='Retta tangente')
plt.scatter([xA, xB], [yA, yB], color='red', label='Punti A e B')
plt.annotate('A', (xA, yA), textcoords="offset points", xytext=(-10,-10), ha='center')
plt.annotate('B', (xB, yB), textcoords="offset points", xytext=(-10,-10), ha='center')
plt.title('Errore nell\'approssimazione')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Stampa dell'errore
plt.text(-4, 20, f'Errore: {error:.2f}', fontsize=12)

# Visualizzazione del grafico
plt.show()
