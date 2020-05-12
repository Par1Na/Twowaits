# Twowaits
Twowaits Problem
l=[12,1,4,14,13,22,4,2]
m=[1,2,3,4,13,12]
def intersect(l,m):
    res=[value for value in l if value in m ]
    return res
print(intersect(l,m))
