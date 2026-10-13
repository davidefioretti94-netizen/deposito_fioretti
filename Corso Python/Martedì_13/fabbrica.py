# Creiamo la classe Padre chiamata Prodotto.
class Prodotto:
    
    # costruttore: la funzione che parte da sola quando creiamo un prodotto.
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        
        # Salviamo il nome del prodotto dentro l'oggetto stesso.
        self.nome = nome
        
        # Salviamo quanto ci costa produrre questo oggetto.
        self.costo_produzione = costo_produzione
        
        # Salviamo a quanto lo venderemo ai clienti.
        self.prezzo_vendita = prezzo_vendita

    # Questa funzione serve per calcolare quanto guadagniamo (il profitto).
    def calcola_profitto(self):
        
        # Il guadagno è:
        return self.prezzo_vendita - self.costo_produzione


# Creiamo la classe Figlia 'Elettronica'. ereditata da Prodotto.
class Elettronica(Prodotto):
    
    # Il costruttore per l'Elettronica chiede nome, costo, prezzo e la garanzia (esclusiva).
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        
        # Invece di rifare tutto, passiamo nome, costo e prezzo al costruttore del Padre usando super().
        super().__init__(nome, costo_produzione, prezzo_vendita)
        
        # E poi salviamo l'attributo specifico solo per i prodotti elettronici.
        self.garanzia = garanzia 


# Creiamo l'altra classe Figlia 'Abbigliamento', che eredita sempre da Prodotto.
class Abbigliamento(Prodotto):
    
    # Il costruttore chiede i soliti dati base più il materiale (esclusivo).
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        
        # Passiamo i dati base al costruttore del Padre per farli gestire a lui.
        super().__init__(nome, costo_produzione, prezzo_vendita)
        
        # Salviamo l'attributo specifico per l'abbigliamento.
        self.materiale = materiale


# Creiamo la classe Fabbrica, che farà da registro per il nostro magazzino.
class Fabbrica:
    
    # Costruttore della Fabbrica: si avvia quando apriamo la fabbrica la prima volta.
    def __init__(self):
        
        # Creiamo una lista vuota.Sarà il nostro magazzino.
        self.inventario = []

    # Funzione per mettere la merce dentro al magazzino.
    def aggiungi_prodotto(self, prodotto, quantita):
        
        # Questo ciclo 'for' ripete l'azione tante volte quanto è il numero 'quantita'.
        for i in range(quantita):
            
            # Inseriamo (append) fisicamente l'oggetto in fondo alla lista del magazzino.
            self.inventario.append(prodotto)
            
        # Stampiamo a video per confermare che l'inserimento è andato a buon fine.
        print("Aggiunti", quantita, "pezzi di", prodotto.nome, "in magazzino.")

    # Funzione per vendere i prodotti ai clienti
    def vendi_prodotto(self, prodotto, quantita):
        
        # Creiamo una variabile per contare a mano quanti pezzi abbiamo. Partiamo da 0.
        pezzi_disponibili = 0
        
        # Guardiamo uno per uno tutti gli elementi presenti nella lista 'inventario'.
        for elemento in self.inventario:
            
            # Se l'elemento che stiamo guardando è identico al prodotto che vogliamo vendere...
            if elemento == prodotto:
                
                #allora aumentiamo il nostro contatore di 1.
                pezzi_disponibili += 1
        
        # Dopo aver contato tutto, controlliamo se i pezzi trovati bastano per la vendita.
        if pezzi_disponibili >= quantita:
            
            # Se ci sono abbastanza pezzi, avviamo un ciclo per il numero di pezzi da vendere.
            for i in range(quantita):
                
                # Cancelliamo l'oggetto dalla lista magazzino una volta per ogni vendita.
                self.inventario.remove(prodotto)
            
            # Calcoliamo i soldi guadagnati: profitto del singolo oggetto moltiplicato
            # per i pezzi venduti.
            profitto_totale = prodotto.calcola_profitto() * quantita
            
            # Stampiamo a video quanti pezzi abbiamo venduto.
            print("Venduti", quantita, "pezzi di", prodotto.nome)
            
            # Stampiamo a video i soldi totali che abbiamo incassato.
            print("Profitto realizzato: €", profitto_totale)
            
        # Se invece non ci sono abbastanza pezzi nel magazzino...
        else:
            
            # Stampiamo un messaggio di errore per avvisare che non possiamo vendere.
            print("Impossibile vendere: quantità di", prodotto.nome, "insufficiente in magazzino.")

    # Funzione per quando un cliente ci restituisce un prodotto (reso).
    def resi_prodotto(self, prodotto, quantita):
        
        # Avviamo un ciclo che si ripete in base a quanti pezzi ci vengono restituiti.
        for i in range(quantita):
            
            # Rimettiamo l'oggetto dentro la lista magazzino, proprio come nell'aggiunta.
            self.inventario.append(prodotto)
            
        # Stampiamo a video la conferma che i prodotti sono tornati sugli scaffali.
        print("Resi", quantita, "pezzi di", prodotto.nome, "riportati in magazzino.")


#INIZIO DEI TEST
# Creiamo un oggetto Elettronica con: nome, costo, prezzo e garanzia.
tv = Elettronica("Televisore Samsung", 300, 500, "2 anni") 

# Creiamo un oggetto Abbigliamento con: nome, costo, prezzo e materiale.
maglietta = Abbigliamento("T-Shirt Nike", 10, 35, "Cotone") 

# Creiamo l'oggetto Fabbrica (all'inizio la sua lista magazzino è completamente vuota).
mia_fabbrica = Fabbrica()


# Chiediamo alla fabbrica di aggiungere 10 televisori nella lista.
mia_fabbrica.aggiungi_prodotto(tv, 10)

# Chiediamo alla fabbrica di aggiungere 50 magliette nella lista.
mia_fabbrica.aggiungi_prodotto(maglietta, 50)


# Stampiamo una linea di separazione per rendere le scritte più leggibili.
print("-------------------")


# Diciamo alla fabbrica di vendere 2 televisori (cancellerà 2 'tv' dalla lista).
mia_fabbrica.vendi_prodotto(tv, 2)         

# Diciamo alla fabbrica di vendere 10 magliette (cancellerà 10 'maglietta' dalla lista).
mia_fabbrica.vendi_prodotto(maglietta, 10) 


# Stampiamo un'altra linea di separazione.
print("-------------------")


# Diciamo alla fabbrica di processare un reso: 1 televisore torna nella lista.
mia_fabbrica.resi_prodotto(tv, 1)