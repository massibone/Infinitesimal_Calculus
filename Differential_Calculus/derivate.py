import sympy as sp

# Definisci la variabile simbolica x
x = sp.Symbol('x')

# Definisci la funzione f(x) = radice terza di x
f = x**(1/3)

# Calcola la derivata di f(x)
f_prime = sp.diff(f, x)

# Valuta la derivata in x = 8
result = f_prime.subs(x, 8)

print("Derivata di f(x) =", f_prime)
print("Derivata valutata in x = 8:", result)
