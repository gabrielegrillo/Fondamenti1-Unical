def main():
    n = int(input())
    l = []
    sum = 0 

    while n != -50:
        sum += n
        l.append(n)
        n = int(input())

    if (len(l) == 0):
        print("VUOTA",end='')
    else:
        piccino = sum
        sum = sum // len(l)
        
        
        for i in range(len(l)):
            if (l[i] >= sum):
                if (l[i] < piccino):
                    piccino = l[i]
        print(piccino, end='')


main()



