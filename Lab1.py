def isprime(k):
    for i in range(2, k//2+1):
        if (k % i == 0):
            return False
    return True
        
def numeromax(A):
    maxA = A[0]
    for i in range(len(A)):
        if (maxA < A[i]):
            maxA = A[i]
    return maxA

def rivelazionecoppie(lista):
    somm = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            s = lista[i] + lista[j]
            if (isprime(s) == False and s % 2 != 0):
                somm.append(s)
    return somm

n = int(input())
l = []
somme = []

for k in range(n):
    l.append(int(input()))

if (n > 2): 
    somme = rivelazionecoppie(l)
    if (len(somme) > 0):
        MassimoDnop = numeromax(somme)
        print(MassimoDnop, end='')
    else:
        print("0", end='')
else:
    print("0", end='')