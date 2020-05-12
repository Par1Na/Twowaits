# Twowaits
Twowaits Problem
def up_pattern(n):
    s=2*n-2
    for i in range(0,n):
        for j in range(0,i):
            print(end=" ")
        print("*",end='')
        for k in range(s):
            print(end=' ')
        s=s-2
        print('*',end='')
        print('\r')
def low_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=' ')
        print('*',end='')
        for j in range(2*i):
            print(end=' ')
        print('*',end='')
        print('\r')
def  complete_pattern(n):
    up_pattern(n)
    low_pattern(n)

complete_pattern(4)
