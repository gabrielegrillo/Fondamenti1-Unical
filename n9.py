x = int(input())
i = 0
while x != 0:
    x =int(input())
    if (x % 3 == 0 and x % 2 != 0):
        i += 1
print(i,end="")