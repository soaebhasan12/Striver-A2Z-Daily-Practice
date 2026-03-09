# Merge Sorting

"""
Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.

A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.

Example 1
Input: nums = [7, 4, 1, 5, 3]
Output: [1, 3, 4, 5, 7]
Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.

Example 2
Input: nums = [5, 4, 4, 1, 1]
Output: [1, 1, 4, 4, 5]
Explanation: 1 <= 1 <= 4 <= 4 <= 5.
Thus the array is sorted in non-decreasing order.
"""


class Solution:
  def mergeSort(self, nums):
    if len(nums) <= 1:
      return nums
    
    start = 0
    end = len(nums) - 1
    
    mid = (start + end) // 2
    
    result = []
    
    left = nums[start: mid+1]
    right = nums[mid+1: end+1]
    
    left = self.mergeSort(left)
    right = self.mergeSort(right)
    
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        result.append(left[i])
        i += 1
      else:
        result.append(right[j])
        j += 1
      
    while i < len(left):
      result.append(left[i])
      i += 1
    
    while j < len(right):
      result.append(right[j])
      j += 1
    
    return result
  
  
obj = Solution()

arr = [5,4,9,2,8,3,7,1,6]
print("\nBefore Using Merge Sort:")
print(" ".join(map(str, arr)))

output = obj.mergeSort(arr)
print("\nBefore Using Merge Sort:")
print(" ".join(map(str, output)))