
# CLASSE BASE 
class MembroSquadra:
    
    # Questa funzione si avvia da sola appena creo una nuova persona, chiedendo nome ed età.
    def __init__(self, nome, eta):
        # Prendo il nome passato tra parentesi e lo salvo dentro l'oggetto self
        self.nome = nome
        # Prendo l'età passata tra parentesi e la salvo dentro l'oggetto self
        self.eta = eta
        # Aggiungo un'etichetta di testo per ricordarmi che ruolo ha. Di base è generico.
        self.tipo = "Membro generico"

    # Una funzione normale per far presentare la persona.
    def descrivi(self):
        # Stampa a schermo una frase combinando il nome e l'età salvati.
        print(f"Membro del club: {self.nome}, Età: {self.eta} anni.")

    # PRIMO METODO SPECIALE:
    def __repr__(self):
        return f"{self.__class__.__name__}(nome='{self.nome}', età={self.eta})"

    #SECONDO METODO SPECIALE: __eq__ ---
    # Questa funzione scatta da sola quando uso il simbolo "==" per paragonare due persone.
    def __eq__(self, altro):
        # Controlla se il nome della prima persona self è uguale al nome della seconda altro.
        return self.nome == altro.nome

# CLASSI DERIVATE

# Creo il Giocatore che eredita tutto dalla classe padre.
class Giocatore(MembroSquadra):
    
    # La funzione di partenza del giocatore chiede in più il ruolo e il numero di maglia.
    def __init__(self, nome, eta, ruolo, numero_maglia):
        # Uso super() per chiamare il padre e fargli salvare il nome e l'età
        super().__init__(nome, eta)
        # Cambio l'etichetta di testo: adesso questa persona è riconosciuta come "Giocatore".
        self.tipo = "Giocatore"
        # Salvo il ruolo specifico (es. Attaccante) dentro la persona.
        self.ruolo = ruolo
        # Salvo il numero di maglia.
        self.numero_maglia = numero_maglia

    # Una mossa che solo il giocatore sa fare.
    def gioca_partita(self):
        # Stampa a schermo che il giocatore sta giocando, mostrando i suoi dati.
        print(f"[{self.ruolo}] {self.nome} (Maglia n.{self.numero_maglia}): Scende in campo e gioca!")


# Creo l'Allenatore. Anche lui copia le basi dal padre MembroSquadra.
class Allenatore(MembroSquadra):
    
    # L'allenatore chiede nome, età e gli anni di esperienza.
    def __init__(self, nome, eta, anni_di_esperienza):
        # Dico al padre (super) di salvare nome ed età.
        super().__init__(nome, eta)
        # Cambio l'etichetta in "Allenatore".
        self.tipo = "Allenatore"
        # Salvo gli anni di esperienza.
        self.anni_di_esperienza = anni_di_esperienza

    # Mossa esclusiva dell'allenatore.
    def dirige_allenamento(self):
        # Stampa a schermo che l'allenatore sta lavorando.
        print(f"Mister {self.nome} dirige l'allenamento sfruttando {self.anni_di_esperienza} anni di esperienza.")


# Creo l'Assistente. Anche lui eredita dal padre.
class Assistente(MembroSquadra):
    
    # L'assistente chiede nome, età e la specializzazione (es. Fisioterapista).
    def __init__(self, nome, eta, specializzazione):
        # Dico al padre (super) di salvare nome ed età.
        super().__init__(nome, eta)
        # Cambio l'etichetta in "Assistente".
        self.tipo = "Assistente"
        # Salvo la specializzazione.
        self.specializzazione = specializzazione

    # Azione esclusiva dell'assistente.
    def supporta_team(self):
        # Stampa a schermo che l'assistente sta aiutando.
        print(f"{self.nome} ({self.specializzazione}) sta fornendo supporto vitale alla squadra.")


# CLASSE CONTENITORE (LA SQUADRA INTERA)

