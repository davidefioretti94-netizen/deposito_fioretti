# Importo le librerie che mi servono: pandas per le tabelle e numpy per generare i numeri casuali
import pandas as pd
import numpy as np


# FASE 1: Generazione dei Dati con NumPy (Data, Città, Prodotto, Vendite)
# Creo le liste di partenza per le 3 città e i 3 tipi di prodotti
citta = ['Roma', 'Milano', 'Napoli']
prodotti = ['Laptop', 'Smartphone', 'Tablet']

# Decido di generare 30 registrazioni di vendite per coprire il periodo di un mese
n_registrazioni = 30

# Genero gli indici casuali interi con randint per pescare a caso dalle liste
indici_citta = np.random.randint(0, len(citta), size=n_registrazioni)
indici_prodotti = np.random.randint(0, len(prodotti), size=n_registrazioni)

# Pesco le città e i prodotti dalle liste usando gli indici casuali
citta_casuali = [citta[i] for i in indici_citta]
prodotti_casuali = [prodotti[i] for i in indici_prodotti]

# Genero i giorni del mese (da 1 a 30) per la colonna Data
giorni = np.random.randint(1, 31, size=n_registrazioni)
date_casuali = [f"2024-11-{giorno:02d}" for giorno in giorni]

# Genero gli importi delle vendite casuali tra 50 e 1000 euro
importi_vendite = np.random.randint(50, 1001, size=n_registrazioni)

# Creo il dizionario con tutti i dati generati
data = {
    'Data': date_casuali,
    'Città': citta_casuali,
    'Prodotto': prodotti_casuali,
    'Vendite': importi_vendite
}

# Converto il dizionario nel DataFrame di pandas
df = pd.DataFrame(data)

# Stampo le prime righe del DataFrame originale per verificare i dati
print("=== DATAFRAME GENERATO ===")
print(df.head(10))



# FASE 2: Creazione della Tabella Pivot (Vendite medie di ciascun prodotto per città)
# Creo la tabella pivot usando pivot_table():
# - index='Prodotto' metto i prodotti sulle righe
# - columns='Città' metto le città sulle colonne
# - values='Vendite' indico quali valori analizzare
# - aggfunc='mean' calcolo la media delle vendite
tabella_pivot = df.pivot_table(index='Prodotto', columns='Città', values='Vendite', aggfunc='mean')

print("\n=== TABELLA PIVOT (VENDITE MEDIE PER PRODOTTO E CITTÀ) ===")
print(tabella_pivot)



# FASE 3: Applicazione di GroupBy (Vendite totali per ogni prodotto)
# Uso groupby sulla colonna 'Prodotto', seleziono 'Vendite' e sommo con sum()
vendite_totali_prodotto = df.groupby('Prodotto')['Vendite'].sum()

print("\n=== VENDITE TOTALI PER OGNI PRODOTTO ===")
print(vendite_totali_prodotto)