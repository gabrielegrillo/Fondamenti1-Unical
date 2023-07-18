n = int(input())
seq = int(input())
k = 0
l = []
crescente = False


while seq != -1:
    l.append(seq)
    seq = int(input())

for i in range(len(l)):
    if (l[i] <= n):
        k += 1
    if k >= n:
        crescente = True
    if (l[i] > n and crescente == False):
        k = 0

if (crescente):
    print("OK", end='')
else:
    print("NO", end='')
    
