n = input()
l = []
condizione = False

while n != "*":
    l.append(n)
    n = input()

if (len(l) > 1 or not l == []):
    for i in range(1,len(l)):
        if (l[i-1] == l[i]):
            condizione = True

if(condizione):
    print("SI",end='')
else:
    print("NO",end='')



