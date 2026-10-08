import random


# 1. Chiedi un numero positivo n
def inserisci_numero():
    # Creiamo un ciclo infinito che continua finché l'utente
    # non inserisce un numero maggiore di zero
    while True:
        n = int(input("Inserisci un numero intero positivo: "))
        if n > 0:
            return n
        else:
            print("Errore: inserisci un numero maggiore di 0.")


# 2. Genera una lista di n numeri casuali tra 1 e n
def genera_lista(n):
    # Creiamo una lista vuota nella quale inseriremo
    # i numeri casuali
    lista = []
    
     # Il ciclo for viene eseguito n volte
    for i in range(n):
        # Generiamo un numero casuale compreso tra 1 e n
        numero = random.randint(1, n)
        # Aggiungiamo il numero casuale alla lista
        lista.append(numero)
    return lista


# 3. Calcola la somma dei numeri pari
def somma_pari(lista):
    # Inizializziamo la variabile somma a zero
    somma = 0
    # Scorriamo tutti gli elementi presenti nella lista
    for numero in lista:
        if numero % 2 == 0:
            # Aggiungiamo il numero alla variabile somma
            somma = somma + numero
    return somma


# 4. Stampa tutti i numeri dispari
def stampa_dispari(lista):
    # Stampiamo un messaggio per indicare cosa stiamo visualizzando
    print("Numeri dispari:")
    # Scorriamo tutti gli elementi della lista
    for numero in lista:
        if numero % 2 != 0:
             # Stampiamo il numero dispari
            print(numero)


# 5. Funzione che determina se un numero è primo (restituisce True o False)
def numero_primo(numero):
    
    # I numeri minori di 2 non sono numeri primi
    if numero < 2:
        return False
    
    # Controlliamo tutti i possibili divisori
    # partendo da 2 fino a numero
    for i in range(2, numero):
        # Controlliamo se il numero è divisibile per i
        # Se il resto è zero significa che abbiamo trovato un divisore
        if numero % i == 0:
            return False
    return True


# Funzione per gestire la scelta 3 del menu (chiede un numero e controlla se è primo)
def verifica_numero_utente():
    numero = int(input("Inserisci un numero da verificare: "))
    if numero_primo(numero):
        print(numero, "è un numero primo.")
    else:
        print(numero, "non è un numero primo.")


# 6. Stampa tutti i numeri primi nella lista
def stampa_primi(lista):
    print("Numeri primi nella lista:")
    for numero in lista:
        if numero_primo(numero):
            print(numero)


# 7. Determina se la somma di tutti i numeri nella lista è un numero primo
def somma_lista_prima(lista):
    somma = 0
    for numero in lista:
        somma = somma + numero

    # Controlliamo se la somma ottenuta è un numero primo
    if numero_primo(somma):
        print("La somma di tutti i numeri è", somma, "ed è un numero primo.")
    else:
        print("La somma di tutti i numeri è", somma, "e non è un numero primo.")


# PROGRAMMA PRINCIPALE (Punto 8 - Menu)

# Richiamiamo la funzione inserisci_numero()
# per ottenere dall'utente un numero positivo
n = inserisci_numero()

# Richiamiamo la funzione genera_lista()
# per creare una lista contenente n numeri casuali
lista = genera_lista(n)

print("Lista generata:", lista)

# Creiamo un ciclo infinito per mantenere attivo il menu
while True:
    print("-- MENU --")
    print("1. Calcolare la somma dei numeri pari")
    print("2. Stampare i numeri dispari")
    print("3. Verificare se un numero è primo")
    print("4. Stampare i numeri primi nella lista")
    print("5. Verificare se la somma della lista è prima")
    print("6. Esci")
    
    
    # Chiediamo all'utente di scegliere un'opzione
    # e convertiamo la scelta in un numero intero
    scelta = int(input("Scegli un'opzione: "))
    
    
    
    if scelta == 1:
        # Richiamiamo la funzione che calcola la somma dei numeri pari
        somma = somma_pari(lista)
        print("La somma dei numeri pari è:", somma)

    elif scelta == 2:
        # Richiamiamo la funzione che stampa i numeri dispari
        stampa_dispari(lista)

    elif scelta == 3:
        #Richiamiamo la funzione per verificare se un numero è primo
        verifica_numero_utente()

    elif scelta == 4:
        # Richiamiamo la funzione che stampa i numeri primi della lista
        stampa_primi(lista)

    elif scelta == 5:
        # Richiamiamo la funzione che calcola la somma della lista
        somma_lista_prima(lista)

    elif scelta == 0:
        print("Programma terminato.")
        break

    else:
        print("Scelta non valida.")