list1=[1,"a",2,"b",3,"c"]
nums=filter(lambda x:(type(x)==int),list1)
print(f"the list of numerics are :{list(nums)}")
alpha=filter(lambda x:(type(x)==str),list1)
print(f"the list of alphabetic characters are :{list(alpha)}")