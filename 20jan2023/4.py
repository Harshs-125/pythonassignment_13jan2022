class NotEligibleForLoan(Exception):
    "Exception occur if salary is less then 10k per month"
    pass

class Apply():
    def __init__(self,salary):
        self.salary=salary
        try:
            if self.salary < 10 :
                raise NotEligibleForLoan
            else:
                print("You are eligible for the loan")
        except NotEligibleForLoan:
            print("Not elible for the loan since your salary us less than 10k per month")

emp1=Apply(int(input()))         