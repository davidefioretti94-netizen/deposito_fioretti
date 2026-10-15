# IMPORTIAMO IL MODULO ABC PER CREARE LE CLASSI ASTRATTE
from abc import ABC, abstractmethod


# DEFINIZIONE DELLA CLASSE ASTRATTA PADRE
class Impiegato(ABC):
    # Costruttore: accetta nome, cognome e stipendio base
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome                        # Salva il nome dell'impiegato
        self.cognome = cognome                  # Salva il cognome dell'impiegato
        self.stipendio_base = stipendio_base    # Salva lo stipendio base

    # Metodo astratto: non ha codice qui, dovra essere implementato dai figli
    @abstractmethod
    def calcola_stipendio(self):
        pass


# DEFINIZIONE DELLA PRIMA CLASSE FIGLIO (IMPIEGATO FISSO)
class ImpiegatoFisso(Impiegato):
    # Costruttore: richiama il costruttore della classe padre
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)  # Eredita nome, cognome e stipendio base

    # Implementazione del metodo astratto: restituisce lo stipendio base senza modifiche
    def calcola_stipendio(self):
        return self.stipendio_base


# DEFINIZIONE DELLA SECONDA CLASSE FIGLIO (IMPIEGATO A PROVVIGIONE)
class ImpiegatoAProvvigione(Impiegato):
    # Costruttore: aggiunge anche le vendite e la percentuale di provvigione
    def __init__(self, nome, cognome, stipendio_base, vendite, provvigione):
        super().__init__(nome, cognome, stipendio_base)  # Eredita i dati base dal padre
        self.vendite = vendite                          # Salva il totale delle vendite
        self.provvigione = provvigione                  # Salva la percentuale (es. 0.10 per il 10%)

    # Implementazione del metodo astratto: stipendio base + bonus sulle vendite
    def calcola_stipendio(self):
        bonus = self.vendite * self.provvigione
        return self.stipendio_base + bonus


# FUNZIONE PER STAMPARE LE INFORMAZIONI DEGLI IMPIEGATI
def stampa_info_impiegato(impiegato):
    stipendio_totale = impiegato.calcola_stipendio()     # Calcola lo stipendio mensile
    print("Impiegato:", impiegato.nome, impiegato.cognome) # Stampa nome e cognome
    print("Stipendio Mensile: €", stipendio_totale)        # Stampa lo stipendio finale
    print("-" * 35)                                        # Riga separatrice per ordine


# CREAZIONE DELLA LISTA PER CONTENERE GLI IMPIEGATI
azienda = []  

# VARIABILE PER GESTIRE LA SCELTA DEL MENU
scelta = ""  

# CICLO CHE RIPETE IL MENU FINCHÉ L'UTENTE NON DIGITA "4"
while scelta != "4":
    # Stampa a schermo le opzioni del menu
    print("\n--- GESTIONE IMPIEGATI AZIENDA ---")
    print("1 - Aggiungi Impiegato Fisso")
    print("2 - Aggiungi Impiegato a Provvigione")
    print("3 - Visualizza tutti gli impiegati e stipendi")
    print("4 - Esci")

    # Chiede all'utente di inserire il numero dell'opzione
    scelta = input("Scegli un'opzione (1-4): ")

    # OPZIONE 1: AGGIUNGI IMPIEGATO FISSO
    if scelta == "1":
        nome = input("Inserisci il nome: ")                     # Legge il nome
        cognome = input("Inserisci il cognome: ")               # Legge il cognome
        stipendio_base = float(input("Inserisci lo stipendio base (€): ")) # Legge lo stipendio numerico
        
        emp = ImpiegatoFisso(nome, cognome, stipendio_base)     # Crea l'oggetto ImpiegatoFisso
        azienda.append(emp)                                     # Lo aggiunge alla lista
        print("Impiegato fisso registrato con successo!")       # Messaggio di conferma

    # OPZIONE 2: AGGIUNGI IMPIEGATO A PROVVIGIONE
    elif scelta == "2":
        nome = input("Inserisci il nome: ")                     # Legge il nome
        cognome = input("Inserisci il cognome: ")               # Legge il cognome
        stipendio_base = float(input("Inserisci lo stipendio base (€): ")) # Legge lo stipendio base
        vendite = float(input("Inserisci l'importo totale vendite (€): ")) # Legge l'ammontare delle vendite
        provvigione = float(input("Inserisci la % di provvigione (es. 0.10 per 10%): ")) # Legge la percentuale
        
        emp = ImpiegatoAProvvigione(nome, cognome, stipendio_base, vendite, provvigione) # Crea l'oggetto
        azienda.append(emp)                                     # Lo aggiunge alla lista
        print("Impiegato a provvigione registrato con successo!") # Messaggio di conferma

    # OPZIONE 3: VISUALIZZA TUTTI GLI IMPIEGATI E STIPENDI
    elif scelta == "3":
        print("\n=== ELENCO IMPIEGATI E STIPENDI ===")
        # Controlla se la lista dell'azienda è vuota
        if len(azienda) == 0:
            print("Nessun impiegato presente nel sistema.")     # Avvisa che non ci sono elementi
        else:
            # Scorre ciascun impiegato presente nella lista
            for emp in azienda:
                stampa_info_impiegato(emp)                      # Invoca la funzione di stampa dedicata

    # OPZIONE 4: ESCI DAL PROGRAMMA
    elif scelta == "4":
        print("Uscita dal programma. Arrivederci!")            # Messaggio prima di fermare il ciclo

    # SCELTA NON VALIDA
    else:
        print("Scelta non valida, riprova!")                  # Avvisa in caso di tasto errato