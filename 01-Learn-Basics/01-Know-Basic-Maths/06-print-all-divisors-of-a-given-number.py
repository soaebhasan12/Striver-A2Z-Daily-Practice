# Divisors of a Number

"""
You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.

A number which completely divides another number is called it's divisor.
"""

class Solution:
    def divisors(self, n):
        divisors_list = []
        for i in range(1, int(n**0.5) +1):
            if n % i == 0:
                divisors_list.append(i)
                if i != n//i:
                    divisors_list.append(n//i)
                    
        divisors_list.sort()

        return divisors_list