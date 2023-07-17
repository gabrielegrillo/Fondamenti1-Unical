# punto 1 - Funzione Ricorsiva
# ciascuna cella nera contenente un numero abbia attaccate 
# esattamente il numero di lampadine richiesto
def check_lampadine(mat, i, j, n, m):
    if (i >= n):
        return 'SI'
    if (j >= m):
        return check_lampadine(mat, i+1, 0, n, m)
    else:
        if (is_cellanera(mat,i,j)):
            if (contalampadine(mat, i, j, n, m) != mat[i][j]):
                return 'NO'
    
    return check_lampadine(mat, i, j+1, n, m)

## punto 2 - tutte le celle vuote siano illuminate.
def celle_vuote_illuminate(mat, n, m):   
    for i in range(n):
        for j in range(m):
            if (mat[i][j] == -1):
                if (not is_cella_illuminata(mat, i, j, n, m, 0)):
                    return 'NO'
    return 'SI'    

## punto 3 - che non ci siano lampadine che si illuminano tra loro.
def punto3(mat, n, m):
    for i in range(n):
        for j in range(m):
            if (mat[i][j] == 6):
                if (is_cella_illuminata(mat, i, j, n, m, 0)):
                    return 'NO'
    return 'SI'

## Funzione ausiliare per il punto 1
def is_cellanera(mat,i,j):
    return (mat[i][j] >= 0 and mat[i][j] <= 4)

## Funzione ausiliare per il punto 1
def contalampadine(mat, i, j, n, m):
    count = 0 
    if (i >= 0 and j >= 0):
        # Controllo elemento di sopra.
        if (i-1 >= 0 and mat[i-1][j] == 6):
            count += 1
        # elemento di sotto
        if (i+1 < n and mat[i+1][j] == 6):
            count += 1
        # elemento di sinistra
        if (j-1 >= 0 and mat[i][j-1] == 6):
            count += 1
        # elemento di destra
        if (j+1 < m and mat[i][j+1] == 6):
            count += 1
    return count


## Funzione ricorsiva e ausiliare per i punti 2 e 3.
def is_cella_illuminata(mat, i, j, n, m, direzione):
    # 0 -> sopra
    # 1 -> giu'
    # 2 -> destra
    # 3 -> sinistra
    if (direzione == 4):
        return False
    else:
        if (direzione == 0):
            for col in range(j-1,-1,-1):
                if (mat[i][col] == 6):
                    return True
                if (mat[i][col] != -1):
                    return is_cella_illuminata(mat, i, j, n, m, direzione+1)
            return is_cella_illuminata(mat, i, j, n, m, direzione+1)
        if (direzione == 1):
            for col in range(j+1, m):
                if (mat[i][col] == 6):
                    return True
                if (mat[i][col] != -1):
                    return is_cella_illuminata(mat, i, j, n, m, direzione+1)
            return is_cella_illuminata(mat, i, j, n, m, direzione+1)
        if (direzione == 2):
            for row in range(i+1, n):
                if (mat[row][j] == 6):
                    return True
                if (mat[row][j] != -1):
                    return is_cella_illuminata(mat, i, j, n, m, direzione+1)
            return is_cella_illuminata(mat, i, j, n, m, direzione+1)
        if (direzione == 3):
            for row in range(i-1, -1, -1):
                if (mat[row][j] == 6):
                    return True
                if (mat[row][j] != -1):
                    return is_cella_illuminata(mat, i, j, n, m, direzione+1)
            return is_cella_illuminata(mat, i, j, n, m, direzione+1)

## Prima idea di funzione ricorsiva... tenuta come ricordo.
def check_lampadine_mia(m,i, j, count, direzione):
    if (direzione == 5 and m[i][j] == count):
        return True
    else:
        # controllo elemento sopra
        if (direzione == 1):
            if (i-1 >= 0 and m[i-1][j] == 6):
                return check_lampadine(m, i, j, count+1, 2)
            else:
                return check_lampadine(m, i, j, count, 2)
        elif (direzione == 2): # controllo elemento sotto
            if (i+1 < len(m) and m[i+1][j] == 6):
                return check_lampadine(m, i, j, count+1, 3)
            else:
                return check_lampadine(m, i, j, count, 3)
        elif (direzione == 3): # controllo verso destra
            if (j+1 < len(m[0]) and m[i][j+1] == 6):
                return check_lampadine(m, i, j, count+1, 4)
            else:
                return check_lampadine(m, i, j, count, 4)
        elif (direzione == 4): # controllo verso sinistra
            if (j-1 >= 0 and m[i][j-1] == 6):
                return check_lampadine(m, i, j, count+1, 5)
            else:
                return check_lampadine(m, i, j, count, 5)
        else:
            return False

def input_matrice(x, y):
    m = []
    for i in range(x):
        r = []
        for j in range(y):
            r.append(int(input()))
        m.append(r)
    return m 

def main():
    n = int(input())
    m = int(input())

    matrice = input_matrice(n,m)
    print(check_lampadine(matrice,0,0,n,m) + celle_vuote_illuminate(matrice, n, m) + punto3(matrice, n, m))


main()