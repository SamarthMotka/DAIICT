# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:23:29 2023

@author: 202311023
"""
#lab-13 29/08/23

# Fibonacci numbers module

def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result