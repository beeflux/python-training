"""
    *   prime_number(a)
        - Determines if the number entered (a) is prime or not
        - If the number is prime returns the prime number
        - Else return 0

    *   max_prime_factor(num)
        - Computes the maximum prime factor of the given number(num)

    *   Problem Statement:
            The prime factors of 13195 are 5, 7, 13 and 29
            What is the largest prime factor of the number 600851475143

    *   Test Cases:
            i. input ==> 13195
               output ==> 29

            ii. input ==> 123456
                output ==> 643

            iii. input ==> 6008514
                 output ==> 58907

            iv. input ==> 600851475143
                output ==> 6857
"""
def max_prime_factor(num):
    n = num
    max_prime_factor_num = None
    while n != 1:
        if num % n == 0:
            if prime_number(n) != 0:
                max_prime_factor_num = n
                break
        n -= 1
    print('''The maximum prime factor of {} is {}'''
            .format(num, max_prime_factor_num))

def prime_number(a):
    i = 2
    flag = 0
    if a == 1 or a == 0:
        flag = 1
    while i < a:
        if a % i == 0:
            flag = 1
            break
        i += 1
    if flag == 0:
        return a
    else:
        return 0

# max_prime_factor(13195)
# max_prime_factor(123456)
# max_prime_factor(6008514)
#max_prime_factor(600851475143)
