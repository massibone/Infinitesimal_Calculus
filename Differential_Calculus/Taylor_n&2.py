import numpy as np
import matplotlib.pyplot as plt

def taylor_approximation(f, x, a, n):
    approximation = f(a)
    for i in range(1, n+1):
        derivative = (f(a + 1e-6) - f(a)) / 1e-6  # Calcolo della derivata numerica
        approximation += derivative / np.math.factorial(i) * (x-a)**i
        f = lambda x: derivative  # Aggiornamento della funzione con la derivata calcolata
    return approximation
def function(x):
    return np.sin(x)

x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Approssimazione di Taylor di ordine 4
taylor_order_4 = taylor_approximation(function, x, 0, 4)

# Approssimazione di Taylor di ordine 2
taylor_order_2 = taylor_approximation(function, x, 0, 2)

plt.figure(figsize=(8, 6))
plt.plot(x, function(x), label='Funzione')
plt.plot(x, taylor_order_4, label='Taylor ordine 4')
plt.plot(x, taylor_order_2, label='Taylor ordine 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approssimazione di Taylor')
plt.legend()
plt.grid(True)
plt.show()
