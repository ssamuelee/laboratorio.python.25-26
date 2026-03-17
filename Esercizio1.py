def is_pari(n):

    if(int(n) % 2 == 0):
        print("Il tuo numero è pari")
        return True
    else:
        print("Il tuo numero è dispari")
        return False

#----------

def is_positivo(n):
        
    while(int(n) <= 0):
        print("Il numero non rispecchia i parametri richiesti\nDeve essere positivo diverso da 0")
        n = input()

    return n
#----------

print("inserisci un numero positivo diverso da 0: ")
numero = input()

#is_pari(numero)
is_positivo(numero)
