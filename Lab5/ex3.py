def vowels(string):
    vowels = []
    for i in range(len(string)):
        if string[i] in ['a','e','i','o','u']:
            vowels.append(string[i])
    return vowels

print(vowels("Programming in Python is fun"))

string = "Programming in Python is fun"
list_comprehension = [string[i] for i in range(len(string)) if string[i] in ['a','e','i','o','u']]

print(list_comprehension)

lambda_vowels = list(filter(lambda x : (x in ['a','e','i','o','u']),string))

print(lambda_vowels)
