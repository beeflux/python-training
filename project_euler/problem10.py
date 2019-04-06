"""
    Summation of primes

    *   Module imported from the problem3 prime_number finder

    *   prime_list(n)
            - generates a list containing the prime number below 'n'
            - sum function sums up all the numbers in the prime_list

    *   Problem Statement
            The sum of primes below 10 is 2 + 3 + 5 + 7 = 17
            Find the sum of all the primes below two million.

    *   Test Cases:
            i.  Input ==> prime_list(10)
                Output ==> 17

            ii. Input ==> prime_list(100)
                Output ==>  1060

            iii. Input  ==> prime_list(1000)
                 Output ==> 76127

            iv. Input  ==> prime_list(20000)
                Output ==> 21171191

            v.  Input  ==> prime_list(2000000)
                Output ==>

"""

from problem3 import prime_number

def prime_list(n):
    primes = []
    i = 2
    while i < n:
        if prime_number(i) != 0:
            primes.append(i)
        i += 1
    print("Sum of primes below {} is {}".format(n, sum(primes)))

prime_list(2000000)
