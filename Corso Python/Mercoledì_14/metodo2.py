#1 CLASSE PADRE
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        pass 


# 2. CLASSI DERIVATE

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ simulato con successo tramite Carta di Credito.")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ simulato con successo tramite PayPal.")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ simulato con successo tramite Bonifico Bancario.")


# 3. GESTORE PAGAMENTI

class GestorePagamenti:
    def __init__(self, metodo):
        self.metodo = metodo 

    def processa(self, importo):
        self.metodo.effettua_pagamento(importo)



# --- MENU INTERATTIVO PER IL TERMINALE ---


print("Benvenuto nel sistema di pagamento!")

# Usiamo un ciclo "while True" per far ripetere il menu finché non decidiamo di uscire
while True:
    print("\nScegli il metodo di pagamento:")
    print("1. Carta di Credito")
    print("2. PayPal")
    print("3. Bonifico Bancario")
    print("0. Esci dal programma")

    # input() ferma il programma e aspetta che l'utente scriva qualcosa
    scelta = input("Inserisci il numero della tua scelta: ")

    # Se l'utente digita 0, interrompiamo il ciclo while con "break"
    if scelta == '0':
        print("Chiusura del programma. Arrivederci!")
        break

    # Controlliamo se la scelta è valida (1, 2 o 3)
    if scelta == '1' or scelta == '2' or scelta == '3':
        
        # Chiediamo l'importo
        importo_testo = input("Inserisci l'importo da pagare (es. 150.50): ")
        
        # input() restituisce sempre un testo (stringa). 
        # Dobbiamo convertirlo in un numero decimale (float) per usarlo come importo
        importo = float(importo_testo)

        # Creiamo l'oggetto giusto in base alla scelta dell'utente
        if scelta == '1':
            metodo_scelto = CartaDiCredito()
        elif scelta == '2':
            metodo_scelto = PayPal()
        elif scelta == '3':
            metodo_scelto = BonificoBancario()

        #Creiamo il gestore consegnandogli l'oggetto del metodo scelto
        gestore = GestorePagamenti(metodo_scelto)
        gestore.processa(importo)
        
    else:
        print("Scelta non valida! Inserisci un numero tra 0 e 3.")