def bomba(matrice):
    for i in range(len(matrice[0])):
        bombetrovate = 0
        for j in range(len(matrice)):
            if (matrice[j][i] == 0):
                bombetrovate += 1
                if (bombetrovate > 1):
                    return False
        if (bombetrovate != 1):
            return False  
        
    for i in range(len(matrice)):
        bombetrovate = 0
        for j in range(len(matrice[0])):
            if (matrice[i][j] == 0):
                bombetrovate += 1
                if (bombetrovate > 1):
                    return False
        if (bombetrovate != 1):
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

    
    if(bomba(mat)):
        print("SI", end='')
    else:
        print("NO", end='')
    
main()