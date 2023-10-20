def run(L = 1000000):
    d = [1] * L
    for i in xrange(2, L//2):
        for j in xrange(2*i, L, i):
            d[j] += i

    max_cl = 0
    for i in xrange(2, L):
        n, chain = i, []
        while d[n] < L:
            d[n], n = L+1, d[n]
            try: k = chain.index(n)
            except ValueError: chain.append(n)
            else: 
                if len(chain[k:]) > max_cl:
                    max_cl, min_link = len(chain[k:]), min(chain[k:])
    return min_link

print ("Smallest member of the longest amicable chain", run())
