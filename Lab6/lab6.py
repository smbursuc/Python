import re
def ex_1():

    def functie_ex1(text):
        result = []
        split_text = text.split(" ")
        r = re.compile('^[a-zA-Z0-9]+$')
        for txt in split_text:
            if r.match(txt):
                result.append(txt)
        return result
    
    print(functie_ex1("hello19 20 world"))

def ex_2():

    def functie_ex2(string,regex,x):
        result = []
        r = re.compile(regex)
        for i in range(len(string)):
            substring = string[i:][:x]
            if r.match(substring):
                result.append(substring)
        return result
    
    print(functie_ex2("hello l99tle world","[0-9][0-9]",2))


#??????????????????????????????????????????????
def ex_3():

    def functie_ex3(string,regex_list):
        result = []
        for s in string:
            already_added = 0
            for regex in regex_list:
                r = re.compile(regex)
                if r.match(s):
                    if(already_added == 0):
                        result.append(s)
                        already_added = 1
        return result

    print(functie_ex3())

def ex_4():

    def functie_ex4(attrs):
        result = []
        # regex = ""
        # for key,value in attrs.items():
        #     string = f"{key}" + "=" + f"\"{value}\""
        #     regex = regex + string
        # print(regex)
        f = open("my_xml.txt",'r')
        data = f.read().splitlines()
        for line in data:
            good = 1
            for key,value in attrs.items():
                r = re.compile(f"{key}" + "=" + f"\"{value}\"")
                if r.search(line):
                    good = 0
            
        return result

    
    print(functie_ex4({"class":"python","name":"python"}))

ex_4()


#print("serban"[0:])
