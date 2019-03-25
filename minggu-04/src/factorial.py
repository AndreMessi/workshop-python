def recur_fac(n):
  """Function to return the factorial
   of a number using recursion"""
  if n == 1:
    return n 
  else:
    return n*recur_fac(n-1)

num = 7

if num < 0:
  print("sorry factorial dosnt exist for negative number")
elif num == 0:
  print("the factorial of 0 i 1")
else:
    print("the factorial of ",num,"is",recur_fac(num))