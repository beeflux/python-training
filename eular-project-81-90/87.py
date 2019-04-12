from Euler import prime_sieve as sieve
from itertools import product
P = set()
for a,b,c in product(sieve(7072), sieve(369), sieve(85)):
	q = a*a + b**3 + c**4
	if q >= 50000000: break
	P.add(q)
print(len(P))
