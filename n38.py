l = []
v = []

for k in range(100):
    l.append(int(input()))

for i in range(len(l)):
    if (l[i] > 50 or l[i] < -50):
        v.append(l[i])

if (v == []):
    print("VUOTO1")
else:
    stringa = ""
    for i in range(len(v)):
        print(v[i], sep='', end='')
    print(end='\n')

j = 0
somma = 0
for i in range(len(l)):
    if (l[i] >= -50 and l[i] <= 50):
        somma += l[i]
        j += 1
if(j == 0):
    print("VUOTO2", end='')
else:
    media = round(somma / j,6)
    print(media, end='')

    
