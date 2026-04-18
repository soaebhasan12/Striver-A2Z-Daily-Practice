# Set Matrix Zeroes

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.

Example 1
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation:
Element at position (1,1) is 0, so set entire row 1 and column 1 to 0.

Example 2
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:
There are two zeroes: (0,0) and (0,3).
Row 0 → all elements become 0
Column 0 and column 3 → all elements become 0
"""


# BRUTE FORCE SOLUTION:

"""
0 milte hi row + column ko directly 0 nahi karte
→ pehle temporary marker (float('inf')) se mark karte hain
→ final pass me marker → 0 convert karte hain

⚠️ Key Point
    Marker unique hona chahiye
    (-1 unsafe hai, float('inf') safe hai)

⏱️ Complexity
    Time → O(n*m*(n+m)) ❌ (heavy)
    Space → O(1) ✅
"""


nums = [[1,1,1],[1,0,1],[1,1,1]]

def markRow(i):
  for j in range(len(nums[i])):
    if nums[i][j] != 0:
      nums[i][j] = -1
      
def markCol(j):
  for i in range(len(nums)):
    if nums[i][j] != 0:
      nums[i][j] = -1

for i in range(len(nums)):
  for j in range(len(nums[i])):
    if nums[i][j] == 0:
      markRow(i)
      markCol(j)
      
for i in range(len(nums)):
  for j in range(len(nums[i])):
    if nums[i][j] == -1:
      nums[i][j] = 0
      
print(nums)



# BETTER APPROACH - (Row + Column Marking):
"""
0 milte hi direct matrix change nahi karte
  → pehle row[] aur col[] arrays me mark karte hain
  → fir second pass me marked rows aur columns ko 0 kar dete hain

⚠️ Key Point
  row[i] → poori row zero hogi
  col[j] → poora column zero hoga
  (i = row index, j = column index)

⏱️ Complexity
  Time → O(n*m) ✅
  Space → O(n + m) ❌ (extra arrays)

🧠 Memory Trick
  “Pehle decide karo → fir ek baar me apply karo”
"""

nums = [[1,1,1],[1,0,1],[1,1,1]]

rows = len(nums)
cols = len(nums[0])

row = [0] * rows
col = [0] * cols

# Step 1: mark rows and columns
for i in range(rows):
  for j in range(cols):
    if nums[i][j] == 0:
      row[i] = 1
      col[j] = 1
      
# Step 2: apply changes
for i in range(rows):
  for j in range(cols):
    if row[i] == 1 or col[j] == 1:
      nums[i][j] = 0
      
print(nums)





# OPTIMAL APPROACH (Matrix Reuse)

"""
0 milte hi direct change nahi karte
  → matrix ke first row aur first column ko marker bana dete hain
  → second pass me un markers ke basis par cells ko 0 kar dete hain

⚠️ Key Point
  matrix[i][0] → row i zero hogi
  matrix[0][j] → column j zero hoga
  matrix[0][0] dono ka marker hai
  → isliye first column ke liye alag variable (col0) use karte hain

⏱️ Complexity
  Time → O(n*m) ✅
  Space → O(1) 🔥 (no extra array)
"""


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

n = len(matrix)
m = len(matrix[0])
col0 = 1 # Variable to handle the first column

# First pass: Mark the first row and first column
for i in range(n):
  if matrix[i][0] == 0:
    col0 = 0
    
for j in range(1, m):
  if matrix[i][j] == 0:
    matrix[i][0] = 0
    matrix[0][j] = 0

# Second pass: Update inner matrix elements based on markers
for i in range(1, n):
  for j in range(1, m):
    if matrix[i][0] == 0 or matrix[0][j] == 0:
      matrix[i][j] = 0

# Final steps: Handle first row and first column separately
if matrix[0][0] == 0:
  for j in range(m):
    matrix[0][j] = 0

if col0 == 0:
  for i in range(n):
    matrix[i][0] = 0
    
print(matrix)