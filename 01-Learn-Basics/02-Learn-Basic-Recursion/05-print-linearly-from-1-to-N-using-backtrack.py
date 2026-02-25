# Print Linearly from 1 to N Using Backtrack

# In Backtrack doing f(i+1, n) (addition) is not allowed.
# we have to do subtraction f(i - 1, n)

def oneToNBacktrack(i, n):
  if i < 1:
    return
  
  oneToNBacktrack(i - 1, n)
  print(i, end=" ")

n = int(input("enter value: "))
oneToNBacktrack(n, n)