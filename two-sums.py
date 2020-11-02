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

#------#

#Given an array of integers 'nums' and a target, find all pairs that sum to target.

def printPairs(nums, target):
  for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
      if (nums[i] + nums[j] == target):
        print(nums[i], nums[j])

nums = [2, 5, 11, 7, 23, -4]
target = 7
printPairs(nums, target)


#-------#
'''
You are given an array of n integers and a number k. 
Determine whether there is a pair of elements in the array that sums to exactly k. 
For example, given the array [1, 3, 7] and  k = 8, the answer is “yes,” but given k = 6 the answer is “no.”

'''
def yesOrNo(n, k):
  for i in range(0, len(n)):
    for j in range(i + 1, len(n)):
      if (n[i] + n[j] == k):
        print('yes')
      else:
        print('no')

n = [1, 3, 7]
k = 8
yesOrNo(n, k)

#-----#
# Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

def findPairs(nums, s):
  newList = []
  for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
      if (nums[i] + nums[j] == s):
        pairs = [nums[i], nums[j]]
        newList.append(pairs)
  return newList

nums = [3, 5, 2, -4, 8, 11]
s = 7
print(findPairs(nums, s))