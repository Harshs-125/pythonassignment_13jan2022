class Animal():
    def __init__(self,t,c,l):
        self.t=t
        self.c=c
        self.l=l
    def type(self):
        print(f"this animal is of type {self.t}")
        
    def characteristic(self):
        print(f"this animal is {self.c}")
    def limbs(self):
        if(self.l==0):
            print("this animal has no limbs")
        else:
            print(f"this animal has {self.l} limbs")

class Cow(Animal):
    def __init__(self,t,c,l):
        self.t=t
        self.c=c
        self.l=l
class Dog(Animal):
    def __init__(self,t,c,l):
        self.t=t
        self.c=c
        self.l=l
class Python(Animal):
    def __init__(self,t,c,l):
        self.t=t
        self.c=c
        self.l=l
cow=Cow('mammal','herbivorous','4')
cow.type()
cow.characteristic()
cow.limbs()

dog=Dog('mammal','omnivorous','4')
dog.type()
dog.characteristic()
dog.limbs()

python=Python('reptile','carnivorous','0')
python.type()
python.characteristic()
python.limbs()


