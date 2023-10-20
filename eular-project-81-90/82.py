from urllib2 import urlopen

file_url = 'https://projecteuler.net/project/resources/p082_matrix.txt'
matrix = [map(int, row.split(',')) for row in urlopen(file_url).readlines()]
n, m = len(matrix), len(matrix[0]) 
cost = [matrix[i][-1] for i in xrange(n)]

for i in xrange(m-2, -1, -1):
	cost[0] += matrix[0][i]
	for j in xrange(1, n):
		cost[j] = min(cost[j], cost[j-1]) + matrix[j][i]
	for j in xrange(n-2, -1, -1):
		cost[j] = min(cost[j], cost[j+1] + matrix[j][i])

print("Minimum path in", n, "by", m, "matrix =", min(cost))
