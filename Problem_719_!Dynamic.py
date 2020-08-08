#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:36:33 2020

@author: isakjones
"""
import time
def S_number(n):
    """
    Tests whether n is an S-number.
    """


    def permute(digits):
        """
        Given a list, provides all permutations as relevant to the problem, in which only adjunct digits can be added into a larger number.
        """
        def add_digits(digits):
            return int("".join(list(map(str, digits))))
    
        if len(digits) == 1:
            return [digits]
        else:
            first = [item + [digits[-1]] for item in permute(digits[:-1])]
            second = permute(digits[:-2] + ["".join(digits[-2:])])
            return first  + second 

    root = n ** 0.5        
    if root ** 2 == n and n != 1:
        for permutation in permute([digit for digit in str(n)]):
            if sum(list(map(int, permutation))) == root:
                return True
    return False

S_numbers = []
start = time.time()
for n in range(int(10 ** 6)):
    if S_number(n):
        S_numbers.append(n)
stop = time.time()
print(S_numbers)
print(stop - start)