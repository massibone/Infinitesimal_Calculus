import numpy as np
import matplotlib.pyplot as plt

def func(x,A,B):
    return A*x**2+B*x

xlist = np.linspace(0,10,100)
ylist = func(xlist,2,1.4)

plt.figure(1,dpi=120)
plt.plot(xlist,ylist,label="Function")

def D(xlist,ylist):
    yprime = np.diff(ylist)/np.diff(xlist)
    xprime=[]
    for i in range(len(yprime)):
        xtemp = (xlist[i+1]+xlist[i])/2
        xprime = np.append(xprime,xtemp)
    return xprime, yprime

xprime, yprime = D(xlist,ylist)
plt.plot(xprime,yprime,label="Derivative")

xprime2, yprime2 = D(xprime,yprime)
plt.plot(xprime2,yprime2,label="2nd Derivative")
plt.legend()
plt.show()