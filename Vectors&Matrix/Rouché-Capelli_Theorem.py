import numpy as np

# Definiamo il sistema di equazioni nella forma Ax = b
A = np.array([[2, 3, -1],
              [4, 1, 0],
              [3, -5, 2],
              [1, -1, 1]])
b = np.array([5, 3, -1, 2])

# Calcoliamo il determinante della matrice dei coefficienti e della matrice estesa
det_A = np.linalg.det(A)
det_Ab = np.linalg.det(np.column_stack((A, b)))

# Applichiamo il Teorema di Rouché-Capelli
if det_A != 0:
    if det_Ab != 0:
        print("Il sistema è determinato.")
    else:
        print("Il sistema è impossibile.")
else:
    if det_Ab == 0:
        print("Il sistema è indeterminato.")
    else:
        print("Il sistema è sovradeterminato.")
