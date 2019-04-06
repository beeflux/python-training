"""
    *   largest_palindrome() function comutes the largest palindrome number
        which is the multiple of thre two digit numbers

    *   check_palindrome() computes the palindromic number, and returns 1 when
        the number palindrome and 0 when the number is not palindrome.

    *   Problem Statement:
        A plaindromic number reads the same both ways.
        The largest palindrome made from the product of two 2 digit numbers is
        9009 = 91 x 99
        Find the largest palindrome made from the product of two 3-digit numbers

    *   Test cases:
            Two 2 digit numbers multiplication resulted in 9009
            Two 3 digit numbers multiplication resulted in 906609
"""

def check_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return 1
    else:
        return 0

def largest_palindrome():
    large = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if check_palindrome(i*j):
                large.append(i*j)

    print("""Largest two 3 digit numbers multiplication number which is
            palindrome is {}"""
            .format(max(large)))

largest_palindrome()
