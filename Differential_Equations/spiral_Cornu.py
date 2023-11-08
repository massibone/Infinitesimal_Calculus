'''
La spirale di Cornu, anche conosciuta come spirale di clothoide, è una spirale logaritmica utilizzata nella progettazione di strade, ferrovie e altre infrastrutture di trasporto. La sua caratteristica principale è che la curvatura della spirale aumenta linearmente rispetto alla sua lunghezza, il che la rende utile per collegare una curva costante (cioè una curva circolare) a una retta in modo graduale e senza brusche variazioni di curvatura
'''

import numpy as np
import matplotlib.pyplot as plt

# Parametri della spirale di Cornu
L = 1.0  # Lunghezza totale della spirale
k_max = 2.0  # Curvatura massima

# Numero di punti per la curva
num_points = 1000

# Calcola la spirale di Cornu
s = np.linspace(0, L, num_points)
k = k_max * s / L
x = np.cumsum(np.cos(np.cumsum(k))) * (L / num_points)
y = np.cumsum(np.sin(np.cumsum(k))) * (L / num_points)

# Crea un grafico per visualizzare la spirale di Cornu
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Spirale di Cornu', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Spirale di Cornu')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
