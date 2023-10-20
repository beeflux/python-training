import urllib2, itertools

def sq(n):
    x = int(''.join(y[letter_set[i]] for i in n))
    return x if int(x**0.5)**2 == x else False

file_url = "https://projecteuler.net/project/resources/p098_words.txt"
words = [(w[1:-1], sorted(w[1:-1])) 
    for w in urllib2.urlopen(file_url).read().split(',') if len(w)>6]

word_pairs = []
while words:
    w = words.pop()
    word_pairs+= ((w[0], a[0]) for a in words if w[1] == a[1])

max_sq = 0
for w, a in word_pairs:
    letter_set = {x:y for y, x in enumerate(set(w))}
    for y in itertools.permutations('123456789', len(letter_set)):
        if sq(w) and sq(a): max_sq = max(sq(w), sq(a), max_sq)

print("Largest square formed by any member of an anagram pair:", max_sq)
