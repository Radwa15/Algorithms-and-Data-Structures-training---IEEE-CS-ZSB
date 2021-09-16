# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:57:13 2021

@author: Ahmed
"""


n = int(input())
for i in range(0,n):
    
    l = int(input())
    r = int(input())
    ans =  l
    if r % 2 == 0:
        ans = max(l, int(r / 2 )+ 1)
    else:
        ans = max(l, int(r / 2 )+ 1)
    print( int(r % ans) )