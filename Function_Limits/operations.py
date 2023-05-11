import sympy as sym
x = sym.Symbol('x')

# definiamo la funzione
f = sym.Function('f')(x)

# calcoliamo il limite della funzione in x che tende a 2
limit_x2 = sym.limit(f, x, 2)

# calcoliamo il limite della funzione in x che tende a 3
limit_x3 = sym.limit(f, x, 3)

# calcoliamo la somma dei limiti
sum_limits = limit_x2 + limit_x3

# calcoliamo il prodotto dei limiti
prod_limits = limit_x2 * limit_x3

# calcoliamo il rapporto dei limiti
ratio_limits = limit_x2 / limit_x3

# stampiamo i risultati
print("Il limite della funzione in x che tende a 2 è:", limit_x2)
print("Il limite della funzione in x che tende a 3 è:", limit_x3)
print("La somma dei limiti è:", sum_limits)
print("Il prodotto dei limiti è:", prod_limits)
print("Il rapporto dei limiti è:", ratio_limits)
