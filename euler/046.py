"""
Project Euler 46:It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square


"""

def run():
    
    n = 5
    f = 1
    primes = set()

    while True:
        if all(n % p for p in primes):
            primes.add(n)
        else:
            if not any((n-2*i*i) in primes for i in range(1, n)):
                break
        n += 3-f
        f = -f

    print("the smallest odd composite that cannot be written as the sum of a prime and twice a square =",n)
if __name__ == '__main__':
	run()
