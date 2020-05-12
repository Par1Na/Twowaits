# Twowaits
Twowaits Problem
l=[12,1,4,12,14,13,22,4,2,1]
def remove(a):
    result=[]
    for i in a:
        if i not in result:
            result.append(i)
    return result
print(remove(l))
