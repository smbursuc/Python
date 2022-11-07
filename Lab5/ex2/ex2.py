def my_function(*args,**kwargs):
    sum=0
    for key,value in kwargs.items():
        sum+=value
    return sum


print(my_function(1,2,c=3,d=4))

anon = lambda *args,**kwargs : sum(kwargs.values())
print(anon(1,2,c=3,d=4)) 