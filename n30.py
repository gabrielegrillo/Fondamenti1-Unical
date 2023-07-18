def entrambigrand(a,b):
    if ( (a.isupper() and b.isupper()) or (a.islower() and b.islower())):
        return True
    else:
        return False


n = input()
l = []

condizione = False 

while n != "*":
    l.append(n)
    n = input()



if (len(l) != 0):
    m = l[0]
    for i in range(1,len(l)):
        if (l[i].isalpha()):
            if (l[i] == m and entrambigrand(l[i], m)):
                condizione = True
        m = l[i]


if (condizione):
    print("SI", end='')
else:
    print("NO", end='')
