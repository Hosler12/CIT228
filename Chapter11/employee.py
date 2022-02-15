class Employee:
    def __init__(self,firstName,lastName, annualSalary):
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary = annualSalary

    def giveRaise(self,increase = 5000):
        self.annualSalary += increase