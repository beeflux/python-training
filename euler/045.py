# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:39:02 2019

@author: gagan
"""
def run():
    #initializing value of i, j and k from 286,166 and 144 respectively
    i = 286
    j = 166
    k = 144
    #while loop starts
    while True:
        triangle = i * (i + 1) // 2
        pentagon = j * (j * 3 - 1) // 2
        hexagon  = k * (k * 2 - 1)
        #checking whether max value is equals to min or not
        minimum = min(triangle, pentagon, hexagon)
        if minimum == max(triangle, pentagon, hexagon):
            #returns the final value where values of triangle,pentagon and hexagon are equal
            #returns the corresponding i,j and k's value
            return pentagon,i,j,k

        if minimum == triangle:
	    #incrementing value of i if triangle value is minimum
            i += 1
        if minimum == pentagon: 
            #incrementing value of j if pentagon value is minimum
            j += 1
        if minimum == hexagon :
	    #incrementing value of k if hexagon value is minimum
            k += 1
            
            
ans = run()
print("the value of i, j and k are respectively:",ans[1],ans[2],ans[3])
print("the final value at which triangle,pentagon and hexagon is:",ans[0])
