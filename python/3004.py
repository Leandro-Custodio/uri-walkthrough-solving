casos_de_testes = int(input())
for i in range(casos_de_testes):
  vetor = []
  linha = input()
  s = linha.split(" ")
  for i in range(4):
    vetor.append(int(s[i]))
  if ((vetor[0] < vetor[2]) and (vetor[1] < vetor[3])):
    print("S")
  elif ((vetor[0] < vetor[3]) and (vetor[1] < vetor[2])):
    print("S")
  else:
    print("N")
