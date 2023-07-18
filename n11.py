n = int(input())
diverso = False

if (n == 0):
    diverso = True

while n != 0:
    ultimacifra = n % 10
    if (ultimacifra == 0):
        diverso = True
    n = n // 10

if (diverso):
    print("NO", end='')
else:
    print("SI", end='')