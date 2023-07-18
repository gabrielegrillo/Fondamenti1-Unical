def bombainquattrosettori(matrice):
    # Primo Settore
    countbombe = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])//3):
            elemento = matrice[i][j]
            if (elemento == 0):
                countbombe += 1
    if (countbombe != 1):
        return False

    # Secondo Settore ()
    countbombe = 0
    for i in range(len(matrice)//2):
        for j in range(len(matrice[0])//3, (len(matrice[0])//3)*2):
            if (matrice[i][j] == 0):
                countbombe += 1
    if (countbombe != 1):
        return False
    
    countbombe = 0
    for i in range(len(matrice)//2, len(matrice)):
        for j in range(len(matrice[0])//3, (len(matrice[0])//3)*2):
            if (matrice[i][j] == 0):
                countbombe += 1
    if (countbombe != 1):
        return False

    countbombe = 0

    for i in range(len(matrice)):
        for j in range((len(matrice[0])//3)*2, len(matrice[0])):
            if (matrice[i][j] == 0):
                countbombe += 1
    if (countbombe != 1):
        return False

    return True


def main():
    n = int(input())
    m = int(input())

    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input()))
        mat.append(row)

    
    if(n % 2 == 0 and m % 3 == 0):
        if(bombainquattrosettori(mat)):
            print("SI", end='')
        else:
            print("NO", end='')
    else:
        print("NO", end='')
                    
main()