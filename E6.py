mat = []

# contare gli anni 
def puntoa(M):
    maxcount = 0
    anno = 0
    for i in range(len(M)):
        count = 0
        for j in range(1,len(M)):
            if (M[i][1] == M[j][1]):
                count += 1
        
        if(count > maxcount):
            maxcount = count
            anno = M[i][1]

    return anno

# def puntob0(anno):
#     sum = 0 
#     for i in range(len(mat)):
#         if (mat[i][1] == anno):
#             sum += mat[i][0]
#     if sum==0: return 'SI' 
#     else: return 'NO'

def puntob(M,anno):
    for i in range(len(M)):
        if(M[i][1] == anno and M[i][0] != 0):
            return 'NO'
    return 'SI' 


def main():
    n = int(input())
    annox = int(input())

    for i in range(n):
        riga = []
        for j in range(2):
            riga.append(int(input()))
        mat.append(riga)

    print(puntoa(mat),puntob(mat,annox),end='')


    




main()