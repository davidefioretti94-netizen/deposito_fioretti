
# DEFINIZIONE DELLE FUNZIONI PER LA GESTIONE DEI FILE


# 1. FUNZIONE PER CREARE O SOVRASCRIVERE UN FILE
def crea_file():

    nome_file = input("Inserisci il nome del file da creare (es. ciccio.txt): ")
    
    testo = input("Inserisci il testo da scrivere nel file: ")
    
    file = open(nome_file, "w")
    
    file.write(testo + "\n")
    
    file.close()
    
    print("File", nome_file, "creato con successo!")


# 2. FUNZIONE PER MODIFICARE UN FILE
def modifica_file():
   
    nome_file = input("Inserisci il nome del file da modificare: ")
    
    testo = input("Inserisci il testo da aggiungere in coda: ")
    
    file = open(nome_file, "a")
    
    file.write(testo + "\n")
    
    file.close()
    
    print("Testo aggiunto al file", nome_file, "con successo!")


# 3. FUNZIONE PER LEGGERE IL CONTENUTO DI UN FILE
def leggi_file():
    
    nome_file = input("Inserisci il nome del file da leggere: ")
    
    file = open(nome_file, "r")
    
    contenuto = file.read()

    file.close()
    
    print("\n--- CONTENUTO DI", nome_file, "---")
    
    print(contenuto)


# 4. FUNZIONE PER SVUOTARE UN FILE SENZA CANCELLARLO
def svuota_file():
   
    nome_file = input("Inserisci il nome del file da svuotare: ")
    
    file = open(nome_file, "w")
    
    file.close()
    
    print("Il file", nome_file, "è stato svuotato con successo!")



# MENU INTERATTIVO

scelta = ""

while scelta != "5":
    print("\n--- GESTIONE FILE (CON FUNZIONI) ---")
    print("1 - Creare un file")
    print("2 - Modificare un file")
    print("3 - Leggere un file")
    print("4 - Svuotare un file")
    print("5 - Esci")

    scelta = input("Scegli un'opzione (1-5): ")

    # Se l'utente ha digitato "1": richiama la funzione per creare il file
    if scelta == "1":
        crea_file()

    # Se l'utente ha digitato "2": richiama la funzione per modificare il file
    elif scelta == "2":
        modifica_file()

    # Se l'utente ha digitato "3": richiama la funzione per leggere il file
    elif scelta == "3":
        leggi_file()

    # Se l'utente ha digitato "4": richiama la funzione per svuotare il file
    elif scelta == "4":
        svuota_file()

    # Se l'utente ha digitato "5": stampa il messaggio di chiusura prima di fermare il ciclo while
    elif scelta == "5":
        print("Arrivederci!")

    # Se l'utente digita un qualsiasi tasto o numero che non sia compreso tra 1 e 5
    else:
        print("Opzione non valida, riprova!")