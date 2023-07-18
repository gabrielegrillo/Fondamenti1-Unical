# TODO: Da aggiustare

n = input()
SoloLettere = False 

while n != ".":
    if (((n >= "A" and n <= "Z") or (n >= "a" and n <= "z"))):
        SoloLettere = True
    n = input()


if (SoloLettere):
    print("SI", end='')
else:
    print("NO", end='')