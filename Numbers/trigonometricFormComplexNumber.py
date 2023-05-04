import cmath


z = complex(3**0.5, 1)

# Calcoliamo il modulo e l'angolo (fase) del numero complesso
r = abs(z)
theta = cmath.phase(z)

# risultato in forma trigonometrica
print(f"{r:.2f}(cos({theta:.2f}) + i sin({theta:.2f}))")



'''
Risultato:
2.00(cos(30.00) + i sin(30.00))

che indica che il numero complesso √3 + i è rappresentabile in forma trigonometrica come 
2(cos(30°) + i sin(30°)).
'''
