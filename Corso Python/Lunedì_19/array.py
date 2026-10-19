import numpy as np

# 1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49
arr = np.arange(10, 50) #il valore finale è escluso
print("Array creato:")
print(arr)

# 2. Verifica il tipo di dato dell'array e stampa il risultato
print("\nTipo di dato iniziale:")
print(arr.dtype)

# 3. Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato
arr_float = arr.astype(np.float64) 
print("\nNuovo tipo di dato dopo il cambio:")
print(arr_float.dtype)

# 4. Stampa la forma dell'array
print("\nForma dell'array:")
print(arr_float.shape)   #restituisce un array monodimensionale di 40 elementi