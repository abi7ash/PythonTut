# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:14:11 2021

@author: abilash
"""

## Program to generate a fibonacee series


#%% Fibonacee generate
def fibgen(N):
  
    #N = 5;
    fibseries=[0,1];#Start List of Fibonacee 
    for i in range(0,N-2):
        fibseries = fibseries + [fibseries[i]+fibseries[i+1]];
    #print(fibseries)
    return fibseries;

#%%

N = int(input("Enter length of fibonacee Series"));
print(fibgen(N));