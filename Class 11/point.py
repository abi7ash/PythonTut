# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:44:08 2021

@author: abilash
"""

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed");

#%%
pt1 = Point()
pt2 = pt1
pt3 = pt1

#%%
print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts


#%%
pt4 = Point()
pt5 = Point()
pt6 = Point()

#%%
print(id(pt4), id(pt5), id(pt6)) # prints the ids of the obejcts


#%%
del pt1

#%%
del pt2
del pt3 
