def somma(a,b):
    return a+b
def sottrazione(a,b):
    return a-b
def moltiplicazione(a,b):
    return a*b
def divisione(a,b):
    # Controllo per evitare l'errore di divisione per zero
    if b==0:
        return "Errore:Divisione per 0 non consentita"
    return a/b
