# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:58:42 2021

@author: Ahmed
"""


import sys
s = input()
count ,x = 0 ,11
if len(s) < 2:
    print("0")
    sys.exit()
while x >= 10:
    x = 0
    
    for i in range(0,len(s)):
        x += int(s[i])
    
    s = str(x)
    count += 1
print(count)