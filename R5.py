def f(lista,dest,index):
    if (index < 0):
        return dest
    else:
        dest.append(lista[index])
        return f(lista, dest, index-1)


def main():
    n = int(input())
    l = []

    while len(l) < n:
        l.append(int(input()))

    ris = f(l,[], len(l)-1)

    for i in range(len(ris)):
        print(ris[i],end='',sep='')


main()