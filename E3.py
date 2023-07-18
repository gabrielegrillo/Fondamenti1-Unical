def setsmassimali(x):
    numsets = 0
    num = 0 

    for i in range(len(x)-1):
        precedente = x[i]
        successivo = x[i+1]
        
        if (precedente == successivo-1):
            num += 1
        else:
            if (num >= 1):
                numsets += 1 
            num = 0

    if (num >= 1):
        numsets += 1

    return numsets


def main():
    n = input()
    l = []

    while n != '*':
        n = int(n)
        l.append(n)
        n = input()
    
    print(setsmassimali(l),end='')


main()