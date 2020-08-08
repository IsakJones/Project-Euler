#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:10:52 2020

@author: isakjones
"""


# =============================================================================
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.
# =============================================================================

def amicable(a, b):
    """ 
    Returns True if a and b are amicable numbers.
    """
    if sum(proper_divisors(a)) == b and sum(proper_divisors(b)) == a:
            return True
    return False

def proper_divisors(n):
    """ 
    Outputs a list of proper divisors of integer n.
    """
    return [i for i in range(1, n) if n % i == 0]

def amicable_sum(k):
    result = []
    for a in range(2, k):
        b = sum(proper_divisors(a))
        if a != b and amicable(a, b) and a not in result:
            result.append(a)
            result.append(b)
    return sum(result)
    
class Solution:
    def __init__(self, k):
        self.k = k
        self.sol = amicable_sum(self.k)
    def __str__(self):
        return str(self.sol)
    
        
print(Solution(10000))