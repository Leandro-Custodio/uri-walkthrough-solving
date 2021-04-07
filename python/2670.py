funcionarios_no_predio = [
  int(input()) 
  for andar in range(3)
]
array_do_tempo = []
array_do_tempo.append(funcionarios_no_predio[0]*4 + funcionarios_no_predio[1] * 2) # se for no ultimo
array_do_tempo.append(funcionarios_no_predio[0]*2 + funcionarios_no_predio[2] * 2) # se for no 2
array_do_tempo.append(funcionarios_no_predio[1]*2 + funcionarios_no_predio[2] * 4) # se for no 1 andar

array_do_tempo.sort()

print(array_do_tempo[0])
