# Inserimento dei dati

nome = input("Inserisci il nome: ")

eta = int(input("Inserisci l'età: "))

sesso = input("Inserisci il sesso M/F: ")

premium = input("Sei premium? si/no: ")


# Controllo nome
if nome == "":
    print("Errore: il nome non può essere vuoto")

# Controllo sesso (char = un solo carattere)
elif len(sesso) != 1:
    print("Errore: il sesso deve essere un solo carattere")

# Controllo premium
elif premium != "si" and premium != "no":
    print("Errore: devi inserire si oppure no")

else:

    # Trasformo premium in bool
    if premium == "si":
        premium = True
    else:
        premium = False


    # Creo la lista
    lista = [nome, eta, sesso, premium]

    print(lista)


    # Chiedo cosa modificare
    print("1 - Nome")
    print("2 - Età")
    print("3 - Sesso")
    print("4 - Premium")

    scelta = int(input("Cosa vuoi modificare? "))


    match scelta:

        case 1:
            nome = input("Inserisci il nuovo nome: ")

            if nome != "":
                lista[0] = nome
            else:
                print("Errore: nome vuoto")


        case 2:
            eta = int(input("Inserisci la nuova età: "))
            lista[1] = eta


        case 3:
            sesso = input("Inserisci il nuovo sesso: ")

            if len(sesso) == 1:
                lista[2] = sesso
            else:
                print("Errore: deve essere un solo carattere")


        case 4:
            premium = input("Sei premium? si/no: ")

            if premium == "si":
                lista[3] = True

            elif premium == "no":
                lista[3] = False

            else:
                print("Errore: inserisci si oppure no")


        case _:
            print("Scelta non valida")


    print("Lista finale:", lista)