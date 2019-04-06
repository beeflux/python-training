# counter to count the number of instances
counter = 0

# for loop to loop from 1 to 9
for i in xrange(1, 10):
    power = 1
    while True:
        if power == len(str(i ** power)):
            counter += 1
        else:
            break
        power += 1

# print the number of instances found
print counter
