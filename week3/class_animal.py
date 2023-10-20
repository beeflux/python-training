#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:49:35 2019
	
	created calss "Animal"
	attributes are defined as name,type,habitat.
	method is defined as foodhunt.	
	
@author: bikram
"""

class Animal:
    #Attributes of the animal are defined
    def __init__(self,name,type,habitat):
        self.name=name
        self.type=type
        self.habitat=habitat
        self.method=[]
        
    #The food hunting method of the animal is defined
    def foodhunt(self,method):
        self.method.append(method)
        
        
#The attributes are assigned with perticular values
x = Animal('Human ','mammal ','land')

#The foodhunt method is assigned with parameter
x.foodhunt('hunt animals')

print("The name, type and habitat of the animal are : ")
print(x.name,x.type,x.habitat)

print("The food gathering method is ")
print(x.foodhunt('kill wild animals'))
