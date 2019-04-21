"""
    def aappend(item , lst):
    lst.append(item)
    return lst

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)
"""

def aappend(item , lst):
    lst.append(item)
    return lst

a = aappend(1, [])
#here we pass empty list as parameter so prints [1]
print(a)

b = aappend(2, a)
#we already know a is a lst, so appending the item is list. prints [1,2]
print(b)

c = aappend(3, [])
#we pass empty list as a parameter, so prints [3]
print(c)