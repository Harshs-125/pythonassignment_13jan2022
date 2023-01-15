def add(a,b):
    print("The addition is ",a+b)

def subtract(a,b):
    print("The subtraction is ",a-b)

def multiply(a,b):
    print("The multiplicatio is ",a*b)

def divide(a,b):
    print("The division is ",a/b)

a=int(input("enter the first number "))
b=int(input("enter the secon number "))
c=int(input("enter choice 1. for add 2. for subtract 3. for multiply 4. for Divide "))
if c==1:
    add(a,b)
elif c==2:
    subtract(a,b)
elif c==3:
    multiply(a,b)
elif c==4:
    divide(a,b)



