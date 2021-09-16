# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 03:17:20 2021

@author: Ahmed
"""


for _ in range(int(input())):
	input()
	k,n,m = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	i = 0
	j = 0
	r = []
	while i!=n or j!=m:
		if i!=n and a[i]<=k:
			r.append(a[i])
			if a[i]==0:
				k += 1
			i += 1
		elif j!=m and b[j]<=k:
			r.append(b[j])
			if b[j]==0:
				k += 1
			j += 1
		else:
			r = [-1]
			break
	print(*r)