# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:53:20 2021

@author: Ahmed
"""


for _ in range(int(input())):
    n = int(input())
    s = input()
    if s == '?' * n:
        s = s.replace('?','R',1)
    while '?' in s:
        s = s.replace('R?','RB')
        s = s.replace('B?', 'BR')
        s = s.replace('?B', 'RB')
        s = s.replace('?R', 'BR')
    print(s)