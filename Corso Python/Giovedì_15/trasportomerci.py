# IMPORTIAMO IL MODULO ABC PER CREARE LA CLASSE ASTRATTA
from abc import ABC, abstractmethod


# 1. CLASSE ASTRATTA: VeicoloTrasporto 
class VeicoloTrasporto(ABC):
    # Costruttore: inizializza gli attributi protetti
    def __init__(self, targa, peso_massimo, tipo):
        self._targa = targa                  # Salva la targa del veicolo
        self._peso_massimo = peso_massimo    # Salva la capacità di carico massima in kg
        self._carico_attuale = 0             # Imposta il carico iniziale a 0 kg
        self._tipo = tipo                    # Salva il nome del tipo di veicolo

    # METODI GETTER PER L'INCAPSULAMENTO
    def get_targa(self):
        return self._targa                   # Restituisce la targa del veicolo

    def get_peso_massimo(self):
        return self._peso_massimo            # Restituisce il peso massimo trasportabile

    def get_carico_attuale(self):
        return self._carico_attuale          # Restituisce il carico di merci attuale

    def get_tipo(self):
        return self._tipo                    # Restituisce la stringa con il tipo di veicolo

    # Metodo concreto: Aumenta il carico se non supera la capacita massima
    def carica(self, peso):
        # Controlla se il nuovo totale rientra nel limite massimo
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale = self._carico_attuale + peso  # Aggiunge il peso al carico
            print("Caricato con successo! Carico attuale:", self._carico_attuale, "kg")
        else:
            print("Errore: Il peso inserito supera la capacità massima!")

    # Metodo concreto: Riporta il carico attuale a 0 kg
    def scarica(self):
        self._carico_attuale = 0             # Svuota il veicolo
        print("Veicolo scaricato! Carico attuale: 0 kg")

    # METODO ASTRATTO: Ogni sottoclasse implementerà la propria regola
    @abstractmethod
    def costo_manutenzione(self):
        pass



# 2. SOTTOCLASSI CONCRETE
# a) 
class Camion(VeicoloTrasporto):
    # Costruttore: passa "Camion" come tipo alla classe padre
    def __init__(self, targa, peso_massimo, numero_assi):
        super().__init__(targa, peso_massimo, "Camion")  # Inizializza i dati del padre
        self.numero_assi = numero_assi                    # Salva il numero di assi

    #Calcola la manutenzione (100 € per asse + 1 € per kg di peso massimo)
    def costo_manutenzione(self):
        return (100 * self.numero_assi) + (1 * self._peso_massimo)


# b) 
class Furgone(VeicoloTrasporto):
    # Costruttore: passa "Furgone" come tipo alla classe padre
    def __init__(self, targa, peso_massimo, alimentazione):
        super().__init__(targa, peso_massimo, "Furgone")  # Inizializza i dati del padre
        self.alimentazione = alimentazione.lower()        # Salva l'alimentazione

    #Calcola la manutenzione (200 € per elettrico, 150 € per diesel)
    def costo_manutenzione(self):
        if self.alimentazione == "elettrico":
            return 200
        else:
            return 150


# c)
class Motocarro(VeicoloTrasporto):
    # Costruttore: passa "Motocarro" come tipo alla classe padre
    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo, "Motocarro")  # Inizializza i dati del padre
        self.anni_servizio = anni_servizio                  # Salva gli anni di servizio

    #Calcola la manutenzione (50 € per ogni anno di servizio)
    def costo_manutenzione(self):
        return 50 * self.anni_servizio



# 3. GestoreFlotta PER LA GESTIONE DEI VEICOLI
class GestoreFlotta:
    # Costruttore: crea la lista vuota 'veicoli'
    def __init__(self):
        self.veicoli = []  # Lista contenente tutti i veicoli

    # Aggiunge un veicolo alla lista della flotta
    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)            # Inserisce l'oggetto nella lista
        print("Veicolo aggiunto alla flotta con successo!")

    # Cerca un veicolo tramite targa e lo rimuove dalla lista
    def rimuovi_veicolo(self, targa):
        trovato = False                        # Variabile di controllo
        for v in self.veicoli:                 # Scorre tutti i veicoli nella lista
            if v.get_targa().upper() == targa.upper():  # Confronta la targa
                self.veicoli.remove(v)         # Elimina il veicolo dalla lista
                print("Veicolo con targa", targa, "rimosso dalla flotta.")
                trovato = True                 # Segnala che è stato trovato
                break                          # Interrompe il ciclo
        if not trovato:
            print("Veicolo con targa", targa, "non trovato!")

    # Calcola la somma dei costi di manutenzione
    def costo_totale_manutenzione(self):
        totale = 0                             # Inizializza il totale a 0
        for v in self.veicoli:                 # Scorre ciascun veicolo nella lista
            totale = totale + v.costo_manutenzione()  # Somma il costo specifico del veicolo
        return totale                          # Restituisce la somma finale

    # Stampa l'elenco dei veicoli mostrando targa, tipo e carico attuale
    def stampa_veicoli(self):
        print("\n--- ELENCO VEICOLI DELLA FLOTTA ---")
        if len(self.veicoli) == 0:              # Controlla se la lista dei veicoli è vuota
            print("Nessun veicolo presente nella flotta.")
        else:
            for v in self.veicoli:             # Scorre ogni veicolo della lista
                # Usa il metodo getter
                print("Tipo:", v.get_tipo(), "| Targa:", v.get_targa(), "| Carico attuale:", v.get_carico_attuale(), "kg")


