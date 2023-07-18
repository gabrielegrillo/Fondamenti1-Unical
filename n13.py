n = int(input())
k = int(input())


counterN = 0
for i in range(1,n+1):
    remainder = n % i
    if (remainder == 0):
        counterN += 1

counterK = 0
for i in range(1,k+1):
    remainder = k % i
    if (remainder == 0):
        counterK += 1

sub = abs(n-k)

if (counterN == 2 and counterK == 2):
    if (sub == 2):
        print("gemelli",end='')
    else:
        print("non gemelli",end='') 
else:
    print("non entrambi primi",end='')