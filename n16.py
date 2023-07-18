x = int(input())
n = int(input())
k = 0
counterX = False

while n != -1:
    if (n == 0):
        k += 1
    else:
        k = 0
    if (k>=x):
        counterX = True
    n = int(input())

if (counterX):
    print("OK", end='')
else:
    print("NO", end='')