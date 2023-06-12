import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione complessa
def complex_function(z):
    return z**2

# Generazione di valori di input complessi
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Calcolo dei valori della funzione complessa
W = complex_function(Z)

# Tracciamento della parte reale della funzione complessa
plt.subplot(121)
plt.imshow(W.real, extent=[-2, 2, -2, 2], cmap='RdYlBu')
plt.colorbar(label='Parte reale')
plt.title('Parte reale della funzione complessa')

# Tracciamento della parte immaginaria della funzione complessa
plt.subplot(122)
plt.imshow(W.imag, extent=[-2, 2, -2, 2], cmap='RdYlBu')
plt.colorbar(label='Parte immaginaria')
plt.title('Parte immaginaria della funzione complessa')

# Configurazione degli assi
plt.subplots_adjust(wspace=0.4)
plt.xlabel('Parte reale')
plt.ylabel('Parte immaginaria')

# Mostra il grafico
plt.show()
