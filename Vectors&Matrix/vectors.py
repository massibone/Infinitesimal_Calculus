import numpy as np

# Definiamo il vettore di riferimento
v = np.array([1,0,2,0])

# Creiamo una matrice casuale di dimensione (4, n)
n = 10
M = np.random.rand(4,n)

# Calcoliamo l'insieme dei vettori perpendicolari a v
perp = M[:,np.dot(v,M)==0]

# Stampiamo l'insieme dei vettori perpendicolari a v
print("Insieme dei vettori perpendicolari a v:\n", perp)

# Calcoliamo la dimensione del sottospazio generato dagli elementi di perp
dim = np.linalg.matrix_rank(perp)

# Stampiamo la dimensione del sottospazio generato dagli elementi di perp
print("Dimensione del sottospazio generato dagli elementi di perp:", dim)

# Stampiamo il sottospazio generato dagli elementi di perp come combinazione lineare di vettori
if dim > 0:
    print("Sottospazio generato dagli elementi di perp come combinazione lineare di vettori:")
    for i in range(dim):
        print(perp[:,i], "x_", i, sep="")
    print("dove x_0, x_1, ..., x_", dim-1, " sono scalari arbitrari.")
else:
    print("Il sottospazio generato dagli elementi di perp è il vettore nullo.")
