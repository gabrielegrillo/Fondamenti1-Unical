a = input()
l = []
l.append(a)

while len(l) != 26:
    a = input()
    l.append(a)
    
n = int(input())

lb = []


for i in range(n):
    e = int(input())
    lb.append(e)

parola = ""

for i in range(len(lb)):
    posizione = lb[i]
    if (posizione < 26):
        parola += l[posizione]

print(parola,end='')