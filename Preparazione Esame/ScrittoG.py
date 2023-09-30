def trova_carattere(s1, c):
    for i in range(len(s1)):
        if s1[i] == c:
            return True
    return False

def input_frase():
    lista = []
    n = input()
    while (n != "FINE"):
        lista.append(n)
        n = input()
    return lista

def determina_lunghezze_frasi(s1,s2):
    if (len(s1) >= len(s2)):
        frasepiulunga = len(s1)
        frasepiucorta = len(s2)
    else:
        frasepiulunga = len(s2)
        frasepiucorta = len(s1)

    return frasepiucorta, frasepiulunga

def conta_caratteri_uguali(s, y):
    count = 0
    for i in range(len(s)):
        if (s[i]== y[i]):
            count += 1
    return count


# Punto 1 - ricorsiva -Percentuale di sovrapposizione tra i testi, calcolata come: numero di parole in comune tra i due testi
# che si trovano esattamente nella stessa posizione diviso numero di parole totali del testo più lungo
# num parole in comune // num parole 
def punto1_iterativo(s1, s2):
    
    frasepiucorta, frasepiulunga = determina_lunghezze_frasi(s1, s2)

    count = 0 
    for i in range(frasepiucorta):
        if (s1[i] == s2[i]):
            count += 1
    
    percentuale = round((count / frasepiulunga) * 100)
    return str(percentuale) + "%"

def punto1(s1, s2, index, lenmin, lenmax, count):
    if (index >= lenmin):
        percentuale = round((count / lenmax) * 100)
        return str(percentuale) + "%"
    else:
        if (s1[index] == s2[index]):
            return punto1(s1, s2, index+1, lenmin, lenmax, count+1)
        else:
            return punto1(s1, s2, index+1, lenmin, lenmax, count)

## Punto 2 - Lunghezza della sequenza di parole consecutive uguali più lunga
def punto2(s1, s2, smin):
    count = 0 
    maxcount = 0
    for i in range(smin):
        if (s1[i] == s2[i]):
            count += 1
        else:
            if (maxcount < count):
                maxcount = count
            count = 0 
    return maxcount

# Punto 3 - Numero di coppie di parole simili nei due testi, ossia parole di uguale lunghezza che differiscono di
# esattamente un carattere (ad esempio, casa e cosa, oppure stella e stalla) oppure parole che
# possono essere ottenute l’una dall’altra con l’aggiunta o la rimozione di solo un carattere (ad
# esempio, lunga e luna, oppure canna e anna)
def punto3(s1, s2, smin):
    
    count = 0
    for i in range(smin):
        # Parole di uguale lunghezza che differiscono di esattamente un carattere
        # scansiono l'altro array uno per uno 
        for j in range(smin):
            if (len(s1[i]) == len(s2[j]) and s1[i] != s2[j]):
                counter = conta_caratteri_uguali(s1[i], s2[j])
                if (counter == len(s1[i])-1):
                    count += 1
        # parole che possono essere ottenute l’una dall’altra con l’aggiunta o la rimozione di solo un carattere
        # esempio: ad lunga e luna, oppure canna e anna
        
            elif (len(s1[i])-1 == len(s2[i])):
                counter = 0
                for k in range(len(s2[i])):
                    if (not trova_carattere(s2[j], s1[i][k])):
                        counter += 1
                
                if (counter == 1):
                    count += 1
        
            elif (len(s1[i]) == len(s2[i])-1):
                counter = 0
                for k in range(len(s1[i])):
                    if (not trova_carattere(s1[j], s2[i][k])):
                            counter += 1
                
                if (counter == 1):
                    count += 1

    return count


            
def main():

    farse1 = input_frase()
    frase2 = input_frase()
    
    frasepiucorta, frasepiulunga = determina_lunghezze_frasi(farse1, frase2)
    # print(farse1, frase2)
    print("Punto 1: " + punto1(farse1, frase2, 0, frasepiucorta, frasepiulunga, 0))
    print("Punto 2: " + str(punto2(farse1, frase2, frasepiucorta)))
    print("Punto 3: " + str(punto3(farse1, frase2, frasepiucorta)))
    # print("Punto 4: " + punto4(farse1, frase2))
    

main()

# L’infinito
# è
# uno
# dei
# testi
# più
# rappresentativi
# di
# Leopardi
# e
# di
# tutta
# la
# letteratura
# italiana
# FINE
# L’infinito
# è
# uno
# dei
# testi
# più
# significativi
# di
# Leopardi
# e
# della
# letteratura
# italiana
# FINE

# vedi
# la
# lunga
# scia
# nel
# cielo
# azzurro
# FINE
# la
# luna
# vedo
# brillare
# nel
# cielo
# di
# notte
# FINE