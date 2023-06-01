'''
In this recipe, we will define a symbolic expression that represents the following function:
f(x) = (x**2 − 2x)**e**(3−x)
Then, we will see how to symbolically differentiate and integrate this function.
'''


import sympy

x = sympy.symbols('x')
f = (x**2 - 2*x)*sympy.exp(3 - x)
fp = sympy.simplify(sympy.diff(f))
print(fp)  # (-x**2 + 4*x - 2)*exp(3 - x)

fp2 = (2*x - 2)*sympy.exp(3 - x) - (
    x**2 - 2*x)*sympy.exp(3 - x)

print(sympy.simplify(fp2 - fp) == 0)  # True

F = sympy.integrate(fp, x)
print(F)  # (x**2 - 2*x)*exp(3 - x)
