def check(arg):
    type_ = type(arg)
    if 'dict' in str(type_):
        if len(arg.keys())>=2:
            for key,value in arg.items():
                if(len(str(key))>=3):
                    return 1
    return 0


def my_function(*args,**kwargs):
    results = []
    for arg in args:
        if check(arg) == 1:
            results.append(arg)

    for arg in kwargs.values():
        if check(arg) == 1:
            results.append(arg)
    
    return results

print(my_function(

 {1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}

))

