import math

vetor = []
linha = input()
s = linha.split(" ")
for i in range(4):
  vetor.append(int(s[i]))
A = vetor[0]
B = vetor[1]
N = vetor[2]
K = vetor[3]

X = A + math.sqrt(B)
possibilidades = int(math.pow(X, N))
if K == 1:
  print(possibilidades//1%10)
elif K == 2:
  print((possibilidades//10%10))
elif K == 3:
  print((possibilidades//100%10))
else:
  print((possibilidades//1000%10))
