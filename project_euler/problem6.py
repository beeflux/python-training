"""
    *   difference_calculator(n)
            - Computes the difference between the sum of squares and squares sum
            - Uses squares_of_sum(n) to compute squares of sum
            - Uses sum_of_squares(n) to compute the sum of squares

    *   Problem Statement:
            The sum of squares of the first 10 natural numbers is:
            1^2 + 2^2 + 3^2 + ... + 10^2 = 385
            The square of the sum of the first 10 natural numbers is:
            (1+2+3+.. 10)^2 = 55^2 = 3025
            Hence the difference between the sum of the squares of the first ten
            natural numbers and the square of the sum is 2025-385 = 2640

            Find the difference between the sum of the squeares of the first one
            hundred natural numbers and the square of the sum.

    * Test Cases:
            Input ==> n = 10
            Output ==> 2640

            Input ==> n = 20
            Output ==> 41230

            Input ==> n = 50
            Output ==> 1582700

            Input ==> n = 100
            Output ==> 25164150

"""
# Computes the squares of the numers and returns the total sum
def squares_of_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result
#print(squares_of_sum(10))

# Computes the sum of all the numbers in that range and returns the total square
def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result**2
#print(sum_of_squares(10))

# Computes the total difference between the sum of squares and squares sum
def difference_calculator(n):
    result =  sum_of_squares(n) - squares_of_sum(n)
    print("""Difference between squares sum and sum of squares from
            1 to {} is {}""".format(n, result))
# difference_calculator(10)
# difference_calculator(20)
# difference_calculator(50)
# difference_calculator(100)
