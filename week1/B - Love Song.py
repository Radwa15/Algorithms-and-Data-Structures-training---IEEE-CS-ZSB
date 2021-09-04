# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:58:41 2021

@author: Ahmed
"""


def pref(li):
    pref_sum = [0]
    for i in li:
        pref_sum.append(pref_sum[-1]+i)
    return pref_sum

    
n, q= map(int, input().split())

s = list(input()) 
pos = []
for i in s:
    pos.append(ord(i) - 96) 

prefixArray = pref(pos) 

for i in range(q):
    l, r = map(int, input().split())
    print(prefixArray[r] - prefixArray[l-1])