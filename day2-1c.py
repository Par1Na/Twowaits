# Twowaits
Twowaits Problem
def order(n):
    x=0
    while(n>0):
        x=x+1
        n=int(n/10)
    return x
def armstrong(n):
    temp=n
    x=order(n)
    sum=0
    while(n>0):
        a=n%10
        sum=sum+pow(a,x)
        n=int(n/10)
    if(sum==temp):
        print("no is armstrong")
    else:
        print("No is not armstrong")
armstrong(num)
