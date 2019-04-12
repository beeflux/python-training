'''    

Just like 2^15 = 32768 and the sum of its digits
is 3 + 2 + 7 + 6 + 8 = 26, Here we are calculating
the sum of the digits of the number 2^1000. For 
this we first calculate the value 2^1000 and assign
it to a variable num. Here we are converting into 
string just to know the length for carrying out the 
loop. Once we've done that, we calculate the remainder
by dividing by 10(of whatever the value is given by 2^1000)
and also omit the last digit(of whatever the value is given 
by 2^1000) by calculating the quotient. In each iteration we 
keep adding the remainder.


'''


class PowerDigit:
    
    def __init__(self):
        self.num = 2**1000
        self.sum = 0
    
    def digit_sum(self):
        epoch = len(str(self.num))
        for i in range(epoch):
            remainder = self.num % 10 #calculating the remainder
            self.sum += remainder #adding the remainder to previously calculated remainder
            self.num = self.num // 10 #calculating quotient
        print('''Sum of the digits of the number 2^1000 is: ''', self.sum )

    def run(self):
        return self.digit_sum()



pd = PowerDigit()
pd.run()

