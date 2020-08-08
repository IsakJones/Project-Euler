#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:00:54 2020

Project Euler Problem 3

@author: isakjones
"""

def is_prime(x, L = []):
    if x in L:
        return True
    elif x == 1 or x % 2 == 0:
        return False
    for divisor in range(1, round(x ** .5)):
        if is_prime(divisor, L):
            if x % divisor == 0:
                return False
    L.append(x)
    return True

# =============================================================================
# for i in range(1, 40):
#     if is_prime(i):
#         print(str(i) + " is prime.")
#     else:
#         print(str(i) + " is not prime.")
# =============================================================================

def largest_prime_factor(n, L = [], S = []):
    """ 
    Find the largest prime factor of n.
    """
    for divisor in range(2, round(n ** 0.5)):
        if n % divisor == 0:
            factor = int(n / divisor) 
            if is_prime(factor, L):
                return factor
            elif is_prime(divisor, L):
                S.append(divisor)
    try:
        return "The divisor is", str(S[-1])
    except IndexError:
        return "No factor is prime."
                

# =============================================================================
# #600851475143
# print(largest_prime_factor(6008514751435))
# seconds_1 = time.time()
# print("Seconds since epoch =", seconds_1)	
# 
# =============================================================================
#print(is_prime(1319))
# =============================================================================
# for i in range(100):
#     if i * 50753 == 1319578:
#         print(i)
# =============================================================================
        
        
