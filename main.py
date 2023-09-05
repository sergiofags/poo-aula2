i = 'S'

while i != 'n':
  print('Escolha qual arquivo deseja acessar!')
  print()
  print('1 - MENOR')
  print('2 - MEDIA')
  print('3 - CRESCENTE')
  print('4 - APROVADO OU REPROVADO')
  print('5 - CARRO')
  print()
  val = int(input('Digite a opção: '))
  print()
  print('-' * 30)
  print()

  if val == 1:
    import menorNumero
    print()
    print('-' * 30)
  elif val == 2:
    import media
    print()
    print('-' * 30)
  elif val == 3:
    import ordemCrescente
    print()
    print('-' * 30)
  elif val == 4:
    import aprovadoOuReprovado
    print()
    print('-' * 30)
  elif val == 5:
    import lugaresCarro
    print()
    print('-' * 30)

  print()
  i = input('Deseja acessar outro arquivo? (S/N)')
  print()
  print('-' * 30)