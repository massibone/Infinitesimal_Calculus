import numpy as np
import matplotlib.pyplot as plt
# Definizione dell'equazione lineare del primo ordine
def first_order_eq(y, t):
    return -0.5 * y

# Definizione dell'equazione lineare del secondo ordine
def second_order_eq(y, t):
    return -0.5 * y - 2 * np.sin(t)

