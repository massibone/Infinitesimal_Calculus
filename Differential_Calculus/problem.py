'''
un contenitore cilindrico cor raggio R=1 metro e altezza 3 metri pieno d'acqua.
Da un rubinetto posto in prossimita del fondo vengono prelevati 10litri al minuto.
Con quale velocita' l'altezza dell'acqua decresce?


'''
import time

# Dati del contenitore cilindrico
raggio = 1  # raggio in metri
altezza = 3  # altezza in metri

# Volume totale del contenitore
volume_totale = 3.14159 * raggio**2 * altezza  # pi * raggio^2 * altezza

# Flusso di uscita dal rubinetto
flusso_uscita = 10  # litri al minuto

# Calcola la velocità di decrescita dell'altezza
velocita = flusso_uscita / (volume_totale * (1 / 60))  # litri al minuto diviso per secondi in un minuto

# Stampa la velocità di decrescita dell'altezza
print(f"La velocità di decrescita dell'altezza dell'acqua è di {velocita:.2f} metri al secondo.")

# Calcola e stampa il tempo necessario per svuotare completamente il contenitore
tempo_svuotamento = (volume_totale / flusso_uscita) * 60  # secondi
print(f"Il contenitore verrà completamente svuotato in {tempo_svuotamento:.2f} minuti.")

# Esegue il conteggio dell'altezza dell'acqua fino allo svuotamento
altezza_acqua = altezza
while altezza_acqua > 0:
    altezza_acqua -= (velocita * (1 / 60))  # decrementa l'altezza in base alla velocità
    print(f"Altezza dell'acqua: {altezza_acqua:.2f} metri")
    time.sleep(1)  # attende 1 secondo prima di visualizzare l'altezza successiva
