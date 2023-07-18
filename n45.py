def convertidati(x):
    lista = []
    for i in range(len(x)):
        elemento = int(x[i])
        lista.append(elemento)
    return lista

def valore(lista):
    num = ""
    for i in range(len(lista)):
        num += str(lista[i])
    return int(num)

def main():
    n = input()
    l = convertidati(n)
    l.sort()
    Nmin = valore(l)
    l.sort(reverse=True)
    Nmax = valore(l)
    print(Nmax-Nmin,end='')

main()
