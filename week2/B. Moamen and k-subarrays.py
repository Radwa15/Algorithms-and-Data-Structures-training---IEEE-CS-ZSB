# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:58:33 2021

@author: Ahmed
"""


for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = sorted([a[i],i] for i in range(n))
    print('Yes' if len([i for i in range(1, n) if b[i][1] != b[i-1][1] + 1]) < k else 'No')