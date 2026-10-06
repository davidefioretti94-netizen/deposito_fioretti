# Creo una lista vuota
lista = []


# Inserimento dati
nome = input("Inserisci il nome: ")

eta = int(input("Inserisci l'età: "))

sesso = input("Inserisci il sesso M/F: ")

premium = input("Sei premium Si/No: ")


# Controllo dei dati inseriti
if nome == "":
    print("Errore! Il nome non può essere vuoto")

elif eta <= 0:
    print("Errore! Età non valida")

elif len(sesso) != 1:
    print("Errore! Il sesso deve essere un solo carattere")

elif premium != "Si" and premium != "No":
    print("Errore! Devi inserire Si oppure No")

else:

    # Converto premium in booleano
    if premium == "Si":
        premium = True
    else:
        premium = False


    # Inserisco i dati nella lista vuota
    lista.append(nome)
    lista.append(eta)
    lista.append(sesso)
    lista.append(premium)


    # Visualizzo la lista
    print("Lista:", lista)


    # Chiedo quale dato modificare
    print("1 - Nome")
    print("2 - Età")
    print("3 - Sesso")
    print("4 - Premium")

    scelta = input("Quale dato vuoi modificare? ")


    # Modifica del dato scelto
    match scelta:

        case "1":
            nome = input("Inserisci il nuovo nome: ")

            if nome == "":
                print("Errore! Il nome non può essere vuoto")
            else:
                lista[0] = nome


        case "2":
            eta = int(input("Inserisci la nuova età: "))

            if eta <= 0:
                print("Errore! Età non valida")
            else:
                lista[1] = eta


        case "3":
            sesso = input("Inserisci il nuovo sesso M/F: ")

            if len(sesso) != 1:
                print("Errore! Il sesso deve essere un solo carattere")
            else:
                lista[2] = sesso


        case "4":
            premium = input("Sei premium Si/No: ")

            if premium == "Si":
                lista[3] = True

            elif premium == "No":
                lista[3] = False

            else:
                print("Errore! Devi inserire Si oppure No")


        case _:
            print("Scelta non valida")


    # Visualizzo la lista dopo la modifica
    print("Lista finale:", lista)