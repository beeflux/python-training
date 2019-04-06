#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:03:33 2019



25)The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

<solution>
Here, because the target number is relatively small, we simply compute each Fibonacci number starting
from the beginning until we encounter one with exactly 1000 degits. The Fibonacci sequence grows
exponentially with a base of about 1.618, so the numbers in base 10 will lengthen by one digit
after every log10(1.618) ~= 4.78 steps on average. This means the answer is at index around 4780.

@author: bikram
"""

import itertools


def run():
    digits = 1000
    previous = 1
    current = 0
    for i in itertools.count():
        #At this point , previous = fibonacci(i -1) and current = fibonacci(i)
        if len(str(current)) > digits:
            raise RuntimeError("not found")
        elif len(str(current)) == digits:
            return str(i)
        
        #Advance the Fibonacci sequence by one step
        previous, current = current, previous + current

print(run())
        
