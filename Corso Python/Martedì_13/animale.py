#Definisco la classe
class Animale:
    #Creo l'attributo condiviso da tutti, il contatore parte da 0
    numero_animali=0
    
    #Costruttore: scatta in automatico ogni volta che creo un nuovo animale
    def __init__(self, nome, specie):
        # Prende il 'nome' passato tra parentesi e lo salva in questo specifico animale (self)
        self.nome=nome
        # Prende la 'specie' passata tra parentesi e la salva in QUESTO specifico animale (self)
        self.specie=specie
        # Va nella classe (Animale) e aggiunge 1 al contatore
        Animale.numero_animali +=1
        
    #Metodo di classe
    # Avvisa Python che il metodo sotto lavorerà sull'intera classe (cls), non sul singolo oggetto (self)
    @classmethod
    # Crea il metodo di classe passando 'cls' (che sta per 'classe' Animale)
    def quanti_animali(cls):
        print("Numero di animali creati:", cls.numero_animali)
        
    #FINE CLASSE
#Creiamo gli oggetti
#Creo il 1° oggetto Animale e lo salva nella variabile animale1 (contatore=1)
animale1= Animale("Ciro", "Cane")
animale2= Animale("Calcestruzzo","Gatto")
animale3= Animale("Governatore dei mari", "Tartaruga")

#Interroga la classe generale(Animale) per stampare quanti animali ha registrato
Animale.quanti_animali()