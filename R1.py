def f(x):
    if x == 0:
        return 2
    else:
        return 3 * (x+1) * f(x-1)

def main():
    n = int(input())

    print(f(n), end='')

main()