import numpy as np
import matplotlib.pyplot as plt

def taylor_series(function, x0, n, interval):
    """
    Calcola e restituisce l'approssimazione di Taylor della funzione data.

    Parametri:
    - function: la funzione da approssimare
    - x0: il punto di espansione
    - n: il grado massimo dell'approssimazione
    - interval: l'intervallo su cui calcolare l'approssimazione
    
