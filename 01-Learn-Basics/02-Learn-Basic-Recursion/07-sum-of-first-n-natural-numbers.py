# Sum of First N Numbers

"""
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

Example 1
Input : N = 4
Output : 10
Explanation : first four natural numbers are 1, 2, 3, 4.
Sum is 1 + 2 + 3 + 4 => 10.

Example 2
Input : N = 2
Output : 3
Explanation : first two natural numbers are 1, 2.
Sum is 1 + 2 => 3.
"""

# 01 - Recursive Method

# class RecursiveSolution:
#     def NnumbersSum(self, N):
#         if N == 0:
#             return 0

#         return N + self.NnumbersSum(N-1)
      
# obj = RecursiveSolution()
# sum = obj.NnumbersSum(5)
# print(sum)
      
      

# 01 - Parametrised Method
# Parametrised method mein:
# Answer hum parameter mein carry karte hain.
# Aur base case pe directly return karte hain.
      
class ParametrisedSolution:
    def NnumbersSum(self, N, sum1):
      if N == 0:
        return sum1
      
      return self.NnumbersSum(N-1, sum1+N)
      
      
      

obj1 = ParametrisedSolution()
sum1 = obj1.NnumbersSum(5, 0)
print(sum1)



