'''
Il metodo di Cramer si basa sulla regola di Laplace per il calcolo del determinante di una matrice. Il programma prende in input i coefficienti delle variabili e il termine noto del sistema di equazioni lineari, e restituisce i valori delle variabili che soddisfano il sistema.
'''
def determinant(matrix):
    # Calcola il determinante di una matrice quadrata
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(len(matrix)):
            submatrix = [row[1:] for row in matrix[1:]]
            det += (-1) ** j * matrix[0][j] * determinant(submatrix)
        return det

def cramer(matrix, b):
    # Risolve un sistema di equazioni lineari utilizzando il metodo di Cramer
    n = len(matrix)
    x = [0] * n
    detA = determinant(matrix)

    
    for i in range(n):
        # Costruisce la matrice con la i-esima colonna sostituita dal vettore dei termini noti
        submatrix = [matrix[j].copy() for j in range(n)]
        for j in range(n):
            submatrix[j][i] = b[j]
        
        # Calcola il determinante della matrice con la i-esima colonna sostituita dal vettore dei termini noti
        detAi = determinant(submatrix)
        
        # Calcola il valore della i-esima incognita
        x[i] = detAi / detA
    
    return x
'''
# Esempio di utilizzo
matrix = [[2, 1, -1], [4, -1, 1], [-2, 5, 2]]
b = [3, 9, -1]
x = cramer(matrix, b)
print(x)  # output atteso: [1.0, 2.0, -2.0]
'''
