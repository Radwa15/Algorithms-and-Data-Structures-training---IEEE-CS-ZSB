# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:58:34 2021

@author: Ahmed
"""


s = int(input())
c = int(input())
res = 1
while True:
    if (s*res)%10 == c or (s*res)%10 == 0:
        print(res)
        break
    res += 1