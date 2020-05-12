# Twowaits
Twowaits Problem
num=int(input("Enter the number to check:\n"))

def check_even_odd(num):
    if (num%2==0):
        print("the given number ",num," is even")
    else:
        print("the given number ",num," is odd")
check_even_odd(num)

def check_prime(num):
    if num>1:
        for i in range(2,num//2):
            if(num%i)==0:
                print("number is not prime")
                break
        else:
            print("number is prime")
    else:
        print("Number is not prime")
check_prime(num)
