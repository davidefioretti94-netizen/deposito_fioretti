#Sistema dinamico
lista=[]

while True:
    
    print("Aggiungi")
    print("Modifica")
    print("Rimuovi")
    print("Visualizza")
    print("Esci")
    
    scelta=input("Scegli un'opzione:")
    
    if scelta=="Aggiungi":
        elemento =input("Inserisci un elemento:")
        lista.append(elemento)
        print("Elemento aggiunto")
        
    elif scelta =="Modifica":
        print(lista)
        
        indice= int(input("Quale posizione vuoi modificare?"))
        nuovo_elemento= input("Inserisci il nuovo elemento: ")
        
        lista[indice]= nuovo_elemento
        print("Elemento modificato")
        
    elif scelta =="Rimuovi":
        print(lista)
        
        elemento= input("Quale elemento vuoi rimuovere?")
        lista.remove(elemento)
        print("Elemento rimosso")
        
    elif scelta == "Visualizza":
        print("Lista completa")
        print(lista)
        
    elif scelta == "Esci":
        print("Programma terminato")
        break
    
    else:
        print("Scelta non valida")