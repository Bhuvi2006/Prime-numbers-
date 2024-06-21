#Prime number
def prime_number(num):
    if num<=0:
        print("Enter a positive number ")
    for i in range(2,num):
        if num%i==0:
            print("It's not a prime number")
            break
        else:
            print("It's a prime number")
            break
num=int(input("Enter a number: "))
prime_number(num)
