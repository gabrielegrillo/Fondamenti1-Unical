n = input()
l = []

s = 0
m = 0
h = 0

while n != "0":
    l.append(n)
    n = input()

for i in range(1,len(l)):
    if (l[i] == "s"):
        s += int(l[i-1])
    elif (l[i] == "m"):
        m += (60 * int(l[i-1]))
    elif (l[i] == "h"):
        h += (60 * 60 * int(l[i-1]))

somma = s + m + h
print(somma, end="")



