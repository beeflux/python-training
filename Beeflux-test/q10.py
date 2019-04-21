"""
    Q10.

d.kind=”white”
d.name=”john”
e.name=”jonny”

what will be output of 

d.kind = > white
e.kind = > canine
d.type => <class 'main.Dog'>
e.type => <class 'main.Dog'>
"""

from q9 import Dog
d = Dog('hi')
e = Dog('hi')


#this will print white, this replace the previous declared value of kind = 'canine'
d.kind='white'
print(d.kind)

#prints canine, as we do not replace anything in the default class
print(e.kind)

print(type(d))#prints <class 'main.Dog'> as we define d to be instance of class Dog

type(e)##prints <class 'main.Dog'> as we define e to be instance of class Dog
