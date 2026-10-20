# Importo la libreria NumPy
import numpy as np

# Creo una variabile con il nome del file di testo dove salvare le operazioni
nome_file = "registro_operazioni.txt"

# Inizializzo la variabile per la matrice principale ponendola vuota
matrice = None

# Definisco una funzione che prende una stringa di testo e la scrive nel file
def salva_su_file(testo):
    # Apro il file in modalità append ("a") così aggiungo il testo in fondo senza cancellare il resto
    with open(nome_file, "a") as f:
        # Scrivo il testo passato alla funzione seguito da due a capo per separare i blocchi
        f.write(testo + "\n\n")

# Stampo a schermo il titolo principale del programma
print("SISTEMA DI GESTIONE MATRICI NUMPY:")

# Faccio partire un ciclo infinito per mostrare il menu fino a quando l'utente non decide di uscire
while True:
    # Stampo l'intestazione del menu
    print("\n--- MENU OPERAZIONI ---")
    # Stampo la prima opzione del menu
    print("1. Crea nuova matrice 2D")
    # Stampo la seconda opzione del menu
    print("2. Estrai sotto-matrice centrale")
    # Stampo la terza opzione del menu
    print("3. Trasponi la matrice")
    # Stampo la quarta opzione del menu
    print("4. Calcola la somma degli elementi")
    # Stampo la quinta opzione del menu
    print("5. Moltiplicazione elemento per elemento (Element-wise)")
    # Stampo la sesta opzione del menu
    print("6. Calcola la media degli elementi")
    # Stampo la settima opzione del menu
    print("7. EXTRA: Calcola il determinante della matrice")
    # Stampo l'ottava opzione del menu
    print("8. Esci dal programma")
    
    # Chiedo all'utente di inserire un numero da 1 a 8 e lo salvo come stringa nella variabile scelta
    scelta = input("Scegli un'opzione (1-8): ")

    
    if scelta == "1":
        # Chiedo quante righe voglio e converto l'input da testo a numero intero
        righe = int(input("Inserisci numero di righe: "))
        # Chiedo quante colonne voglio e converto l'input da testo a numero intero
        colonne = int(input("Inserisci numero di colonne: "))
        
        # Creo la matrice con numeri interi casuali da 1 a 100 della dimensione indicata
        matrice = np.random.randint(1, 101, size=(righe, colonne))
        
        # Stampo la scritta di conferma a schermo
        print("\nMatrice creata:")
        # Stampo la matrice generata
        print(matrice)
        
        # Richiamo la funzione per salvare la creazione della matrice nel file txt
        salva_su_file(f"1. CREAZIONE MATRICE ({righe}x{colonne}):\n{matrice}")

    
    elif scelta == "2":
        # Verifico se la matrice non è ancora stata creata
        if matrice is None:
            # Avviso l'utente che deve prima creare una matrice
            print("Prima devi creare una matrice (opzione 1)!")
        # Se la matrice esiste procedo
        else:
            # Ricavo il numero di righe r e di colonne c della matrice
            r, c = matrice.shape
            
            # Verifico se la matrice ha almeno 3 righe e 3 colonne per avere una parte centrale
            if r > 2 and c > 2:
                # Prendo la matrice escludendo la prima e l'ultima riga e la prima e l'ultima colonna
                sotto_matrice = matrice[1:-1, 1:-1]
                # Stampo l'intestazione
                print("\nSotto-matrice centrale:")
                # Stampo il centro estratto
                print(sotto_matrice)
                # Salvo il risultato estratto nel file txt
                salva_su_file(f"2. SOTTO-MATRICE CENTRALE:\n{sotto_matrice}")
            # Se è troppo piccola entro qui
            else:
                # Avviso a schermo che la matrice è troppo piccola
                print("\nLa matrice è troppo piccola per estrarre il centro (serve almeno 3x3).")
                # Salvo l'avviso nel file txt
                salva_su_file(f"2. SOTTO-MATRICE CENTRALE:\nMatrice {r}x{c} troppo piccola.")

    
    elif scelta == "3":
        # Verifico se la matrice esiste
        if matrice is None:
            # Avviso l'utente
            print("Prima devi creare una matrice (opzione 1)!")
        # Se esiste procedo
        else:
            # Inverto righe e colonne usando la proprietà .T di NumPy
            matrice_trasposta = matrice.T
            # Stampo l'intestazione
            print("\nMatrice trasposta:")
            # Stampo la matrice ruotata
            print(matrice_trasposta)
            # Salvo il risultato della trasposizione nel file txt
            salva_su_file(f"3. TRASPOSIZIONE MATRICE:\n{matrice_trasposta}")

    
    elif scelta == "4":
        # Verifico se la matrice esiste
        if matrice is None:
            # Avviso l'utente
            print("Prima devi creare una matrice (opzione 1)!")
        # Se esiste procedo
        else:
            # Calcolo la somma di tutti gli elementi della matrice con np.sum
            somma = np.sum(matrice)
            # Stampo la somma trovata
            print(f"\nSomma di tutti gli elementi: {somma}")
            # Salvo il risultato della somma nel file txt
            salva_su_file(f"4. SOMMA ELEMENTI: {somma}")

    
    elif scelta == "5":
        # Verifico se la matrice principale esiste
        if matrice is None:
            # Avviso l'utente
            print("Prima devi creare una matrice (opzione 1)!")
        # Se esiste procedo
        else:
            # Recupero le dimensioni della matrice principale
            r, c = matrice.shape
            # Avviso che sto creando una seconda matrice con le stesse righe e colonne
            print(f"\nCreo una seconda matrice delle stesse dimensioni ({r}x{c})...")
            # Genero la seconda matrice con numeri casuali da 1 a 100
            matrice2 = np.random.randint(1, 101, size=(r, c))
            
            # Stampo l'intestazione per la seconda matrice
            print("Seconda matrice:")
            # Stampo la seconda matrice generata
            print(matrice2)
            
            # Moltiplico elemento per elemento le due matrici usando l'operatore *
            risultato_moltiplicazione = matrice * matrice2
            # Stampo l'intestazione del risultato
            print("\nRisultato della moltiplicazione element-wise:")
            # Stampo la matrice risultante
            print(risultato_moltiplicazione)
            
            # Salvo tutto l'operato (prima matrice, seconda matrice e risultato) nel file txt
            salva_su_file(f"5. MOLTIPLICAZIONE ELEMENT-WISE:\nMatrice 1:\n{matrice}\nMatrice 2:\n{matrice2}\nRisultato:\n{risultato_moltiplicazione}")

    
    elif scelta == "6":
        # Verifico se la matrice esiste
        if matrice is None:
            # Avviso l'utente
            print("Prima devi creare una matrice (opzione 1)!")
        # Se esiste procedo
        else:
            # Calcolo la media aritmetica di tutti gli elementi usando np.mean
            media = np.mean(matrice)
            # Stampo il valore della media
            print(f"\nMedia di tutti gli elementi: {media}")
            # Salvo la media nel file txt
            salva_su_file(f"6. MEDIA ELEMENTI: {media}")

    
    elif scelta == "7":
        # Verifico se la matrice esiste
        if matrice is None:
            # Avviso l'utente
            print("Prima devi creare una matrice (opzione 1)!")
        # Se esiste procedo
        else:
            # Estraggo le dimensioni della matrice
            r, c = matrice.shape
            # Controllo se la matrice è quadrata (ovvero se righe == colonne)
            if r == c:
                # Calcolo il determinante usando il modulo linalg di NumPy
                det = np.linalg.det(matrice)
                # Stampo il determinante calcolato
                print(f"\nDeterminante della matrice ({r}x{c}): {det}")
                # Salvo il valore del determinante nel file txt
                salva_su_file(f"7. EXTRA - DETERMINANTE: {det}")
            # Se non è quadrata non posso calcolare il determinante
            else:
                # Stampo il messaggio di errore a schermo
                print(f"\nImpossibile calcolare il determinante: la matrice è {r}x{c} e non è quadrata!")
                # Salvo l'errore nel file txt
                salva_su_file(f"7. EXTRA - DETERMINANTE:\nMatrice {r}x{c} non quadrata.")

    
    elif scelta == "8":
        # Stampo il messaggio di saluto
        print("\nArrivederci!")
        # Rompo il ciclo while
        break

    # Gestisco il caso in cui l'utente inserisca un input diverso dai numeri tra 1 e 8
    else:
        print("\nScelta non valida! Inserisci un numero tra 1 e 8.")