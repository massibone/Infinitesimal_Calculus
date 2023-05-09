# La successione 1/n tende a zero quando n diventa grande

n = 1000  # Numero di termini della successione

successione = []
for i in range(1, n+1):
    successione.append(1/i)

print(successione[-1])  # L'ultimo termine dovrebbe essere vicino a zero

# Esempio di successione divergente
# La successione n^2 diverge a infinito quando n diventa grande

n = 1000  # Numero di termini della successione

successione = []
for i in range(1, n+1):
    successione.append(i**2)

print(successione[-1])  # L'ultimo termine dovrebbe essere molto grande
----------------------------------
NeperoNumber.py
import math

# Calculate Nepero number
nepero = math.e
print("Nepero number:", nepero)

# Calculate example financial rate
principal = 1000
interest_rate = 0.05
years = 3

future_value = principal * (1 + interest_rate)**years
interest_earned = future_value - principal
financial_rate = interest_earned / principal

print("Example financial rate:", financial_rate)
