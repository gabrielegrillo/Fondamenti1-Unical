n = input()
l = []
condizione = False

while n != "*":
    l.append(n)
    n = input()


if (len(l)>2):
    for i in range(1,len(l)):
        if (l[i-1].isalnum() == True and l[i].isalnum() == True):
            if ((l[i-1].isupper() == True and l[i].isupper() == True) or (l[i-1].islower() == l[i].islower() and l[i-1] == l[i])):
                condizione = True

if(condizione):
    print("SI",end='')
else:
    print("NO",end='')



