'''

Here we are supposed to find the sum of the digits in the number 100!.
So we define a class FactorialDigitSum containing the methods calc_sum
in which we calculate the remainder for adding the final sum. We also
calculcate the quotient inorder to remove the last digit one by one

'''


class FactorialDigitSum:

    def __init__(self, num):
        self.fact = 1
        self.num = num
    
    def calc_sum(self):
        sum = 0
        for n in range(1, self.num+1): #calculating the factorial
            self.fact = self.fact * n #storing the value 

        epoch = len(str(self.fact)) #taking the number of digits present in self.fact 
                                    #we need this so that we can iterate as per the number of
                                    # digits present here
        
        for i in range(epoch): #iterating as per the number of digits present in the self.fact
            remainder = self.fact % 10 #calculating remainder
            sum += remainder #adding the remainder and storing in sum
            self.fact = self.fact // 10 #calculating quotient and removing the last digit
        print("The sum of the digits in the number",self.num,"! is: ",sum)


fd = FactorialDigitSum(100)
fd.calc_sum()
