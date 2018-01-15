
l=[1,2,3,4,5]
def nested_sum(l):
    total = 0 
    for i in l:
        if isinstance(i, list):  
            total += nested_sum(i)
        elif not isinstance(i,list):
            total += i
    return total
print(nested_sum(l))
