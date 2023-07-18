n = input()
nessunCarattere = True
while n != ".":
    if ((n >= "A" and n <= "Z") or (n >= "a" and n <= "z")):
        nessunCarattere = False
    n = input()

if (nessunCarattere):
    print("SI", end='')
else:
    print("NO", end='')