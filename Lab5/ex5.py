def my_function(list_):
    result = []
    for arg in list_:
        if type(arg) is dict:
            for key,value in arg.items():
                if type(key) is int or type(arg) is float:
                    result.append(key)
                
                if type(value) is int or type(arg) is float:
                    result.append(key)
        elif type(arg) is list:
            for val in arg:
                if type(val) is int or type(arg) is  float:
                    result.append(val)
        elif type(arg) is int or type(arg) is float:
            result.append(arg)
    return result

print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


