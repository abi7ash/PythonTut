# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:44:01 2021

@author: abilash
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:28:28 2021

@author: abilash
"""

class student:
    'Student class for consisting of student details in any given class'
    
    def __init__(self,name,fname,mname):  #constructor
        '''enter student name - enter name
           enter student branch - cse,cv,ece,eee,me'''
        self.name = name;
        self.father_name = fname;
        self.mothers_name = mname;
        
        '''    def studname(self):
        print("Name of the student is ",self.name);
        '''
        
    def displayfname(self):
        print("The father of the Student ",self.name," is ",self.father_name);
    
    def displaymname(self):
        print("The mother of the Student ",self.name," is ",self.mothers_name);
            

stud1 = student("abi", "ggk","pnp");
stud2 = student("ashu", "nbl","ruk");

stud1.

stud2.displaymname();

#stud1.studname();
