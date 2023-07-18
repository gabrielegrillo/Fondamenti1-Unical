def sommacroce(mat):
    sumout = 0
    sumcroce = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (i != len(mat)//2 and j != len(mat)//2):
                sumout += mat[i][j]
            else:
                sumcroce += mat[i][j]
    
    return 'OK' if sumcroce > sumout else 'NO'


def main():
    n = int(input())

    m = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        m.append(row)
    
    print(sommacroce(m), end='')


main()