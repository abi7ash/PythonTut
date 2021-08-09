# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:51:07 2021
@author: abilash
"""

class Employee:
    'Common base class for all employees'
    empCount = 0

    #def __init__(self)
    def __init__(self, name, salary):
    #Class constructor
        self.name = name
        self.salary = salary
        Employee.empCount += 1
 
    def displayCount(self):
        'displays the employee count within the class'
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

#%% Using the Class
#"This would create first object of Employee class"
emp1 = Employee('Zara', 2000)

#%%
#"This would create second object of Employee class"
emp2 = Employee('Manni', 5000)

#%%

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)


#%% statements to access attributes
#'''
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, age, 8) # Set attribute 'age' at 8
#%%

getattr(emp1, age)    # Returns value of 'age' attribute

#%%
delattr(emp1, 'age')    # Delete attribute 'age'
#'''