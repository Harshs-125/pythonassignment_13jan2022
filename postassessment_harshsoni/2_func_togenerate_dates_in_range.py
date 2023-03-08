import datetime
from datetime import timedelta

def generateInRange():
    from_date=input('enter from data in dd/mm/yyyy')
    from_date=datetime.datetime.strptime(from_date,"%d/%m/%Y")
    to_date=input('enter to data in dd/mm/yyyy')
    to_date=datetime.datetime.strptime(to_date,"%d/%m/%Y")
    curr=from_date
    while(curr<to_date):
        print(curr)
        curr=curr+timedelta(days=1)

generateInRange()

