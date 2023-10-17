import math

def calculate_exp_series(x, terms):
    result = 0
    for n in range(terms):
        result += (x ** n) / math.factorial(n)
    return result

# Numero di termini nella serie
num_terms = 5

# Valore di x per il quale calcolare la serie (ad esempio, x = 2)
x_value = 2

# Calcola la serie di Taylor per e^x
result = calculate_exp_series(x_value, num_terms)

print(f"Serie di Taylor per e^{x_value} con {num_terms} termini: {result}")
