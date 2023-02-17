def addition(x,y=0):
    if(type(x)==int and type(y)==int):
        return x+y
    return "invalid testcase"

def subtraction(x,y=0):
    if(type(x)==int and type(y)==int):
       return x-y
    else:
        return "invalid testcase"

def multiply(x,y=0):
    if(type(x)==int and type(y)==int):
       return x*y
    else:
        return "invalid testcase"

def division(x,y=1):
    if(y==0):
        return "y cannot be zero invalid testcase"
    if(type(x)==int and type(y)==int):
       return x/y
    else:
        return "invalid testcase"