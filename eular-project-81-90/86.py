import math
L, c, a = 1000000, 0, 2

while c < L:
    a += 1
    for bc in range(3, 2*a):
        if (bc*a) % 12 == 0:
            s = math.sqrt(bc*bc + a*a)
            if not s % 1:    # check if s is an perfect square (integer)
                c += min(bc, a+1) - (bc+1)//2 
 
print(a)
