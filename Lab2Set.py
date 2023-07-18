def numerodivisori(x):
    div = 0
    for i in range(1,x):
        if (x % i == 0):
            div += 1
    return div

def debolezza(x):
    deb = 0
    div_x = numerodivisori(x)
    for i in range(1,x):
        div_i = numerodivisori(i)
        if (div_i > div_x):
            deb += 1
    return deb



def main():
    n = int(input())
    max_deb = 0
    for i in range(1, n+1):
        x = debolezza(i)
        if (x > max_deb):
            max_deb = x

    print(max_deb, end='')



main()