casos_de_testes = int(input())
acertos = 0
for i in range(casos_de_testes):
  onde_carro_tava = int(input())
  if (onde_carro_tava != 1):
    acertos+=1

print(acertos)