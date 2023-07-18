def trovaPosto(Reparto):
    i = 0
    maxReparto = 0
    PostoScelto = -1
    
    if (Reparto == "1"):
        maxReparto = 5
    elif(Reparto == "2"):
        i = 5
        maxReparto = 10

    while PostoScelto == -1 and i < maxReparto:
        if (Posti[i] == 0):
            PostoScelto = i
            Posti[i] = 1
        else:
            i += 1
    return PostoScelto
        
def controlloTuttiOccupati():
    for i in range(len(Posti)):
        if (Posti[i] == 0):
            return False
    return True
Posti = [0,0,0,0,0,0,0,0,0,0]
while(not controlloTuttiOccupati()):
    
    SceltaReparto = input("Digitare 1 per fumatori o 2 per non fumatori:")

    PostoScelto = trovaPosto(SceltaReparto)

    if (PostoScelto != -1 and SceltaReparto == "1"):
        postostampa = PostoScelto+1
        print("Reparto fumatori, posto", postostampa)

    if (PostoScelto != -1 and SceltaReparto == "2"):
        postostampa = PostoScelto+1
        print("Reparto NON fumatori, posto", postostampa)

    if (PostoScelto == -1):
        scelta = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
        if (scelta == "N"):
            print("Il prossimo volo parte tra 3 ore")
        
        if (scelta == "S"):
            PostoScelto == -1
            if (SceltaReparto == "1"):
                PostoScelto = trovaPosto("2")
                postostampa = PostoScelto+1
                print("Reparto NON fumatori, posto", postostampa)
            else:
                PostoScelto = trovaPosto("1")
                postostampa = PostoScelto+1
                print("Reparto fumatori, posto", postostampa)