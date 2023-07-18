x = int(input())
k = 1
l = []

crescente = True
solodispari = True

if (x != 0):
    n = int(input())
    l.append(n)

    while k < x:  
        n = int(input())
        l.append(n)
        k += 1
    
    i = 0
    while i < x-2:
        if (l[i] >= l[i+2]):
            crescente = False
        i += 2

    i = 1
    while i < x:
        if (l[i] % 2 == 0):
            solodispari = False
        i += 2


print("SI" if crescente and solodispari else "NO", end='')
