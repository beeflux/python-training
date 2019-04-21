"""
Q13.

Write a function to give squareroot of a value if it is int or float, raise an exception otherwise.
def sqt(x):
"""

def sqt(x):
    try:#execute only when the x data type is int and flot
        return (x**2)
    except:
        return ("X is neither int nor float")



y = sqt(2)# we pass the parameter 2 which is type int, so prints result
print(y)

z = sqt(2.5)# we pass the parameter 2 which is type float, so prints result
print(z)

x = sqt('hi')# we pass the parameter hi which is type str, so runs exception
print(x)