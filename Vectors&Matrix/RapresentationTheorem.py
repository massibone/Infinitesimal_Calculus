import numpy as np

# Definiamo una trasformazione lineare T: R^2 -> R^2
def T(x):
    return np.array([2*x[0] + x[1], x[0] - 3*x[1]])

# Definiamo una base per lo spazio di partenza (R^2)
e1 = np.array([1, 0])
e2 = np.array([0, 1])
B1 = [e1, e2]

# Definiamo una base per lo spazio di arrivo (R^2)
f1 = np.array([1, 1])
f2 = np.array([1, -1])
B2 = [f1, f2]

# Costruiamo la matrice di rappresentazione di T rispetto alle due basi
M = np.zeros((2, 2))
for i in range(2):
    M[:, i] = T(B1[i])

# Stampa la matrice di rappresentazione
print("Matrice di rappresentazione di T:")
print(M)
