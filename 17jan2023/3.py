def generator():
    x=0
    while(True):
        x=x+1
        yield x

y=generator()
#whenever we call counter will increase
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))