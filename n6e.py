SemeBriscola=int(input())
SemePlayer1=int(input())
CartaPlayer1=int(input())
SemePlayer2=int(input())
CartaPlayer2=int(input())

if(CartaPlayer1==1):
    CartaPlayer1=20
elif(CartaPlayer1==3):
    CartaPlayer1=19

if(CartaPlayer2==1):
    CartaPlayer2=20

elif(CartaPlayer2==3):
    CartaPlayer2=19

#Caso in cui si butta una briscola e l'avversasrio un seme qualsiasi
if(SemeBriscola==SemePlayer1 and SemeBriscola!=SemePlayer2):
    print("VINCE GIOCATORE 1", end="")
#Caso in cui si butta una briscola e l'avversasrio un seme qualsiasi
elif(SemeBriscola==SemePlayer2 and SemeBriscola!=SemePlayer1):
    print("VINCE GIOCATORE 2", end="")

#Caso in cui si butta una briscola più grande di quella avversaria
elif(SemeBriscola==SemePlayer1 and SemeBriscola==SemePlayer2):
    if(CartaPlayer1>CartaPlayer2):
        print("VINCE GIOCATORE 1", end="")
    else:
        print("VINCE GIOCATORE 2", end="") 
#Caso in cui il primo giocatore butta un seme e l'avversario risponde con un seme diverso dalla briscola e dal seme buttato dal primo
elif(SemePlayer1!=SemeBriscola and SemePlayer2!=SemeBriscola and SemePlayer1!=SemePlayer2):
    print("VINCE GIOCATORE 1", end="")

#Caso in cui il primo giocatore butta un seme e l'avversario risponde con un seme diverso dalla briscola ma uguale a quello tirato dal primo

elif(SemePlayer1!=SemeBriscola and SemePlayer2!=SemeBriscola and SemePlayer1==SemePlayer2):
    if(CartaPlayer1>CartaPlayer2):
        print("VINCE GIOCATORE 1", end="")
    else:
        print("VINCE GIOCATORE 2", end="")