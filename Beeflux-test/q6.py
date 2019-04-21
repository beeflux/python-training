"""
def aappend(item , lst=[]):
    lst = []
    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)

"""

def aappend(item , lst=[]):
    lst = []
    """here we are returning the method to append item in list
       in order to get the result, we need to pass actual lst, 
       not the lst.append(item)"""
    return lst.append(item)

a = aappend(1, [])
#it prints None, cause we are returning method to append item in list
print(a)

b = aappend(2, a)
#it prints None, cause we are returning method to append item in list
print(b)

c = aappend(3, [])
#it prints None, cause we are returning method to append item in list
print(c)