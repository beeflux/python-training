'''

  Q11.

Create a Iteratr class for givng numbers up to given input values.


e.g. b = IteratorBee(10), returns same.

Create a generator function factors to give factors of input.
def factors(n):
    ………………….


'''




class IterationBee:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

y=IterationBee(10)
print(y)


#Create a generator function factors to give factors of input.

def factors(x,i):
    if i==0:
        return
    if x%i == 0:
        print(i)
    return factors (x,i-1) #recursive step

factors(12,12)



