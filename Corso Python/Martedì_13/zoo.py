# 1. LA CLASSE PADRE (o Superclasse)
class Animale:
    
    # Il costruttore della classe Padre
    def __init__(self, nome, eta):
        # Prende il 'nome' passato tra parentesi e lo salva in self
        self.nome = nome
        self.eta = eta

    # Un metodo generico della classe Padre
    def fai_suono(self):
        print(self.nome, "emette un suono indefinito.")


# 2. LE CLASSI FIGLIE

class Leone(Animale):
    
    # Il costruttore della classe Figlia (Leone)
    #richiede i dati base (nome, eta) PIÙ uno esclusivo (dimensione_criniera)
    def __init__(self, nome, eta, dimensione_criniera):
        # La classe Figlia richiama il costruttore della classe Padre
        # super() indica il Padre
        # Gli passiamo nome ed età così li salva lui senza dover riscrivere le regole
        super().__init__(nome, eta)
        
        # La classe Figlia aggiunge il suo attributo specifico
        # Imposta e salva l'attributo specifico che appartiene SOLO ai leoni
        self.dimensione_criniera = dimensione_criniera

    # La classe Figlia sovrascrive il metodo del Padre
    def fai_suono(self):
        print(self.nome, "ruggisce potentemente!")

    # La classe Figlia crea un metodo totalmente nuovo e specifico
    def caccia(self):
        print(self.nome, "sta cacciando la preda.")


class Giraffa(Animale):
    
    def __init__(self, nome, eta, altezza_collo):
        super().__init__(nome, eta)
        self.altezza_collo = altezza_collo

    def fai_suono(self):
        print(self.nome, "emette un basso ronzio.")
        
    def mangia_foglie_alte(self):
        print(self.nome, "mangia foglie in alto usando il suo collo di", self.altezza_collo, "metri.")


class Pinguino(Animale):
    
    def __init__(self, nome, eta, velocita_nuoto):
        super().__init__(nome, eta)
        self.velocita_nuoto = velocita_nuoto

    def fai_suono(self):
        print(self.nome, "suona come un piccolo clacson.")

    def scivola(self):
        print(self.nome, "scivola sul ghiaccio a", self.velocita_nuoto, "km/h!")


# --- ZONA DI TEST ---

mio_leone = Leone("Simba", 5, "Grande")
mia_giraffa = Giraffa("Melman", 7, 5.5)
mio_pinguino = Pinguino("Kowalski", 3, 30)

# Eseguiamo i metodi
mio_leone.fai_suono()
mio_leone.caccia()

mia_giraffa.fai_suono()
mia_giraffa.mangia_foglie_alte()

mio_pinguino.fai_suono()
mio_pinguino.scivola()