def convertidati(x):
    lista = []
    for i in range(len(x)):
        elemento = int(x[i])
        lista.append(elemento)
    return lista

def checkfortunato(x):
    array = convertidati(x)
    
    primameta = array[:len(array)//2]
    sumprimo = 0
    secondameta = array[len(array)//2:]
    sumsecondo = 0 

    for i in range(len(primameta)):
        sumprimo += primameta[i]

    for i in range(len(secondameta)):
        sumsecondo += secondameta[i]

    return sumprimo == sumsecondo
    

def main():
    n = input()

    if(checkfortunato(n)):
        print("FORTUNATO",end='')
    else:
        print("SFORTUNATO",end='')



main()