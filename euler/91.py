def check_right(x1,y1,x2,y2):
    a = x1**2 + y1**2
    b =x2**2 + y2**2
    c = ((x2-x1)**2 + (y2-y1)**2)
    return (a+b ==c) or (b+c == a) or (c +a ==b)
#check_right(2,0,1,2)

def calculate():
    L = 10
    final = sum(1
            for x1 in range(L)
            for x2 in range(L)
            for y1 in range(L)
            for y2 in range(L)
            if y2*x1 < x2* y1 and check_right(x1,y1,x2,y2))
    return final

calculate()
