"""
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
def run():
    MOD =10000000000
    ans = 0
    #returns the sum of mod of iterative value to the power of the same iterative value 
    for i in range(1,1001):
        ans = (ans + (i**i))% MOD
    return ans
print(run())
