# Importo le librerie necessarie: pandas per le tabelle, numpy per i dati casuali e matplotlib per i grafici
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# FASE 1 E 2: Generazione Dati (365 giorni) e DataFrame con Date come Indice
# Genero una serie temporale di 365 date consecutive a partire dal 1° gennaio 2026
date = pd.date_range(start='2026-01-01', periods=365)

# Genero 365 numeri casuali (media 2000 visitatori, deviazione standard 500)
visitatori = np.random.normal(2000, 500, 365)

# Arrotondo e converto in numeri interi (persone)
visitatori = visitatori.astype(int)
#Questo perché NumPy crea numeri decimali con la virgola (float)


# Creo il DataFrame impostando la colonna delle date direttamente come indice
df = pd.DataFrame({'Visitatori': visitatori}, index=date)

# Stampo le prime 5 righe per verificare la struttura della tabella
print("=== PRIME RIGHE DEL DATAFRAME ===")
print(df.head())



# FASE 3: Analisi dei Dati (Media e Deviazione Standard Mensile)

# Estraggo il mese direttamente dall'indice delle date per creare la colonna Mese
df['Mese'] = df.index.month

# Calcolo la media mensile dei visitatori raggruppando per la colonna Mese
media_mensile = df.groupby('Mese')['Visitatori'].mean()

# Calcolo la deviazione standard mensile raggruppando per la colonna Mese
dev_std_mensile = df.groupby('Mese')['Visitatori'].std()
#Raggruppa le 365 righe della tabella in 12 "sotto-gruppi", 
# uno per ogni mese dell'anno (da 1 a 12).

# Stampo i risultati dell'analisi mensile a schermo
print("\n=== MEDIA VISITATORI PER MESE ===")
print(media_mensile)

print("\n=== DEVIAZIONE STANDARD PER MESE ===")
print(dev_std_mensile)



# FASE 4: Visualizzazione dei Dati

# Calcolo la media mobile a 7 giorni con la funzione
#La funzione rolling crea una finestra scorrevole di 7 elementi
#non guarda tutta la colonna insieme, ma prende i dati a gruppi di 7 giorni per volta,
# scorrendo verso il basso riga dopo riga
df['Media_Mobile_7G'] = df['Visitatori'].rolling(7).mean()


# --- PRIMO GRAFICO: Visitatori giornalieri e Media Mobile a 7 giorni ---

# Disegno la linea dei visitatori giornalieri
plt.plot(df.index, df['Visitatori'], label='Visitatori Giornalieri')
#df.index svolge il ruolo di asse X del grafico.
#df['Visitatori'] svolge il ruolo di asse Y
#label serve a dare un nome identificativo alla linea del grafico.

# Disegno la linea della media mobile a 7 giorni per la tendenza settimanale
plt.plot(df.index, df['Media_Mobile_7G'], label='Media Mobile (7 giorni)')

# Aggiungo titolo, etichette e legenda al primo grafico
plt.title("Visitatori Giornalieri e Tendenza Settimanale")
plt.xlabel("Data")
plt.ylabel("Numero Visitatori")
plt.legend()
plt.show()


# --- SECONDO GRAFICO: Media mensile dei visitatori ---

# Disegno il grafico della media mensile usando i numeri dei mesi (1-12)
plt.plot(media_mensile.index, media_mensile.values)
#media_mensile.index (Asse X ):
#Prende gli indici della serie media_mensile, ovvero i numeri dei mesi che vanno da 1 a 12.
# Passandoli come primo elemento dentro plt.plot()
#media_mensile.values (Asse Y):
#Prende i valori effettivi contenuti nella serie, ovvero i numeri che rappresentano 
# la media dei visitatori calcolata per ogni mese. Passandoli come secondo elemento

# Aggiungo titolo ed etichette al secondo grafico
plt.title("Media Mensile dei Visitatori del Parco")
plt.xlabel("Mese dell'Anno")
plt.ylabel("Media Visitatori")
plt.show()