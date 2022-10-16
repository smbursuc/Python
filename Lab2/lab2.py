def ex_1():
    n = int(input("n:"))
    a=1
    b=1
    s=0
    for i in range (n-3):
        s=a+b
        a=b
        b=s
    print(s)


def ex_2():
    n = int(input("n:"))

    list = []
    for i in range(n):
        list.append(int(input("nr:")))

    def isPrime(nr):
        prime = 1
        if nr == 0 or nr==1:
            prime = 0
        for i in range(2,int(nr/2)):
            if nr%i == 0:
                prime = 0
        return prime
    
    def functie_ex2(list):
        prime_nr = []
        for i in range(n):
            if isPrime(list[i]):
                prime_nr.append(list[i])
        print(prime_nr)
    
    functie_ex2(list)

def ex_3():
    n = int(input("n:"))
    m = int(input("m:"))

    a=[]
    b=[]
    for i in range(n):
        a.append(int(input("nr prima lista:")))

    for j in range(n):
        b.append(int(input("nr a doua lista:")))

    a=set(a)
    b=set(b)

    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))
    print(b.difference(a))

def ex_4():
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = []
    n = int(input("n:"))
    for i in range(n):
        moves.append(int(input("move:")))

    start = int(input("start:"))

    def functie_ex4(notes,moves,start):
        print(notes[start])
        for i in range (n):
            if start + moves[i] > n:
                start = moves[i] - (n-start) -1
            elif start + moves[i] < 0:
                start = n + start + moves[i]
            else:
                start = start + moves[i]
            print(notes[start])
    functie_ex4(notes,moves,start)

def ex_5():
    n = int(input("n:"))
    matrix = [[1 for i in range(n)] for j in range(n)]

    def functie_ex5(matrix):
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
        print(matrix)

    functie_ex5(matrix)




    

