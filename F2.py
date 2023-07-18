# cifraparola_array ok, aggiustare quello con l'ord

def cifraparola_ord(x, y, p):
    stringa = ""
    for i in range(len(p)):
        nuovocarattere = ""
        if (i+1 % 2 == 0):
            nuovocarattere = chr(ord(p[i])+x)
            if (nuovocarattere > 'Z'):
                posizioneprec = ord(p[i])+x
                nuovocarattere = chr(ord('A')+(posizioneprec-26))
        else:
            nuovocarattere = chr(ord(p[i])-y)
            if (nuovocarattere < 'A'):
                posizioneprec = ord(p[i])-y
                nuovocarattere = chr(ord('Z')+(posizioneprec+26))

        stringa += nuovocarattere

    return stringa

# Soluzione con l'array
def cifraparola(n,m,p):
    stringa = ""
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    for i in range(len(p)):
        pos_alfabeto = alfabeto.index(p[i])
        if (i+1) % 2 != 0:
            pos_alfabeto += n
            if pos_alfabeto > 25:
                pos_alfabeto = 0 + (pos_alfabeto-26)
        else:
            pos_alfabeto -= m
            if pos_alfabeto < 0:
                pos_alfabeto =  26 + pos_alfabeto
        
        stringa += alfabeto[pos_alfabeto]

    return stringa

            

def main():
    n1 = int(input())
    n2 = int(input())
    s = input().upper()
    parola = ""

    while s != ".":
        parola += s
        s = input().upper()
    
    result = cifraparola(n1, n2, parola)

    if (result != ""):
        print(result, end='')


main()