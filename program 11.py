# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:45:51 2024

@author: K.Shiva Kumari
"""

def min_sum(arr):
    arr.sort(reverse=True)
    total = arr[0]
    avg = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < avg:
            break
        total += arr[i]
        avg = (total) / (i + 1)
    
    return total

n = int(input())
arr = list(map(int, input().split()))

result = min_sum(arr)
print(result)