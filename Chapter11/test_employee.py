import unittest
from employee import Employee

class test_employee(unittest.TestCase):
    def setUp(self):
        firstName = 'John'
        lastName = 'Doe'
        annualSalary = 40000
        self.employee = Employee(firstName,lastName,annualSalary)

    def test_give_default_raise(self):
        self.employee.giveRaise()
        self.assertEqual(self.employee.annualSalary,45000)

    def test_give_custom_raise(self):
        self.employee.giveRaise(10000)
        self.assertEqual(self.employee.annualSalary,50000)

if __name__ == '__main__':
    unittest.main()