# 4.MENU 
flotta = GestoreFlotta()  # Crea l'oggetto per gestire la flotta
scelta = ""               # Variabile per memorizzare l'opzione inserita dall'utente

# Ciclo che ripete il menu fino a quando l'utente sceglie "6"
while scelta != "6":
    print("\n=== GESTIONE FLOTTA TRASPORTI ===")
    print("1 - Aggiungi Veicolo (Camion, Furgone, Motocarro)")
    print("2 - Rimuovi Veicolo per Targa")
    print("3 - Carica / Scarica Veicolo")
    print("4 - Visualizza Elenco Veicoli")
    print("5 - Calcola Costo Totale Manutenzione")
    print("6 - Esci")

    scelta = input("Scegli un'opzione (1-6): ")  # Legge la scelta dell'utente

    # OPZIONE 1: AGGIUNGI UN VEICOLO
    if scelta == "1":
        tipo = input("Tipo veicolo (1=Camion, 2=Furgone, 3=Motocarro): ")
        targa = input("Inserisci targa: ")
        peso_massimo = int(input("Inserisci capacità di carico massima (kg): "))

        # Inserimento Camion
        if tipo == "1":
            numero_assi = int(input("Inserisci numero di assi: "))
            v = Camion(targa, peso_massimo, numero_assi)
            flotta.aggiungi_veicolo(v)
        # Inserimento Furgone
        elif tipo == "2":
            alimentazione = input("Inserisci alimentazione (diesel/elettrico): ")
            v = Furgone(targa, peso_massimo, alimentazione)
            flotta.aggiungi_veicolo(v)
        # Inserimento Motocarro
        elif tipo == "3":
            anni_servizio = int(input("Inserisci anni di servizio: "))
            v = Motocarro(targa, peso_massimo, anni_servizio)
            flotta.aggiungi_veicolo(v)
        else:
            print("Tipo di veicolo non valido!")

    # OPZIONE 2: RIMUOVI UN VEICOLO
    elif scelta == "2":
        targa = input("Inserisci la targa del veicolo da rimuovere: ")
        flotta.rimuovi_veicolo(targa)

    # OPZIONE 3: CARICA O SCARICA UN VEICOLO
    elif scelta == "3":
        targa = input("Inserisci la targa del veicolo: ")
        trovato = False #Immaginiamo di non aver ancora trovato nulla
        # Cerca il veicolo per targa
        for v in flotta.veicoli:
            if v.get_targa().upper() == targa.upper():
                trovato = True
                azione = input("Vuoi caricare (c) o scaricare (s)? ").lower()
                if azione == "c":
                    peso = int(input("Inserisci il peso da caricare (kg): "))
                    v.carica(peso)              # Richiama il metodo carica
                elif azione == "s":
                    v.scarica()                 # Richiama il metodo scarica
                else:
                    print("Azione non valida!")
                break
        if not trovato:
            print("Veicolo non trovato!")

    # OPZIONE 4: VISUALIZZA ELENCO VEICOLI
    elif scelta == "4":
        flotta.stampa_veicoli()

    # OPZIONE 5: CALCOLA COSTO TOTALE MANUTENZIONE
    elif scelta == "5":
        totale = flotta.costo_totale_manutenzione()
        print("\nCosto totale di manutenzione per l'intera flotta: €", totale)

    # OPZIONE 6: ESCI DAL PROGRAMMA
    elif scelta == "6":
        print("Uscita dal programma")

    # OPZIONE NON VALIDA
    else:
        print("Opzione non valida, riprova!")