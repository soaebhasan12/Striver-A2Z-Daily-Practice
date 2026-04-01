# Union of two sorted arrays

"""
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.


The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]
Explanation:
The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2
Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
Output: [1, 3, 4, 5, 6, 7, 8, 9]
Explanation:
The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
"""


class Solution:
    def unionArray(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        
        answer = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if len(answer) == 0 or answer[-1] != nums1[i]:
                    answer.append(nums1[i])
                i += 1

            elif nums1[i] > nums2[j]:
                if len(answer) == 0 or answer[-1] != nums2[j]:
                    answer.append(nums2[j])
                j += 1

            else:  # nums1[i] == nums2[j]
                if len(answer) == 0 or answer[-1] != nums1[i]:
                    answer.append(nums1[i])
                i += 1
                j += 1

        # Remaining elements
        while i < n1:
            if len(answer) == 0 or answer[-1] != nums1[i]:
                answer.append(nums1[i])
            i += 1

        while j < n2:
            if len(answer) == 0 or answer[-1] != nums2[j]:
                answer.append(nums2[j])
            j += 1

        return answer