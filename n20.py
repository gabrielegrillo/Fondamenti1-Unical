n = input()
soloCaratteri = True
while n != ".":
    if ((n <= "@" or (n >= "[" and n <= "`") or (n >= "{" and n <= "˜"))):
        soloCaratteri = False
    n = input()

if (soloCaratteri):
    print("SI", end='')
else:
    print("NO", end='')