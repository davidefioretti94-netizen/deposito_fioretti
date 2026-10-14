# DEFINIZIONE DELLA CLASSE PADRE
class Posto:
    # Metodo costruttore: crea un nuovo posto con numero e fila
    def __init__(self, numero, fila):
        self._numero = numero     # Salva il numero del posto
        self._fila = fila         # Salva la fila del posto
        self._occupato = False    # Imposta lo stato iniziale a False (libero)
    
    # Restituisce il numero del posto
    def get_numero(self):
        return self._numero
    
    # Restituisce la fila del posto
    def get_fila(self):
        return self._fila
    
    # Restituisce True se il posto è occupato, False se è libero
    def is_occupato(self):
        return self._occupato
    
    # Metodo per prenotare il posto
    def prenota(self):
        # Se il posto NON è occupato
        if not self._occupato:
            self._occupato = True  # Cambia lo stato in occupato
            print("Posto prenotato!")
        else:
            print("Posto già occupato!")
    
    # Metodo per liberare il posto
    def libera(self):
        # Se il posto è occupato
        if self._occupato:
            self._occupato = False     # Cambia lo stato in libero
            print("Posto liberato!")
        else:
            print("Il posto era già libero.")

# DEFINIZIONE DELLA CLASSE DERIVATA
class PostoVIP(Posto):
    # Costruttore che aggiunge la lista dei servizi extra
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)   # Chiama il costruttore della classe Posto
        self.servizi_extra = servizi_extra  # Salva i servizi extra (es. ["Bevanda inclusa"])
    
    # Modifica il metodo prenota per includere i servizi VIP
    def prenota(self):
        if not self._occupato:
            self._occupato = True # Imposta come occupato
            print("Posto VIP prenotato! Servizi:", self.servizi_extra)
        else:
            print("Posto VIP già occupato!")

# DEFINIZIONE DELLA CLASSE DERIVATA
class PostoStandard(Posto):
    # Costruttore che aggiunge il prezzo del posto
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila) # Chiama il costruttore della classe Posto
        self.costo = costo   # Salva il prezzo (es. 20)
    
    # Modifica il metodo prenota per mostrare il costo
    def prenota(self):
        if not self._occupato:
            self._occupato = True # Imposta come occupato
            print("Posto Standard prenotato! Costo:", self.costo, "€")
        else:
            print("Posto Standard già occupato!")

# DEFINIZIONE DELLA CLASSE "TEATRO" PER GESTIRE TUTTI I POSTI
class Teatro:
    # Costruttore che crea la lista vuota per contenere i posti
    def __init__(self):
        self._posti = []  # Lista dove salveremo tutti gli oggetti Posto
    
    # Aggiunge un nuovo posto alla lista del teatro
    def aggiungi_posto(self, posto):
        self._posti.append(posto)   # Inserisce il posto nella lista
    
    
    # Cerca un posto per numero e fila e prova a prenotarlo
    def prenota_posto(self, numero, fila):
        # Esamina ogni posto presente nella lista uno alla volta
        for p in self._posti:
            # Controlla se numero e fila corrispondono a quelli cercati
            if p.get_numero() == numero and p.get_fila() == fila:
                p.prenota()  # Esegue la prenotazione sul posto trovato
    
    # Mostra tutti i posti attualmente prenotati
    def stampa_posti_occupati(self):
        print("--- Posti occupati ---")
        # Controlla tutti i posti nella lista
        for p in self._posti:
            if p.is_occupato():
                # Se il posto risulta occupato, stampa i suoi dettagli
                print("Fila:", p.get_fila(), "Numero:", p.get_numero())


# CREAZIONE TEATRO (3 FILE x 3 POSTI = 9 POSTI)
teatro = Teatro()   # Crea l'oggetto teatro

# Fila A (VIP)
teatro.aggiungi_posto(PostoVIP(1, "A", ["Bevanda inclusa"]))
teatro.aggiungi_posto(PostoVIP(2, "A", ["Bevanda inclusa"]))
teatro.aggiungi_posto(PostoVIP(3, "A", ["Bevanda inclusa"]))

# Fila B (STANDARD-2O EURO)
teatro.aggiungi_posto(PostoStandard(1, "B", 20))
teatro.aggiungi_posto(PostoStandard(2, "B", 20))
teatro.aggiungi_posto(PostoStandard(3, "B", 20))

# Fila C (Standard-15 EURO)
teatro.aggiungi_posto(PostoStandard(1, "C", 15))
teatro.aggiungi_posto(PostoStandard(2, "C", 15))
teatro.aggiungi_posto(PostoStandard(3, "C", 15))


# INPUT UTENTE E MENU
scelta = ""  # Variabile per memorizzare l'opzione
# Ciclo che continua finché l'utente non digita "3" per uscire
while scelta != "3":
    print("\n1. Prenota posto")
    print("2. Mostra posti occupati")
    print("3. Esci")
    
    scelta = input("Scegli: ")

    if scelta == "1":
        fila = input("Inserisci fila (A, B, C): ")
        numero = int(input("Inserisci numero (1, 2, 3): "))
        teatro.prenota_posto(numero, fila)  # Chiama il metodo per prenotare
    
    
    elif scelta == "2":
        teatro.stampa_posti_occupati()   # Mostra l'elenco dei posti occupati
        
  
    elif scelta == "3":
        print("Uscita dal programma.")

    # Se l'utente inserisce qualsiasi altro valore non valido
    else:
        print("Scelta non valida! Riprova.")