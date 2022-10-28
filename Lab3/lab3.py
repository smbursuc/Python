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

def ex_3(): #

    dict1 = {'A':1,'B':2,'C': {'D':1,'D':2}}
    dict1 = dict(dict1)
    dict2 = {'A':1,'B':2,'C': {'D':1,'D':3}}
    dict2 = dict(dict2)
    dict3 = {'A':1,'B':2,'C': {'D':1,'D':2}}
    dict3 = dict(dict3)

    def functie_ex3(dict1, dict2):
        dict1_keys = []
        dict1_values = []
        for key in dict1.keys():
            dict1_keys.append(key)
            dict1_values.append(dict1[key])
        
        dict2_keys = []
        dict2_values = []
        for key in dict2.keys():
            dict2_keys.append(key)
            dict2_values.append(dict2[key])
        
        print("dict1 val",dict1_values)
        print("dict1 keys",dict1_keys)
        print("dict2 val",dict2_values)
        print("dict2 keys",dict2_keys)

        tuples = []

        for key in dict1.keys():
            tuples.append((key,dict1[key]))
        
        for key in dict2.keys():
            tuples.append((key,dict2[key]))
        
        #tuples = sorted(tuples, key=lambda x:x[0])

        for tuple in tuples:
            if tuples.count(tuple)!=2:
                return False
        
        return True
    
    print(functie_ex3(dict1,dict2))
    print(functie_ex3(dict1,dict3))

#ex_3()

def ex_4():

    def build_xml_element(tag, content, **kwargs):
        line = "<" + tag
        for key,value in kwargs.items():
            line = line + " " + key + "=\"" + value + "\""
        line = line + ">"

        line = line + content + "</" + tag + ">"

        return line
    
    print(build_xml_element("a", "Hello there", href = "http://python.org", _class= "my-link", id = "someid"))

def ex_5(): #

    rules = {("key1", "", "inside", "")}
    dictionary = {"key1": "inside it's too cold out"}
    def validate_dict(rules,dictionary):
        for rule in rules:
            if rule[0] not in dictionary:
                return False
            
            value = dictionary[rule[0]]

            split_value = value.split(" ")

            spotted = 0
            for i in range(1,len(split_value)-1):
                if split_value[i] == rule[2]:
                    spotted = 1
            
            if spotted == 0:
                return False
            
            if rule[1] == '':
                if split_value[len(split_value)-1] != rule[3]:
                    return False
            elif rule[3] == '':
                if split_value[0] != rule[1]:
                    print('a')
                    return False
            elif rule[1] != split_value[0] or rule[3] != split_value[len(split_value)-1]:
                return False


        return True
    
    print(validate_dict(rules,dictionary))

ex_5()
def ex_6():

    def functie_ex6(lista):
        unique_elems = set(lista)
        duplicate_elems = 0
        for elem in unique_elems:
            if lista.count(elem) > 1:
                duplicate_elems += 1
        
        return (len(unique_elems),duplicate_elems)
    
    print(functie_ex6([1,2,3,4,5,6,7,8,8,8,9,9,10,10]))

def ex_7():

    def functie_ex7(*args):
        dict = {}
        for i in range(0,len(args),2):
            #A = args[i]
            #B = args[i+1]
            operators = ["|","&","-"]
            for operator in operators:
                key  = "{"
                #"{1, 2} | {2, 3}"
                count_A = 0
                for elem in args[i]:
                    if count_A != len(args[i])-1:
                        key = key + str(elem) + ", "
                    else:
                        key = key + str(elem)
                    count_A+=1
                
                key = key + "} " + operator+ " {"

                count_B = 0
                for elem in args[i+1]:
                    if count_B != len(args[i+1])-1:
                        key = key + str(elem) + ", "
                    else:
                        key = key + str(elem)
                    count_B+=1

                key = key + "}"

                if operator == "|":
                    dict[key] = args[i].union(args[i+1])
                elif operator == "&":
                    dict[key] = args[i].intersection(args[i+1])
                elif operator == '-':
                    dict[key] = args[i].difference(args[i+1])
    
        return dict
    
    print(functie_ex7({1,2},{2,3}))

def ex_8(): #
    
    #mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': 'x', '2': 'y', 'y': 'start'} loop
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    def loop(mapping):
        visited = []
        key = 'start'
        visited.append(mapping[key])
        key = mapping['start'] 
        while True:
            if mapping[key] in visited and mapping[key]!='start':
                break
            visited.append(mapping[key])
            if visited[len(visited)-1] == visited[len(visited)-2]:
                break
            key = mapping[key]
        
        return visited
    
    print(loop(mapping))


def ex_9():

    #1, 2, 3, 4, {"x":1, "y":2, "z":3, "w":5}
    def functie_ex9(*args,**kwargs):
        count = 0
        values = []
        for key,value in kwargs.items():
            values.append(value)
        for arg in args:
            if values.count(arg)!=0:
                count+=1
        return count
    
    print(functie_ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))




        
        







        

        


    



