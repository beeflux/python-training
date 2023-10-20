#This is the solutionn to euler problem no.75
import eulerlib, fractions


def run():
	LIMIT = 1500000
	# 
	# Pythagorean triples theorem:
	#   Every primitive Pythagorean triple with a odd and b even can be expressed as
	#   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2, where s > t > 0 are coprime odd integers.
	# 
	triples = set()
	for s in range(3, eulerlib.sqrt(LIMIT) + 1, 2):
		for t in range(s - 2, 0, -2):
			if fractions.gcd(s, t) == 1:
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a + b + c <= LIMIT:
					triples.add((a, b, c))
	
	ways = [0] * (LIMIT + 1)
	for triple in triples:
		sigma = sum(triple)
		for i in range(sigma, len(ways), sigma):
			ways[i] += 1
	
	ans = ways.count(1)
	return str(ans)


if __name__ == "__main__":
print(run())
