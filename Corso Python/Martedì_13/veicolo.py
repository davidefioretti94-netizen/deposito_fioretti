class Veicolo:
def __init__(self, marca, modello):
self.marca = marca
self.modello = modello

def mostra_informazioni(self):
print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
def __init__(self, dotazioni):
self.dotazioni = dotazioni

def mostra_dotazioni(self):
print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")



# --- FUORI DALLE CLASSI 
# 1. Creazione di un oggetto Veicolo
# L'__init__ chiede 'marca' e 'modello'
mio_veicolo = Veicolo("Fiat", "Panda")

# Testiamo il suo metodo
mio_veicolo.mostra_informazioni() 


# 2. Creazione di un oggetto DotazioniSpeciali
# L'__init__ chiede 'dotazioni'. Gli passiamo una lista di stringhe.
lista_optional = ["Aria condizionata", "Cerchi in lega", "Bluetooth"]
mie_dotazioni = DotazioniSpeciali(lista_optional)

# Testiamo il suo metodo
mie_dotazioni.mostra_dotazioni()