X = int(input())
N = int(input())
i = 1
ris = ""
for i in range (1, N+1):
    Y = int(input())
    if (X > Y and Y % 2 == 0):
        ris += str(Y)
    
if (len(ris) > 0):
    print(ris, end="")
#   15 1 15 3