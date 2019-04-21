"""
Q11.

Create a Iteratr class for givng numbers up to given input values.


e.g. b = IteratorBee(10), returns same.

Create a generator function factors to give factors of input.
def factors(n):
"""

class Counter:
    #here class is iterator, __iter__ and __next__ function defines class to iterator
	def __init__(self, num):
		self.num = num

	def __iter__(self):
		return self

	def __next__(self):
        for i in range(self.num):
            if (i!=0):
                print(i)
            else:   
		        raise StopIteration

def factors(n):
    #function to print factors of n using generator
    for i in range(n):
        if (i!=0):
            if (n%i==0):
                yield(i)

for i in factors(10):
    print(i)



