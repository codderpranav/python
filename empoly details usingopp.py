class employ:
    def __init__(self,Name,Id ,Salary):
        self.Name=Name
        self.empid=Id
        self.empsalary=Salary
    def showdetails(self):
        print(f"employ name={self.Name},employ id={self.empid},emploly salary={self.empsalary}")
employ1=employ("Pranav Satish Shinde","A1238907645",150000)
employ2=employ("Rohit Ajay Thakhur","A1238907646",160000)
employ3=employ("pranita rahul Singh","A1238907647",100000)
employ4=employ("Suresh Rohan Patil","A1238907648",90000)
employ5=employ("Shubham Arjun Jaybhayu","A1238907649",80000)
employ1.showdetails()
employ2.showdetails()
employ3.showdetails()
employ4.showdetails()
employ5.showdetails()