#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:28:49 2019

27)Euler discovered the remarkable quadratic formula:
            n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
is clearly divisible by 41.
The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
    n2+an+b
, where |a|<1000 and |b|≤1000
where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.


@author: bikram
"""

import eulerlib, itertools

def run():
    ans = max(((a,b) for a in range(-999, 1000) for b in range(2, 1000)), key = count_consecutive_primes)
    return str(ans[0] * ans[1])

def count_consecutive_primes(ab):
    a, b = ab
    for i in itertools.count():
        n= i*i + a+b
        if not is_prime(n):
            return i
        
isprimecache = eulerlib.list_primality(1000)

def is_prime(n):
    if n<0:
        return False
    elif n< len(isprimecache):
        return isprimecache[n]
    else:
        return eulerlib.is_prime(n)
if __name__ == "__main__":
    print(run())

