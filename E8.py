def verificaNumeriRipetuti(M):
    for i in range(len(M)):
        for j in range(1,len(M)):
            if (M[i][j] == M[i][j-1]):
                return "NO"

    for i in range(1,len(M)):
        for j in range(len(M)):
            if (M[j][i] == M[j][i-1]):
                return "NO"
    return "SI"


def main():
    n = int(input())

    mat = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        mat.append(row)

    print(verificaNumeriRipetuti(mat),end='')

main()