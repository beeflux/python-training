'''

  Q7.

def aappend(item , lst):
    lst = []
    lst.append(item)
    return lst

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)

'''

def aappend(item , lst):
    lst = [] #initialization of list which is empty
    lst.append(item)
    return lst

a = aappend(1, [])
print(a)
#prints [1] as output ,1 is added to the lst and lst is returned to a

b = aappend(2, a)
print(b)
#prints [2] as output ,2 is added to the lst and lst is returned to b
#list a is emptied by function so result [1,2] is not seen


c = aappend(3, [])
print(c)
#prints [3] as output ,3 is added to the lst and lst is returned to c


