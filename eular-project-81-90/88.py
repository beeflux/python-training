def prodsum(p, s, c, start):
    k = p - s + c     # product - sum + number of factors
    if k < kmax:
        if p < n[k]: n[k] = p
        for i in xrange(start, kmax//p*2 + 1):
            prodsum(p*i, s+i, c+1, i)

kmax = int(input('Enter a value for kmax?'))
if kmax > 12: kmax+= 1
n = [2*kmax] * kmax
prodsum(1, 1, 1, 2)

print("Project Euler 88 Solution =", sum(set(n[2:])))
