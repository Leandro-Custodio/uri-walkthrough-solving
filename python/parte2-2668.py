import math 

A, B, N, K = map(int, input().split())
X = A + math.sqrt(B)

valor = X**N
meno_sign = valor%K
print(round(meno_sign))