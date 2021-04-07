
casos_de_teste = int(input())
for i in range(casos_de_teste):
  bloco1 = []
  bloco2 = []
  deu_certo1 = 0
  vetor = []
  linha = input()
  s = linha.split(" ")
  for i in range(6):
    vetor.append(int(s[i]))

  ALTURA = 0
  COMPRIMENTO = 1
  LARGURA = 2
  bloco1.append(vetor[0])
  bloco1.append(vetor[1])
  bloco1.append(vetor[2])
  bloco2.append(vetor[3])
  bloco2.append(vetor[4])
  bloco2.append(vetor[5])

  if bloco1[ALTURA] < bloco2[ALTURA] and bloco1[COMPRIMENTO] < bloco2[COMPRIMENTO] or bloco1[COMPRIMENTO] < bloco2[COMPRIMENTO] and bloco1[LARGURA] < bloco2[LARGURA] or bloco1[ALTURA] < bloco2[ALTURA] and bloco1[LARGURA] < bloco2[LARGURA] or bloco1[ALTURA] < bloco2[ALTURA] and bloco1[COMPRIMENTO] < bloco2[LARGURA] or bloco1[ALTURA] < bloco2[COMPRIMENTO] and bloco1[COMPRIMENTO] < bloco2[LARGURA] or bloco1[COMPRIMENTO] < bloco2[ALTURA] and bloco1[LARGURA] < bloco2[LARGURA]:
    print("pode empilhar bloco1 no bloco2")
    deu_certo1 += 1

  if bloco1[ALTURA] > bloco2[ALTURA] and bloco1[COMPRIMENTO] > bloco2[COMPRIMENTO] or bloco1[COMPRIMENTO] > bloco2[COMPRIMENTO] and bloco1[LARGURA] > bloco2[LARGURA] or bloco1[ALTURA] > bloco2[ALTURA] and bloco1[LARGURA] > bloco2[LARGURA] or bloco1[ALTURA] > bloco2[ALTURA] and bloco1[COMPRIMENTO] > bloco2[LARGURA] or bloco1[ALTURA] > bloco2[COMPRIMENTO] and bloco1[COMPRIMENTO] > bloco2[LARGURA] or bloco1[COMPRIMENTO] > bloco2[ALTURA] and bloco1[LARGURA] > bloco2[LARGURA]:
    print("pode empilhar bloco2 no bloco1")
    deu_certo1 += 2

  if deu_certo1 == 3:
    print("tanto faz")
  elif deu_certo1 == 2:
    print("bloco2 cabe no 1")
  elif deu_certo1 == 1:
    print("bloco1 cabe no 2")
  else:
    print("não cabe")
