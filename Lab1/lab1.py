def ex_1():
    y = int(input("Numarul de nr de introdus:"))
    nr = []
    for x in range(y):
        n = int(input("Numerele:"))
        nr.append(n)
    div = 0
    for x in range(1, max(nr)):
        a = 0
        for i in range(len(nr)):
            #print("X:", x)
            #print("Nr:", nr[i])
            if nr[i] % x != 0:
                break
            a = a + 1
        #print(a, len(nr))
        if a == len(nr):
            div = x
    print(div)

def ex_2():
    string = str(input("Introdu string:"))
    vocale = 'aeiouAEIOU'
    nr_voc = 0
    for i in range(len(string)):
        print(string[i])
        if string[i] in vocale:
            nr_voc = nr_voc + 1

    print(nr_voc)


def ex_3():
    string1 = input("String 1:")
    string2 = input("String 2:")
    print(string2.count(string1))


def ex_4():
    upcc_string = input("Upper camel case:")
    res = [upcc_string[0].lower()]
    for c in upcc_string[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    print(''.join(res))


def ex_5():
    def spiralOrder(matrix):
        ans = []
    
        if (len(matrix) == 0):
            return ans
    
        m = len(matrix)
        n = len(matrix[0])
        seen = [[0 for i in range(n)] for j in range(m)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        x = 0
        y = 0
        di = 0
    
        # Iterate from 0 to R * C - 1
        for i in range(m * n):
            ans.append(matrix[x][y])
            seen[x][y] = True
            cr = x + dr[di]
            cc = y + dc[di]
    
            if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
                x = cr
                y = cc
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]
        return ans

    n = int(input("n:"))
    m = int(input("m:"))
    matrix = [["" for x in range(m)] for y in range(n)]

    for i in range(n):
        input_str = input("Enter string:")
        a = list(input_str)
        for j in range(m):
            matrix[i][j] = a[j]

    for x in spiralOrder(matrix):
            print(x, end="")

def ex_6():
    n = input("Numar:")
    palindrom = 1
    for i in range(int(len(n)/2)):
        if not n[i] == n[len(n)-i-1]:
            palindrom = 0

    if palindrom:
        print("Este palindrom")
    else:
        print("Nu este palindrom")


def ex_7():
    input_string = input("String:")
    res = ""
    for i in range(len(input_string)):
        if input_string[i] in ('1234567890'):
            res+=input_string[i]
            i+=1
            while input_string[i] in ('1234567890'):
                res+=input_string[i]
                i+=1
            break
    print(res)

def ex_8():
    n = int(input("Numar:"))
    binar = bin(n)
    print(binar)
    print(binar.count('1'))

def ex_9():
    input_string = input("String:")
    max = 0
    character = ''
    for c in input_string:
        if c.isalpha():
            if input_string.count(c) > max:
                max = input_string.count(c)
                character = c
    print(character)

def ex_10():
    input_string = input("String:")
    print(len(input_string.split(" ")))

ex_8()


