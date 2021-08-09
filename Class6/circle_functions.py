# -*- coding: utf-8 -*-
"""
Created on Fri May 28 06:51:46 2021

@author: abilash
"""

import math

#%% Function to find Area of a circle

def circArea(r):
	#PI = 3.142
	#return PI * (r*r);
    return math.pi * (r*r);

#%% Function to find Circumference of a circle

def circCircumf(r):
        PI=3.142
        return 2*PI*r

#%% Driver method
rad = int(input("Enter radius of the circle"));

print("Area is ",circArea(rad));

print("Circumference is %.2f" % circCircumf(rad));
