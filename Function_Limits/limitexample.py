import sympy as smp

x, y = smp.symbols('x y')

#limit x -> pi   sin(x/2 + sin(x))
print(smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi))

#limit x ->0+   (2e**1/x)/e**1/x+1
print(smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0,dir='+'))