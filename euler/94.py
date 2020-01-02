side0, side, s, p, m = 1, 1, 0, 0, 1

L = 10**9
while p <= L:
	side0, side, m = side, 4*side - side0 + 2*m, -m
	s += p
	p = 3*side - m

print("Sum of perimeters less than", L, " =", s)
