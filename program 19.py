# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:51:13 2024

@author: K.Shiva Kumari
"""

def reverse_words(string):
    words = string.split()  
    words.reverse()  
    reversed_string = " ".join(words)  
    return reversed_string
input_string = input()
reversed_string = reverse_words(input_string)
print(reversed_string)