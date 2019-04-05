"""
Project Euler 47: The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?


"""

def run(L, nf, ns):
	L+= ns
	f = [0]*L
	for n in range(2, L):
		if f[n] == nf:
			c+= 1
			if c == ns:
				print(n-ns+1)
				c-= 1
		else:
			c = 0
			if f[n] == 0: f[n::n] = [x+1 for x in f[n::n]]
	return
print(run(300000,4,4))
