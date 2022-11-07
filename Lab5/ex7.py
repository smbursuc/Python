def generate_fib(nr):
    nrs = []
    nrs.append(0)
    nrs.append(1)
    nrs.append(1)
    first = 1
    second = 1
    sum = 0
    while (len(nrs)<=nr):
        sum = first+second
        nrs.append(sum)
        first = second
        second = sum
    return nrs
    

def process(**kwargs):
    filters = []
    limit = 0
    offset = 0
    if 'filters' in kwargs:
        filters = kwargs.get('filters')
    
    if 'limit' in kwargs:
        limit = kwargs.get('limit')
    
    if 'offset' in kwargs:
        offset = kwargs.get('offset')
    
    fib_nrs = generate_fib(1000)

    filtered = fib_nrs.copy()
    for filter_ in filters:
        filtered = list(filter(filter_,filtered))
    

    filtered = filtered[offset:]
    
    filtered = filtered[:limit]

    return filtered

def sum_digits(x):
    return sum(map(int, str(x)))

print(process(

    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

    limit=2,

    offset=2

))