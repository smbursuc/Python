import re
import exrex
import os
def ex_1():

    def functie_ex1(text):
        words = re.findall("\w+", text)
        print(words)
            
        
    
    functie_ex1("hello19 20 world")

ex_1()

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


def ex_3():

    def functie_ex3(string_list,regex_list):
        result = []
        for string in string_list:
            for regex in regex_list:
                r = re.compile(regex)
                if r.match(string):
                    result.append(string)
                    break
        return result

    print(functie_ex3(["ana","n-are","mere"],["^[a-zA-Z]+$"]))


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
        print(re.sub('[aeiouAEIOU][a-zA-Z0-9]*[aeiouAEIOU]', censor, text))
    
    functie_ex6("hello world anasdasdasdaasda ea are")

def ex_7():

    def functie_ex7(cnp):
        regex = "^[1-8][0-9][0-9](0[1-9]|[0-9][0-9])(0[1-9]|[0-9][0-9])(0[1-9]|[0-9][0-9])(00[1-9]|[0-9][0-9][0-9])[0-9]$"
        #10335875
        r = re.compile(regex)
        print(exrex.getone(regex))
        if r.match(cnp):
            print("CNP valid dupa regex")
        else:
            print("CNP invalid dupa regex")
        
        c = "279146358279"

        sum = 0
        for i in range(12):
            sum+= int(cnp[i])*int(c[i])
        
        if sum % 11 < 10:
            if sum % 11 == int(cnp[len(cnp)-1]):
                print("CNP valid dupa algoritm")
        elif sum % 11 == 10:
            if int(cnp[len(cnp)-1]) == 1:
                print("CNP valid dupa algoritm")


        



    functie_ex7("9960902269613")


#
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
            for full_file in root:
                file = full_file.split('.')[0]
                r = re.compile(regex)
                file_matched = 0
                file_text_matched = 0
                if r.match(file):
                    file_matched = 1
                f = open(os.path.join(dirs,full_file),'r')
                data = f.read().splitlines()
                for line in data:
                    search = re.findall(regex, line)
                    if len(search)>0:
                        file_text_matched = 1
                f.close()
                if file_matched == 1 and file_text_matched == 1:
                    print(">> " + file)
                elif file_matched == 1 or file_text_matched == 1:
                    print(file)
                
    functie_ex8(".",'^([a-zA-Z0-9]+_[a-zA-Z0-9]+)$')

ex_8()
