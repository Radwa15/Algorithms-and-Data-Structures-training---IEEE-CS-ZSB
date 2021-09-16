# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:52:19 2021

@author: Ahmed
"""


t = int(input())
while t != 0:
        t -= 1
        n = int(input())
        a = n//3
        b = n//3
        rem = n%3
        if rem == 1:
            print(a+1, b)
        elif rem == 2:
            print(a, b+1)
        else:
            print(a, b)