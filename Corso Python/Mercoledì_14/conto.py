# Definizione della classe ContoBancario
class ContoBancario:
    
    # Metodo costruttore che viene chiamato automaticamente quando si crea un nuovo conto. 
    # Prende il nome del titolare e un saldo iniziale (che se non viene passato, vale 0.0 di base).
    def __init__(self, titolare, saldo_iniziale=0.0):
        # Inizializza l'attributo privato titolare con una stringa vuota
        self.__titolare = ""
        # Inizializza l'attributo privato saldo con 0.0 come valore di partenza
        self.__saldo = 0.0
        
        # Chiama il metodo set_titolare per assegnare il nome
        self.set_titolare(titolare)
        
        # Controlla se il saldo iniziale fornito è maggiore o uguale a zero
        if saldo_iniziale >= 0:
            # Se è valido, converte il valore in float e lo assegna al saldo
            self.__saldo = float(saldo_iniziale)
        # Se il saldo iniziale passato è negativo
        else:
            # Stampa a schermo un messaggio di errore; il saldo rimarrà a 0.0 (valore di default)
            print("Errore: Il saldo iniziale non può essere negativo. Impostato a 0.0")


    # GETTER
    # Metodo per recuperare e leggere il nome del titolare dall'esterno in modo sicuro
    def get_titolare(self):
        # Restituisce semplicemente il valore dell'attributo privato __titolare
        return self.__titolare

    # Metodo per recuperare e leggere il valore del saldo dall'esterno in modo sicuro
    def get_saldo(self):
        # Restituisce semplicemente il valore dell'attributo privato __saldo
        return self.__saldo


    # SETTER
    # Metodo per modificare il nome del titolare, applicando un controllo di sicurezza
    def set_titolare(self, nuovo_titolare):
        # Controlla in modo semplice che la variabile nuovo_titolare non sia una stringa vuota
        if nuovo_titolare != "":
            # Se la stringa non è vuota, la assegna all'attributo __titolare
            self.__titolare = nuovo_titolare
        # Se l'utente ha passato una stringa vuota
        else:
            # Stampa un messaggio di errore
            print("Errore: Il nome del titolare non può essere vuoto.")

    # Metodo per impostare il saldo, applicando un controllo di sicurezza
    def set_saldo(self, nuovo_saldo):
        # Controlla che il nuovo valore non sia un numero negativo
        if nuovo_saldo >= 0:
            # Se è maggiore o uguale a zero, lo assegna all'attributo __saldo convertendolo in float
            self.__saldo = float(nuovo_saldo)
        # Se si sta cercando di impostare un valore negativo
        else:
            # Stampa un messaggio di errore
            print("Errore: Il saldo non può essere negativo.")


    # METODI PUBBLICI
    # Metodo per aggiungere fondi al conto bancario
    def deposita(self, importo):
        # Verifica che la cifra che si vuole versare sia strettamente maggiore di zero
        if importo > 0:
            # Somma l'importo al saldo attuale
            self.__saldo += importo
            # Stampa un messaggio di conferma per mostrare i valori aggiornati
            print(f"Deposito di {importo} completato. Nuovo saldo: {self.__saldo}")
        # Se la cifra da versare è zero o negativa
        else:
            # Blocca l'operazione e stampa l'errore
            print("Errore: L'importo da depositare deve essere maggiore di zero.")

    # Metodo per sottrarre fondi dal conto bancario
    def preleva(self, importo):
        # Per prima cosa verifica che l'importo richiesto per il prelievo sia maggiore di zero
        if importo > 0:
            # Controlla se i soldi disponibili sul conto sono maggiori o uguali alla cifra richiesta
            if self.__saldo >= importo:
                # Se ci sono fondi, sottrae l'importo dal saldo
                self.__saldo -= importo
                # Stampa il messaggio di conferma e il saldo rimanente
                print(f"Prelievo di {importo} completato. Nuovo saldo: {self.__saldo}")
            # Se i fondi sul conto sono inferiori all'importo richiesto
            else:
                # Blocca il prelievo e segnala che non ci sono abbastanza soldi
                print("Errore: Fondi insufficienti per prelevare questa cifra.")
        # Se l'importo richiesto è zero o negativo
        else:
            # Blocca l'operazione perché non si possono prelevare cifre non valide
            print("Errore: L'importo da prelevare deve essere maggiore di zero.")

    # Metodo per mostrare a schermo il saldo senza permetterne la modifica diretta
    def visualizza_saldo(self):
        # Richiama il metodo get_saldo() che abbiamo creato sopra e ne restituisce il risultato
        return self.get_saldo()



#UTILIZZO
# Questo blocco if serve a far eseguire il codice di test solo se avviamo questo script direttamente
if __name__ == "__main__":
    # Crea un nuovo oggetto di tipo ContoBancario, passandogli nome e 100.0 come saldo iniziale
    mio_conto = ContoBancario("Focaccina al pesto", 100.0)
    
    # Chiama visualizza_saldo() sull'oggetto e stampa il risultato a schermo
    print(f"Saldo iniziale: {mio_conto.visualizza_saldo()}")
    
    # Esegue un deposito valido di 50.0 sul conto
    mio_conto.deposita(50.0)
    # Tenta di depositare un valore negativo, il metodo bloccherà l'azione e stamperà errore
    mio_conto.deposita(-10.0)
    
    # Esegue un prelievo valido di 30.0 dal conto
    mio_conto.preleva(30.0)
    # Tenta di prelevare 200.0, ma avendo meno soldi sul conto, il metodo bloccherà l'azione
    mio_conto.preleva(200.0)
    
    # Tenta di cambiare il titolare con una stringa vuota, il metodo bloccherà la modifica
    mio_conto.set_titolare("") 
    # Cambia con successo il nome del titolare inserendo una stringa valida
    mio_conto.set_titolare("Lello friariello")
    # Usa il metodo get_titolare() per leggere il nuovo nome e lo stampa a schermo
    print(f"Nuovo titolare: {mio_conto.get_titolare()}")