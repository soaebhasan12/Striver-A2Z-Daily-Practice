# Print name N times using recursion.

def printName(i, n):
  if i > n:
    return 
  print("STRIVER")
  printName(i + 1, n)
  
n = int(input("Enter the Value: "))

printName(1, n)
