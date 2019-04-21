"""
Q3.
Consider a function

def student(name, roll, age, address):
    print(name, roll, age, address)
"""


#define function that actually prints students data
def student(name, roll, age, address):
    print(f"Student Name:{name}")
    print(f"Student Roll: {roll}")
    print(f"Student Age:{age}")
    print(f"Student Address: {address}")


#function to print students name, roll, age and address
#student(name, roll, age,address)

student('pratima', name='pratima', 20, 20, 20)
#this actually print error as number of parameter is 5

student('pratima', 20, 25, 'kathmandu')
#Student Name:pratima
#Student Roll: 20
#Student Age:25
#Student Address: kathmandu

student('pratima')
#not enough functional parameter
  