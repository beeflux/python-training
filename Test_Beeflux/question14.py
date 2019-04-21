'''
Q14.
  Write a short program that takes as input three integers, a, b, and c,
  from the console and determines if they can be used in a correct arithmetic
  formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
  
'''


a= int(input("Enter integer a :"))
b= int(input("Enter integer b :"))
c= int(input("Enter integer c :"))

if (a + b ==c):
    print("the given integers are in form : ** a + b = c ***")
    
elif (b - c == a):
    print("the given integers are in form : ** a = b - c ***")
    exit
elif (a * b == c):
    print("the given integers are in form : ** a * b == c ***")
    exit
else:
    print("these numbers cant be used in the correct arithematic forms")
