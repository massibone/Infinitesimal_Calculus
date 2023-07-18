from scipy import integrate

def trapezium(func, a, b, n_steps):
    """Estimate an integral using the trapezium rule"""
    h = (b - a) / n_steps
    x_vals = np.arange(a + h, b, h)
    y_vals = func(x_vals)
    return 0.5*h*(func(a) + func(b) + 2.*np.sum(y_vals))