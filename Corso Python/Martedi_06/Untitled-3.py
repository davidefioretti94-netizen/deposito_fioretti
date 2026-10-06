
#Chiedo all'utente di superare tre livelli di difficoltà
livello1= input("Scrivi SI per superare il primo livello: ")

#Controllo se l'utente ha superato il primo livello
if livello1 == "SI":
    print("Primo livello superato")
    
    
   #Se il primo livello è corretto, passo al secondo
   livello2=input("Scrivi CICCIO per superare il secondo livello:")
   
   #Controllo la risposta del secondo livello
   if livello2 == "CICCIO":
       print("Secondo livello superato")
       
       #Se anche il secondo livello è corretto, passo al terzo
       livello3=input("Quanto fa 3+3?")
       
       #Controlo la risposta del terzo livello
       if livello3 == "6":
             print("Terzo livello superato")
       #Se la risposta del terzo livello è sbagliata
       else:
              print("Terzo livello non superato")
    else:
        print("Secondo livello non superato")
else:
    print("Primo livello non superato") 
