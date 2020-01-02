'''

  Q6.

def aappend(item , lst=[]):
    lst = []
    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)



'''

def aappend(item , lst=[]):
    lst = []
    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)


#all the prints are none as the method lst.append(item) return none not the append value
