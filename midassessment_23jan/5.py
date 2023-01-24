from datetime import datetime
datestr=input("enter the date to be checked in space separated in dd mm yy format ")
d=int(datestr.split()[0])
m=int(datestr.split()[1])
y=int(datestr.split()[2])

dateToCheck=datetime(y,m,d)

datestr2=input("enter the starting date to be compared in space separated in dd mm yy format ")
d2=int(datestr2.split()[0])
m2=int(datestr2.split()[1])
y2=int(datestr2.split()[2])

startDate=datetime(y2,m2,d2)

datestr3=input("enter the end date to be checked in space separated in dd mm yy format ")
d3=int(datestr3.split()[0])
m3=int(datestr3.split()[1])
y3=int(datestr3.split()[2])

endDate=datetime(y,m,d)

if(dateToCheck<=endDate and dateToCheck>=startDate):
    print("Yes the date is in the given range")
else:
    print("No the date is not in the given range")