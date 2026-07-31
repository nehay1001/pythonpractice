# practice
#WAP to check if number entered by the user is odd or even.
num=int(input("enter number:"))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")



#WAP to find the greatest of 3 number entered by the user.
a=int(input ("enter first number:"))
b=int (input("enter second number :"))
c=int(input("enter third number:"))

if (a>=b and a>=c):
    print("first number is largest ", a)
elif(b>=c):
    print ("second number is largest",b)
else:
    print("third number is largest", c)




#WAP to check if number is a multiple of 7 or not.
num=int(input("enter number:"))
if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple")

