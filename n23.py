n = input()
almenouna = False
while n != "*":
    if (n == "a" or n == "e" or n == "i" or n == "o" or n == "u"):
        almenouna = True 
    n = input()

if (almenouna):
    print("ALMENO 1 VOCALE", end='')
else:
    print("NESSUNA VOCALE", end='')