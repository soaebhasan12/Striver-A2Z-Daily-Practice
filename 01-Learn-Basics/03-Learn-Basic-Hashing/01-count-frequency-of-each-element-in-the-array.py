# Counting Frequencies of Array Elements

"""
Given an array nums of size n which may contain duplicate elements.

Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.

You may return the result in any order, but each element must appear exactly once in the output.


Example 1
Input: nums = [1, 2, 2, 1, 3]
Output: [[1, 2], [2, 2], [3, 1]]

Explanation:
- 1 appears 2 times
- 2 appears 2 times
- 3 appears 1 time
Order of output can vary.

Example 2
Input: nums = [5, 5, 5, 5]
Output: [[5, 4]]
Explanation:
- 5 appears 4 times.
"""

class Solution:
    # def __init__(self):
    #     self.map_dict = {}

    def countFrequencies(self, nums):
        map_dict = {}
        for i in nums:
            if i not in map_dict:
                map_dict[i] = 1
            else:
                map_dict[i] += 1
        
        return list(map_dict.items())