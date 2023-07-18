n = int(input())
noncifradecimale = False
num = ""

while n != -1:
    if (n < 0 or n > 9):
        noncifradecimale = True
    else:
        num += str(n)
    n = int(input())


if (n == -1 and num == ""):
    print("VUOTO", end='')
else:
    if(noncifradecimale):
        print("ERRORE", end='')
    else:
        print(num)
        if (int(num) % 3 == 0):
            print("SI", end='')
        else:
            print("NO", end='')

