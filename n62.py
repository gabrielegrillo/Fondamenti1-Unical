def spirale(m, list):
    top = 0
    bottom = len(m)-1
    left = 0 
    right = len(m[0])-1
    dir = 0 # 0 = right; 1 = down; 2 = left; 3 = top

    k = 0

    while (top <= bottom and left <= right):
        if (dir == 0):
            for j in range(top, right+1):
                if(k >= len(list)):
                    k = 0
                if (m[top][j] == "*" and k < len(list)):
                    m[top][j] = list[k]
                    k += 1
            top += 1
            dir = 1
        elif(dir == 1):
            for i in range(top, bottom+1):
                if(k >= len(list)):
                    k = 0
                if (m[i][right] == "*" and k < len(list)):
                    m[i][right] = list[k]
                    k += 1
            right -= 1
            dir = 2
        elif (dir == 2):
            for j in range(right,left-1,-1):
                if(k >= len(list)):
                    k = 0
                if (m[bottom][j] == "*" and k < len(list)):
                    m[bottom][j] = list[k]
                    k += 1
            bottom -= 1
            dir = 3
        elif (dir == 3):
            for i in range(bottom,top-1,-1):
                if(k >= len(list)):
                    k = 0
                if (m[i][left] == "*" and k < len(list)):
                    m[i][left] = list[k]
                    k += 1
            left += 1
            dir = 0
    

    


def main():
    k = int(input())

    l = []

    while len(l) < k:
        l.append(int(input()))

    n = int(input())
    m = int(input())

    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append("*")
        mat.append(row)

    spirale(mat, l)

    for i in range(n):
        riga = ""
        for j in range(m):
            riga += str(mat[i][j])
        print(riga)




main()