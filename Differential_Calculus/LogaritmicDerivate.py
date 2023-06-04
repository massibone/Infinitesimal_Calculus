import sympy as sp
#Definizione della variabile e della funzione

x = sp.Symbol('x')

f = sp.log(x)

# Calcolo della derivata logaritmica (elasticità)

elasticita = sp.diff(f, x) / f

# Stampa la derivata logaritmica (elasticità)

print(f"Derivata logaritmica (elasticità) di f(x) = log(x):")

print(elasticita)
