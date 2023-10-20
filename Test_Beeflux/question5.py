'''

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



 ANSWER:


a = aappend(1, []) 
print(a)
Output : None ,append item is a method dont return anything


b = aappend(2, a)
print(b)
Output : a cant be taken as list type , its a none type


c = aappend(3, [])
print(c)
Outputs : None , append item is a method dont return anything


'''
