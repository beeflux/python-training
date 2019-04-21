"""
Q4.
Whats the difference between tuple and list.
Ans: Tuple is a immutable object and list is mutable.
     Tuple gives fast result and List gives comparatively slow result

Consider a list
l = [1,2,3,4,5,6,7,8,9]

how can you get last 4 items in l
"""

#given list
l = [1,2,3,4,5,6,7,8]
count = len(l)
#for loop to print last 4 digit:
for i in l:
    count = count-1
    if count < 4:
        print(i)


