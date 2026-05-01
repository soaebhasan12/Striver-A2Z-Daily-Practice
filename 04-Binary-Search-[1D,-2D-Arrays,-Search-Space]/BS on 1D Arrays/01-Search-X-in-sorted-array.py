# Search X in sorted array

"""
Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. If the target is found in the array, return its index. If the target is not found, return -1.


Example 1
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: The target integer 9 exists in nums and its index is 4


Example 2
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: The target integer 2 does not exist in nums so return -1
"""

# 1 - Implementation:

nums = [-1,0,2,3,5,9,12]
target = 2

low = 0 
high = len(nums) - 1

while low <= high:
  mid = (low + high) // 2
  
  if target == nums[mid]:
    print(mid)
    break
  elif target > nums[mid]:
    low = mid + 1
  else:
    high = mid - 1

if high < low:
  print("-1")