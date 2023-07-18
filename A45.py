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

def main():
    n = input()

    if(controllosintattico(n)):
        print("SI",end='')
    else:
        print("NO", end='')

main()