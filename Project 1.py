n=5
for i in range(1,n+1):
  for g in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
      print("*",end="")
  print()