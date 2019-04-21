"""
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
"""



def aappend(item , lst):
    lst = []#lst is local variable
    lst.append(item)
    return lst

"""
    Instead of appending in to the same list, the below function prints separate list,
    this is because, we declare the lst = [] inside the function which is local variable,
    so, everytime the aappend() function called, it declare lst = [] as empty list
""" 

a = aappend(1, [])
#prints [1], Every time function is call, 
# the list is empty list cause we define lst = [], inside the function which become local variable
print(a)

b = aappend(2, a)
#prints [2], Every time function is call, 
# the list is empty list cause we define lst = [], inside the function which become local variable
print(b)
#prints [3], Every time function is call, 
# the list is empty list cause we define lst = [], inside the function which become local variable
c = aappend(3, [])
#prints [3]
print(c)