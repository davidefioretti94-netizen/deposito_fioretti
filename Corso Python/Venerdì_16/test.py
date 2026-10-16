#FASE 1. CLASSE PADRE
class Elettrodomestico:
    # Costruttore con attributi privati
    def __init__(self, marca, modello, anno_acquisto, guasto):
        self.__marca = marca                    # Salva la marca
        self.__modello = modello                # Salva il modello
        self.__anno_acquisto = anno_acquisto    # Salva l'anno di acquisto
        self.__guasto = guasto                  # Salva la descrizione del guasto

    #GETTER E SETTER PER ACCEDERE AGLI ATTRIBUTI PRIVATI
    def get_marca(self):
        return self.__marca    #Restituisce la marca dell'elettrodomestico

    def set_marca(self, marca):
        self.__marca = marca   #Modifica il valore della marca

    def get_modello(self):
        return self.__modello   #Restituisce il modello dell'elettrodomestico

    def set_modello(self, modello):
        self.__modello = modello   #Modifica il valore del modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto  #Restituisce l'anno di acquisto

    def set_anno_acquisto(self, anno_acquisto):
        # Controllo di validità: l'anno non può essere nel futuro (maggiore di 2026)
        if anno_acquisto > 2026:
            print("Errore: L'anno non può essere nel futuro! Impostato 2026.")
            self.__anno_acquisto = 2026 #Se errato, imposta l'anno di default 2026
        else:
            self.__anno_acquisto = anno_acquisto  # Se valido, imposta l'anno inserito dall'utente

    def get_guasto(self):
        return self.__guasto  # Restituisce il testo del guasto

    def set_guasto(self, guasto):
        self.__guasto = guasto    # Modifica la descrizione del guasto

    # Restituisce una stringa con tutti i dettagli dell'elettrodomestico
    def descrizione(self):
        return "Marca: " + self.__marca + " | Modello: " + self.__modello + " | Anno: " + str(self.__anno_acquisto) + " | Guasto: " + self.__guasto

    # Costo base di diagnosi generico per qualsiasi elettrodomestico
    def stima_costo_base(self):
        return 30.0  # Restituisce il valore numerico di partenza (30 €)



# FASE 2. CLASSI DERIVATE
# 1). Sottoclasse Lavatrice
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)  # Eredita gli attributi dal padre
        self.capacita_kg = capacita_kg                            # Attributo extra per la capacità
        self.giri_centrifuga = giri_centrifuga                    # Attributo extra per i giri

    # Sovrascrittura del metodo stima_costo_base
    def stima_costo_base(self):
        costo = 40.0
        # Maggiorazione se la capacità supera i 7 kg
        #Se la lavatrice supera i 7 kg, aggiunge un costo extra di 15 € al prezzo base
        if self.capacita_kg > 7:
            costo = costo + 15.0
        return costo


# 2. Sottoclasse Frigorifero
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)  # Eredita gli attributi dal padre
        self.litri = litri                                        # Attributo extra per la capienza
        self.ha_freezer = ha_freezer                              # Attributo extra booleano

    # Sovrascrittura del metodo stima_costo_base
    def stima_costo_base(self):
        costo = 50.0
        # Maggiorazione se ha il freezer o se la capienza supera i 300 litri
        if self.ha_freezer:
            #Maggiorazione di 10 euro se ha il freezer
            costo = costo + 10.0
        if self.litri > 300:
            #Maggiorazione di 20 euro se supera i 300 litri
            costo = costo + 20.0
        return costo


# 3. Sottoclasse Forno
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)  # Eredita gli attributi dal padre
        self.tipo_alimentazione = tipo_alimentazione.lower()      # Attributo extra ("elettrico" o "gas")
        self.ha_ventilato = ha_ventilato                          # Attributo extra booleano

    # Sovrascrittura del metodo stima_costo_base
    def stima_costo_base(self):
        costo = 35.0
        # Maggiorazione se alimentato a gas o se ha la funzione ventilata
        if self.tipo_alimentazione == "gas":
           # Se il forno è alimentato a gas,si aggiungono 15 €
            costo = costo + 15.0
        if self.ha_ventilato:
            # Se il forno ha la funzione ventilata, si aggiungono 10 €
            costo = costo + 10.0
        return costo



