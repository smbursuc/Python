def is_prime(nr):
    if nr == 0 or nr == 1:
        return 0
    
    for i in range(2,int(nr/2)):
        if nr % i == 0:
            return 0
    
    return 1



def process_item(nr):
    nr+=1
    found = 0
    while found == 0:
        if is_prime(nr) == 1:
            print(nr)
            found = 1
        else:
            nr+=1
        