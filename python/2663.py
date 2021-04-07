casos_de_testes = int(input())
numeros_classificados = int(input())
vetor = []
for i in range(casos_de_testes):
  valor = int(input())
  vetor.append(valor)
vetor.sort(reverse=True)
resultado = 0
for j in range(casos_de_testes):
  if j == numeros_classificados-1 and not vetor[j] == vetor[j+1]:
    break
  else:
    resultado += 1
print(resultado)

