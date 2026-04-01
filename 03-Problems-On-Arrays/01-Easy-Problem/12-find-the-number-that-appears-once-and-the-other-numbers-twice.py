# Single Number - I

"""
Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.

Example 1
Input : nums = [1, 2, 2, 4, 3, 1, 4]
Output : 3
Explanation : The integer 3 has appeared only once.

Example 2
Input : nums = [5]
Output : 5
Explanation : The integer 5 has appeared only once.
"""



class Solution:
    def singleNumber(self, nums):
        map_dict = {}

        for i in range(len(nums)):
            if nums[i] not in map_dict:
                map_dict[nums[i]] = 1
            else:
                map_dict[nums[i]] += 1
        
        for key in map_dict:
            if map_dict[key] == 1:
                return key
            else:
                continue