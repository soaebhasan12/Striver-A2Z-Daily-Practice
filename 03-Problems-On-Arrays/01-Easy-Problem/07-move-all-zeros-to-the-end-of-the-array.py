# Move Zeros to End

"""
Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.

This must be done in place, without making a copy of the array.

Example 1
Input: nums = [0, 1, 4, 0, 5, 2]
Output: [1, 4, 5, 2, 0, 0]
Explanation:
Both the zeroes are moved to the end and the order of the other elements stay the same

Example 2
Input: nums = [0, 0, 0, 1, 3, -2]
Output: [1, 3, -2, 0, 0, 0]
Explanation:
All 3 zeroes are moved to the end and the order of the other elements stay the same
"""


class Solution:
    def moveZeroes(self, nums):
      n = len(nums)
      i = 0
      
      for j in range(n):
          if nums[j] != 0:
              nums[i], nums[j] = nums[j], nums[i]
              i += 1
        
      return nums