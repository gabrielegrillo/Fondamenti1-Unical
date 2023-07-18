from math import log2

def controlloValiditàStringa(str):
    for i in range(len(str)):
        if (str[i] != '0' and str[i] != "1"):
            return False
    return True

def neg(listastr):
    listastr = list(listastr)
    for i in range(len(listastr)):
        if listastr[i] == '0':
            listastr[i] = '1'
        else:
            listastr[i] = '0'
    return ''.join(listastr)

def costruisciThueMorseRev(n):
    if (n == 0):
        return '0'
    else:
        previous = costruisciThueMorseRev(n-1)
        return previous + neg(previous) 
    
def costruisciThueMorse(n):
    seq = "0"
    for i in range(1, n):
        seq += neg(seq)
    return seq

def main():
    successione = input()

    if (controlloValiditàStringa(successione)):
        if (len(successione) > 25):
            if (costruisciThueMorse(len(successione)//3)[0:len(successione)] == successione):
                print("SI", end='')
            else:
                print("NO", end='')
        else:
            if (costruisciThueMorse(len(successione))[0:len(successione)] == successione):
                print("SI", end='')
            else:
                print("NO", end='')
    else:
        print("NO", end='')

main()


""" if (costruisciThueMorse(len(successione))[0:len(successione)] == successione):
            print("SI", end='')
        else:
            print("NO", end='') """