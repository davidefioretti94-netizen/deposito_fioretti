#3 Scegli gli esercizi con il while

while True:
    scelta=input("Scegli ex1, ex2, ex3 oppure end")
    
    #ex1:Inserire numeri interi fino a quando l'utente inserisce il numero 0
    if scelta == "ex1":
        
        somma=0
        numero= int(input("Inserisci un numero:"))
        
        #Quando viene inserito il numero 0 il programma calcola e stampa la somma di tutti i numeri 
        # inseriti
        while numero!= 0:
            somma= somma+numero
            numero= int(input("Inserisci un numero: "))
            
            print("La somma è: ",somma)
     
    #ex2:Inserire una parola e utilizzare un ciclo for per stampare ogni lettera della parola su 
    # una nuova riga      
    if scelta == "ex2":
        
        parola= input("Inserisci una parola:")
        for lettera in parola:
            print(lettera)
            
    
    #ex3:Utilizza un ciclo for con range per stampare fino a un massimo N dato dall'utente
    #tramite uno steps dato dall'utente
    if scelta == "ex3":
        n= int(input("Inserisci il numero massimo:"))
        
        step=int(input("Inserisci lo step:"))
        
        for numero in range(0, n+1, step):
            print(numero)
            
    if scelta.lower() == "end":
        break