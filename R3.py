def sommadiagonalesecondariaricorsiva(M,rows,columns):
    if (rows >= len(M)):
        return 0
    if (columns >= len(M)):
        return M[rows][columns-1] + sommadiagonalesecondariaricorsiva(M,rows+1,columns)
    else:
        return M[rows][columns] + sommadiagonalesecondariaricorsiva(M,rows+1,columns-1)

def sommadiagonalesecondariaiter(M):
    sum = 0
    for i in range(len(M)):
        sum += M[i][len(M)-i-1]
    return sum


def main():
    n = int(input())
    M = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        M.append(row)

    print(sommadiagonalesecondariaiter(M),";",sommadiagonalesecondariaricorsiva(M,0,len(M)-1),end='',sep='')


main()