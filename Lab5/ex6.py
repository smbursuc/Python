def my_function(list_):
    odd = {}
    odd_index = 0
    even = {}
    even_index = 0

    for val in list_:
        if val % 2 == 0:
            even[even_index] = val
            even_index +=1
        else:
            odd[odd_index] = val
            odd_index += 1
    
    tuples = []
    for i in range(int(len(list_)/2)):
        tuples.append((even[i],odd[i]))
    
    return tuples

print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
