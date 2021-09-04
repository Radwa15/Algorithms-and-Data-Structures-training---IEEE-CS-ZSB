# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:58:35 2021

@author: Ahmed
"""


t = int(input())
while t > 0:
    k = int(input())
    j , res , a = 0, 0, 1
    while j < k:
        if a%3 != 0 and a%10 != 3:
            res = a
            j += 1
        a += 1
    print(res)
    t -= 1