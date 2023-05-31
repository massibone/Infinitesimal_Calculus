from sympy import symbols, limit, oo

# Definizione delle variabili simboliche
x = symbols('x')

# Definizione della funzione
f = (x**2 - 1) / (x - 1)

# Calcolo dei limiti
limit_f_1 = limit(f, x, 1)  # Limit x -> 1

# Output dei risultati
print("Limite di f(x) quando x tende a 1:")
print(limit_f_1)
