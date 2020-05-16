# Twowaits
Twowaits Problem
def replace(arr):
    size=len(arr)
    max=arr[size-1]
    for i in range(size-1,-1,-1):
        arr[size-1]=-1
        for i in range(size-2,-1,-1):
            temp=arr[i]
            arr[i]=max
            if(max<temp):
                max=temp
        return arr
arr=[2,4,3,5,12,5] 
print(replace(arr))
