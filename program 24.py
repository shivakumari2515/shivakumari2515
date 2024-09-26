# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:55:11 2024

@author: K.Shiva Kumari
"""

a=input()
p=int(input())
k=int(input())
s=max(0,p-k-1)
e=min(len(a),p+k)
print(min(a[s:e]))