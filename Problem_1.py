#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:47:54 2020

Project Euler 1

@author: isakjones
"""


def find_sum(limit):
    L = []
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0:
            L.append(i)
    return sum(L)

print(find_sum(1000))