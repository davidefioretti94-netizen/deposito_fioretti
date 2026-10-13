#Creo la classe Convertitore
class Convertitore:
    # Avvisa Python che il metodo sotto non ha bisogno di creare oggetti per funzionare
    @staticmethod
    # Crea la funzione che prende in ingresso un valore chiamato 'euro'
    def euro_in_dollari(euro):
        #Prende il valore euro e lo moltiplica
        return euro * 1.08
    
    @staticmethod
    # Crea la funzione che prende in ingresso una distanza chiamata 'km'
    def km_in_miglia(km):
        #Prende il valore km e lo converte in miglia
        return km * 0.621371

# Stampa la frase e il risultato chiamando la funzione 'euro_in_dollari' direttamente dalla classe
print("10 euro in dollari sono:", Convertitore.euro_in_dollari(10))
print("5 Km in Miglia sono:", Convertitore.km_in_miglia(5))