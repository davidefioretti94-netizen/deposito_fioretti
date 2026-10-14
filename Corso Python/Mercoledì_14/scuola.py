class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentazione(self):
        print(f"Mi chiamo {self.nome} e ho {self.eta} anni.")


class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.voti = voti

    def calcola_media(self):
        if len(self.voti) == 0:
            return 0
            
        somma_voti = 0
        for voto in self.voti:
            somma_voti += voto
            
        return somma_voti / len(self.voti)

   
    def presentazione(self):
        media = self.calcola_media()
        
        print(f"Mi chiamo {self.nome}, ho {self.eta} anni e la mia media voti è {media}.")


class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia

    def presentazione(self):
        print(f"Mi chiamo {self.nome}, ho {self.eta} anni e insegno {self.materia}.")


# ESEMPIO DI UTILIZZO
if __name__ == "__main__":
    # Test della classe base
    print("--- TEST PERSONA ---")
    persona_generica = Persona("Luca", 40)
    persona_generica.presentazione()

    # Test della sottoclasse Studente
    print("\n--- TEST STUDENTE ---")
    studente1 = Studente("Giulia", 16, [8, 7, 9, 8])
    studente1.presentazione()
    
    # Test della sottoclasse Professore
    print("\n--- TEST PROFESSORE ---")
    professore1 = Professore("Marco", 45, "Matematica")
    professore1.presentazione()