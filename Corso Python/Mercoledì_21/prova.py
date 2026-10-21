# Importo le librerie che mi servono: pandas per gestire le tabelle e numpy per i numeri casuali
import pandas as pd
import numpy as np


# PUNTO 1: Carico i dati in un DataFrame generandoli a caso


# Creo due liste di partenza con i nomi e le città
nomi = ['Alice', 'Bob', 'Carla', 'Davide', 'Elena', 'Marco', 'Giulia']
citta = ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna']

# Decido di generare un gruppo di 10 persone
n_persone = 10

# Creo degli indici casuali interi con randint per evitare np.random.choice
indici_nomi = np.random.randint(0, len(nomi), size=n_persone)
indici_citta = np.random.randint(0, len(citta), size=n_persone)

# Estraggo i nomi e le città dalle liste usando gli indici casuali appena creati
nomi_casuali = [nomi[i] for i in indici_nomi]
citta_casuali = [citta[i] for i in indici_citta]

# Creo il dizionario convertendo i numeri di NumPy in liste di Python con .tolist()
# così poi posso usare .append() senza far crashare il programma
data = {
    'Nome': nomi_casuali,
    # Genero 10 età casuali tra 10 e 80 anni
    'Età': np.random.randint(10, 80, size=n_persone).tolist(),
    'Città': citta_casuali,
    # Genero 10 salari casuali tra 1200 e 3500 euro
    'Salario': np.random.randint(1200, 3500, size=n_persone).tolist()
}

# Duplico il primo elemento in fondo alle liste per testare i duplicati
data['Nome'].append(data['Nome'][0])
data['Età'].append(data['Età'][0])
data['Città'].append(data['Città'][0])
data['Salario'].append(data['Salario'][0])

# Converto il dizionario nel DataFrame di pandas
df = pd.DataFrame(data)

# Inserisco a mano due valori mancanti (NaN) per testare la pulizia nei punti successivi
df.loc[2, 'Età'] = np.nan
df.loc[4, 'Salario'] = np.nan



# PUNTO 2: Visualizzo le prime e le ultime cinque righe

# Stampo tutta la tabella per vederla dall'inizio
print("DataFrame Originale:")
print(df)

# Stampo le prime 5 righe usando .head()
print("\nPrime 5 righe (head):")
print(df.head())

# Stampo le ultime 5 righe usando .tail()
print("\nUltime 5 righe (tail):")
print(df.tail())



# PUNTO 3: Visualizzo il tipo di dati di ciascuna colonna


print("\nInformazioni e Tipi di Dati:")
# Uso info() che mi mostra i tipi di dati di tutte le colonne e i valori non nulli
print(df.info())



# PUNTO 4: Calcolo le statistiche descrittive per le colonne numeriche


print("\nStatistiche Descrittive (describe):")
# describe() calcola in automatico media, deviazione standard, min, max e quantili
print(df.describe())

# Stampo a parte le mediane delle colonne numeriche come chiesto dalla traccia
print("\nMediana dell'Età:", df['Età'].median())
print("Mediana del Salario:", df['Salario'].median())



# PUNTO 5: Identifico e rimuovo eventuali duplicati
# Conto quante righe duplicate ci sono nella tabella
duplicati = df.duplicated().sum()
print(f"\nRighe duplicate trovate: {duplicati}")

# Rimuovo la riga duplicata con drop_duplicates()
df = df.drop_duplicates()
print("Duplicati rimossi con successo!")



# PUNTO 6: Gestisco i valori mancanti sostituendoli con la mediana


# Calcolo prima le mediane per l'Età e per il Salario
mediana_eta = df['Età'].median()
mediana_salario = df['Salario'].median()

# Sostituisco i valori vuoti (NaN) con la relativa mediana usando fillna()
df['Età'] = df['Età'].fillna(mediana_eta)
df['Salario'] = df['Salario'].fillna(mediana_salario)

print("\nValori mancanti sostituiti con la mediana!")



# PUNTO 7: Aggiungo la nuova colonna "Categoria Età"


# Creo la colonna impostando inizialmente per tutti il valore 'Adulto'
df['Categoria Età'] = 'Adulto'

# Uso le selezioni condizionali con i filtri per aggiornare i valori:
# Se l'età è minore o uguale a 18 imposto 'Giovane'
df.loc[df['Età'] <= 18, 'Categoria Età'] = 'Giovane'

# Se l'età è maggiore di 65 imposto 'Senior'
df.loc[df['Età'] > 65, 'Categoria Età'] = 'Senior'

# Stampo la tabella finale completa di tutte le modifiche
print("\nDataFrame Finale con la nuova colonna Categoria Età:")
print(df)