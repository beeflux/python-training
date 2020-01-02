# exponent continued fraction
e = [2,]

# iterator
i = 1

# while loop to get 100 numbered list
while len(e) < 100:
    e.extend([1, 2*i, 1])
    i += 1

# initial numerator
numerator = 1

# last number of the list as denominator
denominator = e.pop()

# looping through the list to get the convergents
for i in e[::-1]:
    denominator, numerator =  (denominator * i + numerator, denominator)

# finding the answer
# remember denominator is the new numerator
print (sum([int(digit) for digit in str(denominator)]))
