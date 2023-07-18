def seqmax(lista):
    seq = lista[0]
    for i in range(len(lista)):
        if (len(lista[i]) > len(seq)):
            seq = lista[i]
    return seq


def sottoseqdecrescente(lista):
    if (len(lista) <= 2):
        return 0
    
    sottoseq = []
    for i in range(1,len(lista)):
        prec = lista[i-1]
        attuale = lista[i]
        if (prec > attuale):
            stringa = lista[i-1] + lista[i]
            sottoseq.append(stringa) 
            inizio = i+1 
            for j in range(inizio,len(lista)):
                successivo = lista[j]
                attuale = lista[i]
                if (attuale >= successivo):
                    stringa += lista[j]
                    sottoseq.append(stringa)
                else: 
                    break

                
    if (len(sottoseq) < 2):
        return 0
    
    seq = seqmax(sottoseq)
    indiceinizio = seq[0]
    indicefine = seq[len(seq)-1]
    for i in range(len(seq)):
        if (seq[i] < indiceinizio):
            indiceinizio = seq[i]
        
        if (seq[i] > indicefine):
            indicefine = seq[i]
    
    numcaratteridistanti = 0
    # calcolare distanza caratteri
    for i in range(ord(indiceinizio), ord(indicefine)-1):
        numcaratteridistanti += 1

    return numcaratteridistanti


def main():
    n = input()
    l = []

    while n != "*":
        l.append(n)
        n = input()

# aggiustare output per domjudge
    print(sottoseqdecrescente(l), end='')


main()