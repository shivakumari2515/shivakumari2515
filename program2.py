# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:28:39 2024

@author: K.Shiva Kumari
"""
def count_returns_to_start(N, A):
    current_position = 0
    return_count = 0
    
    for move in A:
        current_position += move
        if current_position == 0:
            return_count += 1
            
    return return_count

# Example usage:
N = int(input())
A = list(map(int,input().split())) # Example moves
result = count_returns_to_start(N, A)
print(result)
  
