voto = int(input())

VotoPrimoCandidato = 0
VotoSecondoCandidato = 0
VotoTerzoCandidato = 0

if (voto == 0):
    print("BALLOTTAGGIO", end="")
else:
    while voto != 0:
        if (voto == 1):
            VotoPrimoCandidato += 1
        elif (voto == 2):
            VotoSecondoCandidato += 1
        elif (voto == 3):
            VotoTerzoCandidato += 1
        voto = int(input())

    PercentualePrimoCandidato = VotoPrimoCandidato / (VotoPrimoCandidato+VotoSecondoCandidato+VotoTerzoCandidato) * 100
    PercentualeSecondoCandidato = VotoSecondoCandidato / (VotoPrimoCandidato+VotoSecondoCandidato+VotoTerzoCandidato) * 100
    PercentualeTerzoCandidato = VotoTerzoCandidato / (VotoPrimoCandidato+VotoSecondoCandidato+VotoTerzoCandidato) * 100

    print("1", VotoPrimoCandidato, round(PercentualePrimoCandidato,1))
    print("2", VotoSecondoCandidato, round(PercentualeSecondoCandidato,1))
    print("3", VotoTerzoCandidato, round(PercentualeTerzoCandidato,1))


    if (PercentualePrimoCandidato > 50):
        print("VINCE 1", end="")
    elif (PercentualeSecondoCandidato > 50):
        print("VINCE 2", end="")
    elif (PercentualeTerzoCandidato > 50):
        print("VINCE 3", end="")
    else: 
        print("BALLOTTAGGIO", end="")
