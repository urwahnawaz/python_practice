class Employee: 
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amount(cls, amount): 
        cls.raise_amt = amount
    
    @classmethod 
    def from_string(cls, emp_str): 
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day): 
        if day.weekday == 5 or day.weekday() == 6:
            return False 
        return True  



# To perform some kind of action, need to provide method to the class 
# Method underneath the class automatically take in the instance automatically 
# When we access class variables, we need to access them through the class itself or the instance 
# self is for calling the instance within the class
# class methods and static methods 

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang 

class Manager(Employee): 

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else: 
            self.employees = employees