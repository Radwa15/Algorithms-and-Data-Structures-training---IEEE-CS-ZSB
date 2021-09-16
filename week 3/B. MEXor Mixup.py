# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 03:18:21 2021

@author: Ahmed
"""


for _ in range(int(input())):
  a,b=map(int,input().split())
  x=[0,a//4*4,1,a][a%4]
  if b==x:
    print(a)
  elif x^b==a:
    print(a+2)
  else:
    print(a+1)