import csv
import os
import sys 
s=set()
file = open(os.path.join(sys.path[0], "first.csv"), mode ='r')
csvreader=csv.reader(file)

#for list we already get list
list=[]
s=set()
dict={}
for row in csvreader:
    #print(row)
    list.append(row)
    s.add(tuple(row))
    dict[row[0]+" "+row[1]]=row[2]
print("the list",list)
print("The set ",s)
print("The dictionary ",dict)

# output
#the list [['John', 'Ken', '11'], ['Ronny', 'Baggs', '12'], ['Sam', 'Shone', '13']]
#The set  {('John', 'Ken', '11'), ('Ronny', 'Baggs', '12'), ('Sam', 'Shone', '13')}
#The dictionary  {'John Ken': '11', 'Ronny Baggs': '12', 'Sam Shone': '13'}
    

