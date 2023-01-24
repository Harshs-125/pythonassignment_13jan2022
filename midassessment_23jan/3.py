list1=[1,2,3,1,3,4,6,5,3]
frequency={}

for item in list1:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

print(frequency)

uniquenumbers=[]
for items in frequency:
    if(frequency[items]==1):
        uniquenumbers.append(items)

print(f"the unique numbers in the given list are = {uniquenumbers}")