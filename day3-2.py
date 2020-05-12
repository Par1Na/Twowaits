# Twowaits
Twowaits Problem
x="hello"
result=[]
def permute(x,i,length):
    if length==i:
        result.append(''.join(x))
    else:
        for j in range(i,length):
            x[i],x[j]=x[j],x[i]
            permute(x,i+1,len(x))
            x[i],x[j]=x[j],x[i]
permute(list(x),0,len(x))
print(str(result))
#inbuilt function
from itertools import permutations    
print([''.join(i) for i in permutations(x)])
