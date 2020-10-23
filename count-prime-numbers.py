# Count the number of prime numbers less than a non-negative number, n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""
U
    input n = 10
        There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    -> 4
P
    def a helper function
        check if i % index is == 0
            if yes then it is NOT a prime
                return False
        return True 
    loop over range(input)
        set counter
        run helper function
        if true increase counter
E
R
"""
class Solution2:
    def helper(self, n):
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        counter = 0
        for i in range(2, n):
            print(i, self.helper(i))
            if self.helper(i) == True:
                counter +=1
        return counter

