def d(n):
  n=n+sum(map(int,str(n)))
  return n

production=[]


for i in range(1,10001):
  production[i]=d(i)


for i in range(1,10001):
  if i not in production:
    print(i)