"""
    *   smallest_divisible(num) computes the smallest number divisible from 1 to
        number provided by user.

    *   numpy package is used to get all the range of numbers from 1 to number
        provided by user.

    *   Problem Statement:

        2520 is the smallest number that can be divided by each numbers from
        1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all the
        numbers from 1 to 20

    *   Test cases:
            input ==> smallest_divisible(10)
            output ==> 2520

            input ==> smallest_divisible(5)
            output ==> 60

            input ==> smallest_divisible(15)
            output ==> 360360

            input ==> smallest_divisible(20)
            output ==> 232792560
"""
import numpy as np

def smallest_divisible(num):
    n = 1
    i = np.arange(1,num+1,1)
    while True:
        if sum(n%i) == 0:
            print("""largest number divisible by all the numbers
            from 1 to {} is {}"""
            .format(num, n))
            break
        n += 1
#smallest_divisible(10)
# smallest_divisible(5)
# smallest_divisible(15)
#smallest_divisible(20)
