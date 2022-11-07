import math
def my_function(tuples):
    result = []
    for tuple in tuples:
        dict = {}
        dict['sum'] = tuple[0] + tuple[1]
        dict['prod'] = tuple[0] * tuple[1]
        dict['pow'] = math.pow(tuple[0],tuple[1])
        result.append(dict)
    return result

print(my_function([(5, 2), (19, 1), (30, 6), (2, 2)]))