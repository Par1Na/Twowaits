# Twowaits
Twowaits Problem
a="My name is parna"
def remove_duplicate(a,n):
    index=0
    for i in range(0,n):
        for j in range(0,i+1):
            if(a[i]==a[j]):
                break
        if(j==i):
            a[index]=a[i]
            index=index+1
    return ''.join(a[:index])
n=len(a)
print(remove_duplicate(list(a),n))
