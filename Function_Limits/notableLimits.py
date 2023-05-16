import sympy as sym

# definiamo la variabile indipendente x
x = sym.Symbol('x')

# calcoliamo il limite di (sin(x))/x per x che tende a 0
limit_sin = sym.limit(sym.sin(x) / x, x, 0)

# calcoliamo il limite di (1-cos(x))/x^2 per x che tende a 0
limit_cos = sym.limit((1 - sym.cos(x)) / x**2, x, 0)

# calcoliamo il limite di (e^x - 1)/x per x che tende a 0
limit_exp = sym.limit((sym.exp(x) - 1) / x, x, 0)

# calcoliamo il limite di log(1+x)/x per x che tende a 0
limit_log = sym.limit(sym.log(1 + x) / x, x, 0)

# stampiamo i risultati
print("Il limite di sin(x)/x per x che tende a 0 è:", limit_sin)
print("Il limite di (1-cos(x))/x^2 per x che tende a 0 è:", limit_cos)
print("Il limite di (e^x - 1)/x per x che tende a 0 è:", limit_exp)
print("Il limite di log(1+x)/x per x che tende a 0 è:", limit_log)
