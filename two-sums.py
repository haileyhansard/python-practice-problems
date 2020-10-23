# Input: 
# flightLength: duration of the flight in minutes
# movies: array of movie times in minutes

# Output:
# boolean, true if there exists TWO different movies that add up EXACTLY to the flight flightLength

# Examples:
# flightLength 160
# movies [80, 110, 40] => False
# [80, 110, 80] =>  True
# [20, 30, 110, 40, 50] =>  True

#Hashtable Usage to make it O(n)
movies = [60, 120, 30]
flightLength = 180

def movieTimes(movies, flightLength):
    #sums = []
    hashTable = {}

    for i in range(len(movies)):
      sumMinusElement = flightLength - movies[i]
      if sumMinusElement in hashTable:
        return True
      hashTable[movies[i]] = movies[i]

    return False

print(movieTimes(movies, flightLength))

#---------------#

#Naive appraoch with two for loops
flightLength = 200
movies = [80, 110, 80] 
#this case will return false
def movieTimes2(movies, flightLength):
  for i in range(len(movies)):
    for j in range(len(movies)):
      if i != j:
        if (movies[i] + movies[j]) == flightLength:
          return True
  return False
print(movieTimes2(movies, flightLength))

#---------------#

"""
:type nums: List[int]
:type target: int     
:rtype: List[int]
"""

class Solution(object):
    def twoSum(self, nums, target):
        cache = {}
        for i in range(len(nums)):
            if target - nums[i] in cache:
                return [cache[target - nums[i]],i]
            else:
                cache[nums[i]]=i

input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20)) #this one is printing the index of the two nums that add up to 20
