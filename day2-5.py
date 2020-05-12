# Twowaits
Twowaits Problem
def up(n):
    for i in range(n):
        for j in range(1,2*n):
            if j%2==1:
                print(n,end='')
            else:
                print('*',end='')
        n=n-1
        print('\r')
def low(n):
    for i in range(n):
        for j in range(1,2*i+2):
            if j%2==1:
                print(i+1,end='')
            else:
                print('*',end='')
        print('\r')
def full(n):
    up(n)
    low(n)
full(5)
    
