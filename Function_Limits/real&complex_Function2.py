import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione complessa
def complex_function(z):
    return np.sin(z) / z

# Generazione di valori di input complessi
x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Calcolo dei valori della funzione complessa
W = complex_function(Z)

# Tracciamento della parte reale della funzione complessa
plt.subplot(131)
plt.imshow(W.real, extent=[-10, 10, -10, 10], cmap='gray')
plt.colorbar(label='Valore')
plt.title('Parte reale della funzione complessa')

# Tracciamento della parte immaginaria della funzione complessa
plt.subplot(132)
plt.imshow(W.imag, extent=[-10, 10, -10, 10], cmap='gray')
plt.colorbar(label='Valore')
plt.title('Parte immaginaria della funzione complessa')

# Tracciamento del modulo della funzione complessa
plt.subplot(133)
plt.imshow(np.abs(W), extent=[-10, 10, -10, 10], cmap='gray')
plt.colorbar(label='Valore')
plt.title('Modulo della funzione complessa')

# Configurazione degli assi
plt.subplots_adjust(wspace=0.4)
plt.xlabel('Parte reale')
plt.ylabel('Parte immaginaria')

# Mostra il grafico
plt.show()
