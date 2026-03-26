# Second Largest Element

"""
Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


Example 1
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation:
The largest value in nums is 8, the second largest is 7

Example 2
Input: nums = [10, 10, 10, 10, 10]
Output: -1
Explanation:
The only value in nums is 10, so there is no second largest value, thus -1 is returned
"""


# # Brute Force

class Solution:
  def secondLargestElement(self, nums):
    largest = nums[0]
    secondLargest = int('-inf')
    
    for i in range(len(nums)):
      if nums[i] > largest:
        secondLargest = largest
        largest = nums[i]
      elif nums[i] != largest and nums[i] > secondLargest:
        secondLargest = nums[i]
    
    if secondLargest == int('-inf') or len(nums) == 0:
       return -1
    
    return secondLargest


# Better Approach


# Optimal Approach

