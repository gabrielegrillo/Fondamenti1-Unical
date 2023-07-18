# 1. si cerchino tutte le occorrenze dell’intero target,
# 2. nelle relative posizioni si sostituisca target con 0;
# 3. sia inoltre il numero di queste occorrenze C;
# 4. si ponga target = C e si ripeta il procedimento appena illustrato ricominciando dallo step 1.
def trova(lista, index, t, occ):
    if (index >= len(lista)):
        if (occ > 0):
            return trova(lista, 0, occ, 0)
        else:
            return 0
    else:
        if (lista[index] == t):
            lista[index] = 0
            return 1 + trova(lista,index+1,t,occ+1)
        else:
            return trova(lista,index+1,t,occ)


def main():
    x = int(input())
    n = int(input())
    l = []

    while len(l) < n:
        l.append(int(input()))

    print(trova(l,0,x,0), end='')

    

main()