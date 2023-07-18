n = int(input())
k = 0
l = []

while k != 2:
    if (n == 0):
        k += 1
    else:
        k = 0
    l.append(n)
    if (k < 2):
        n = int(input())
    

sums = []
index = 0
sum = 0
for i in range(len(l)-1):
    if (l[i] != 0):
        sum += l[i]
    elif (l[1] and i == 0):
        sum = 0
        sums.append(sum)
    else:
        sums.append(sum)
        sum = 0

for i in range(len(sums)):
    print(sums[i])





