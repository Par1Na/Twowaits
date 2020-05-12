# Twowaits
Twowaits Problem
def upPattern(n):
    for i in range(n):
        for j in range(i,n):
            print('* ',end='')
        for m in range(0,4*i+1):
            print(end=' ')
        for p in range(i,n):
            print('* ',end='')
        print('\r')

def lowPattern(n):
    s=4*n-3
    for i in range(n):
        for j in range(i+1):
            print('* ',end='')
        for k in range(s):
            print(end=' ')
        s=s-4
        for m in range(i+1):
            print('* ',end='')
        print('\r')

def comPattern(n):
    upPattern(n)
    lowPattern(n)

comPattern(5)
