from urllib import urlopen
s = 0

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and (i % 9)/3 == (j % 9)/3)
def r(a):
    global s
    i = a.find('0')
    if i == -1:
        s+=int(a[0:3])

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            r(a[:i] + m + a[i+1:])

file = urlopen('https://projecteuler.net/project/resources/p096_sudoku.txt','r').readlines()
fx = ''.join([line[:9] for line in file if not 'Grid' in line])
fx = [fx[i:(i+81)] for i in range(0,len(fx),81)]

[r(p) for p in fx]

print("Project Euler 96 Solution =", s)
