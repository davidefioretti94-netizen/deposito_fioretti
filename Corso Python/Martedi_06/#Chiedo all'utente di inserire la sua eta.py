#Chiedo all'utente di inserire la sua eta'
eta= int(input("Inserisci la tua eta': "))

#Se l'eta' e' inferiore a 18
if eta<18:
    print("Mi dispiace, non puoi vedere questo film")
    
#Se l'eta' e' 18 o superiore
if eta>= 18:
    print("Puoi vedere questo film")


#Chiedo all'utente il primo numero

num1= float(input("Inserisci il primo numero:"))

#Chiedo all'utente il secondo numero

num2=float(input("Inserisci il secondo numero:"))

#Chiedo quale operazione vuole eseguire
operazione = input("Inserisci operazione: +,-,*,/ ")

#Controllo l'operazione scelta

match operazione:
    case "+":
        risultato=num1+num2
        print("Risultato", risultato)
        
    case "-":
        risultato=num1-num2
        print("Risultato", risultato)
    
    case "*":
        risultato=num1*num2
        print("Risultato", risultato)
    
    case "/":
        #Controllo se il secondo numero è zero
        if num2 == 0:
            print("Divisione per 0 NON CONSENTITA")
            
        else:
            risultato = num1/num2
            print("Risultato", risultato)
    
    case _:
        print("Operazione non valida")
