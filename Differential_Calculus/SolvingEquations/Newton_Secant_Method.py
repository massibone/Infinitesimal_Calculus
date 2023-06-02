from scipy import optimize

from math import exp
def f(x):
  return x*(x - 2)*exp(3 - x)

#The derivative of this function was computed in:
def fp(x):
  return -(x**2 - 4*x + 2)*exp(3 - x)

optimize.newton(f, 1, fprime=fp) # Using the Newton-Raphson method (2.0)

optimize.newton(f, 1., x1=1.5) # Using x1 = 1.5 and thesecant method (1.999999)
