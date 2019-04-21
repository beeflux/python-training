"""
Q5.

consider a function

def aappend(item , lst):
    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)
"""



def aappend(item , lst):
#in the function the parameter is not defined to be list,
#so, returning lst.append(item) generates error,
#as the type is not defined 

    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)
