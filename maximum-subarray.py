'''
Leetcode #53 Maximum Subarray Problem

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
'''

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
    greatest = 0
    current = nums[0]
    
    for i in nums:
        greatest = greatest + i
        print(f'greatest {greatest}')
        print(f'current {current}')
        if greatest > current:
            current = greatest
        if greatest < 0:
            greatest = 0
            
    return current

print(maxSubArray(nums)) #should print 6