# TODO: Da finire... 
def vocale(x):
    ''' Verifica se una stringa è una consonante o vocale
        se restituisce vero è una vocale altrimenti è una consonante'''
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        return True
    else:
        return False

n = input()
m = ""
o = ""
voc = False
cons = False
c1 = voc
c2 = cons
countersets = 1
if (n == "."):
    countersets = 0
while n != ".":
    m = o
    o = n
    c1 = voc
    c2 = cons
    voc = vocale(n)
    cons = not vocale(n)
    if (c1 == True and voc == True):
        countersets += 1
    if (c2 == True and cons == True):
        countersets += 1
    n = input()
    if (n == "."):
        voc = False
        cons = False

print(countersets, end='')

