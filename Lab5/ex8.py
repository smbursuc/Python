def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
    return lambda *args,**kwargs : "Args are: " + str(args) + ", " + str(kwargs) + "\n" + str(function(*args))

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  
print(x)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)


def multiply_output(function):
    return lambda x : 2*function(x)

def multiply_by_three(x):
    return x * 3

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)

print(x)


