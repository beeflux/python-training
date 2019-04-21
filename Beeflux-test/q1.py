"""
Create a function to sum Input Numbers (parameters) which returns sum of inputed numbers. Also write Unittest for the function.

my_sum(1,2)    should return 3 e.g.
my_sum(1,2,3) should return 6
my_sum(1,3,5,7,8) = 24
"""

def my_sum(*args):
#declare function name my_sum and return the total sum
    sum = 0
    for item in args:
        sum = sum+item

    print(sum)

my_sum(1,3,5,7,8)