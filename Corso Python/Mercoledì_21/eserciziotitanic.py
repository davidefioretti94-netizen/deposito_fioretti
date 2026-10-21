# Importo le librerie necessarie: pandas per le tabelle e numpy per le operazioni numeriche
import pandas as pd
import numpy as np

# 1. Carico il file CSV scaricato nella cartella del progetto
# Leggo il file CSV che ho salvato nella cartella del progetto
df = pd.read_csv(r"Corso Python\Mercoledì_21\titanic.csv")


# 2. Esplorazione dei dati
# Stampo tutta la tabella per vederla dall'inizio
print("DataFrame Originale:")
print(df)

# Stampo solo le prime 5 righe usando .head()
print("\nPrime 5 righe:")
print(df.head())

# Stampo solo le ultime 5 righe usando .tail()
print("\nUltime 5 righe:")
print(df.tail())

# Stampo le informazioni sui tipi di dati e sui valori nulli presenti
print("\nInformazioni e Tipi di Dati:")
print(df.info())

# Stampo le statistiche descrittive generali (media, min, max)
print("\nStatistiche Descrittive:")
print(df.describe())


# 3. Pulizia dei dati

# Cerco quante righe duplicate ci sono nella tabella
duplicati = df.duplicated().sum()
print(f"\nRighe duplicate trovate: {duplicati}")

# Rimuovo eventuali duplicati con drop_duplicates()
df = df.drop_duplicates()

# Calcolo la mediana dell'età (colonna 'Age') per la sostituzione dei dati vuoti
mediana_eta = df['Age'].median()

# Sostituisco i valori vuoti NaN dell'età con la mediana usando fillna()
df['Age'] = df['Age'].fillna(mediana_eta)

print("Valori mancanti dell'età sostituiti con la mediana!")


# 4. Creazione delle due nuove colonne

# PRIMA NUOVA COLONNA:
# Convertiamo il prezzo del biglietto (colonna 'Fare') in euro moltiplicando per 1.15
df['Prezzo_In_Euro'] = df['Fare'] * 1.15

# SECONDA NUOVA COLONNA:
# Creiamo la colonna 'Fascia_Eta' impostando per tutti il valore di partenza 'Adulto'
df['Fascia_Eta'] = 'Adulto'

# Se l'età è minore o uguale a 18 imposto 'Giovane'
df.loc[df['Age'] <= 18, 'Fascia_Eta'] = 'Giovane'

# Se l'età è maggiore di 60 imposto 'Anziano'
df.loc[df['Age'] > 60, 'Fascia_Eta'] = 'Anziano'


# 5. Presentazione dei dati finali

print("\nDataFrame Finale con le due nuove colonne:")
# Seleziono le colonne principali da mostrare a schermo
colonne_da_mostrare = ['Name', 'Age', 'Fare', 'Prezzo_In_Euro', 'Fascia_Eta']
print(df[colonne_da_mostrare].head(10))