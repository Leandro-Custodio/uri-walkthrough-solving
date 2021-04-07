numero_de_estrela = int(input())
vetor_estrela = []
vetor_carneiro = []
aux = 0

for i in range(numero_de_estrela):
  vetor_carneiro.append(int(input()))

while(True):
  if(aux==0 and vetor_carneiro[aux] % 2 == 0):
    vetor_estrela[aux] = 1
    if (vetor_carneiro[aux] > 0):
      vetor_carneiro[aux] -= 1
  elif (aux == (numero_de_estrela-1) and vetor_carneiro[aux] % 2 == 0):
    vetor_estrela[aux] = 1
    if (vetor_carneiro[aux] > 0):
      vetor_carneiro[aux] -= 1








# vetor = []
# numero_casos = int(input())
# linha = input()
# vetor = linha.split(" ")
# for i in range(numero_casos):
#   if vetor[i]%2==0:
#     for j in range(i,0,-1):
#       carneiro.append(int(vetor[j]))
#     quebra = True
#   else:
#     carneiro += 1
#     carneiro.append(int(vetor[j]))

#   if quebra:
#     break
# print("{}".format(carneiro, estrela))
# print(estrela)