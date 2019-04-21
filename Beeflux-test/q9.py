"""
    class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

What Is the output of 
d.kind

d.type

e.kind
e.type
"""

class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

#this prints canine, because we define kind to be method, defined outside the constructor __init__
print(d.kind)

print(type(d))#prints <class 'main.Dog'> as we define d to be instance of class Dog

#this prints canine, because we define kind to be method, defined outside the constructor __init__
print(e.kind)

type(e)##prints <class 'main.Dog'> as we define e to be instance of class Dog
