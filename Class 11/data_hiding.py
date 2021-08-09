# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:02:17 2021

@author: abilash
"""

class JustCounter:
    __secretCount = 0
  
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

#%%
counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount);