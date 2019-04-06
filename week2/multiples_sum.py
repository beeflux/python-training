""" List of all the natural numbers below 10 that are multiples of
    3 or 5, we get 3,5,6,9 and the sum is 23
    FInd the sum of all the multiples of 3 or 5 below 1000"""
def multiples_calculator(n):
    i = 1
    sum = 0
    while i < n:
        if i%3 == 0 or i%5 == 0:
            sum += i
        i += 1
    print "sum of multiples is " + str(sum)

multiples_calculator(10)
multiples_calculator(1000)
