from sympy import sin,series,Symbol
import matplotlib.pyplot as plt

x = Symbol('x')
s10 = sin(x).series(x,0,10).removeO()
s20 = sin(x).series(x,0,20).removeO()
s = sin(x)
xx = []
y10 = []
y20 = []
y = []
for i in range(1000):
  xx.append(i / 100.0)
  y10.append(float(s10.subs({x:i/100.0})))
  y20.append(float(s20.subs({x:i/100.0})))
  y.append(float(s.subs({x:i/100.0})))

fig, ax = plt.subplots(figsize=(15, 8))
ax.set_xlabel('x')
ax.set_ylabel('s10, s20, sin(x)')
ax.margins(x=0.,y=0.1)
ax.grid(True)
ax.plot(xx, y10, c='b', label='O(10) sin(x)')
ax.plot(xx, y20, c='r', label='O(20) sin(x)')
ax.plot(xx, y, c='k', label='sin(x)')
ax.set_ylim(-2.,2.)
#ax.legend(fontsize=' x-large ')
ax.legend(fontsize='20')
plt.show()
