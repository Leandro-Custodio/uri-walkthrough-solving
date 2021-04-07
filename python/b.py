v_n = int(input())
ar = []
while(True):
  f = 1
  for i in range(1,v_n+1):
    at = f
    f = f * i
    if (v_n < f):
      g = i-1
      if(f ==2):
        at = f
      ar.append(g)
      break
  if(v_n == 1):
    ar.append(1)
  v_n -= at
  if(v_n ==0):
    break
n = len(ar)
print(n)
  
  