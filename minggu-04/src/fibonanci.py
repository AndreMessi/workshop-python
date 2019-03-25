def recur_fibo(n):
  """Recursive function to
  print Fibonacci sequence"""
  if n <= 1:
    return n
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
  print("please enter a positif integer")
else:
  print("fibonanci square")
  for i in range(nterms):
    print(recur_fibo(i))
            
