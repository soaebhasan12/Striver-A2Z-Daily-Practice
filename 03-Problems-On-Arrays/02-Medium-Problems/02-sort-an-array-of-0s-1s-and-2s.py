# Sort an array of 0's 1's and 2's

"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.

The sorting must be done in-place, without making a copy of the original array.

Example 1
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation:
The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Example 2
Input: nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation:
The nums array in sorted order has 2 zeroes, 3 ones and zero twos
"""


# SOLVED USING THREE APPROACHES - BRUTE, OPTIMIZED, OPTIMAL (DNF ALGORITHM)

class Solution:
    def sortColors(self, nums):
        # 1. BRUTE FORCE [ O(nlogn) ]
        # return nums.sort()

        # 2. SLIGHTLY MORE OPTIMIZED  - O(n) - Two Passes
        # count0, count1, count2 = 0, 0, 0

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count0 += 1
        #     elif nums[i] == 1:
        #         count1 += 1
        #     else:
        #         count2 += 1  

        # idx = 0
        # for i in range(count0):
        #     nums[idx] = 0
        #     idx += 1

        # for i in range(count1):
        #     nums[idx] = 1
        #     idx += 1

        # for i in range(count2):
        #     nums[idx] = 2
        #     idx += 1

        # return nums


        # 3. DUTCH NATIONAL FLAG (DNF) ALGORITHM - O(n) - Single Pass
        n = len(nums)

        low, mid = 0, 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        
        return nums