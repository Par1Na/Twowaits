# Twowaits
Twowaits Problem

def two_way_sort(arr, arr_len):

    l, r = 0, arr_len - 1

    k = 0

    while(l < r): 

        while(arr[l] % 2 != 0): 

            l += 1
            k += 1

        while(arr[r] % 2 == 0 and l < r): 

            r -=1

        if(l < r): 

            arr[l], arr[r] = arr[r], arr[l] 

    odd = arr[:k] 

    even = arr[k:]

    odd.sort(reverse = True) 

    even.sort() 

    odd.extend(even) 
    return odd 

arr_len = 6

arr = [1, 3, 2, 7, 5, 4] 

result = two_way_sort(arr, arr_len) 

for i in result: 

    print(str(i) + " "), 
