Matrice = []

def controllaMatriceNonogram(lrighe,lcolonne):
    m = len(Matrice)

    # Scansione righe
    for i in range(m):
        cellerighe = lrighe[i]
        for j in range(m):
            if (Matrice[i][j] == 1):
                cellerighe -= 1
        
        if (cellerighe != 0):
            return False

    # Scansione Colonne
    for i in range(m):
        cellecolonne = lcolonne[i]
        for j in range(m):
            if (Matrice[j][i] == 1):
                cellecolonne -= 1
        
        if (cellecolonne != 0):
            return False

    return True
        

def main():
    n = int(input())

    for i in range(n):
        riga = []
        for j in range(n):
            riga.append(int(input()))
        Matrice.append(riga)

    ListaNumsColonna = []
    for i in range(n):
        ListaNumsColonna.append(int(input()))
    
    ListaNumsRiga = []
    for i in range(n):
        ListaNumsRiga.append(int(input()))

    if(controllaMatriceNonogram(ListaNumsRiga, ListaNumsColonna)):
        print("SI", end='')
    else:
        print("NO", end='')

main()