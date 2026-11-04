import numpy as np  # Importo numpy per le operazioni numeriche e per creare array
import pandas as pd  # Importo pandas per gestire i dati in tabelle DataFrame
import matplotlib.pyplot as plt  # Importo matplotlib per tracciare i grafici
from sklearn.datasets import load_breast_cancer  # Importo il dataset del tumore al seno
from sklearn.model_selection import train_test_split  # Importo la funzione per la suddivisione dei dati
from sklearn.dummy import DummyClassifier  # Importo il modello baseline Dummy
from sklearn.neighbors import KNeighborsClassifier  # Importo il classificatore KNN
from sklearn.tree import DecisionTreeClassifier, export_text  # Importo l'Albero di Decisione e la funzione per esportare le regole
from sklearn.preprocessing import StandardScaler, MinMaxScaler  # Importo gli scaler per la normalizzazione dei dati
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, ConfusionMatrixDisplay  # Importo le metriche di valutazione

#Punto 1: Definizione del problema
# 1. Tipo di apprendimento: Supervisionato (abbiamo sia le caratteristiche X sia le etichette reali y).
# 2. Tipo di problema: Classificazione Binaria (dobbiamo prevedere se il tumore e' maligno o benigno).
# 3. Colonna Target: E' il vettore 'y' (target), dove la classe d'interesse (maligno) e' rappresentata dal valore 0.

#Punto 2: Esplorazione dei dati
cancer = load_breast_cancer(as_frame=True)  # Carico il dataset in formato DataFrame pandas
X = cancer.data  # Separo la matrice delle 30 caratteristiche numeriche X dal target
y = cancer.target  # Separo il vettore target y contenente le etichette (0 = maligno, 1 = benigno)

print(f"Forma di X: {X.shape}, Forma di y: {y.shape}")  # Stampo le dimensioni della matrice X (569 righe, 30 colonne) e del vettore y
print("Nomi delle feature:", cancer.feature_names)  # Stampo i nomi delle 30 caratteristiche cliniche
print("Nomi delle classi:", cancer.target_names)  # Stampo i nomi delle due classi: 'malignant' (0) e 'benign' (1)
print("\nPrime 5 righe di X:\n", X.head())  # Stampo le prime 5 righe del DataFrame
print("\nContenuto DESCR (primi 500 caratteri):\n", cancer.DESCR[:500])  # Stampo le informazioni iniziali sull'origine dei dati e le unita' di misura

print("\nConteggio campioni per classe:\n", y.value_counts())  # Verifico il bilanciamento: 357 benigni (1) e 212 maligni (0)

stats = X.describe()  # Calcolo le statistiche descrittive principali per tutte le colonne
print("\nMinimo e Massimo per feature:\n", stats.loc[["min", "max"]])  # Stampo solo la riga del minimo e del massimo per ciascuna colonna

#Punto 3: Divisione dei dati
# Passaggio 1: Separo il 20% dei dati per il Test Set finale e l'80% per il Train + Validation
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y) 

# Passaggio 2: Divido l'80% rimanente in 60% Training effettivo e 20% Validation (20/80 = 0.25)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=42, stratify=y_train_val)

print(f"Dimensioni - Train: {X_train.shape[0]}, Validation: {X_val.shape[0]}, Test: {X_test.shape[0]}")  # Stampo il numero di righe dei tre sottoinsiemi (341 train, 114 val, 114 test)
print(f"Percentuale maligni (0) - Train: {(y_train == 0).mean():.2%}, Val: {(y_val == 0).mean():.2%}, Test: {(y_test == 0).mean():.2%}")  # Verifico che stratify=y abbia mantenuto esattamente la stessa quota di maligni (~37.26%) nei tre blocchi

#Punto 4: Baseline
dummy = DummyClassifier(strategy="most_frequent")  # Creo il modello baseline che predice sempre la classe maggioritaria (benigno = 1)
dummy.fit(X_train, y_train) 

