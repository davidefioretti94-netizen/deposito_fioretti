import numpy as np

# Nome del file dove vado a salvare le risposte
nome_file = "risultati.txt"

# Apro il file in scrittura
with open(nome_file, "w") as f:

    # Esercizio 1: Somma e Media di Elementi
  
    f.write("=== ESERCIZIO 1 ===\n")

    # Array di 15 numeri casuali tra 1 e 100 (uso 101 perché il limite superiore è escluso)
    arr1 = np.random.randint(1, 101, size=15)
    f.write(f"Array generato: {arr1}\n")

    # Sommo tutti i numeri dell'array
    somma = np.sum(arr1)
    f.write(f"Somma degli elementi: {somma}\n")

    # Faccio la media dei numeri
    media = np.mean(arr1)
    f.write(f"Media degli elementi: {media}\n\n")


    # Esercizio 2: Manipolazione di Array Multidimensionali

    f.write("=== ESERCIZIO 2 ===\n")

    # Creo la matrice 5x5 con i numeri da 1 a 25
    # arange fa la lista da 1 a 25 e reshape la mette in tabella 5x5
    matrice = np.arange(1, 26).reshape(5, 5)
    f.write(f"Matrice 5x5:\n{matrice}\n\n")

    # Estraggo la seconda colonna (ha indice 1 perché si parte da 0)
    seconda_colonna = matrice[:, 1]
    f.write(f"Seconda colonna: {seconda_colonna}\n")

    # Estraggo la terza riga (indice 2)
    terza_riga = matrice[2, :]
    f.write(f"Terza riga: {terza_riga}\n")

    # Per la diagonale uso il fancy indexing:
    # le posizioni sulla diagonale sono (0,0), (1,1), (2,2), (3,3), (4,4)
    indici_diagonale = [0, 1, 2, 3, 4]
    diagonale = matrice[indici_diagonale, indici_diagonale]
    
    # Poi sommo i numeri trovati sulla diagonale
    somma_diagonale = np.sum(diagonale)
    f.write(f"Somma della diagonale principale: {somma_diagonale}\n\n")



    # Esercizio 3: Operazioni con Fancy Indexing
   
    f.write("=== ESERCIZIO 3 ===\n")

    # Creo la matrice 4x4 con numeri casuali interi tra 10 e 50 come chiede la traccia
    arr3 = np.random.randint(10, 51, size=(4, 4))
    f.write(f"Array originale (4x4):\n{arr3}\n\n")

    # Prendo i punti richiesti col fancy indexing: (0,1), (1,3), (2,2) e (3,0)
    righe = [0, 1, 2, 3]
    colonne = [1, 3, 2, 0]
    elementi_selezionati = arr3[righe, colonne]
    f.write(f"Elementi agli indici (0,1), (1,3), (2,2), (3,0): {elementi_selezionati}\n")

    # Prendo le righe dispari (cioè quelle con indice 1 e 3)
    righe_dispari = arr3[[1, 3], :]
    f.write(f"Righe dispari (indici 1 e 3):\n{righe_dispari}\n\n")

    # Aggiungo 10 ai 4 elementi che avevo preso prima
    arr3[righe, colonne] += 10
    f.write(f"Array modificato (+10 agli elementi selezionati):\n{arr3}\n")

print(f"Fatto! I risultati sono stati scritti nel file '{nome_file}'.")