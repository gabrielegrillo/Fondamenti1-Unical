a = int(input())
Multiplo = False
while a != 5:
    if (a % 5 == 0):
        Multiplo = True
    a =int(input())

if (Multiplo):
    print("ALMENO 1",end="")
else:
    print("NESSUNO", end="")
