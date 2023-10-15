def fibonacci(n):
  a=0
  b=1

  for i in range(n):
    print(a,end='')
    temp = a
    a = b
    b = temp + a



print(fibonacci(10000))