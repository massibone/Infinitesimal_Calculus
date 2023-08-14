import numpy as np
import matplotlib.pyplot as plt

def f(x, A, T):
    return (2 * A / T) * np.abs(x)

def f_prime(x, A, T):
    return np.sign(x) * (2 * A / T)

# Parametri della funzione
A = 1.5  # Amplitude
T = 4.0  # Period

# Crea un array di valori x nell'intervallo desiderato
x = np.linspace(-T/2, T/2, 1000)

# Calcola i valori della funzione f(x) e della sua derivata f'(x)
y = f(x, A, T)
y_prime = f_prime(x, A, T)

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, y_prime, label="f'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funzione periodica f(x) e sua derivata')
plt.legend()
plt.grid(True)
plt.show()
