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
'''
from IPython import get_ipython
get_ipython().magic('reset -sf')
get_ipython().magic('clear')
'''
            
class semester:
    def assign_semester(self,sem):
        self.semester = sem;
        
    def displaysem(self):
        print("The current semester of the student is",self.semester);

class branch:
    def branch(self,branch):
        self.branch = branch;
    
    def dispbranch(self):
        print("The current branch of the student is",self.branch);

class student(semester,branch):
    'Student class for consisting of student details in any given class'

    def __init__(self,*args):  #constructor
        '''enter student name - enter name
           enter student branch - cse,cv,ece,eee,me'''
        
        if(len(args) == 3): 
            self.name = args[0];
            self.father_name = args[1];
            self.mothers_name = args[2];
        elif(len(args) == 2): 
            self.fathers_name = args[0];
            self.name = args[1];
        elif(len(args) == 1):
            self.name = args[0];
        
               
    def displayfname(self):
        print("Current student count is ",self.fname);
    
    def displaymname(self):
        print("The mother of the Student ",self.name," is ",self.mothers_name);
   
'''
stud1 = student();
stud1.newstudent_withparents("abi", "ggk", "pnp")
'''

stud2 = semester();

#%%
stud2.assign_semester(3);
stud2.displaysem();

stud5 = student("hsn","mk","pa");
stud5.assign_semester(6);
stud5.displaysem();

stud6 = student();
stud7 = student('gm','vs');
print("Student ",stud7.name,"'s fathers name is ",stud7.fathers_name);
print(stud7.mothers_name);

'''
stud5.branch(5);
stud5.dispbranch();

print("The student ",stud5.name," with fathers name ",\
      stud5.father_name," is from the semester ",\
      stud5.semester);
'''
#stud3 = branch("rocky","cse")


