from sympy import symbols, sqrt, oo, limit

# Definizione della variabile simbolica
x = symbols('x')

# Definizione della funzione
f = sqrt(x + 2) - sqrt(x + 5)

# Calcolo del limite
limit_f_inf = limit(f, x, oo)

# Output del risultato
print("Limite di f(x) quando x tende a infinito:")
print(limit_f_inf)
