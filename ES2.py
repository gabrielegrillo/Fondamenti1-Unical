def controlloripetizioni(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[j] == l[i]):
                return False
    return True

def isasubset(l1,l2):
    if (controlloripetizioni(l2)):
        k = 0
        for i in range(len(l2)):
            e = l2[i]
            for j in range(len(l1)):
                if (l1[j] == e):
                    k += 1
        
        if (k == len(l2)):
            return True
        else:
            return False 
    else:
        return False

def sumfree(l):
    for i in range(1,len(l)):
        sum = l[i-1] + l[i]
        for j in range(len(l)):
            if (sum == l[j]):
                return False
    return True


def main():
    n = int(input())
    m = int(input())

    s = []
    s1 = []
    while len(s) != n:
        s.append(int(input()))
    
    while len(s1) != m:
        s1.append(int(input()))

    if (isasubset(s,s1) and sumfree(s1)):
        print('OK',end='')
    else:
        print('NO',end='')

main()
