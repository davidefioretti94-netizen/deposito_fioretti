#Creo una lista di parole

parole = ["antonio", "luca" , "francesca"]

#Creo una lista di numeri

numeri= [1,2,3,]

#Chiedo all'utente quale lista vuole utilizzare

scelta= input("Scegli la lista: 1=parole, 2=numeri:")

#Se l'utente sceglie 1, lavoriamo con la lista delle parole
if scelta_lista == "1":
    
    #Chiedo se vuole aggiungere o rimuovere una parola
    operazione= input("1=aggiungi, 2=rimuovi:")
    
    #Se sceglie 1, aggiungo una parola
    if operazione == "1"
    parola= input("Inserisci la parola da aggiungere:")
    parola.append(parola)
    
    #Se sceglie 2, rimuovo una parola
    elif operazione == "2"
    parola= input("Inserisci la parola da rimuovere:")
    parola.remove(parola)
    
    #Stampo la lista finale
    print(parole)
    
#Se l'utente sceglie, lavoriamo con la lista dei numeri
elif scelta== "2";

#Chiedo se vuole aggiungere o rimuovere un numero
operazione= input("1= aggiungi, 2=rimuovi:")

#Se sceglie 1, aggiungo un numero
if operazione =="1":
    numero=int(input("Inserisci il numero da aggiungere:"))
    numeri.append(numero)

#Se sceglie 2, rimuovo un numero
elif operazione =="2":
    numero=int(input("Inserisci il numero da rimuovere:"))
    numeri.remove(numero)
    
    #Stampo la lista finale
    print(numeri)
    
#Se non scrive ne 1 ne 2
else:
    print("scelta non valida")