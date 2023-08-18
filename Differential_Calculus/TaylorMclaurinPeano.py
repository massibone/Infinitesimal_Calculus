import numpy as np
import matplotlib.pyplot as plt

def taylor_approximation(f, x, n):
    approximation = 0
    for i in range(n+1):
        approximation += f(0, i) * x**i / np.math.factorial(i)
    return approximation

def function(x, n):
    return x**n

x = np.linspace(-2, 2, 100)
n = 4

plt.figure(figsize=(8, 6))
plt.plot(x, function(x, n), label='Funzione')
plt.plot(x, taylor_approximation(function, x, n), label='Approssimazione di Taylor')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approssimazione di Taylor-Maclaurin')
plt.legend()
plt.grid(True)
plt.show()
