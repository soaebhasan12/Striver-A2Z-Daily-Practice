# Rotate matrix by 90 degrees
"""
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.

The rotation must be done in place, meaning the input 2D matrix must be modified directly.

Example 1
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Example 2
Input: matrix = [
                  [0, 1, 1, 2], 
                  [2, 0, 3, 1], 
                  [4, 5, 0, 5], 
                  [5, 6, 7, 0]
                ]
                
Output: matrix = [
                   [5, 4, 2, 0], 
                   [6, 5, 0, 1], 
                   [7, 0, 3, 1], 
                   [0, 5, 1, 2]
                 ]
"""




# BRUTE FORCE: Time - O(n^2) & Space - O(n^2)

matrix = [
            [0, 1, 1, 2], 
            [2, 0, 3, 1], 
            [4, 5, 0, 5], 
            [5, 6, 7, 0]
          ]

n = len(matrix)
m = len(matrix[0])

answer = [[0]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        answer[j][n-1-i] = matrix[i][j]

# copy back to original matrix
for i in range(n):
    for j in range(m):
        matrix[i][j] = answer[i][j]

print(matrix)


# OPTIMAL APPROACH: TRANSPOSE Matrix + REVERSE ROW

matrix = [
            [0, 1, 1, 2], 
            [2, 0, 3, 1], 
            [4, 5, 0, 5], 
            [5, 6, 7, 0]
          ]

n = len(matrix)

for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
    for j in range(n//2):
        matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        
print(matrix)