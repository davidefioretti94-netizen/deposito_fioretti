#Esercizio: Andare a creare un sistema ripetibile che permetta di inserire: 
# sia al fondo che nella posizione che vogliamo noi, modificare, stampare ed eliminare liste,
# che sono divise dal tipo che viene scelto.



# DEFINIZIONE DELLE LISTE
# Creiamo 4 liste vuote separate, una per ciascun tipo di dato.

lista_str = []    # Lista destinata a contenere le stringhe 
lista_int = []    # Lista destinata a contenere i numeri interi
lista_float = []  # Lista destinata a contenere i numeri decimali
lista_bool = []   # Lista destinata a contenere i valori booleani 


def seleziona_lista():
    
    #Funzione di supporto che mostra un menu all'utente per scegliere su quale lista operare.
    #Restituisce due valori:
    #1. La variabile della lista selezionata
    #2. Una stringa con il nome del tipo selezionato
    
    print("\nScegli tipo: 1.str | 2.int | 3.float | 4.bool")
    tipo = input("Tipo lista (1-4): ")

    if tipo == "1":
        return lista_str, "str"
    elif tipo == "2":
        return lista_int, "int"
    elif tipo == "3":
        return lista_float, "float"
    elif tipo == "4":
        return lista_bool, "bool"
    else:
        print("Tipo non valido!")
        return "", ""


def inserisci_elemento():
    
    #Funzione che permette di inserire un elemento in due modalità:
    #- In fondo alla lista (usando il metodo .append())
    #- In una posizione/indice specifico (usando il metodo .insert())
    
    lista, tipo = seleziona_lista()
    
    if tipo == "":
        return

    
    print("Inserisci il valore per la lista:", tipo)
    valore = input("Valore: ")
    
    pos_scelta = input("Vuoi inserirlo in fondo? (s/n): ")

    if pos_scelta == "s":
        # OPERAZIONE SULLE LISTE: .append(valore)
        lista.append(valore)
        print(" Elemento inserito in fondo!")
    else:
        # OPERAZIONE SULLE LISTE: len(lista)
        limite = len(lista)
        
        print("Inserisci la posizione (da 0 a", limite, "):")
        pos = int(input("Indice: "))

        if pos >= 0 and pos <= limite:
            # OPERAZIONE SULLE LISTE: .insert(posizione, valore)
            lista.insert(pos, valore)
            # Stampa pulita usando la virgola per unire testo e variabile
            print(" Elemento inserito in posizione", pos, "!")
        else:
            print(" Posizione fuori dai limiti!")


def modifica_elemento():
    
    #Funzione che sovrascrive un valore esistente all'interno di una lista dato un certo indice.
    
    lista, tipo = seleziona_lista()
    if tipo == "":
        return

    # OPERAZIONE SULLE LISTE: len(lista)
    if len(lista) == 0:
        print(" La lista", tipo, "è vuota!")
        return

    stampa_singola(lista, tipo)
    pos = int(input("Inserisci l'indice dell'elemento da modificare: "))

    if pos >= 0 and pos < len(lista):
        nuovo_valore = input("Inserisci il nuovo valore: ")
        vecchio = lista[pos]
        
        # OPERAZIONE SULLE LISTE: Modifica diretta tramite indice lista[pos] = nuovo_valore
        lista[pos] = nuovo_valore
        print(" Elemento modificato da '", vecchio, "' a '", nuovo_valore, "'!")
    else:
        print(" Indice non valido!")


def elimina_elemento():
    
    #Funzione per eliminare un singolo elemento per indice oppure svuotare interamente la lista.
    
    lista, tipo = seleziona_lista()
    if tipo == "":
        return

    if len(lista) == 0:
        print(" La lista", tipo, "è vuota!")
        return

    print("\n1. Elimina singolo elemento")
    print("2. Svuota interamente la lista")
    scelta = input("Scegli un'opzione (1/2): ")

    match scelta:
        case "1":
            stampa_singola(lista, tipo)
            pos = int(input("Inserisci l'indice da eliminare: "))
            
            if pos >= 0 and pos < len(lista):
                elemento = lista[pos]
                # OPERAZIONE SULLE LISTE: .remove(elemento)
                lista.remove(elemento)
                print(" Elemento '", elemento, "' rimosso!")
            else:
                print(" Indice non valido!")
                
        case "2":
            # OPERAZIONE SULLE LISTE: Ciclo while insieme a len() e .remove()
            while len(lista) > 0:
                lista.remove(lista[0])
            print(" La lista", tipo, "è stata svuotata!")
            
        case _:
            print(" Scelta non valida!")


def ordina_lista():
    
    #Funzione per ordinare gli elementi della lista selezionata.
    
    lista, tipo = seleziona_lista()
    if tipo == "":
        return

    if len(lista) == 0:
        print(" La lista", tipo, "è vuota!")
        return

    # OPERAZIONE SULLE LISTE: .sort()
    lista.sort()
    print(" La lista", tipo, "è stata ordinata!")


def stampa_singola(lista, tipo):
    
    #Funzione di supporto per stampare a schermo il contenuto di una specifica lista.
    
    print("\n--- Contenuto lista [", tipo, "] ---")
    
    if len(lista) == 0:
        print("(Lista vuota)")
    else:
        # OPERAZIONE SULLE LISTE: for con range(len(lista))
        for i in range(len(lista)):
            print(" Indice", i, ":", lista[i])


def stampa_tutto():
    
    #Funzione che stampa il contenuto di tutte e 4 le liste in un'unica operazione.
    
    titolo = ["=== STATO", "DI", "TUTTE", "LE", "LISTE ==="]
    print("\n")
    
    # OPERAZIONE SPLAT (*):
    print(*titolo)

    stampa_singola(lista_str, "str")
    stampa_singola(lista_int, "int")
    stampa_singola(lista_float, "float")
    stampa_singola(lista_bool, "bool")



# CICLO PRINCIPALE DEL PROGRAMMA

attivo = True

while attivo:
    print("\n--- MENU GESTIONE LISTE ---")
    print("1. Inserisci elemento")
    print("2. Modifica elemento")
    print("3. Elimina elemento o svuota lista")
    print("4. Ordina una lista")
    print("5. Stampa tutte le liste")
    print("6. Stampa una singola lista")
    print("7. Esci")

    scelta = input("Seleziona un'operazione (1-7): ")

    match scelta:
        case "1":
            inserisci_elemento()
        case "2":
            modifica_elemento()
        case "3":
            elimina_elemento()
        case "4":
            ordina_lista()
        case "5":
            stampa_tutto()
        case "6":
            lista, tipo = seleziona_lista()
            if tipo != "":
                stampa_singola(lista, tipo)
        case "7":
            print("Chiusura del programma. Arrivederci!")
            attivo = False
        case _:
            print(" Opzione non valida! Riprova.")