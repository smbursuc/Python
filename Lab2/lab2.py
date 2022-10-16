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

def ex_6():

    x=2
    #list = [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]
    def functie_ex6(x,*args):
        elements = []
        for arg in args:
            elements = elements + arg
        
        from collections import Counter
        frecventa = Counter(elements)
        raspuns = []
        for i in range(len(elements)):
            if frecventa[i] == 2:
                raspuns.append(i)
        return raspuns
    print(functie_ex6(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))

def ex_7():
    n = int(input("n:"))
    nr_list = []
    for i in range(n):
        nr_list.append(int(input("nr:")))

    def palindrom(n):
        n = str(n)
        palindrom = 1
        for i in range(int(len(n)/2)):
            if not n[i] == n[len(n)-i-1]:
                palindrom = 0

        if palindrom:
            return True
        else:
            return False
    
    def functie_ex7(nr_list):
        cmm = 0
        count = 0
        sorted(nr_list, reverse=True)
        for i in range(n):
            if(palindrom(nr_list[i])):
                count=count+1
                cmm = nr_list[i]
        
        a = (count,cmm)
        return a
    
    print(functie_ex7(nr_list))

def ex_8():
    x = int(input("x:"))
    strings = ["test", "hello", "lab002"]
    flag = False
    raspuns = []
    for string in strings:
        caractere = []
        for c in string:
            if ord(c)%x == 0:
                if(flag == True):
                    caractere.append(c)
            elif flag == False:
                caractere.append(c)
        raspuns.append(caractere)
    
    print(raspuns)

def ex_9():
    stadion = [[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]]
    def functie_ex9(stadion):
        scunzi = []
        for i in range(len(stadion)):
            for j in range(len(stadion[0])):
                for k in reversed(range(0, i)):
                    if(stadion[i][j]<=stadion[k][j]):
                        #print(i,j,k)
                        tuplu = (i,j)
                        scunzi.append(tuplu)
                        break
        return scunzi
    print(functie_ex9(stadion))

def ex_10(*args):
    list = []
    #ex_10([1,2,3], [5,6,7], ["a", "b", "c"])
    for i in range(len(args[0])):
        tuplu = []
        for j in range(len(args)):
            tuplu.append(args[j][i])
        tuplu = tuple(tuplu)
        list.append(tuplu)
    print(list)


def ex_11():
    lista = [('abc', 'bcd'), ('abc', 'zza')]
    dictionar = {}
    for tupla in lista:
        dictionar[tupla] = tupla[1][2]
    
    dictionar = sorted(dictionar.items(), key=lambda item: item[1])
    print(list(dict(dictionar).keys()))

def ex_12():
    from collections import defaultdict
    lista = ['ana', 'banana', 'carte', 'arme', 'parte']
    dictionar = defaultdict(list)
    for string in lista:
        dictionar[string[-2:]].append(string)
    
    raspuns = []
    for key in dictionar.keys():
        raspuns.append(dictionar[key])
    
    print(raspuns)

print("serban"[1:])
    
    





    




    

