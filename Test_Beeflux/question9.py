'''

  Q9.


class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')

What Is the output of 
d.kind

d.type

e.kind
e.type


'''


class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')


print(d.kind)
#output is 'canine' as it initializes for all objects in Dog class


#print(d.type)
#Output is error : there is ino 'type' attribute in dog


print(e.kind)
#output is 'canine' as it initializes for all objects in Dog class



#print(e.type)
#output is error : there is ino 'type' attribute in dog
