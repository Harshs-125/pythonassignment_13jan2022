import random

def random_from_list():
    list1=[1,2,3,4,5,6,7]
    print(f"random number from list {list1} : ",end="")
    print(random.choice(list1))

def random_from_string():
  str="harsh"
  print(f"random character from the given string {str}: ",end="")
  print(random.choice(str))

def random_between_zeroandone():
    print("random number between zero and one : ",end="")
    print(random.random())

def random_using_shuffle():
    list1=['H','A','R','S','H']
    print("the original list : ",end="")
    print(list1)
    random.shuffle(list1)
    print("the shuffled list : ",end="")
    print(list1)

random_from_list()
random_from_string()
random_between_zeroandone()
random_using_shuffle()
