# Risolvere questo test case: ))()(( 
def check1_originale(s):
    countOpeningBrackets = 0
    countClosingBrackets = 0
    for i in range(len(s)):
        if (s[i] == '('):
            countOpeningBrackets += 1
        if (s[i] == ')'):
            countClosingBrackets += 1
    return countOpeningBrackets + countClosingBrackets

def check1(s):
    count = 0
    for i in range(len(s)):
        if (s[i] == '('):
            j = i+1
            trovato = False
            while j <= len(s)-1 and trovato == False:
                if (s[j] == ')'):
                    trovato = True
                j += 1
            if (trovato):
                count += 1

    return count*2 == check1_originale(s)
        

def check2(s):
    for i in range(1,len(s)):
        if (s[i-1] == '(' and s[i] == ')'):
            return False
    return True

n = input()

if (check1(n)):
    print("ok1")
else:
    print("no1")

if (check2(n)):
    print("ok2")
else:
    print("no2")
