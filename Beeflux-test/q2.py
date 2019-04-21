"""
Q2.
Consider a dictionary
d = {1:1, 2:2, 3:3}
a. whats the value of d[4] ?? raise KeyError
b. How can you set 9 value in 2 key.=> Ans: d[2]=9
Write a program to print value with 2 key.
"""

#here the dictionery
d = {1:1, 2:2, 3:3}
#simply assigning new value to key 2
d[2]=9

for i in d:
    if i==2:
        print(f"Key: {i}")
        print(f"Value: {d[2]}")



