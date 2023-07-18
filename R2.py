def checkequalhalf(start,end,list):
    if (end+1 == len(list)):
        if (list[start] == list[end]):
            return "SI"
        else:
            return "NO"
    else:
        if (list[start] == list[end]):
            return checkequalhalf(start+1,end+1,list)
        else:
            return "NO"

#  1, 2, 3, 1, 2, 3, 0, 5
def main():
    n = int(input())
    l = []
    
    while len(l) < n:
        l.append(int(input()))

    print(checkequalhalf(0,len(l)//2,l), end='')

main()