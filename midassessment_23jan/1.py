list1=["name512", "same1example", "joy18full"]
list2=[]
#basic method using for loop
num="1234567890"
for str in list1:
    str2=""
    for ch in str:
        if ch not in num:
            str2+=ch
    list2.append(str2)

print("the new list using forloop:",end="")
print(list2)

#using join:

list1=["name512", "same1example", "joy18full"]
list2=[]
for str in list1:
    str2="".join(filter(lambda x: not x.isdigit(),str))
    list2.append(str2)

print("the new list using filter and join and lambda:",end="")
print(list2)

