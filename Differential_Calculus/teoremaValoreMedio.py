'''
Il Teorema del Valor Medio (TVM) delle derivate afferma quanto segue:

Supponiamo che una funzione f(x) sia continua sull'intervallo chiuso [a, b] 
e derivabile sull'intervallo aperto (a, b).
Allora esiste almeno un punto c in (a, b) tale che 
la derivata istantanea f'(c) della funzione nel punto c è uguale 
al rapporto incrementale medio della funzione sull'intervallo [a, b].

'''

import sympy as sp

# Definizione della variabile e delle funzioni
x = sp.Symbol('x')
f = sp.Function('f')(x)

# Definizione dell'intervallo [a, b]
a = 0
b = 2

# Calcolo della derivata di f
df = sp.diff(f, x)

# Calcolo del valore medio di f sull'intervallo [a, b]
valor_medio = (f.subs(x, b) - f.subs(x, a)) / (b - a)

# Verifica delle conseguenze del Teorema del Valor Medio

# Conseguenza 1: Se f è continua sull'intervallo [a, b] e derivabile su (a, b),
# allora esiste almeno un punto c in (a, b) tale che f'(c) = valor_medio
conseguenza_1 = sp.solveset(df - valor_medio, x, domain=sp.Interval.open(a, b))

# Conseguenza 2: Se f'(x) > 0 per ogni x in (a, b), allora f è strettamente crescente sull'intervallo [a, b]
conseguenza_2 = df > 0


# Stampa dei risultati
print("Teorema del Valor Medio:")
print("Il valore medio di f(x) sull'intervallo [a, b] è:", valor_medio)
print("Conseguenza 1 del TVM: Esiste almeno un punto c in (a, b) tale che f'(c) = valor_medio.")
print("Soluzioni per c:", conseguenza_1)
print("Conseguenza 2 del TVM: Se f'(x) > 0 per ogni x in (a, b), allora f è strettamente crescente sull'intervallo [a, b].")
print("La funzione f'(x) è strettamente positiva sull'intervallo [a, b]:", conseguenza_2)

#SOLUTION
'''
Teorema del Valor Medio:
Il valore medio di f(x) sull'intervallo [a, b] è: -f(0)/2 + f(2)/2
Conseguenza 1 del TVM: Esiste almeno un punto c in (a, b) tale che f'(c) = valor_medio.      
Soluzioni per c: ConditionSet(x, Eq(f(0)/2 - f(2)/2 + Derivative(f(x), x), 0), Interval.open(0, 2))
Conseguenza 2 del TVM: Se f'(x) > 0 per ogni x in (a, b), allora f è strettamente crescente sull'intervallo [a, b].
La funzione f'(x) è strettamente positiva sull'intervallo [a, b]: Derivative(f(x), x) > 0 
'''

