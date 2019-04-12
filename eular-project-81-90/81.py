matrix = [map(int, row.split(',')) for row in open("p081_matrix.txt").readlines()]
def run():

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if i*j > 0:
				temp = min(matrix[i - 1][j], matrix[i][j - 1])
			elif i:
				temp = matrix[i - 1][j]
			elif j:
				temp = matrix[i][j - 1]
			else:
				temp = 0
			matrix[i][j] += temp
	return str(matrix[-1][-1])

print(run())

