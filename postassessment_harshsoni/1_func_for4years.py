import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
def generate():
    current_date=datetime.date.today()
    temp_date=datetime.date.today() 
    while(current_date<temp_date+relativedelta(years=4)):
        print(current_date)
        current_date=current_date+timedelta(days=1)
generate()