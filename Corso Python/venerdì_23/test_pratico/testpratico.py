# Importo pandas per gestire le tabelle e matplotlib per fare i grafici
import pandas as pd
import matplotlib.pyplot as plt


# FASE 1: Caricamento e Pulizia Dati
# Carico i due file CSV
df_data = pd.read_csv(r"Corso Python\venerdì_23\test_pratico\candy-data.csv")
df_vendite = pd.read_csv(r"Corso Python\venerdì_23\test_pratico\candy-vendite.csv")

# Stampo le statistiche descrittive generali (media, min, max, ecc.) dei due file
print("STATISTICHE DESCRITTIVE CARATTERISTICHE:")
print(df_data.describe())

print("\nSTATISTICHE DESCRITTIVE METRICHE VENDITE:")
print(df_vendite.describe())

# Pulisco il primo file: tolgo le righe duplicate e poi elimino quelle con dati mancanti
df_data = df_data.drop_duplicates().dropna()

# Pulisco il secondo file: tolgo i duplicati e riempio eventuali celle vuote con 0
df_vendite = df_vendite.drop_duplicates().fillna(0)

# Unisco le due tabelle in una sola usando il nome della caramella come punto d'incontro
df = pd.merge(df_data, df_vendite, on='competitorname')

# Creo la colonna del fatturato moltiplicando le unità vendute per il prezzo
df['fatturato'] = df['unita_vendute'] * df['prezzo_euro']

# Creo la colonna del profitto sottraendo il costo dal prezzo e moltiplicando per i pezzi venduti
df['profitto'] = (df['prezzo_euro'] - df['costo_unitario_euro']) * df['unita_vendute']



# FASE 2: Analisi delle Metriche per Area Geografica
# Raggruppo per area di vendita e calcolo la somma totale per i volumi e i soldi
print("\nANALISI COMPLETA PER AREA DI VENDITA (TOTALI):")
analisi_totali_area = df.groupby('area_vendita')[['unita_vendute', 'giacenza_magazzino', 'budget_marketing_euro', 'fatturato', 'profitto']].sum()
print(analisi_totali_area)

# Raggruppo per area di vendita e calcolo la media per prezzi e voti dei clienti
print("\nANALISI COMPLETA PER AREA DI VENDITA (MEDIE):")
analisi_medie_area = df.groupby('area_vendita')[['prezzo_euro', 'costo_unitario_euro', 'valutazione_clienti']].mean()
print(analisi_medie_area)



# FASE 3: Analisi degli Ingredienti
# Salvo in una lista tutti i nomi delle colonne degli ingredienti e formati
ingredienti = [
    'chocolate', 'fruity', 'caramel', 'peanutyalmondy', 
    'nougat', 'crispedricewafer', 'hard', 'bar', 'pluribus'
]

print("\nCONFRONTO FATTURATO MEDIO PER OGNI INGREDIENTE/FORMATO:")

# Faccio un giro per ogni ingrediente della lista senza dover riscrivere il groupby 9 volte
for elemento in ingredienti:
    # Calcolo il fatturato medio distinguendo tra chi ha l'ingrediente (1) e chi no (0)
    media_ingrediente = df.groupby(elemento)['fatturato'].mean()
    print(f"\nAnalisi per: {elemento}")
    print(f"Senza {elemento} (0): {media_ingrediente.get(0, 0):.2f} €")
    print(f"Con {elemento} (1):   {media_ingrediente.get(1, 0):.2f} €")



# FASE 4: Grafici
# GRAFICO 1: Grafico a barre con i totali delle vendite per ogni area
plt.figure()
plt.bar(analisi_totali_area.index, analisi_totali_area['unita_vendute'])
plt.title("Unità Vendute Totali per Area di Vendita")
plt.xlabel("Area di Vendita")
plt.ylabel("Unità Vendute")
plt.show()

# GRAFICO 2: Grafico a punti per vedere se aumentando il marketing aumentano le vendite
plt.figure()
plt.scatter(df['budget_marketing_euro'], df['unita_vendute'])
plt.title("Relazione tra Budget Marketing e Unità Vendute")
plt.xlabel("Budget Marketing")
plt.ylabel("Unità Vendute")
plt.show()

# GRAFICO 3: Grafico a punti per vedere se il prezzo influenza la soddisfazione dei clienti
plt.figure()
plt.scatter(df['prezzo_euro'], df['valutazione_clienti'])
plt.title("Relazione tra Prezzo (€) e Valutazione Clienti")
plt.xlabel("Prezzo (€)")
plt.ylabel("Valutazione Clienti (1-5)")
plt.show()

# GRAFICO 4: Creo una lista vuota per raccogliere le vendite medie di ogni ingrediente
medie_con_ingrediente = []

# Popolo la lista filtrando solo i prodotti che contengono l'ingrediente (valore uguale a 1)
for elemento in ingredienti:
    media_vendite = df[df[elemento] == 1]['unita_vendute'].mean()
    medie_con_ingrediente.append(media_vendite)

# Disegno il grafico a barre finale mettendoci sopra tutti gli ingredienti presi dalla lista
plt.figure()
plt.bar(ingredienti, medie_con_ingrediente)
plt.title("Unità Vendute Medie per Presenza degli Ingredienti e Formati")
plt.xlabel("Caratteristiche Prodotto")
plt.ylabel("Unità Vendute Medie")
plt.show()