"""
    Special Pythagorean Triplet

    *   pythagorean_triplet()
            - Computes the a, b, c value given the condition
                    ===     a^2 + b^2 = c^2
                    ===     a + b + c = 1000

    *   Problem Statement:

            A Pythagorean triplet is a set of three natural numbers, a < b < c,
            for which
                        a^2 + b^2 = c^2
            For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
            There exists exactly one Pythagorean triplet for which a + b + c = 1000.
            Find the product of abc
"""

def pythagorean_triplet():
    for c in range(2, 1000):
        for a in range(1, c):
            b = 1000 - c - a

            # Pythagoras theorem
            if a**2 + b**2 == c**2:
                print('a = {}, b = {}, c = {}'.format(a,b,c))
                return a,b,c
                break
    print('Product of pythagorean triplet is {}'.format(a*b*c))
