def ispotenza2(n):
    if(n==0):
        return False
    while(n != 1):
        n = n/2
        if (n%2 != 0 and n != 1):
            return False
    return True

n = int(input())
l = []
i = 0
potenze2 = True

while n != 0:
    l.append(n)
    n = int(input())

while potenze2 and i < len(l):
    if (not ispotenza2(l[i])):
        potenze2 = False
    i += 1

if (potenze2):
    print("SI", end='')
else:
    print("NO", end='')