#FASE 3. CLASSE TicketRiparazione
class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket                        # ID univoco privato
        self.__elettrodomestico = elettrodomestico          # Oggetto elettrodomestico privato
        self.__stato = "aperto"                             # Stato iniziale privato
        self.__note = []                                    # Lista note inizialmente vuota

    # GETTER E SETTER
    def get_id_ticket(self):
        return self.__id_ticket   # Restituisce l'ID del ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico    # Restituisce l'oggetto elettrodomestico

    def get_stato(self):
        return self.__stato   # Restituisce lo stato attuale del ticket

    def set_stato(self, stato):
        self.__stato = stato   # Modifica lo stato

    def get_note(self):
        return self.__note   # Restituisce la lista delle note

    # Metodo per aggiungere una nota alla lista
    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    # METODO VARIADICO: accetta un numero qualsiasi di costi aggiuntivi
    def calcola_preventivo(self, *voci_extra):
        #Richiama il metodo stima_costo_base specifico dell'elettrodomestico
        totale = self.__elettrodomestico.stima_costo_base()
        # Somma tutte le voci extra passate al metodo
        for voce in voci_extra:
            totale = totale + voce
        return totale



#FASE 4. CLASSE Officina

class Officina:
    # Costruttore per inizializzare l'officina
    def __init__(self, nome):
        self.nome = nome # Salva il nome dell'officina
        self.tickets = []  # Crea una lista vuota per contenere i ticket

    # Aggiunge un ticket alla lista dell'officina
    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)
        print("Ticket #" + str(ticket.get_id_ticket()) + " aggiunto con successo!")

    # Cambia lo stato di un determinato ticket in chiuso
    def chiudi_ticket(self, id_ticket):
        trovato = False # Variabile di controllo
        for t in self.tickets: # Scorre tutti i ticket presenti nella lista
            if t.get_id_ticket() == id_ticket:  # Se l'ID corrisponde a quello cercato
                t.set_stato("chiuso")   # Modifica lo stato in chiuso
                print("Ticket" + str(id_ticket) + " impostato come CHIUSO.")
                trovato = True # Segnala che l'ha trovato
                break  # Esce dal ciclo
        if not trovato:
            print("Ticket #" + str(id_ticket) + " non trovato!")

    # Mostra l'elenco dei ticket che risultano ancora aperti
    def stampa_ticket_aperti(self):
        print("\n--- TICKET APERTI ---")
        trovati = False  # Variabile di controllo
        for t in self.tickets:   # Scorre tutti i ticket
            if t.get_stato() == "aperto": # Controlla se lo stato è aperto
                elettro = t.get_elettrodomestico() # Prende l'oggetto elettrodomestico contenuto nel ticket
                # Stampa ID, tipo della classe dell'elettrodomestico usando type() e lo stato
                print("ID Ticket: " + str(t.get_id_ticket()) + " | Tipo: " + type(elettro).__name__ + " | Stato: " + t.get_stato())
                print("   Dettagli: " + elettro.descrizione()) # Stampa la descrizione dettagliata
                trovati = True # Segnala che c'è almeno un ticket aperto
        if not trovati:
            print("Nessun ticket attualmente aperto.")

    # Somma il preventivo di tutti i ticket presenti
    def totale_preventivi(self):
        totale = 0.0 # Inizializza il totale a 0
        for t in self.tickets: # Scorre ciascun ticket
            totale = totale + t.calcola_preventivo()  # Somma il preventivo di ciascun ticket
        return totale

    #REQUISITO 5: Conta quante lavatrici, frigoriferi o forni ci sono usando type()
    def statistiche_per_tipo(self):
        num_lavatrici = 0  # Inizializza il contatore per le lavatrici
        num_frigoriferi = 0 # Inizializza il contatore per i frigoriferi
        num_forni = 0 # Inizializza il contatore per i forni

        for t in self.tickets:   # Scorre tutti i ticket della lista
            elettro = t.get_elettrodomestico() # Estrae l'elettrodomestico dal ticket
            # Uso di type() per identificare la classe reale dell'oggetto associato
            if type(elettro) == Lavatrice:
                num_lavatrici = num_lavatrici + 1
            elif type(elettro) == Frigorifero:
                num_frigoriferi = num_frigoriferi + 1
            elif type(elettro) == Forno:
                num_forni = num_forni + 1   
        
        # Stampa i risultati del conteggio
        print("\n=== STATISTICHE RIPARAZIONI PER TIPO ===")
        print("Numero di lavatrici in riparazione: " + str(num_lavatrici))
        print("Numero di frigoriferi in riparazione: " + str(num_frigoriferi))
        print("Numero di forni in riparazione: " + str(num_forni))



#FASE 5: MENU

officina = Officina("Officina RiparaTutto")   # Istanzia l'oggetto della classe Officina
prossimo_id_ticket = 1   # Contatore progressivo per l'ID dei nuovi ticket
scelta = ""   # Variabile per contenere la scelta dell'utente

