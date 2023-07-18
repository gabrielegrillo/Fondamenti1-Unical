def controlloalberi(m, indiceriga, numalberi, count):
    if (indiceriga >= len(m)):
        return numalberi == count
    else:
        countalbeririga = 0
        for j in range(len(m[0])):
            if (m[indiceriga][j] == "*"):
                countalbeririga += 1
        
        return controlloalberi(m, indiceriga+1, numalberi, count+countalbeririga)

def controllopiucase(m):
    for i in range(len(m)):
        countalberi = 0
        countcase = 0
        for j in range(len(m[0])):
            if (m[i][j] == "*"):
                countalberi += 1
            else:
                if (m[i][j] != "0"):
                    countcase += 1
        if (countalberi > countcase):
            return False 
    
    return True

def controlloalberiadiacenti(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (m[i][j] != "0" and m[i][j] != "*"):
                countalberi = 0
                for k in range(i-1,i+2):
                    if (k < 0 or k >= len(m)):
                        continue
                    else:
                        for l in range(j-1,j+2):
                            if (l < 0 or l >= len(m[0])):
                                continue
                            else:
                                if (m[k][l] == "*"):
                                    countalberi += 1

                if (str(countalberi) != m[i][j]):
                    return False
    return True

def main():
    n = int(input())
    m = int(input())
    a = int(input())

    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(input())
        mat.append(row)

    # print("Controllo alberi:", controlloalberi(mat, 0, a, 0))
    # print("Controllo più case che alberi", controllopiucase(mat))
    # print("Controllo alberi adiacenti alle case", controlloalberiadiacenti(mat))

    if (controlloalberi(mat, 0, a, 0) and controllopiucase(mat) and controlloalberiadiacenti(mat)):
        print("OK", end='')
    else:
        print("NO", end='')



main()