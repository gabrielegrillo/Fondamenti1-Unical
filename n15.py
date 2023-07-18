n = int(input())
m = -1
i = 0
k = 1
countersets = 0 
finish = False
counterFinish = 0
while counterFinish != 3:
    if (n == 9):
        counterFinish += 1
    else:
        counterFinish = 0
        if (n == m):
            k += 1
        else:
            k = 1
        if (k >= 3):
            countersets += 1
    if (counterFinish != 3):
        m = n
        n = int(input())

print(countersets, end='')
        
    

