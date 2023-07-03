import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione
def f(x):
    return np.sin(x)

# Definizione del dominio della funzione
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = f(x)

# Calcolo delle derivate successive
df = np.gradient(y, x)
d2f = np.gradient(df, x)
d3f = np.gradient(d2f, x)

# Calcolo delle approssimazioni successive
approx_df = np.diff(y) / np.diff(x)
approx_d2f = np.diff(approx_df) / np.diff(x[:-1])
approx_d3f = np.diff(approx_d2f) / np.diff(x[:-2])

# Aggiunta di valori fittizi per le approssimazioni
x_approx = x[:-1]
x_approx_d2 = x[:-2]

# Creazione del grafico delle differenze
plt.subplot(2, 1, 1)
plt.plot(x, df, label='Derivata reale')
plt.plot(x_approx, approx_df, label='Approssimazione derivata')
plt.legend()
plt.title('Differenza tra derivata reale e approssimazione (1° ordine)')

plt.subplot(2, 1, 2)
plt.plot(x, d2f, label='Derivata seconda reale')
plt.plot(x_approx_d2, approx_d2f, label='Approssimazione derivata seconda')
plt.legend()
plt.title('Differenza tra derivata seconda reale e approssimazione (2° ordine)')

plt.tight_layout()

# Visualizzazione del grafico
plt.show()
