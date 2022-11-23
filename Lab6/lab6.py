import re
import exrex
import os
def ex_1():

    def functie_ex1(text):
        # Regex that checks if the string is a sentence
        regex = "^([A-Za-z0-9]+ [A-Za-z0-9]+)+$"
        r = re.compile(regex)
        #print(exrex.getone(regex))
        if r.match(text):
            print("Este propozitie")
        else:
            print("Nu este propozitie")
            
        
    
    functie_ex1("hello19 20 world")

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
        f = open("my_xml.txt",'r')
        data = f.read().splitlines()
        for line in data:
            good = 1
            for key,value in attrs.items():
                keyval = f"{key}" + "=" + f"\"{value}\""
                regex = f'(<.* {keyval} .*((/>)|>))|(<.* {keyval}((/>)|>))'
                r = re.compile(regex)
                if not r.match(line):
                    good = 0
            if good == 1:
                result.append(line)
            
        return result

    
    print(functie_ex4({"class":"python","name":"python"}))

def ex_5():
    def functie_ex5(attrs):
        result = []
        f = open("my_xml.txt",'r')
        data = f.read().splitlines()
        for line in data:
            for key,value in attrs.items():
                keyval = f"{key}" + "=" + f"\"{value}\""
                regex = f'(<.* {keyval} .*((/>)|>))|(<.* {keyval}((/>)|>))'
                r = re.compile(regex)
                #print(exrex.getone(regex))
                if r.match(line):
                    result.append(line)
                    break
            
        return result

    
    print(functie_ex5({"class":"python","fake":"fake"}))


def ex_6():

    def censor(matchObj):
        text = matchObj.group(0)
        cenzurat = ''
        for i in range(len(text)):
            if i % 2 == 0:
                cenzurat += '*'
            else:
                cenzurat += text[i]
        return cenzurat
    def functie_ex6(text):
        print(re.sub('[aeiouAEIOU][a-zA-Z0-9][aeiouAEIOU]', censor, text))
    
    functie_ex6("hello world ana are")

def ex_7():

    def functie_ex7(cnp):
        regex = "^[1-8][0-9][0-9](0[1-9]|[0-9][0-9])(0[1-9]|[0-9][0-9])(0[1-9]|[0-9][0-9])(00[1-9]|[0-9][0-9][0-9])[0-9]$"
        #10335875
        r = re.compile(regex)
        print(exrex.getone(regex))
        if r.match(cnp):
            print("CNP valid")
        else:
            print("CNP invalid")

    functie_ex7("1971027265798")

def ex_8():

    def generate_substrings(string):
        result = []
        for i in range(len(string)):
            for j in range(i,len(string)):
                result.append(string[i:j+1])
        return result

    def functie_ex8(dir,regex):
        result = []
        for dirs, subdirs, root in os.walk(dir):
            for file in root:
                file = file.split('.')[0]
                substrings = generate_substrings(file)
                found = 0 
                for substring in substrings:
                    r = re.compile(regex)
                    if r.match(substring):
                        found=1
                        print(">> " + file)
                        break
                if found == 0:
                    print(file)
    functie_ex8(".",'^([a-zA-Z0-9]+_[a-zA-Z0-9]+)$')


ex_8()
