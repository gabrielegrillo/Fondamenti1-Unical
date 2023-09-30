import random
## Punto 1 - funzione ricorsiva
## tutte le caselle ad eccezione di quelle danneggiate devono essere coperte da una tessera 
## e quindi lecelle corrispondenti devono contenere un valore maggiore o uguale ad 1.
def validitatessera(matrice_schema, matrice_possibile, n, row):
    if (row >= n):
        return True
    else:
        for j in range(n):
            if (matrice_schema[row][j] != -1):
                if (matrice_possibile[row][j] < 1):
                    return False
        return validitatessera(matrice_schema, matrice_possibile, n, row+1)
## Punto 2 - le tessere non possono essere rotte, perciò ogni tessera deve essere usata per ricoprire esattamente
## due celle che devono essere adiacenti orizzontalmente o verticalmente.
def controlloadiacente(mat, n):
    for i in range(n):
        for j in range(n):
            if (mat[i][j] >= 1):
                if (not trova_tessera(mat, mat[i][j], i, j, n)):
                    return False
    return True
## Punto 3 - permutazione matrice 
def crea_possibile_soluzione(matpartenza, matvalori, n):
    numeritessere = []
    posizionitessere = []
    for i in range(n):
        for j in range(n):
            if (matvalori[i][j] != -1 and not trova_elemento(numeritessere, matvalori[i][j])):
                    numeritessere.append(matvalori[i][j])
                    stringa = f"{i};{j};"
                    if (i+1 < n and matvalori[i][j] == matvalori[i+1][j]):
                        stringa += f"{i+1};"
                        stringa += f"{j};"
                    elif (j+1 < n and matvalori[i][j] == matvalori[i][j+1]):
                        stringa += f"{i};"
                        stringa += f"{j+1};"
                    posizionitessere.append(stringa)


    mat = matpartenza
    while (len(numeritessere) != 0): 
        x = random.choice(numeritessere)
        y = random.choice(posizionitessere)
        array = y.split(";")
        if (mat[int(array[0])][int(array[1])] == 0 and mat[int(array[2])][int(array[3])] == 0):
            mat[int(array[0])][int(array[1])] = x
            mat[int(array[2])][int(array[3])] = x
            numeritessere.remove(x)
            posizionitessere.remove(y)

    return mat
## Funzione ausiliare per il punto 2.
def trova_tessera(mat, target, i, j, n):
    if (i >= 0 and j >= 0 and i < n and j < n):
        ## Elemento di sopra
        if (i-1 >= 0 and mat[i-1][j] == target):
            return True
        ## Elemento di sotto
        if (i+1 < n and mat[i+1][j] == target):
            return True
        ## Elemento di destra
        if (j+1 < n and mat[i][j+1] == target):
            return True    
        ## Elemnto di sinistra
        if (j-1 >= 0 and mat[i][j-1] == target):
            return True
    return False
## Funzione ausiliare per il punto 3.
def trova_elemento(l, x):
    for i in range(len(l)):
        if (l[i] == x):
            return True
    return False

def print_matrice(mat):
    for i in range(len(mat)):
        print(mat[i])

def inputmatrice(x):
    m = [] 
    for i in range(x):
        row = []
        for j in range(x):
            row.append(int(input()))
        m.append(row)
    return m

def main():
    n = int(input())

    matpartenza = inputmatrice(n)
    mataggiustata = inputmatrice(n)

    if (len(matpartenza) == len(mataggiustata) and len(matpartenza[0]) == len(matpartenza[0])):
        if (validitatessera(matpartenza, mataggiustata, n, 0) and controlloadiacente(mataggiustata, n)):
            print("OK", end='')
            ## Genera 
            print()
            print_matrice(crea_possibile_soluzione(matpartenza, mataggiustata, n))

    else:
        print("NO",end='')


main()