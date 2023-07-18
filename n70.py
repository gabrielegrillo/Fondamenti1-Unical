def isvocale(x):
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        return True
    else:
        return False

def codificafarfallina(str):
    codificata = ""
    for i in range(len(str)):
        if (isvocale(str[i])):
            codificata += str[i] + 'f' + str[i]
        else:
            codificata += str[i]
    return codificata

def invertistringa(str):
    invertita = ""
    for i in range(len(str)//2, len(str)):
        invertita += str[i]
    for j in range(0,len(str)//2):
        invertita += str[j]
    return invertita

def main():
    n = input()

    print(invertistringa(codificafarfallina(n)),end='')

main()

