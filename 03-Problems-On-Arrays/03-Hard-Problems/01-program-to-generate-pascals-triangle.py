# Pascal's Triangle I

"""
Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.

In Pascal's triangle:
1. The first row contains a single element 1.
2. Each row has one more element than the previous row.
3. Every row starts and ends with 1.

For all interior elements (i.e., not at the ends), the value at position (r, c) is computed as the sum of the two elements directly above it from the previous row:

Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
where indexing is 1-based

Example 1
Input: r = 4, c = 2
Output: 3

Explanation:
The Pascal's Triangle is as follows:
    1
    1 1
    1 2 1
    1 3 3 1

Thus, value at row 4 and column 2 = 3

Example 2
Input: r = 5, c = 3
Output: 6

Explanation:
The Pascal's Triangle is as follows:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Thus, value at row 5 and column 3 = 6


Constraints
  1 <= r, c <= 30
  c <= r
  All values will fit inside a 32-bit integer.

"""

# BRUTE FORCE:

r = 5
c = 3

n = r - 1
k = c - 1

def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact*i
    return fact

n_fact = factorial(n)
k_fact = factorial(k)
nk_fact = factorial(n-k)

print(n_fact // (k_fact * nk_fact))
      
      
      
# OPTIMAL SOLUTION

r = 5
c = 3

n = r - 1
k = c - 1

res = 1

for i in range(1, k + 1):
  res = res * (n - i + 1) // i

print(res)