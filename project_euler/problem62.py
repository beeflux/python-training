
# list to store cubes
cubes = []

# iterator
i = 0

# while loop
while True:
    # cube of the number
    cube = sorted(list(str(i**3)))
    # appending the cube to cubes list
    cubes.append(cube)
    # check if it occured 5 times
    if cubes.count(cube) == 5:
        # print the cube of the smallest such cube
        print ((cubes.index(cube))**3)
        break
    i += 1

