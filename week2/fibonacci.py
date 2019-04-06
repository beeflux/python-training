#!/usr/bin/python3

def fibonacci_num(n):
    a,b=0,1
    while a<n:
        print(a,end=',')
        a,b=b,a+b

fibonacci_num(10)
