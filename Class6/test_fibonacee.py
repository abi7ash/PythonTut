# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:47:12 2021

@author: abilash
"""

## Test if a number is a part of the fibonacee series

#%% generate Fibonacee with last number in series less than N
def fibgen4val(N):
  
    #N = 7;
    fibseries=[0,1];
    fib_end = len(fibseries)-1;
    while fibseries[fib_end] < N:
        fibseries = fibseries + [fibseries[fib_end - 1]+fibseries[fib_end]];
        fib_end = len(fibseries)-1;
    return fibseries;

#%%
y = int(input("Enter the number to test in Fibonacee Series \n"));


fibo_ser = fibgen4val(y);  

if fibo_ser.count(y) == 0:
    print("Number ",y," not a part of Fibonacee Series \n");
else:
    print("Number ",y," is part of Fibonacee Series \n");
    print("Number ",y," has position ",fibo_ser.index(y)+1)

print("The Valid series is\n",fibo_ser);
#return fibseries;
