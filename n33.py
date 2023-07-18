import random 
random.seed(0)
punteggioUtente = 0
punteggioPC = 0

while (punteggioPC < 3 and punteggioUtente < 3):
    sceltaPC = random.randint(1,3)

    sceltaUtente = int(input('Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):'))
    while(sceltaUtente > 3 or sceltaUtente < 1):
        sceltaUtente = int(input('Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):'))

    if (sceltaUtente == 1):
        print("hai giocato sasso")
    elif (sceltaUtente == 2):
        print("hai giocato carta")
    else:
        print("hai giocato forbice")


    if (sceltaPC == 1):
        print("il PC ha giocato sasso")
    elif (sceltaPC == 2):
        print("il PC ha giocato carta")
    else:
        print("il PC ha giocato forbice")


    if (sceltaPC == sceltaUtente):
        print("Pari:")
    elif (sceltaPC == 2 and sceltaUtente == 1):
        print("Vince il PC:")
        punteggioPC += 1
    elif (sceltaPC == 1 and sceltaUtente == 2):
        print("Vinci tu:")
        punteggioUtente += 1
    elif (sceltaPC == 1 and sceltaUtente == 3):
        print("Vince il PC:")
        punteggioPC += 1
    elif (sceltaPC == 3 and sceltaUtente == 1):
        print("Vinci tu:")
        punteggioUtente += 1
    elif (sceltaPC == 3 and sceltaUtente == 2):
        print("Vince il PC:")
        punteggioPC += 1
    elif (sceltaPC == 2 and sceltaUtente == 3):
        print("Vinci tu:")
        punteggioUtente += 1

    print(punteggioUtente,punteggioPC, sep='-')

if (punteggioPC == 3):
    print("Il PC ha vinto la sfida!")
else:
    print("Hai vinto la sfida!")