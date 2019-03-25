num = 407

if num > 1:
  for i in range(2,num):
    if (num % i) == 0:
      print(num,"not is frime number")
      print(i,"item",num//i,"is",num)
      break
  else:
    print("number is frime")
else:
    print(num,"number is not frime")      