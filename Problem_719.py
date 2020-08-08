#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:27:24 2020

@author: isakjones
"""
import time

# =============================================================================
# We define an S-number to be a natural number, n, that is a perfect square and its square root can be obtained by splitting the decimal representation of n into 2 or more numbers then adding the numbers.
# 
# For example, 81 is an S-number because 81 ** 0.5 = 8 + 1.
# 6724 is an S-number: 6724 ** 0.5 = 6 + 72 + 4.
# 8281 is an S-number: 8281 ** 0.5 = 8 + 2 + 81.
# 9801 is an S-number: 9801 ** 0.5 = 98 + 0 + 1
# 
# Further we define T(N) to be the sum of all S-numbers n <= N. You are given T(10 ** 4) = 41333.
# 
# Find T(10 ** 12)
# =============================================================================

def S_number(n, memo = {}):
    """
    Tests whether n is an S-number.
    """

    def permute(digits, memo = {}):
        """
        Given a list of string digits, provides all permutations as relevant to the problem, in which only adjunct digits can be added into a larger number.
        """
        
        if len(digits) == 1:
            return [digits]
        elif tuple(digits) in memo:
            return memo[tuple(digits)]
        else:
            first = [item + [digits[-1]] for item in permute(digits[:-1], memo)]
            second = permute(digits[:-2] + ["".join(digits[-2:])], memo)
            memo[tuple(digits)] = first + second
            return first  + second 

    root = n ** 0.5        
    if root ** 2 == n and n != 1:
        for permutation in permute([digit for digit in str(n)], memo):
            if sum(list(map(int, permutation))) == root:
                return True
    return False

S_numbers = []
memo = {}
start = time.time()
for n in range(int(10 ** 6)):
    if S_number(n, memo):
        S_numbers.append(n)
stop = time.time()
print(S_numbers)
print(stop - start)
#print(S_number(10 ))

#Huh... The memoized version takes much longer (almost 4 times as much when 10 ** 6)