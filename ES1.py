def altamentecomposto(x):
    if (x < 0):
        return 'NO1'
    
    numerodivisori = 0
    for i in range(1,x+1):
        if (x % i == 0):
            numerodivisori += 1

    numdiv = 0
    for i in range(1,x): 
        numdiv = 0
        for j in range(1,i+1):
            if (i % j == 0):
                numdiv += 1
        if (numdiv > numerodivisori):
            return 'NO1'

    if (numerodivisori > numdiv):
        return 'OK1'
    else:
        return 'NO1'

def divisoriuguali(x,y):

    for i in range(1,x):
        numdiv = 0
        for j in range(1,i):
            if (i % j == 0):
                numdiv += 1
        if (numdiv == y):
            return 'OK2'
    
    return 'NO2'
        

def main():
    n = int(input())
    m = int(input())
    print(altamentecomposto(n),divisoriuguali(n,m),sep='',end='')


main()