y_val_dummy = dummy.predict(X_val)  # Effettuo le predizioni sul validation set
acc_dummy = accuracy_score(y_val, y_val_dummy)  # Calcolo l'accuratezza del modello dummy
rec_dummy = recall_score(y_val, y_val_dummy, pos_label=0, zero_division=0)  # Calcolo la recall focalizzandomi sui tumori maligni (pos_label=0)

print(f"Baseline Dummy - Accuratezza Val: {acc_dummy:.4f}, Recall Maligni: {rec_dummy:.4f}")

# L'accuratezza del Dummy e' del ~62.7% solo perche' la maggior parte dei casi e' benigna, ma la Recall sui maligni e' zero!

#Punto 5:Primo modello: KNN senza scaling
knn_grezzo = KNeighborsClassifier(n_neighbors=5)  # Creo il modello KNN con k=5 sui dati non scalati
knn_grezzo.fit(X_train, y_train)  # Addestro il KNN sui dati grezzi di training

acc_tr_grezzo = knn_grezzo.score(X_train, y_train)  # Calcolo l'accuratezza ottenuta sui dati di training
acc_val_grezzo = knn_grezzo.score(X_val, y_val)  # Calcolo l'accuratezza ottenuta sui dati di validation
print(f"KNN grezzo (k=5) - Accuratezza Train: {acc_tr_grezzo:.4f}, Validation: {acc_val_grezzo:.4f}") 

distanze, indici = knn_grezzo.kneighbors(X_val.iloc[[0]])  # Estraggo le distanze e gli indici dei 5 vicini piu' prossimi per il primo campione del validation set
voti_prob = knn_grezzo.predict_proba(X_val.iloc[[0]])  # Calcolo la frazione di voti delle due classi per lo stesso campione

print("Distanze dei 5 vicini:", distanze)  
print("Classi dei 5 vicini:", y_train.iloc[indici[0]].values)  
print("Probabilita' stimate [Maligno(0), Benigno(1)]:", voti_prob)  

knn_grezzo = KNeighborsClassifier(n_neighbors=5)  # Creo il modello KNN con k=5 sui dati non scalati
knn_grezzo.fit(X_train, y_train)  # Addestro il KNN sui dati grezzi di training

acc_tr_grezzo = knn_grezzo.score(X_train, y_train)  # Calcolo l'accuratezza ottenuta sui dati di training
acc_val_grezzo = knn_grezzo.score(X_val, y_val)  # Calcolo l'accuratezza ottenuta sui dati di validation
print(f"KNN grezzo (k=5) - Accuratezza Train: {acc_tr_grezzo:.4f}, Validation: {acc_val_grezzo:.4f}")  # Stampo le due accuratezze

distanze, indici = knn_grezzo.kneighbors(X_val.iloc[[0]])  # Estraggo le distanze e gli indici dei 5 vicini piu' prossimi per il primo campione del validation set
voti_prob = knn_grezzo.predict_proba(X_val.iloc[[0]])  # Calcolo la frazione di voti delle due classi per lo stesso campione

print("Distanze dei 5 vicini:", distanze)  # Stampo le distanze euclidee calcolate dal KNN
print("Classi dei 5 vicini:", y_train.iloc[indici[0]].values)  # Stampo le etichette reali dei 5 vicini trovati
print("Probabilita' stimate [Maligno(0), Benigno(1)]:", voti_prob)  # Stampo la frazione di voti per le due classi

# Spiegazione sulla feature dominante:
# La feature che pesa di piu' e' 'worst area' (o 'mean area') perche' ha valori dell'ordine delle migliaia, oscurando completamente caratteristiche importanti che variano tra 0 e 1.

#Punto 6: Scaling e regola d'oro
scaler_std = StandardScaler()  # Inizializzo lo StandardScaler
X_tr_std = scaler_std.fit_transform(X_train)  # Applico la Regola d'Oro: fit_transform SOLO sui dati di training
X_val_std = scaler_std.transform(X_val)  # Trasformo il validation set usando media e deviazione standard del training
X_te_std = scaler_std.transform(X_test)  # Trasformo il test set usando unicamente i parametri calcolati sul training

