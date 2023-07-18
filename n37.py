def isvocale(x):
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        return True
    else:
        return False

l = []
cont = 0
precedentevocale = ""

for c in range(100):
    l.append(input())

for i in range(len(l)):
    if (isvocale(l[i]) and precedentevocale != l[i]):
        cont += 1
        precedentevocale = l[i]

if (cont <= 1):
    print("OK", end='')
else:
    print("ERRORE", end='')
