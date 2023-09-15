import numpy as np
import scipy.integrate as intg
import matplotlib.pyplot as plt

sigma=5.67e-8
qgen=400000 #more for parable function
k=40 # m**-1 K**-1
T1=0
epsilon=0.8
Tsur=500   #+273.15 #convert C to K
L=1
nodes=50
x=np.linspace(0,L,nodes)

def f(x,y):
    return np.vstack((y[1],np.full_like(x,-qgen/k)))

def bc(ya,yb):
    return np.array([ya[0]-T1,k*yb[1]+sigma*epsilon*(yb[0]**4-Tsur**4)])

y0=np.zeros((2,x.size))

solution= intg.solve_bvp(f,bc,x,y0)
T=solution.y[0]
dTdx = solution.y[1]

Ts1=T[0]
