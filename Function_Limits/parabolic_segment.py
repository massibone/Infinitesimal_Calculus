import matplotlib.pyplot as plt
import numpy as np
import random


def rec():
    x = list(np.arange(-15, 16, 1))
    y = [-35, 35]

    y0 = []
    for xv in x:
        p = (xv, y[0])
        y0.append(p)

    y1 = []
    for xv in x:
        q = (xv, y[-1])
        y1.append(q)

    # plt.plot(x_val, y_val)
    x_range = [elx[0] for elx in y0]
    y_nve = [ely[1] for ely in y0]

    # plt.plot(x_val, y_val)
    y_pve = [ely[1] for ely in y1]

    return x, x_range, y_nve, y_pve


def parabolic_ins():
    x, x_range, y_nve, y_pve = rec()
    nl = []
    xr = []
    for xp, yp in zip(x, y_pve):
        if -7 <= xp <= 7:
            a = 1
            b = 0
            c = 2
            yc = yp
            yp = a * (xp ** 2)  # yp value should not cross 35 so that parabola doesn't shift with corner edge
            if yp <= yc:
                nl.append(yp)
                xr.append(xp)
            print(nl, xr)
        else:
            nl.append(yp)
            xr.append(xp)
    nk = [-x for x in nl]
    aa = xr + xr
    bb = nl + nk

    plt.plot(aa, bb)
    # plt.axis([x_range, nl])
    plt.show()


parabolic_ins()
