class AgeException(Exception):
    "this exception will be raised when input age is less than 18"
    pass

age =int(input())
try:
    if(age<18):
        raise AgeException
    else:
        print("eligible to vote ")
except AgeException:
    print("Not eleible for voting since age is less than 18 ")