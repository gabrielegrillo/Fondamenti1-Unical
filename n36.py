l = []
cond = True

for c in range(10):
    l.append(int(input()))

x = int(input())    

# aggiustare while 

# i = 0
# while cond == True or i < 9:
#     if (l[i] % x == 0):
#         cond = False 
#     i += 1

for i in range(len(l)):
    if (l[i] % x == 0):
        cond = False 

if (cond):
    print("OK", end='')
else:
    print("NO", end='')