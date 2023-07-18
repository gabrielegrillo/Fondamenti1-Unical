def rip(n):
    while n != 0:
        n = int(input())
    return n 

prec = int(input())
esito = True
check1 = False


if (prec != 0):
    precnn = int(input())
    if (precnn != 0):
        if (precnn > prec):
            prec = precnn
            n = int(input())
        else:
            n = rip(int(input()))
    else:
        esito = False
        n = 0
    if (n !=0):
        while n != 0:
            if (prec >= n):
                check1 = True

            if (check1):
                if (prec <= n):
                    esito = False
            
            prec = n
            n = int(input())


print("SI" if check1 and esito else "NO", end='')
