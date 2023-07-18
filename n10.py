X = int(input())
N = X
RevX = 0 
while X != 0:
    Posizione = int(X % 10)
    RevX = (RevX * 10) + Posizione
    X //= 10

X = int(N - RevX)
print( X, end='')