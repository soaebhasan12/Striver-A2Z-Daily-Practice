# Reverse an array

"""
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Example 2
Input: n=6, arr = [1,2,1,1,5,1]
Output: [1,5,1,1,2,1]
Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].
"""


# Method 1 -Recursion Approach

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        def helper(start, end):
            if start >= end:
                return

            arr[start], arr[end] = arr[end], arr[start]
            helper(start+1, end-1)
        helper(0, n-1)









# Method 2 -Brute Force Approach

class Solution:
    def reverse(self, arr: list, n: int) -> None:
      len_arr = len(arr)
      reversed_arr = []
      
      for i in range(len_arr-1, -1, -1):
        reversed_arr.append(i)
      
      return reversed_arr
        


# Method 3 -Better Approach - Pointer Method

class Solution:
    def reverse(self, arr: list, n: int) -> None:
      start = 0
      end = len(arr) - 1
      
      while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
      
      return arr
    
# Agar condition start <= end kar dein
# toh kya problem hogi?



# Method 4 -Built-in Library Function Approach

class Solution:
    def reverse(self, arr: list, n: int) -> None:
      arr.reverse()
      # OR
      arr[::-1]