# Questa classe non è una persona singola, ma è il "raccoglitore" di tutti i membri.
class Squadra:
    
    # Quando creo una squadra nuova, devo darle un nome.
    def __init__(self, nome_squadra):
        # Salvo il nome della squadra.
        self.nome_squadra = nome_squadra
        # Dichiaro una lista vuota dove scriverò solo i nomi
        self.nomi_membri = []
        # Dichiaro una seconda lista vuota dove metterò fisicamente le persone (gli oggetti).
        self.oggetti_membri = []

    # Funzione per ingaggiare una persona e metterla nella squadra.
    def aggiungi_membro(self, membro):
        # Aggiungo (append) il nome della persona nella prima lista.
        self.nomi_membri.append(membro.nome)
        # Aggiungo (append) l'oggetto persona nella seconda lista.
        self.oggetti_membri.append(membro)
        # Stampo un messaggio per confermare che l'acquisto è andato a buon fine.
        print(f"[{self.nome_squadra}] Ingaggiato: {membro.nome}")

    # Funzione per leggere la lista di tutte le persone in squadra.
    def mostra_rosa(self):
        # Stampo un titolo con il nome della squadra.
        print(f"\n--- Rosa Ufficiale: {self.nome_squadra} ---")
        
        # Controllo: se la lista delle persone è vuota non c'è nessuno
        if not self.oggetti_membri:
            # stampo questo avviso.
            print("La squadra attualmente non ha membri.")
        
        # Faccio un ciclo for prendendo le persone una ad una dalla lista.
        for membro in self.oggetti_membri:
            # Stampo la persona.
            print(f" - {membro}")
        # Riga di decorazione finale.
        print("-----------------------------------")

    # Funzione per far giocare la mia squadra contro un'altra squadra nemica (avversaria).
    def gioca_contro(self, avversaria):
        # Stampo l'annuncio della partita.
        print(f"\n⚽ INIZIO MATCH: {self.nome_squadra} VS {avversaria.nome_squadra} ⚽")
        
        # Faccio un ciclo passando tutti i miei membri.
        for membro in self.oggetti_membri:
            
            #Leggo scritto Giocatore?
            if membro.tipo == "Giocatore":
                # Se sì, lo faccio scendere in campo usando la sua mossa speciale.
                membro.gioca_partita()
                
            # Altrimenti, leggo scritto Allenatore?
            elif membro.tipo == "Allenatore":
                # Se sì, stampo che sta dando ordini dalla panchina.
                print(f"  -> L'allenatore {membro.nome} dà indicazioni da bordo campo.")
                
        # Il giro è finito, la partita è conclusa.
        print(f"TRIPLICE FISCHIO! Grande partita tra {self.nome_squadra} e {avversaria.nome_squadra}.")

    # TERZO METODO SPECIALE:
    # Questa è la funzione "spia". Scatta in automatico ogni volta che cerco di leggere una variabile della squadra.
    def __getattribute__(self, name):
        # Controllo se la variabile che si sta cercando di leggere è una delle mie due liste private.
        if name in ["nomi_membri", "oggetti_membri"]:
            # Se è vero, stampo a schermo un avviso per segnalare l'accesso.
            print(f"\n[SISTEMA] -> Lettura liste interne in corso: '{name}'")
            
        # Finita la nostra ispezione, diciamo al super 
        # di restituire la variabile così il programma non si blocca.
        return super().__getattribute__(name)




# ESECUZIONE E TEST DEL PROGRAMMA
# Questo comando dice al computer: "Fai partire queste righe solo se sto eseguendo questo file".
if __name__ == "__main__":
    
    # 1. Creo la mia prima squadra e la chiamo "Focaccine".
    squadra_a = Squadra("Focaccine")
    
    # 2. Creo le persone e le infilo una per una dentro la squadra_a usando la funzione "aggiungi_membro".
    squadra_a.aggiungi_membro(Allenatore("Allegri ma non troppo", 64, 30))
    squadra_a.aggiungi_membro(Giocatore("Filippo Maccarone", 25, "Attaccante", 9))
    squadra_a.aggiungi_membro(Giocatore("Salvatore Pesto", 22, "Centrocampista", 10))
    squadra_a.aggiungi_membro(Assistente("Antonio giro", 45, "Fisioterapista"))

    # 3. Creo una seconda squadra e la chiamo "Pennette al sugo".
    squadra_b = Squadra("Pennette al sugo")
    # Infilo un allenatore nella squadra_b.
    squadra_b.aggiungi_membro(Allenatore("Antonio Conte", 54, 18))
    # Infilo un giocatore nella squadra_b.
    squadra_b.aggiungi_membro(Giocatore("Mario Acqua", 28, "Difensore", 3))

    # 4. Ordino alla squadra_a di mostrare a schermo tutti i suoi componenti. 
    # (Questo farà suonare l'allarme di __getattribute__ e formatterà i nomi grazie a __repr__).
    squadra_a.mostra_rosa()

    # 5. Ordino alla squadra_a di giocare una partita contro la squadra_b.
    squadra_a.gioca_contro(squadra_b)

    # 6. Ultima prova per vedere se il controllo dei nomi uguali (__eq__) funziona.
    print("\n--- Test di Uguaglianza (__eq__) ---")
    
    # Creo due giocatori su carta che hanno lo stesso identico nome.
    gioc_1 = Giocatore("Marco Giordano", 25, "Attaccante", 9)
    gioc_2 = Giocatore("Marco Giordano", 25, "Attaccante", 9)
    
    # Metto "==" tra di loro per confrontare: Python fa scattare di nascosto la funzione __eq__ che abbiamo creato.
    if gioc_1 == gioc_2:
        # Se la nostra funzione risponde che i nomi sono identici, stampa questo successo.
        print("I due giocatori si chiamano allo stesso modo (__eq__ verificato con successo).")
