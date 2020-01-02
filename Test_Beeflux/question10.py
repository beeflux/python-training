'''

  What Is the output of 
d.kind

d.type

e.kind
e.type

Q10.

d.kind=”white”
d.name=”john”
e.name=”jonny”

what will be output of 

d.kind
e.kind
d.type
e.type

'''

class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind="white"
d.name="john"
e.name="jonny"

print(d.kind)
#output is white as it is laer updated to attribute of 'd' as d.kind="white"

print(e.kind)
#output is canine by default as 'kind = canine'


#dog has no attribute named 'type' , thus following gives error
#print(d.type)
#print(e.type)






