# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:59:54 2021

@author: Ahmed
"""


for _ in range(int(input())):
    n,a,b=[int(i) for i in input().split()]
    k=input()
    print(n*a+b*n) if b >= 0 else print(n*a+b*(max(k.count('01'),k.count('10'))+1))