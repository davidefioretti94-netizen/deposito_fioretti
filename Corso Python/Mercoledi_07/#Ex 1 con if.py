#Ex 1 con if

numero = int(input("Inserisci un numero:"))

if numero %2 == 0:
    print("Pari")
else:
    print("Dispari")
    
    
    
#Ex 2 con while e range
while True:
    
    n= int(input("Inserisci un numero intero positivo: "))
    
    if n>=0:
        
        for numero in range(n, -1, -1):
            print(numero)
            
    else:
        print("Il numero deve essere positivo")

