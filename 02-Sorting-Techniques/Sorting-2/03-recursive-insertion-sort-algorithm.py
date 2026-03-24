# Recursive Insertion Sort

"""
Given an array of integers nums, sort the array in non-decreasing order using the recursive Insertion Sort algorithm, and return the sorted array.

You must implement Insertion Sort using recursion only.
Do not use loops (like for or while) or built-in sorting functions (sort, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or equal to all elements that come before it.

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

Constraints
1 <= nums.length <= 1000
-104 <= nums[i] <= 104
nums[i] may contain duplicate values.
"""

class Solution:
    # def insertionSort(self, nums):
    def insertionSort(self, nums, n=None):
        if n is None:
          n = len(nums)
           
        # if len(nums) <= 1:
        if n <= 1:
            # return nums
            return

        # n = len(nums)

        # Step 1: sort first n-1 elements
        self.insertionSort(nums, n-1)
        # self.insertionSort(nums[:n-1])
                
        # Step 2: pick last element
        element = nums[n - 1]
        i = n - 2

        # Step 3: shift elements
        while i >= 0 and element < nums[i] :
            nums[i+1] = nums[i]
            i -= 1
        
        # Step 4: insert element at correct position
        nums[i+1] = element

        return nums


obj = Solution()

arr = [5,4,9,2,8,3,7,1,6]
print("\nBefore Using Bubble Sort:")
print(" ".join(map(str, arr)))

output = obj.insertionSort(arr)
print("\nBefore Using Bubble Sort:")
print(" ".join(map(str, output)))