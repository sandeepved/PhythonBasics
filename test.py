import random
class employee:
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
emp1=employee('rahul','kapoor',random.randint(10000,90000))
print(emp1.fname,emp1.lname)