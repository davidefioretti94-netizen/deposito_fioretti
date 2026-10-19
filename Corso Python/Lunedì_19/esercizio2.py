import numpy as np

# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50
#usiamo 51 come limite superiore perché np.random.randint esclude l'estremo superiore
array_originale = np.random.randint(10, 51, size=20)

# 2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array
primi_10 = array_originale[:10]

# 3. Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array
ultimi_5 = array_originale[-5:]

# 4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso)
da_5_a_15 = array_originale[5:15]

# 5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array
ogni_terzo = array_originale[::3]

# Creiamo una copia per non sovrascrivere l'array originale prima della stampa
array_modificato = array_originale.copy()

# 6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99
array_modificato[5:10] = 99

# 7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing
print("Array originale:\n", array_originale)
print("\nPrimi 10 elementi:\n", primi_10)
print("\nUltimi 5 elementi:\n", ultimi_5)
print("\nElementi dall'indice 5 al 15 (escluso):\n", da_5_a_15)
print("\nOgni terzo elemento dell'array:\n", ogni_terzo)
print("\nArray dopo la modifica (valore 99 dall'indice 5 al 10 escluso):\n", array_modificato)