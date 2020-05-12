# Twowaits
Twowaits Problem
num=int(input("Enter the number of terms\n"))
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def show_fibo(num):
    print("the fibo series of ",num," numbers is:")
    for i in range(num):
        print(fibo(i))
show_fibo(num)
