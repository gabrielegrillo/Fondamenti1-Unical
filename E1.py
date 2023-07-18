def controllosintattico(s):
    if ((s[0] >= '0' and s[0] <= '9' ) or (s[0] == ' ')):
        return False
    else:
        esito = True
        for i in range(1,len(s)):
            if (s[i] <= '/'):
                esito = False
            else:
                if (s[i] >= ':' and s[i] <= '@'):
                    esito = False
                else:
                    if (s[i] >= '[' and s[i] <= '`' and s[i] != '_'):
                        esito = False
                    else:
                        if (s[i] >= '{'):
                            esito = False
        return esito
   
def controlloparametri(d):
    esito = True
    check1 = True
    check2 = True
    for i in range(0, len(d), 2):
        if (not controllosintattico(d[i]) or d[i] == ","):
            check1 = False 

    for j in range(1, len(d), 2):
        if (d[j] != ","):
            check2 = False
    
    return check1 and check2




n = input()
l = []
funzione = True


while n != ":":
    l.append(n)
    n = input()

if (n == ":"):
    if (l[0] == "def" and l[2] == "(" and l[len(l)-1] == ")"):
        if (controllosintattico(l[1])):
            p = l[3:len(l)-1]
            if (controlloparametri(p) or p == []):
                print("SI", end="")
            else: 
                funzione = False
        else: 
            funzione = False 
    else:
        funzione = False 


if (not funzione):
    print("NO", end='')
        
