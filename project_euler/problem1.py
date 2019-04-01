"""
    sum_multiples_3_5 function prints the sum of multiples of 3 or 5with in the
    given range from 0 to n provided by the user.

    * n refers to the natural numbers

    * Problem Statement : If we list all the natural numbers below 10that are
      multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
      23. Find the sum of all the multiples of 3 or 5 below 1000


    * Test Cases

      i. n = 10 -> Sum of Multiples of 3 or 5 with in the range 10 is 23

      ii. n = 1000 -> Sum of Multiples of 3 or 5 with in the range 1000 is 233168

    * Completed by Adarsh Ghimire Roll - 1, Beeflux
"""
def sum_multiples_3_5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print("""Sum of Multiples of 3 or 5 with in the range {} is {}"""
        .format(n,sum))

#sum_multiples_3_5(10)
#sum_multiples_3_5(1000)
