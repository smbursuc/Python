from genericpath import isfile
import os
from pathlib import Path
import sys
def ex_1():

    def functie_ex1(dir):
        dict = {}
        for file in os.listdir(dir):
            split_text = file.split(".")
            dict[split_text[0]] = split_text[1]
        sort = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
        sort = set(sort.values())
        for val in sort:
            print(val)
    
    functie_ex1(".")

def ex_2():

    def functie_ex2(dir,file):
        f = open(file,"a")
        for file in os.listdir(dir):
            if os.path.isfile(file):
                if file[0] == 'A':
                    f.write(os.path.abspath(file) + "\n")
        f.close()
    
    functie_ex2(".","ex2.txt")

ex_2()

def ex_3():

    def functie_ex3(my_path):
        if os.path.isfile(my_path):
            f = open(my_path,'r')
            data = f.read().replace('\n','')
            data = data[len(data)-20:]
            f.close()
            print(len(data))
        elif os.path.isdir(my_path):
            dict = {}
            for root, subdirs, files in os.walk(my_path):
                for file in files:
                    split_text = file.split(".")
                    if split_text[1] not in dict:
                        dict[split_text[1]] = 1
                    else:
                        dict[split_text[1]] += 1
            dict = {k: v for k,v in sorted(dict.items(), key=lambda item:item[1], reverse=True)} 
            for key,value in dict.items():
                print((key,value))
    
    functie_ex3("F:\\Git\\repos\\Python\\lab4\\ex3.txt")
    functie_ex3("F:\\Git\\repos\\Python\\lab4")


def ex_4():
    def functie_ex4():
        dir = sys.argv[1]
        list = []
        for file in os.listdir(dir):
            if os.path.isfile(file):
                split_text = file.split(".")
                list.append(split_text[1])
        list = sorted(set(list))
        return list
    
    print(functie_ex4())

def ex_5():
    def functie_ex5(target,to_search):
        try:
            files_with_to_search = []
            if os.path.isfile(target):
                f = open(target,'r')
                data = f.read()
                if to_search in data:
                    files_with_to_search.append(target)
            elif os.path.isdir(target):
                for root, subdirs, files in os.walk(target):
                    for file in files:
                        file_path = os.path.join(root,file) #echivalentul la root + "\\" + file
                        f = open(file_path,'r')
                        data = f.read()
                        if to_search in data:
                            files_with_to_search.append(file_path)
                        f.close()
            else:
                raise ValueError("Target is not a file nor a directory")
            return files_with_to_search
        except Exception as e:
            print(str(type(e)) + ": " + str(e))
            sys.exit(1)

    #print(functie_ex5("???",">???"))
    print(functie_ex5("ex5.txt","wanted"))
    print(functie_ex5("F:\\Git\\repos\\Python\\lab4","wanted"))

def ex_6():

    def callback(e):
        print(str(type(e)) + ": " + str(e))
        sys.exit(1)

    def functie_ex6(target,to_search,callback):
        try:
            files_with_to_search = []
            if os.path.isfile(target):
                f = open(target,'r')
                data = f.read()
                if to_search in data:
                    files_with_to_search.append(target)
            elif os.path.isdir(target):
                for root, subdirs, files in os.walk(target):
                    for file in files:
                        file_path = os.path.join(root,file) #echivalentul la root + "\\" + file
                        f = open(file_path,'r')
                        data = f.read()
                        if to_search in data:
                            files_with_to_search.append(file_path)
                        f.close()
            else:
                raise ValueError("Target is not a file nor a directory")
            return files_with_to_search
        except Exception as e:
            callback(e)

    print(functie_ex6("???",">???",callback))
    print(functie_ex6("ex5.txt","wanted",callback))
    print(functie_ex6("F:\\Git\\repos\\Python\\lab4","wanted",callback))

def ex_7():

    def functie_ex7(path):
        dict = {}
        dict['full_path'] = os.path.abspath(path)
        dict['file_size'] = os.path.getsize(path)
        if os.path.isfile(path):
            filename, file_extension = os.path.splitext(path)
            dict['file_extension'] = file_extension
        elif os.path.isdir(path):
            dict['file_extension'] = ''
        dict['can_read'] = os.access(path, os.R_OK)
        dict['can_write'] = os.access(path, os.W_OK)
        return dict
    
    print(functie_ex7("randomtext.txt"))

def ex_8():

    def functie_ex8(path):
        files = os.listdir(path)
        result = []
        for file in files:
            if os.path.isfile(file):
                result.append(os.path.abspath(file))
        return result
    
    print(functie_ex8("."))

ex_8()






    






