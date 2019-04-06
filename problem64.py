# square root function
from math import sqrt


# function to calculate the continued fraction
def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    period = 0
    if a0 != sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period

# counter
counter = 0

# for loop from 0 to 10000
for i in range(10000):
    if cf(i) % 2 != 0:
        counter += 1

# number of instances
print (counter)
