import calcolatrice

def menu():
    # Ciclo infinito per mostrare continuamente il menu finché l'utente non decide di uscire
    while True:
        print("-- MENU CALCOLATRICE --")
        print("1.Somma")
        print("2.Sottrazione")
        print("3.Moltiplicazione")
        print("4.Divisione")
        print("5.Esci")
        
        scelta = input("Scegli un'opzione (1-5):")
        
        if scelta == '5':
            print("Arrivederci!")
            break
        
        if scelta =='1' or scelta == '2' or scelta == '3' or scelta == '4':
            num1 = float(input("Inserisci il primo numero:"))
            num2 = float(input("Inserisci il secondo numero: "))
            
            if scelta == '1':
                risultato = calcolatrice.somma(num1, num2)
            elif scelta == '2':
                risultato = calcolatrice.sottrazione(num1,num2)
            elif scelta == '3':
                risultato = calcolatrice.moltiplicazione(num1,num2)
            elif scelta == '4':
                risultato = calcolatrice.divisione(num1,num2)
                
            print("Risultato:", risultato)
        else:
            print("Scelta non valida, riprova!")
menu()