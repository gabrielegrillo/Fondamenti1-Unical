n = input()
p = n
i = 0
termina = False
while termina == False:
    n = input()
    if (p == "o" and n == "k"):
        termina = True
    else:
        i += 1
    p = n

print(i, end='')
    
