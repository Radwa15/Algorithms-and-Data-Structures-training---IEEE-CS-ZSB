# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:58:33 2021

@author: Ahmed
"""


import numpy as np
a = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
c = 0
for i in range(0,5):
    for j in range(0,5):
        a[i][j] = input()
        if a[i][j] == 1:
            c += (abs(i-2) + abs(j-2))
            break

print(c)