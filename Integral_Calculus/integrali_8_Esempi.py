'''
Scegliere il metodo giusto per calcolare un integrale dipende dalla forma dell'integranda e dalle caratteristiche dell'integrale stesso. Esistono diverse tecniche standard per risolvere integrali, e la scelta del metodo dipenderà dalla complessità dell'integranda e dalla presenza di particolari strutture o pattern. Ecco alcuni dei metodi comuni:

1. **Sostituzione (o Cambio di variabile)**: Questo metodo è utile quando si può fare una sostituzione intelligente per semplificare l'integranda o renderla più riconoscibile.

2. **Per parti**: Utile quando l'integranda è il prodotto di due funzioni che possono essere differenziate o integrate più facilmente separatamente.

3. **Frazioni parziali**: Usato per integrare frazioni razionali, dove l'integranda è un rapporto di polinomi.

4. **Scomposizione in elementi semplici**: Utile per integrare funzioni razionali, scomponendo l'integranda in una somma di funzioni più semplici.

5. **Integrazione trigonometrica**: Utilizzato per integrare funzioni contenenti funzioni trigonometriche.

6. **Integrazione per funzioni speciali**: A volte è possibile riconoscere l'integranda come una funzione speciale con una formula di integrazione specifica.

7. **Metodo delle serie di potenze**: Può essere applicato quando l'integranda può essere rappresentata come una serie infinita di potenze di una variabile.

8. **Metodo delle mappe di contorno (analisi complessa)**: Applicato in alcune situazioni speciali, particolarmente utilizzato quando si lavora con funzioni complesse.

Per scegliere il metodo più appropriato, è utile avere una buona comprensione dei vari metodi e della struttura dell'integranda. Spesso, l'esperienza e la pratica aiutano a sviluppare l'intuizione su quale metodo potrebbe funzionare meglio in una determinata situazione. Inoltre, provare vari metodi può essere utile se non si è sicuri del percorso migliore da seguire.
'''

import numpy as np
import matplotlib.pyplot as plt

# Definire le funzioni integrate
def integrate_substitution(x):
    return 0.5 * np.exp(x**2)

def integrate_by_parts(x):
    return x * np.sin(x) - np.cos(x)

# Definire l'intervallo di x
x = np.linspace(0, 2, 400)

# Calcolare i risultati dei primi due integrali
result_substitution = integrate_substitution(x)
result_by_parts = integrate_by_parts(x)

# Creare il grafico
plt.figure(figsize=(10, 6))
plt.plot(x, result_substitution, label='Substitution Method')
plt.plot(x, result_by_parts, label='Integration by Parts')
plt.xlabel('x')
plt.ylabel('Integral Value')
plt.legend()
plt.title('Integrals using Substitution and Integration by Parts')
plt.grid(True)
plt.show()
