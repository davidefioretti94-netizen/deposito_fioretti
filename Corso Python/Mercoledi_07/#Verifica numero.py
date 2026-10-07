risultati = []

while True:

    # Chiediamo un numero intero positivo
    n = int(input("Inserisci un numero intero positivo, oppure 0 per terminare: "))

    if n == 0:
        print("Risultati finali:", risultati)
        break

    # Ex1: Controlliamo che il numero sia positivo
    while n < 0:
        print("Il numero deve essere positivo")
        n = int(input("Inserisci un numero intero positivo: "))


    # Ex2: Somma dei numeri pari da 1 a n
    somma = 0

    for numero in range(2, n + 1, 2):
        somma = somma + numero

    print("La somma dei numeri pari è:", somma)


    # Ex3: Stampiamo i numeri dispari da 1 a n
    print("I numeri dispari sono:")

    for numero in range(1, n + 1, 2):
        print(numero)


    # Ex4: Controlliamo se n è un numero primo
    primo = True

    if n == 1:
        primo = False

    for numero in range(2, n):
        if n % numero == 0:
            primo = False

    if primo == True:
        print(n, "è un numero primo")
    else:
        print(n, "non è un numero primo")


    # Salviamo il risultato
    risultati.append(n)

    print("Risultati salvati:", risultati)