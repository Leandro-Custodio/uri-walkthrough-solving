numero_de_cartas = int(input())

# Já que o baralho já vem ordenado é preciso que seja embaralhado 1 vez 
numero_de_embaralhamento = 1
# Como foi embaralhado no minimo 2 estão desordenadas
minimo_de_cartas_embaralhadas = 2

while(minimo_de_cartas_embaralhadas != 1):
  if(minimo_de_cartas_embaralhadas <= numero_de_cartas/2):
    minimo_de_cartas_embaralhadas += minimo_de_cartas_embaralhadas
  else:
    minimo_de_cartas_embaralhadas = minimo_de_cartas_embaralhadas - (numero_de_cartas - minimo_de_cartas_embaralhadas + 1)

  numero_de_embaralhamento += 1

print(numero_de_embaralhamento)