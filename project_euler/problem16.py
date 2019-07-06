"""
    Sum of the digits of the number x^y

    *x and y refers to any whole numbers 

    *problem statement: 2^15=32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
     What is the sum of the digits of the number 2^1000?
    
    *completed by Pramod Pujara, Beeflux
"""

def sum_of_the_digits(x,y):
    power=pow(x,y)             #stores value of x^y
    to_get_item=str(power)     #converts to str making it indexable   
    length=len(str(power))      
    sum_of_digits,i=0,0        #initializes    
    while i!=length:
        sum_of_digits=sum_of_digits+int(to_get_item[i])
        i+=1
    return sum_of_digits
print sum_of_the_digits(2,15)
#print sum_of_the_digits(2,1000)
