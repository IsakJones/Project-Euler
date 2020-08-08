#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:48:56 2020

Euler Problem 5

@author: isakjones
"""
def list_of_divisibles(n):
    """ 
    Extracts the list of divisibles up to n. That includes all squares, cubes, etc. of primes and remaining primes.
    """
    def is_prime(x, L = []):
        if x in L or x == 2:
            return True
        elif x == 1 or x % 2 == 0:
            return False
        for divisor in range(1, round(x ** .5)):
            if is_prime(divisor, L):
                if x % divisor == 0:
                    return False
        return True
                
    def largest_exponent(i, n):
        """
        Given a limit n and a base i, finds the largest exponenet x such that i ^ x <= n, and outputs i ^ x.

        """
        x = 1
        while i ** x <= n:
            x += 1
        x -= 1
        print(i, x, i**x)
        return i ** x
    
    L = []
    for i in range(2, n+1):
        if i in L:
            continue
        elif is_prime(i):
            L.append(largest_exponent(i, n))
    return L

import numpy 

def find_min_prod(n):
    return numpy.prod(list_of_divisibles(n))

L = list_of_divisibles(20)

S = list_of_divisibles(10)

print(L)
print(S)

print(find_min_prod(20))



# =============================================================================
# def find_min_multiple(L):
#     condition = False
#     n = 2520
#     while not condition:
# =============================================================================
        
            
        
        


