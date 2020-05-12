# Twowaits
Twowaits Problem
def check_pallindrome(num):
    temp=num
    sum=0
    while num>0:
        r=num%10
        sum=(sum*10)+r
        num=int(num/10)
    if(temp==sum):
        print("number is pallindrome")
    else:
        print("number is not pallindrome")
check_pallindrome(num)
