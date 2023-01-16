from datetime import datetime
str1='2022-12-17'
str2='2022-05-12'

d1=datetime.strptime(str1,"%Y-%m-%d")
d2=datetime.strptime(str2,"%Y-%m-%d")

difference=d1-d2
print(f"the difference  is {difference.days}")
#the output is the difference is 219


str_time1="5:20:57"
str_time2="3:46:48"
t1=datetime.strptime(str_time1,"%H:%M:%S")
t2=datetime.strptime(str_time2,"%H:%M:%S")

difference = t1-t2
print(f"The difference in time is {difference}")
