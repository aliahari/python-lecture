def sum(a,b):
    out = a + b
    return out

def sumList(inList):
    """
    calculates sum of the list
    INPUT:
    inList: input list 
    OUTPUT:
    sum: sum of the input list
    """
    sum = 0
    for num in inList:
        sum += num
    return sum

print(sum(a=1,b=2))
inList = [1,2,3,4]
print(sumList(inList))