def controlloRisposte(ris, m):
    for i in range(len(m)):
        rispostestudente = m[i][1]
        # scansione rispsote e attribuzioni punti
        for j in range(len(ris)):
            if (rispostestudente[j] == ris[j]):
                m[i][2] += 2
            elif (rispostestudente[j] != ris[j] and rispostestudente[j] != 'X'):
                m[i][2] -= 1

def main():
    n = input()
    mat = []

    for i in range(90):
        row = []
        for j in range(3):
            if(j != 2):
                row.append(input())
            else:
                row.append(0)
        mat.append(row)

    controlloRisposte(n, mat)
        
    for i in range(len(mat)):
        print(mat[i][0],mat[i][2])


main()