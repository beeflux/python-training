'''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
We are supposed to display a number under one million, that produces the longest
chain. 
# We will count the number of times division takes place and store it in the 
  dictionary as value.
# If the number is already present in the dictionary we take its value(which
  will be a length of its chain) and directly add to the count. This makes our 
  calculation faster.
# Each time we are also storing the value of count in the list so that we can 
  easily find the largest chain length(which the value of count)
# We are also re-initializing the value of count also, so that previous value of
  count does not affect another number's count value


'''


class CollatzSequence:

    def __init__(self):
        self.chain_lst = []
        self.chain_dct = {1:0} #initializing such that we can check if the chain
                               #finishes at 1  

    def chain_generate(self):
        for num in range(1, 1000001): # running loop 1 million times
            count = 0 #initalizing the value of count inorder to count the data in chain
            n = num #substituting the value such that we can store it as a key in dictionary later

            while num not in self.chain_dct: #if the number at anytime is not found in the dictionary,
                                            # we keep on carrying out operation

                if num % 2 == 0:  #in case the number is even            
                    num //= 2  #taking the quotient only
                else: #in case the number is odd
                    num = 3 * num + 1 
                    count += 1 #each time we count the value, no matter either odd or even
                    
            count += self.chain_dct[num] #Most clever step. While carrying out the operation if the 
                                        #the number is found to be in the dictionary, we take its count value and add it
                                        # this increases speed of calculation

            self.chain_dct[n] = count #we add the number as key and corresponding count as value

            self.chain_lst.append(count) #we are adding only the count value in list so that we can easily 
                                         #get the maxium length of chain   

        max_chain = max(self.chain_lst) #we get the maximum chain length
        # we are trying to display the corresponding key by searching the dictionary for the maximum length 
        # and taking its corresponding key only
        for key, value in self.chain_dct.items():
            if max_chain == value:
                print("{} has maximum length chain of length {}".format(key, max_chain))



czs = CollatzSequence()
czs.chain_generate()

            

