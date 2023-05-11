import sympy as sp

# Definiamo la variabile simbolica x
x = sp.Symbol('x')

# Definiamo la funzione
f = (x**2 - 4) / (x - 2)

# Calcoliamo il limite della funzione per x che tende a 2
limit = sp.limit(f, x, 2)

print("Il limite della funzione per x che tende a 2 è:", limit)

# Verifichiamo se la funzione è continua in x = 2
continuity = sp.limit(f, x, 2, dir='+') == sp.limit(f, x, 2, dir='-')

if continuity:
    print("La funzione è continua in x = 2")
else:
    print("La funzione non è continua in x = 2")
