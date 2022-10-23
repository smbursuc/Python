def ex_1():

    A = [1,2,3,4]
    B = [2,3,9,0]

    def functie_ex_1(A,B):
        result = []
        A = set(A)
        B = set(B)
        result.append(A.intersection(B))
        result.append(A.difference(B))
        result.append(A.union(B))
        result.append(B.difference(A))
        return result

    print(functie_ex_1(A,B))

def ex_2():

    String = "serbann"

    def functie_ex2(String):
        dictionar = dict()
        for i in range(len(String)):
            dictionar[String[i]]=String.count(String[i])
        return dictionar
    
    print(functie_ex2(String))

ex_2()
    



