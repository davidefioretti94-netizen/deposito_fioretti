# Importo le librerie che mi servono: pandas per le tabelle e numpy per generare i numeri casuali
import pandas as pd
import numpy as np


# PUNTO 1: Carico i dati in un DataFrame
# Creo due liste di partenza con i nomi dei prodotti e delle città
prodotti = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Tastiera']
citta = ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna']

# Decido di generare un totale di 15 vendite
n_vendite = 15

# Creo degli indici casuali interi con randint per pescare a caso dalle due liste
indici_prodotti = np.random.randint(0, len(prodotti), size=n_vendite)
indici_citta = np.random.randint(0, len(citta), size=n_vendite)

# Estraggo i prodotti e le città usando gli indici casuali appena generati
prodotti_casuali = [prodotti[i] for i in indici_prodotti]
citta_casuali = [citta[i] for i in indici_citta]

# Creo il dizionario con tutti i dati della tabella
data = {
    'Prodotto': prodotti_casuali,
    # Genero quantità casuali tra 1 e 10 pezzi
    'Quantità': np.random.randint(1, 11, size=n_vendite),
    # Genero prezzi unitari casuali tra 50 e 800 euro
    'Prezzo Unitario': np.random.randint(50, 801, size=n_vendite),
    'Città': citta_casuali
}

# Converto il dizionario nel DataFrame di pandas
df = pd.DataFrame(data)

# Stampo la tabella iniziale appena creata
print("=== DATAFRAME INIZIALE ===")
print(df)


# PUNTO 2: Aggiungo la colonna "Totale Vendite"
# Creo la colonna 'Totale Vendite' moltiplicando la colonna Quantità per il Prezzo Unitario
df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']

# Stampo la tabella aggiornata con il totale
print("\n=== DATAFRAME CON TOTALE VENDITE ===")
print(df)



# PUNTO 3: Raggruppo per Prodotto e calcolo il totale delle vendite
# Uso groupby su 'Prodotto', seleziono la colonna 'Totale Vendite' e sommo con sum()
totale_per_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()

# Stampo il totale di incasso per ogni prodotto
print("\n=== TOTALE VENDITE PER CIASCUN PRODOTTO ===")
print(totale_per_prodotto)



# PUNTO 4: Trovo il prodotto più venduto in termini di Quantità
# Raggruppo per 'Prodotto' e sommo le quantità vendute
quantita_per_prodotto = df.groupby('Prodotto')['Quantità'].sum()

# Trovo qual è il numero massimo di pezzi venduti con max
max_quantita = quantita_per_prodotto.max()

# Filtro per vedere quale prodotto ha quella quantità massima
prodotto_piu_venduto = quantita_per_prodotto[quantita_per_prodotto == max_quantita]

# Stampo il prodotto più venduto
print("\n=== PRODOTTO PIÙ VENDUTO (IN QUANTITÀ) ===")
print(prodotto_piu_venduto)



# PUNTO 5: Identifico la città con il maggior volume di vendite totali
# Sommo il 'Totale Vendite' raggruppando per la colonna 'Città'
totale_per_citta = df.groupby('Città')['Totale Vendite'].sum()

# Trovo la cifra massima incassata tra tutte le città
max_vendite_citta = totale_per_citta.max()

# Filtro la serie per trovare la città corrispondente a quell'incasso massimo
citta_maggior_volume = totale_per_citta[totale_per_citta == max_vendite_citta]

# Stampo la città con le vendite più alte
print("\n=== CITTÀ CON MAGGIOR VOLUME DI VENDITE TOTALE ===")
print(citta_maggior_volume)



# PUNTO 6: Creo un nuovo DataFrame con le vendite superiori a 1000 euro
# Salvo in un nuovo DataFrame solo le righe dove 'Totale Vendite' è maggiore di 1000
df_grandi_vendite = df[df['Totale Vendite'] > 1000]

# Stampo il nuovo DataFrame filtrato
print("\n=== NUOVO DATAFRAME (VENDITE SUPERIORI A 1000 EURO) ===")
print(df_grandi_vendite)


# PUNTO 8: Visualizzo il numero di vendite per ogni città
# Uso value_counts() sulla colonna 'Città' per contare quante righe/operazioni ci sono per ogni città
numero_vendite_citta = df['Città'].value_counts()

# Stampo il conteggio delle operazioni per città
print("\n=== NUMERO DI OPERAZIONI DI VENDITA PER OGNI CITTÀ ===")
print(numero_vendite_citta)