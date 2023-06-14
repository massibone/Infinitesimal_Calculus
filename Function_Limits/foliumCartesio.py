import numpy as np
import matplotlib.pyplot as plt

# Generazione dei valori di t
t = np.linspace(-2, 2, 100)

# Calcolo dei valori di x e y
x = t*(t-1)
y = t*(t-1)*(2*t-1)

# Creazione del grafico
plt.plot(x, y)

# Etichette degli assi
plt.xlabel('x')
plt.ylabel('y')

# Titolo del grafico
plt.title('Folium di Cartesio')

# Visualizzazione del grafico
plt.show()
