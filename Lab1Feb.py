def controllo(num,den):
    possalvata = -1
    for i in range(1, len(num)):
        ac = num[i-1] * num[i]
        bd = den[i-1] * den[i]

        if (ac // bd == -1):
            print(f"Frazione trovata: {num[i-1]}/{den[i-1]} e {num[i]}/{den[i]}")
            if (possalvata != -1):
                if (possalvata == i-1):
                    return True
            else:
                possalvata = i
        else:
            possalvata = -1
    
    
    return False


def main():
    n = int(input())
    numeratori = []
    denominatori = []

    while len(numeratori) < n:
        numeratori.append(int(input()))

    while len(denominatori) < n:
        denominatori.append(int(input()))

    if (controllo(numeratori,denominatori)):
        print("SI",end='')
    else:
        print("NO",end='')

main()