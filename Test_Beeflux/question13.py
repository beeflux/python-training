'''

  Q13.

Write a function to give squareroot of a value if it is int or float, raise an exception otherwise.
def sqt(x):
……….


'''


import math

def sqt(a):
    if(isinstance(a,int) or isinstance(a,float)):
        print(math.sqrt(a))
    else:
        print("You inputted other than integer and float value ")

sqt("b")
#output :You inputted other than integer and float value

sqt(25)
#output : 5.0

