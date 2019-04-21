"""
Q19
class Progression: 
2 ”””Iterator producing a generic progression. 
3 
4 Default iterator produces the whole numbers 0, 1, 2, ... 
5 ””” 
6 
7 def init (self, start=0): 
8 ”””Initialize current to the first value of the progression.””” 
9 self. current = start 
10 
11 def advance(self): 
12 ”””Update self. current to a new value. 
13 
14 This should be overridden by a subclass to customize progression. 
15 
16 By convention, if current is set to None, this designates the 
17 end of a finite progression. 
18 ””” 
19 self. current += 1 
20 
21 def next (self): 
22 ”””Return the next element, or else raise StopIteration error.””” 
23 if self. current is None: # our convention to end a progression 
24 raise StopIteration( ) 
25 else: 
26 answer = self. current # record current value to return 
27 self. advance( ) # advance to prepare for next time 
28 return answer # return the answer 
29 
30 def iter (self): 
31 ”””By convention, an iterator must return itself as an iterator.””” 
32 return self 
33 
34 def print progression(self, n)
35 ”””Print next n values of the progression.””” 
36 print( .join(str(next(self)) for j in range(n)))

a. Create implementation of an ArithmeticProgression class, which relies on Progression as its base class. The constructor for this new class accepts both an increment value and a starting value as parameters, although default values for each are provided. By our convention, ArithmeticProgression(4) produces the sequence 0,4,

b.
Implementation of geometric progression, in which each value is produced 
by multiplying the preceding value by a fixed constant, known as the base 
of the geometric progression. The starting point of a geometric progression is 
traditionally 1, rather than 0, because multiplying 0 by any factor results in 0. 
As an example, a geometric progression with base 2 proceeds as 1,2,4,8,16,... .

c.
Implement
class FibonacciProgression(Progression): 
”””Iterator producing a generalized Fibonacci progression.”””

For example, if we start with values 4 and 6, the series proceeds as 4,6,10,16,26,42,.


if name == __main__ :
 print( ‘Default progression: ‘) 
Progression( ).print progression(10)

print(‘Arithmetic progression with increment 5: ‘) 
ArithmeticProgression(5).print progression(10)

print( ‘Arithmetic progression with increment 5 and start 2: ‘)
 ArithmeticProgression(5, 2).print progression(10) 

print( ‘Geometric progression with default base: ‘) 
GeometricProgression( ).print progression(10) 

print( ‘Geometric progression with base 3: ‘) 
GeometricProgression(3).print progression(10) 

print( ‘Fibonacci progression with default start values: ‘)
 FibonacciProgression( ).print progression(10) 

print( ‘Fibonacci progression with start values 4 and 6: ‘)
 FibonacciProgression(4, 6).print progression(10)
"""


class Progression: 
    """
        Iterator producing a generic progression. 
        Default iterator produces the whole numbers 0, 1, 2, ... 
    """
    
    def __init__ (self, start=0): 
        self. current = start   
 
    def advance(self): 
        self. current += 1 
 
    def __next__ (self): 
        if self. current is None: # our convention to end a progression 
            raise StopIteration( ) 
        else: 
            answer = self. current # record current value to return 
            self. advance() # advance to prepare for next time 
            return answer # return the answer 
    def __iter__ (self): 
        return self
    
    def print_progression(self, n):
        #this function simply print out the result that is return from __next__
        print(" ,".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    #here class ArithmeticProgresssion is defined and is inherited from base class Progression
    def __init__(self,increment, value):
        self.increment = increment
        self.value = value
        self.current = value
    
    def advance(self):
        #it replace the property of method advance of base class
        self.current = self.current + self.increment

    def __iter__(self):
        return self
    
    def __next__(self):
        answer = self.current
        self.advance()
        return answer

    def print_progression(self, n):
        print(" ,".join(str(next(self)) for j in range(n)))

class GeometricProgression(Progression):
    #similarly, we define GeometricProgression and is inherited from baseclass Progression
    def __init__(self,incrementer):
        self.incrementer = incrementer
        self.current = 1

    def __iter__(self):
        return self

    def advance(self):
        self.current = self.current * self.incrementer
        return self.current

    def __next__(self):
        answer = self.current
        self.advance()
        return answer

    def print_progression(self, n):
        """Print next n values of the progression.""" 
        print(" ,".join(str(next(self)) for j in range(n)))


class FibonacciProgression:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return self

    def __next__(self):
        self.x , self.y = self.y, self.x+self.y
        return self.y

    def print_progression(self, n):
        print(" ,".join(str(next(self)) for j in range(n)))



if __name__ == '__main__':
    print( "Arithmetic progression with increment 5 and start 2:" )
    ArithmeticProgression(5, 2).print_progression(10)
    print("Geometric progression with base 3: ")
    GeometricProgression(3).print_progression(10)
    print("‘Fibonacci progression with start values 4 and 6: ‘")
    FibonacciProgression(4, 6).print_progression(10)