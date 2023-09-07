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

