# DEFINIZIONE DELLA CLASSE PADRE
class Prodotto:
    # Costruttore: si attiva quando creiamo un nuovo prodotto
    def __init__(self, nome, quantita):
        self.nome = nome            # Salva il nome del prodotto
        self.quantita = quantita    # Salva la quantità prodotta


# DEFINIZIONE DELLA CLASSE FIGLIO
class PezzoProdotto(Prodotto):
    # Costruttore: richiama il costruttore della classe padre Prodotto
    def __init__(self, nome, quantita):
        super().__init__(nome, quantita)  #Eredita nome e quantità dal padre

    # Metodo per stampare le informazioni del prodotto
    def mostra(self):
        print("Prodotto:", self.nome, "| Quantità:", self.quantita)


# CREAZIONE DELLA LISTA PER CONTENERE TUTTI I PRODOTTI
prodotti = []  

# VARIABILE PER GESTIRE LA SCELTA DEL MENU
scelta = ""  

# CICLO CHE RIPETE IL MENU FINCHÉ NON DIGIT0 "7"
while scelta != "7":
    # menu
    print("\n--- MENU PRODUZIONE ---")
    print("1 - Aggiungi prodotto")
    print("2 - Visualizza produzione")
    print("3 - Cerca prodotto")
    print("4 - Modifica quantità")
    print("5 - Rimuovi prodotto")
    print("6 - Calcola totale pezzi prodotti")
    print("7 - Esci")

    scelta = input("Scegli un'opzione (1-7): ")

    # OPZIONE 1: AGGIUNGI UN NUOVO PRODOTTO
    if scelta == "1":
        nome = input("Inserisci il nome del prodotto: ")        
        quantita = int(input("Inserisci la quantità: "))       
        
        p = PezzoProdotto(nome, quantita)  # Crea l'oggetto della classe figlio
        prodotti.append(p)     # Aggiunge il prodotto appena creato alla lista
        print("Prodotto registrato con successo!")             

    # OPZIONE 2: VISUALIZZA LA PRODUZIONE DI TUTTA LA GIORNATA
    elif scelta == "2":
        print("\n--- PRODUZIONE DEL GIORNO ---")
        # Se la lista dei prodotti è vuota
        if len(prodotti) == 0:
            print("Nessun prodotto registrato.")
        # Altrimenti mostra tutti i prodotti
        else:
            # Ciclo for che scorre ogni singolo elemento presente nella lista prodotti
            for p in prodotti:
                p.mostra()# Esegue il metodo mostra() per ogni prodotto

    # OPZIONE 3: CERCA UN PRODOTTO PER NOME
    elif scelta == "3":
        cerca = input("Nome del prodotto da cercare: ")       
        # Controlla tutti i prodotti nella lista uno alla volta
        for p in prodotti:
            # Se il nome del prodotto corrisponde a quello cercato
            if p.nome == cerca:
                p.mostra()# Mostra i dettagli del prodotto trovato

    # OPZIONE 4: MODIFICA LA QUANTITÀ DI UN PRODOTTO GIÀ ESISTENTE
    elif scelta == "4":
        cerca = input("Nome del prodotto da modificare: ")     
        #Scorre la lista dei prodotti
        for p in prodotti:
            #Se trova il prodotto cercato
            if p.nome == cerca:
                nuova_qta = int(input("Inserisci la nuova quantità: "))#Chiede la nuova quantità numerica
                p.quantita = nuova_qta #Aggiorna il valore dentro l'oggetto
                print("Quantità modificata!")                  

    # OPZIONE 5: RIMUOVI UN PRODOTTO DALLA LISTA
    elif scelta == "5":
        cerca = input("Nome del prodotto da rimuovere: ")      
        # Scorre la lista dei prodotti
        for p in prodotti:
            # Se trova il prodotto
            if p.nome == cerca:
                prodotti.remove(p) # Rimuove l'oggetto p dalla lista
                print("Prodotto rimosso!")                     

    # OPZIONE 6: CALCOLA IL TOTALE DEI PEZZI PRODOTTI
    elif scelta == "6":
        totale = 0  # Inizializza il contatore del totale a zero
        # Scorre ciascun prodotto presente nella lista
        for p in prodotti:
            totale = totale + p.quantita # Somma la quantità del prodotto al totale
        print("Totale pezzi prodotti oggi:", totale)         

    # OPZIONE 7: CHIUSURA DEL PROGRAMMA
    elif scelta == "7":
        print("Uscita dal programma")            

    # SCELTA NON VALIDA
    else:
        print("Scelta non valida, riprova!")                  