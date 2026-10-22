# Importo le due librerie fondamentali: pandas per lavorare con i DataFrame e numpy per gestire i valori mancanti (NaN)
import pandas as pd
import numpy as np

# DATI DA CREARE
# 1. DataFrame Iscritti (inserisco direttamente 11 righe, con 1 duplicato 'Marco' in fondo e 1 np.nan sull'età)
data_iscritti = {
    'Nome': ['Marco', 'Giulia', 'Luca', 'Sara', 'Matteo', 'Elena', 'Davide', 'Chiara', 'Alessandro', 'Francesca', 'Marco'],
    'Eta': [22, 28, np.nan, 45, 52, 16, 33, 29, 61, 24, 22],
    'Citta': ['Roma', 'Milano', 'Napoli', 'Torino', 'Roma', 'Milano', 'Napoli', 'Torino', 'Roma', 'Milano', 'Roma'],
    'Tipo_Abbonamento': ['Base', 'Premium', 'Family', 'Base', 'Premium', 'Family', 'Base', 'Premium', 'Family', 'Base', 'Base']
}
# Trasformo il dizionario nel primo DataFrame degli iscritti
df_iscritti = pd.DataFrame(data_iscritti)

# 2. DataFrame Presenze (creo il dizionario con 15 righe, 3 date e 3 città diverse)
data_presenze = {
    'Data': ['2025-01-10', '2025-01-10', '2025-01-10', '2025-01-11', '2025-01-11', '2025-01-11', '2025-01-12', '2025-01-12', '2025-01-12', '2025-01-13', '2025-01-13', '2025-01-13', '2025-01-14', '2025-01-14', '2025-01-14'],
    'Corso': ['Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga', 'Crossfit', 'Nuoto'],
    'Citta': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli'],
    'Partecipanti': [12, 25, 8, 15, 30, 18, 22, 10, 14, 20, 27, 9, 16, 11, 24]
}
# Converto il dizionario delle presenze in DataFrame
df_presenze = pd.DataFrame(data_presenze)

# 3. DataFrame Costi Abbonamento (dizionario con i prezzi mensili per ciascun abbonamento)
data_costi = {
    'Tipo_Abbonamento': ['Base', 'Premium', 'Family'],
    'Costo_Mensile': [40, 70, 100]
}
# Converto la tabella dei costi in DataFrame
df_costi = pd.DataFrame(data_costi)



# 1. INTRODUZIONE
# Stampo la tabella iniziale degli iscritti per controllare i dati di partenza
print("=== ISCRITTI ORIGINALI ===")
print(df_iscritti)

# Filtro la tabella per mostrare a schermo solo gli iscritti con età maggiore di 25 anni
print("\n=== ISCRITTI OVER 25 ===")
print(df_iscritti[df_iscritti['Eta'] > 25])

# Creo la colonna 'Attivo' controllando con l'operate OR se l'abbonamento è Premium oppure Family
df_iscritti['Attivo'] = (df_iscritti['Tipo_Abbonamento'] == 'Premium') | (df_iscritti['Tipo_Abbonamento'] == 'Family')



# 2. PULIZIA DATI
# Rimuovo la riga duplicata dalla tabella degli iscritti
df_iscritti = df_iscritti.drop_duplicates()

# Calcolo l'età media degli iscritti
media_eta = df_iscritti['Eta'].mean()

# Sostituisco il valore nullo (np.nan) presente nell'età con il valore della media appena calcolato
df_iscritti['Eta'] = df_iscritti['Eta'].fillna(media_eta)


#3.Apply con funzione personalizzata
# Creo la funzione per catalogare gli iscritti in base alla loro età
def calcola_fascia(eta):
    # Se l'età è minore di 18 assegno Junior
    if eta < 18:
        return 'Junior'
    # Se l'età è compresa tra 18 e 44 anni assegno Adulto
    elif eta <= 44:
        return 'Adulto'
    # In tutti gli altri casi (da 45 anni in su) assegno Senior
    else:
        return 'Senior'

# Applico la funzione su ogni riga della colonna Eta usando apply e creo la nuova colonna Fascia_Eta
df_iscritti['Fascia_Eta'] = df_iscritti['Eta'].apply(calcola_fascia)



# 4. ANALISI PRESENZE
# Ordino il DataFrame delle presenze in ordine crescente per Citta e poi per Partecipanti
df_presenze_ordinato = df_presenze.sort_values(by=['Citta', 'Partecipanti'])

# Raggruppo per Corso e calcolo la somma totale dei partecipanti per ciascun corso
totale_corso = df_presenze.groupby('Corso')['Partecipanti'].sum()

# Raggruppo per Citta e calcolo la media dei partecipanti per ciascuna città
media_citta = df_presenze.groupby('Citta')['Partecipanti'].mean()

# Creo la tabella pivot: Corso sulle righe, Citta sulle colonne e la media dei Partecipanti nelle celle
pivot_presenze = df_presenze.pivot_table(index='Corso', columns='Citta', values='Partecipanti', aggfunc='mean')



# 5. MULTIINDEX
# Creo il dizionario con i dati di Sede, Anno e numero Iscritti
data_multi = {
    'Sede': ['Nord', 'Nord', 'Centro', 'Centro', 'Sud', 'Sud'],
    'Anno': [2024, 2025, 2024, 2025, 2024, 2025],
    'Iscritti': [150, 180, 200, 210, 90, 115]
}
# Creo il nuovo DataFrame per la gestione del MultiIndex
df_multi = pd.DataFrame(data_multi)

# Imposto le colonne Sede e Anno come indici strutturati a due livelli
df_multi = df_multi.set_index(['Sede', 'Anno'])

# Seleziono e stampo tutte le righe appartenenti alla sede Nord
print("\n=== TUTTE LE RIGHE SEDE NORD ===")
print(df_multi.loc['Nord'])

# Estraggo con .loc il valore preciso del numero di iscritti della sede Nord per l'anno 2025
iscritti_nord_2025 = df_multi.loc[('Nord', 2025), 'Iscritti']
# Stampo il valore specifico a schermo
print(f"\nIscritti Nord 2025: {iscritti_nord_2025}")


# 6. MERGE
# Unisco la tabella iscritti con quella dei costi usando la colonna comune Tipo_Abbonamento
df_iscritti_costi = pd.merge(df_iscritti, df_costi, on='Tipo_Abbonamento')

# Calcolo il costo annuale moltiplicando la colonna Costo_Mensile per 12
df_iscritti_costi['Costo_Annuale'] = df_iscritti_costi['Costo_Mensile'] * 12


# 7. OUTPUT FINALE
# Salvo la tabella iscritti pulita nel file CSV (senza salvare i numeri di riga dell'indice)
df_iscritti.to_csv('iscritti_puliti.csv', index=False)

# Salvo la tabella pivot del report presenze nel file CSV
pivot_presenze.to_csv('report_presenze_pivot.csv')

# Salvo la tabella finale con iscritti e costi nel file CSV (senza l'indice)
df_iscritti_costi.to_csv('iscritti_con_costi.csv', index=False)

# Stampo la conferma dell'avvenuto salvataggio dei 3 file
print("\nEsecuzione completata e file CSV salvati!")