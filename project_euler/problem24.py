#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:54:23 2019

24)A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
        012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


@author: bikram
"""

import itertools

#we initialize a list as the lowest permutation of the given digits, which is the sequence
#(0,1,2,3,4,5,6,7,8,9), Then we call a Python library function that generates a stream of
#all permutations of the values, seek to the 999 999th element (0-based indexing), and stringify it.
def run():
    arr = list(range(10))
    temp = itertools.islice(itertools.permutations(arr),999999, None)
    return "".join(str(x) for x in next(temp))

if __name__ == "__main__":
    print(run())


