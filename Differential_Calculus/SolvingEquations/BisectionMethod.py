#not so fast method

from math import copysign
def bisect(f, a, b, tol=1e-5):
    """Bisection method for root finding"""
    fa, fb = f(a), f(b)
    assert not copysign(fa, fb) == fa, "Function must change
signs"
    while (b - a) > tol:
        m = (a + b)/2 # mid point of the interval
        fm = f(m)
        if fm == 0:
            return m
        if copysign(fm, fa) == fm: # fa and fm have the same
sign
            a = m
            fa = fm
        else: # fb and fm have the same sign
            b = m
    return a
