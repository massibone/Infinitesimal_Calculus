import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import scipy as sp
import sympy as smp

x, a, b, c = smp.symbols('x a b c', real=True)

f = smp.exp(a*smp.sin(x**2)) * smp.cos(b**x) * smp.atan(c*smp.sin(x) /x)
dfdx = smp.diff(f, x)

dfdx = smp.diff(f, x)
dfdx2 = smp.diff(f, x, 4)
dfdx2Function = smp.lambdify((x,a,b,c), dfdx2)

x = np.linspace(1,2,100)
y = dfdx2Function(x, a=1, b=2, c=3)
