import numpy as np

# Definiamo il vettore v
v = np.array([1, 0, 2, 0])

# Creiamo una matrice con i vettori standard per fare il prodotto scalare
standard_vectors = np.eye(len(v))

# Usiamo il prodotto scalare per trovare i vettori perpendicolari a v
perp_vectors = [vec for vec in standard_vectors if np.dot(vec, v) == 0]

# Determiniamo la dimensione del sottospazio vettoriale
dim = len(perp_vectors)

# Visualizziamo gli elementi dell'insieme dei vettori perpendicolari
print("Insieme dei vettori perpendicolari:")
for vec in perp_vectors:
  print(vec)

# Visualizziamo la dimensione del sottospazio vettoriale
print("Dimensione del sottospazio vettoriale:", dim)

# Visualizziamo il sottospazio vettoriale come una combinazione lineare dei vettori perpendicolari
print("Sottospazio vettoriale:")
for i, vec in enumerate(perp_vectors):
  print(f"{vec} * x_{i}", end="")
  if i < dim-1:
    print(" + ", end="")
    print()
