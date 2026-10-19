import numpy as np

# 1. Genero la matrice 6x6 con numeri random tra 1 e 100
# Metto 101 perché randint esclude il valore finale
matrice_originale = np.random.randint(1, 101, size=(6, 6))

# 2. Prendo la parte centrale 4x4
# Escludo i bordi prendendo gli indici da 1 a 4
sotto_matrice_centrale = matrice_originale[1:5, 1:5]

# 3. Inverto l'ordine delle righe
# Passo -1 sulle righe per capovolgerle dall'alto in basso
matrice_invertita = sotto_matrice_centrale[::-1, :]

# 4. Estraggo gli elementi della diagonale principale
diagonale_principale = matrice_invertita.diagonal()

# 5. Sostituisco i multipli di 3 con -1 usando i cicli e l'if
matrice_modificata = matrice_invertita.copy() # faccio una copia per sicurezza

for i in range(matrice_modificata.shape[0]):
    for j in range(matrice_modificata.shape[1]):
        # controllo se il numero è divisibile per 3 (resto uguale a zero)
        if matrice_modificata[i, j] % 3 == 0:
            matrice_modificata[i, j] = -1

# 6. Stampo tutti i risultati per verificare il procedimento
print("1. Matrice Originale (6x6):\n", matrice_originale)
print("\n2. Sotto-matrice Centrale (4x4):\n", sotto_matrice_centrale)
print("\n3. Matrice Invertita:\n", matrice_invertita)
print("\n4. Diagonale Principale:\n", diagonale_principale)
print("\n5. Matrice Modificata:\n", matrice_modificata)