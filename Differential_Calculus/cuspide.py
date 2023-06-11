import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.abs(x)**(1/3)

def f_prime(x):
    return np.sign(x) * (1/3) * np.abs(x)**(-2/3)
