

def divide(*args):
    for r in args:
        a=r[0]
        b=r[1]
        if(b==0):
            print("divison not possible answer will be infinit")
        elif(type(a)==type('a') or type(b) == type('a')):
            print("divison not possible ")
        else:
            d=a/b
            print(f"the answer is {d}")

divide([1,0],[2,1],[4,2],[1,"a"])




## other way to solve this question
def divide2(*args):
    try:
        for r in args:
          a=r[0]
          b=r[1]
          div=a/b
          print(f"the answer is {div}")
    except TypeError:
        print(f"divison not possible because of this error {NameError}")

divide2([2,1],[4,2],[1,"a"])