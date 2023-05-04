import numpy as np

# Definiamo due punti sulla retta
p1 = np.array([1, 2, 3])
p2 = np.array([4, 5, 6])

# Calcoliamo il vettore direzione della retta
v = p2 - p1

# Definiamo un punto generico sulla retta
p = np.array([0, 0, 0])

# Calcoliamo il parametro t della retta
t = np.dot((p - p1), v) / np.dot(v, v)

# Calcoliamo il punto sulla retta corrispondente al parametro t
q = p1 + t*v

# Stampa del risultato
print(f"L'equazione parametrica della retta è:\n x = {p1[0]} + {t}*({p2[0]} - {p1[0]})\n y = {p1[1]} + {t}*({p2[1]} - {p1[1]})\n z = {p1[2]} + {t}*({p2[2]} - {p1[2]})\n")
print(f"Il punto sulla retta corrispondente al parametro t è:\n ({q[0]}, {q[1]}, {q[2]})")
