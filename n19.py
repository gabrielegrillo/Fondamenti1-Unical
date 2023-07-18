n = input()
leastone = False

while n != "*":
    if (n >= "0" and n <= "9"):
        leastone = True
    n = input()

if (leastone):
    print("ALMENO UNA", end='')
else:
    print("NESSUNA", end='')
