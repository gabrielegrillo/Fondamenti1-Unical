V = int(input())

if (V >= 0 and V <= 30):
    if (V >= 18):
        print("ESAME SUPERATO", end="")
    else:
        print("BOCCIATO", end="")
else:
    print("VOTO NON VALIDO", end="")