valor_n = int(input())
array = []
n = 1
while(True):
  fatorial = 1
  guard = fatorial
  for i in range(1,n+1):
    fatorial = fatorial * i
    if (valor_n <= fatorial):
      if(fatorial==2):
        guard +=1
      array.append(guard)
  n+=1
  valor_n -= guard
  if(valor_n ==0):
    break
n = len(array)
print(n)
