# Importo le tre librerie necessarie: pandas per i dati, numpy per i numeri casuali e matplotlib per i grafici
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Genero 30 temperature casuali (valori interi tra 15 e 35 gradi) per i giorni del mese
temperature_casuali = np.random.randint(15, 36, size=30)

# Creo il DataFrame con la colonna 'temperature' come richiesto dalla traccia
df = pd.DataFrame({'temperature': temperature_casuali})

# Calcolo la temperatura massima con max
temp_massima = df['temperature'].max()

# Calcolo la temperatura minima con min
temp_minima = df['temperature'].min()

# Calcolo la temperatura media con mean
temp_media = df['temperature'].mean()

# Calcolo la mediana con median
temp_mediana = df['temperature'].median()

# Stampo i risultati numerici a schermo
print("STATISTICHE DEL MESE:")
print(f"Temperatura massima: {temp_massima}°C")
print(f"Temperatura minima: {temp_minima}°C")
print(f"Temperatura media: {temp_media:.2f}°C")
print(f"Mediana delle temperature: {temp_mediana}°C")


# GRAFICO
# Creo il grafico a linee semplice passandogli la colonna delle temperature
plt.plot(df['temperature'])

# Aggiungo il titolo al grafico
plt.title("Andamento della Temperatura Giornaliera")

# Aggiungo l'etichetta dell'asse X (i giorni)
plt.xlabel("Giorno del Mese")

# Aggiungo l'etichetta dell'asse Y (i gradi)
plt.ylabel("Temperatura (°C)")

# Mostro il grafico a schermo
plt.show()