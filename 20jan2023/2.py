import numpy
import statistics
class Calculate():
    def __init__(self,list):
        self.list=list
        self.np = numpy.array(self.list)
        self.n=len(self.list)
        self.list.sort()

    def mean(self):
        s=sum(self.list)
        return s/self.n

    def median(self):
        if self.n%2==0:
            a=self.list[self.n//2]
            b=self.list[(self.n//2)+1]
            return (a+b)/2
        else:
            med=self.list[(self.n + 1)//2]
            return med

    def mode(self):
        d = dict()
        for i in self.list:
            if(i in d):
                d[i] += 1
            else:
                d[i] = 1 
        arr = []
        for k,v in d.items():
            arr.append((v,k))
        return max(arr[1])
    
    def stdev(self):
        return statistics.stdev(self.list)





obj1=Calculate([1,2,3,4,5,6,7,8])
print(obj1.mean())
print(obj1.median())
print(obj1.mode())
print(obj1.stdev())
