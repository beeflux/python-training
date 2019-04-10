'''

class LargestProduct contains method for calculating up, down, left, right,
and vertical elements product. For each direction methods have been defined
as up_calc, down_calc, left_calc, right_calc and vertical_calc

Here we are supposed to the greatest product of four adjacent numbers
in the same direction (up, down, left, right, or diagonally) in the 20×20 grid.
this we have defined a method for each direction. We also have created an
empty dictionary where we will be storing the resultant product as key and the 
digits involved in the product as value(this makes easy to understand what's happening).
-> In case of up direction, we start from 339th index and continue until 60th index.
On doing so only, we will have four adjacent elements. 
-> In case of down direction, we start from 60th index and continue till the 339th 
index. On doing so only, we will have four adjacent elements. 
-> In case of right direction, we start from 0th index till the 396th index.
On doing so only, we will have four adjacent elements.
-> In case of left direction we start from the 339th index until 2nd index. only
on doing so we will have 4 elements to multiply.
-> In case of vertical direction we start from the 0th index till 16th index right in column
and 0th index till 320th index down in row and only until the 336th index. Only on doing so
we will have four elements for multiplying

'''


class LargestProduct:
    def __init__(self):
        self.lst= ['''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                      49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                      81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                      52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                      22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                      24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                      32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                      67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                      24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                      21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                      78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                      16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                      86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                      19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                      04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                      88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                      04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                      20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                      20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                      01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48''']
        self.grid = self.lst[0].split()
    
    def up_calc(self):
        dct = {}
        product_lst = []
        for i in range(len(self.grid)-1, -1, -1): #iterating from 339 all the way till  0
            if i >= 60: #we iterate until the value of i is 60. Only on doing so we will have four elements for multiplying
                n1 = i - 20 #each time we take the neighboring elements decreasing the index by 20
                n2 = n1 - 20 #each time we take the neighboring elements decreasing the index by 20
                n3 = n2 - 20 #each time we take the neighboring elements decreasing the index by 20
                product = int(self.grid[i]) * int(self.grid[n1]) * int(self.grid[n2]) * int(self.grid[n3]) #multiplying
                dct[product] = [self.grid[i]+' '+ self.grid[n1] +' '+ self.grid[n2] +' '+self.grid[n3]] #storing in dictionary
                product_lst.append(product) #storing the product in list so that we can get the maximum value
        print("The maximum product in up direction", dct[max(product_lst)], "=", max(product_lst))

    def down_calc(self):
        dct = {}
        product_lst = []
        for i in range(60, len(self.grid)): #we are taking elements from 60 to 339 
            if i <= 339: #from the current position in left direction
                n1 = i + 20 #each time we take the neighboring elements increasing the index by 20
                n2 = n1 + 20 #each time we take the neighboring elements increasing the index by 20
                n3 = n2 + 20 #each time we take the neighboring elements increasing the index by 20
                product = int(self.grid[i]) * int(self.grid[n1]) * int(self.grid[n2]) * int(self.grid[n3]) 
                dct[product] = [self.grid[i]+' '+ self.grid[n1] +' '+ self.grid[n2] +' '+self.grid[n3]] #storing in dictionary
                product_lst.append(product)#storing the product in list so that we can get the maximum value
        print("The maximum product in down direction", dct[max(product_lst)], "=", max(product_lst))

    def right_calc(self):
        dct = {}
        product_lst = []
        for i in range(0, len(self.grid)): #taking elements from index 0 to 339
            if i <= 396: #we only need the elements till 396 index and from the current position in left direction
                n1 = i + 1 #each time we take the neighboring elements increasing the index by 1
                n2 = n1 + 1 #each time we take the neighboring elements increasing the index by 1
                n3 = n2 + 1 #each time we take the neighboring elements increasing the index by 1
                product = int(self.grid[i]) * int(self.grid[n1]) * int(self.grid[n2]) * int(self.grid[n3])
                dct[product] = [self.grid[i]+' '+ self.grid[n1] +' '+ self.grid[n2] +' '+self.grid[n3]] #storing in dictionary
                product_lst.append(product)
        print("The maximum product in right direction", dct[max(product_lst)], "=", max(product_lst))

    def left_calc(self):
        dct = {}
        product_lst = []
        for i in range(len(self.grid)-1, -1, -1 ): #starting iteration from the last index of the list
            if i > 2: #until value of i is greater than 2
                n1 = i - 1 #taking the elements in one step previous position 
                n2 = n1 - 1 #from the current position in left direction
                n3 = n2 - 1 #each time we take the neighboring elements decreasing the index by 1
                product = int(self.grid[i]) * int(self.grid[n1]) * int(self.grid[n2]) * int(self.grid[n3]) #Multiplying
                dct[product] = [self.grid[i]+' '+ self.grid[n1] +' '+ self.grid[n2] +' '+self.grid[n3]] #storing in dictionary
                product_lst.append(product) #storing the product in list so that we can get the maximum value
        print("The maximum product in left direction", dct[max(product_lst)], "=", max(product_lst))

    def vertical_calc(self):
        dct = {}
        product_lst = []
        a = 0
        b = 17
        for epoch in range(17): #We only need elements from 0 to 320 and 
            for i in range(a, b): # 16 to 336 in row. So we iterate 
                n1 = i + 21 #since we need the adjacent data in vertical 
                n2 = n1 + 21  # we are taking the elements that are in +21 position  from each other
                n3 = n2 + 21
                product = int(self.grid[i]) * int(self.grid[n1]) * int(self.grid[n2]) * int(self.grid[n3])
                # we are storing the product as key and 
                # the elements involved in multiplication as value 
                dct[product] = [self.grid[i]+' '+ self.grid[n1] +' '+ self.grid[n2] +' '+self.grid[n3]] 
                product_lst.append(product) #storing in list for taking the maximum resultant product
            a += 20 # incrementing the index position by 20 in column
            b = a + 17 #incrementing the index position by 17 in row
        print("The maximum product in vertical direction", dct[max(product_lst)], "=", max(product_lst))



LP = LargestProduct()
LP.up_calc()
LP.down_calc()
LP.right_calc()
LP.left_calc()
LP.vertical_calc()