print("Media colonna 0 Train scalato:", X_tr_std[:, 0].mean())  # Verifico che la media sul training sia 0
print("Dev.Std colonna 0 Train scalato:", X_tr_std[:, 0].std())  # Verifico che la deviazione standard sul training sia 1.0
print("Media colonna 0 Val scalato:", X_val_std[:, 0].mean())  # Verifico che la media sul validation NON sia esattamente 0

knn_std = KNeighborsClassifier(n_neighbors=5)  # Creo il KNN con k=5 sui dati standardizzati
knn_std.fit(X_tr_std, y_train)  # Addestro il modello sui dati di train scalati
acc_val_std = knn_std.score(X_val_std, y_val)  # Calcolo l'accuratezza sul validation set scalato
print(f"KNN con StandardScaler - Accuratezza Validation: {acc_val_std:.4f}")  # Stampo il nuovo risultato

scaler_minmax = MinMaxScaler()  # Inizializzo il MinMaxScaler
X_tr_mm = scaler_minmax.fit_transform(X_train)  # Alleno e trasformo il training set
X_val_mm = scaler_minmax.transform(X_val)  # Trasformo il validation set

knn_mm = KNeighborsClassifier(n_neighbors=5)  # Creo il KNN con k=5 per i dati scalati MinMax
knn_mm.fit(X_tr_mm, y_train)  # Addestro il modello sui dati MinMax
acc_val_mm = knn_mm.score(X_val_mm, y_val)  # Calcolo l'accuratezza sul validation set
print(f"KNN con MinMaxScaler - Accuratezza Validation: {acc_val_mm:.4f}")  # Stampo l'accuratezza con MinMax

# Spiegazione sui modelli che richiedono lo scaling:
# Il KNN necessita assolutamente dello scaling perche' calcola le distanze euclidee.
# L'Albero di Decisione NON ne ha bisogno perche' esegue split su singole variabili preservando l'ordinamento relativo.

#Punto 7: Scelta di k e diagnosi del modello
k_valori = range(1, 42, 2)  # Genero la sequenza di valori k dispari da 1 a 41
acc_train_list, acc_val_list = [], []  # Creo due liste vuote per salvare le accuratezze di train e validation

for k in k_valori:  # Scorro i diversi valori di k dispari
    knn_k = KNeighborsClassifier(n_neighbors=k)  # Creo il modello KNN impostando il k corrente
    knn_k.fit(X_tr_std, y_train)  # Alleno il modello sui dati di train scalati
    acc_train_list.append(knn_k.score(X_tr_std, y_train))  # Salvo l'accuratezza ottenuta sul train set
    acc_val_list.append(knn_k.score(X_val_std, y_val))  # Salvo l'accuratezza ottenuta sul validation set

plt.figure(figsize=(8, 5))  # Imposto le dimensioni della figura
plt.plot(k_valori, acc_train_list, label="Accuratezza Training", color="blue", marker="o")  # Traccio la curva del training
plt.plot(k_valori, acc_val_list, label="Accuratezza Validation", color="orange", marker="s")  # Traccio la curva di validation
plt.xlabel("Numero di Vicini (k)")  # Inserisco l'etichetta per l'asse X
plt.ylabel("Accuratezza")  # Inserisco l'etichetta per l'asse Y
plt.title("Curva di Complessità per il KNN (Scelta di k)")  # Inserisco il titolo del grafico
plt.legend()  # Inserisco la legenda dei colori
plt.grid(True)  # Attivo la griglia di sfondo
plt.show()  # Mostro il grafico a schermo

miglior_idx = np.argmax(acc_val_list)  # Individuo l'indice associato al valore massimo dell'accuratezza sul validation set
miglior_k = list(k_valori)[miglior_idx]  # Seleziono il miglior k basandomi unicamente sul validation set
print(f"Miglior k scelto sul Validation Set: {miglior_k} con accuratezza del {acc_val_list[miglior_idx]:.4f}")  # Stampo il valore ottimale di k trovato

# 1. Zona di Overfitting (k piccolissimi, es. k=1): Accuratezza sul train al 100%, ma curva di validation piu' bassa.
# 2. Zona di Underfitting (k grandi, es. k=35-41): Entrambe le curve scendono perche' il modello diventa troppo generalizzato.