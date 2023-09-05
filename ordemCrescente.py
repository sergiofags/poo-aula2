num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
  print(f'A ordem crescente é: {num2}, {num1}')
elif num1 < num2:
  print(f'A ordem crescente é: {num1}, {num2}')
elif num1 == num2:
  print('Os números são iguais!')