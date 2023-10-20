import networkx as nx
from urllib2 import urlopen

file_url = 'https://projecteuler.net/project/resources/p082_matrix.txt'
matrix = [map(int, row.split(',')) for row in urlopen(file_url).readlines()]
n, m = len(matrix), len(matrix[0])

G = nx.DiGraph()
for i in xrange(n):
    for j in xrange(m):
        neighbors = [(i+x, j+y) for x, y in (-1,0), (0,-1), (1,0), (0,1) 
            if 0 <= i+x < n and 0 <= j+y < m]
        for ix, jy in neighbors:
            G.add_edge((i, j), (ix, jy), weight = matrix[ix][jy])

path_length = nx.dijkstra_path_length(G, source=(0,0), target=(n-1,m-1))

print("Minimum path sum in", n, "by", m, "matrix =", path_length + matrix[0][0])
