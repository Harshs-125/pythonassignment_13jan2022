import time
def decorator(func):
    def inner(t,interval):
      for i in range(0,t):
         time.sleep(interval)
         func(t,i)
    return inner

@decorator
def tryfunction(t,i):
    print("Hello function is running")


tryfunction(3,3)
