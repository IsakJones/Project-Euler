#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:56:50 2020

@author: isakjones
"""
def find_nth_prime(n):
    
    def is_prime(x, L = []):
        """
        Classic function, but returns a list.

        """
        if x in L:
            return True
        elif x == 1 or x % 2 == 0:
            return False
        for divisor in range(1, round(x ** .5)):
            if is_prime(divisor, L):
                if x % divisor == 0:
                    return False
        L.append(x)
        return True, L