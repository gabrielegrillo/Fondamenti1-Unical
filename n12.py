n = int(input())

counter = 0

for i in range(1,n+1):
    remainder = n % i
    if (remainder == 0):
        counter += 1

if (counter == 2):
    print("SI",end='')
else:
    print("NO", end='')