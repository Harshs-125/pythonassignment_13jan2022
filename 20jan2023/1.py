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
    def sound(self):
        print("mooo sound")
class Dog(Animal):
    def __init__(self,t,c,l):
        self.t=t
        self.c=c
        self.l=l
    def sound(self):
        print("barking sound")
class Python(Animal):
    def __init__(self,t,c,l):
        self.t=t
        self.c=c
        self.l=l
    def sound(self):
        print("hissing sound ")
cow=Cow('mammal','herbivorous','4')
cow.type()
cow.characteristic()
cow.limbs()
cow.sound()

dog=Dog('mammal','omnivorous','4')
dog.type()
dog.characteristic()
dog.limbs()
dog.sound()

python=Python('reptile','carnivorous','0')
python.type()
python.characteristic()
python.limbs()
python.sound()