# Ciclo che ripete il menu fino a quando l'utente non inserisce "6"
while scelta != "6":
    print("\n--- MENU OFFICINA " + officina.nome + " ---")
    print("1 - Apri nuovo Ticket Riparazione")
    print("2 - Mostra Ticket Aperti")
    print("3 - Calcola Preventivo Ticket (con voci extra)")
    print("4 - Mostra Statistiche per Tipo (uso di type())")
    print("5 - Chiudi Ticket")
    print("6 - Esci")

    scelta = input("Seleziona un'opzione (1-6): ")

    # OPZIONE 1: CREA NUOVO TICKET
    if scelta == "1":
        print("\nSeleziona il tipo di elettrodomestico:")
        print("1 = Lavatrice | 2 = Frigorifero | 3 = Forno")
        tipo_e = input("Scegli: ") #Legge la sottoclasse da creare

        marca = input("Marca: ")      # Legge la marca
        modello = input("Modello: ")  #Legge il modello
        anno = int(input("Anno acquisto: "))  #Legge l'annata e lo converte in intero
        guasto = input("Descrizione guasto: ") # Legge la descrizione del problema
        
        # Creazione di un oggetto della sottoclasse Lavatrice
        if tipo_e == "1":
            kg = int(input("Capacità in kg: "))
            giri = int(input("Giri centrifuga: "))
            elettro = Lavatrice(marca, modello, anno, guasto, kg, giri)
        # Creazione di un oggetto della sottoclasse Frigorifero
        elif tipo_e == "2":
            litri = int(input("Litri di capienza: "))
            freezer_str = input("Ha il freezer? (si/no): ").lower()
            ha_freezer = (freezer_str == "si")
            elettro = Frigorifero(marca, modello, anno, guasto, litri, ha_freezer)
       # Creazione di un oggetto della sottoclasse Forno
        elif tipo_e == "3":
            alim = input("Alimentazione (elettrico/gas): ")
            vent_str = input("È ventilato? (si/no): ").lower()
            ha_ventilato = (vent_str == "si")  # Converte la risposta "si" in valore booleano True/False
            elettro = Forno(marca, modello, anno, guasto, alim, ha_ventilato)
        else:
            print("Tipo non valido! Creazione annullata.")
            elettro = None   # Se la scelta è errata, l'oggetto rimane vuoto
        
        # Se l'elettrodomestico è stato creato correttamente
        if elettro != None:
            t = TicketRiparazione(prossimo_id_ticket, elettro)  # Crea il ticket associando l'oggetto
            officina.aggiungi_ticket(t) # Salva il ticket nella lista dell'officina
            prossimo_id_ticket = prossimo_id_ticket + 1 # Incrementa l'ID per il prossimo ticket

    # OPZIONE 2: MOSTRA ELENCO TICKET APERTI
    elif scelta == "2":
        officina.stampa_ticket_aperti()

    # OPZIONE 3: CALCOLA PREVENTIVO CON METODO VARIADICO (*voci_extra)
    elif scelta == "3":
        id_t = int(input("Inserisci ID Ticket per il preventivo: "))  # Legge l'ID del ticket da calcolare
        trovato = False   # Variabile per verificare l'esistenza dell'ID
        for t in officina.tickets:   # Scorre la lista dei ticket dell'officina
            if t.get_id_ticket() == id_t:  # Se trova il ticket con l'ID richiesto
                trovato = True # Segnala che è stato trovato
                print("Inserisci 2 voci extra di costo (es. pezzi di ricambio). Inserisci 0 se nessuna.")
                ricambio = float(input("Costo pezzo ricambio (€): "))  # Legge il costo del ricambio
                manodopera_extra = float(input("Manodopera extra (€): "))  # Legge il costo della manodopera
                
                # Chiamata al metodo variadico passandogli i costi extra come argomento
                totale = t.calcola_preventivo(ricambio, manodopera_extra)
                print("\nPreventivo calcolato per Ticket #" + str(id_t) + ": €" + str(totale))
                break
        if not trovato:
            print("Ticket non trovato!")

    # OPZIONE 4: STATISTICHE PER TIPO, USO DI type
    elif scelta == "4":
        officina.statistiche_per_tipo() 

    # OPZIONE 5: CHIUDI TICKET
    elif scelta == "5":
        id_t = int(input("Inserisci ID Ticket da chiudere: "))  #Legge l'ID del ticket da chiudere
        officina.chiudi_ticket(id_t)   #Richiama il metodo di chiusura

    # OPZIONE 6: ESCI
    elif scelta == "6":
        print("Uscita dal gestionale officina. Arrivederci!")

    else:
        print("Opzione non valida! Riprova.")