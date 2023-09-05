numeroPessoas = int(input('Digite o numero de Pessoas: '))
numerosLugaresCarro = 5

carros = numeroPessoas//5
sobrando = numeroPessoas%5

if sobrando == 0:
  print(f'Para {numeroPessoas} pessoas são necessários {carros} carros, e não sobrou nenhum lugar')
else:
  print(f'Para {numeroPessoas} pessoas são necessários {carros + 1} carros, e ficou sobrando {numerosLugaresCarro - sobrando} lugares')
