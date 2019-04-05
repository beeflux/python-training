"""
    *   Import the prime number module from problem 3
            - It returns the number if the number is prime
            - Else returns 0 when the number is not prime

    *   index_prime(n)
            - Computes the prime number at the particular index

    *   Problem Statement:
            By listing the first six prime numbers 2, 3, 5, 7, 11, and 13, we
            can see that 6th prime is 13

            What is the 10001st prime number?

    *    Test Cases:
            i.  Input ==> index_prime(6)
                Output ==> 13

            ii. Input ==> index_prime(100)
                Output ==> 541

            iii.Input ==> index_prime(1000)
                Output ==> 7919

            iv. Input ==> index_prime(10001)
                Output ==> 104743

"""
from problem3 import prime_number
def index_prime(n):
    prime = []
    i = 2
    while len(prime) != n:
        if prime_number(i) != 0:
            prime.append(i)
        i += 1
    print('Prime number at the index {} is {}'.format(n, prime[n-1]))

# index_prime(6)
# index_prime(100)
# index_prime(1000)
# index_prime(10001)
