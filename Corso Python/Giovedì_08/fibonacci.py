#Creiamo la funzione per calcolare la sequenza di Fibonacci
def fibonacci(N):
    
    #Impostiamo i primi due numeri della sequenza
    a=0
    b=1
    
    #Ripetiamo finché il numero è <= a N
    while a<=N:
        
        #Stampiamo il numero della sequenza
        print(a)
        
        #Calcoliamo il numero successivo
        somma=a+b
        
        #Spostiamo b nella posizione di a
        a=b
        
        #Mettiamo la somma nella posizione di b
        b=somma
        
#Chiediamo all'utente di inserire il valore massimo N
N= int(input("Inserisci un numero: "))

#Richiamiamo la funzione passando N
fibonacci(N)