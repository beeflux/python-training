"""
Q14.
Write a short program that takes as input three integers, a, b, and c, from the console and determines 
if they can be used in a correct arithmetic formula (in the given order),
 like “a+b = c,” “a = b−c,” or “a ∗ b = c.”

"""

a = int(input("Enter the first Variable: "))
b = int(input("Enter the second Variable: "))
c = int(input("Enter the third Variable: "))

def check_arithmetic_function(a,b,c):
    #this function simply check whether the three integer gives the arithmetic formula or not
    #we define the condition and checks whether the arithmetic formula meet or not
    if (a+b==c and a == b-c and a*b == c):
        print("The integers can be used in all three formula as: {a} + {b} = {c} & {b} - {c} = {a} & {a} * {b} = {c}")
    if (a+b==c):
        print(f"Yes three variable forms arithmetic a+b=c as: {a} + {b} = {c}")
    elif(a==b-c):
        print(f"Yes three variable forms arithmetic b-c=a as: {b} - {c} = {a}")
    elif(a*b==c):
        print(f"Yes three variable forms arithmetic a*b=c as: {a} * {b} = {c}")
    else:
        print("The integers do not form any arithmetic formula: ")

check_arithmetic_function(a,b,c)


