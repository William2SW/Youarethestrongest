# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:47:41 2021

@author: William_SkyWalk
"""

for i in range(1,8):
    for j in range(i,7):
        print(" ", end = '')
    for k in range(1,i*2):
        print("*", end = '')
    for l in range(i,7):
        print(" ", end = '')
    print("")